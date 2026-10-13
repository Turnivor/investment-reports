// Runs before every /api/* call. Cloudflare Access already stops anyone who is not on the friends list,
// but this checks Access's signed token as well, so the API stays closed even if the Access setup
// is ever missing or wrong (for example on a preview address it does not cover).
// On success the caller's email is in context.data.email.
//
// Needs two settings on the Pages project (see FRIENDS-SETUP.md):
//   ACCESS_TEAM_DOMAIN  e.g. "turnivor.cloudflareaccess.com"
//   ACCESS_AUD          the Access application's "Application Audience (AUD) Tag"
//                       (several tags separated by commas, e.g. production and previews)

let certs = { at: 0, keys: [] };

export async function onRequest(context) {
  const { request, env, data } = context;
  const url = new URL(request.url);

  // Local testing only (wrangler pages dev): pretend to be DEV_EMAIL. Ignored on any real address.
  if (env.DEV_EMAIL && (url.hostname === "localhost" || url.hostname === "127.0.0.1")) {
    data.email = String(env.DEV_EMAIL).toLowerCase();
    return context.next();
  }

  if (!env.ACCESS_TEAM_DOMAIN || !env.ACCESS_AUD) {
    return json({ error: "The site's login is not set up yet (ACCESS_TEAM_DOMAIN / ACCESS_AUD missing)." }, 500);
  }

  const token = request.headers.get("Cf-Access-Jwt-Assertion") || cookie(request, "CF_Authorization");
  if (!token) return json({ error: "Not signed in." }, 401);

  try {
    data.email = await verify(token, env);
  } catch (err) {
    return json({ error: "Your sign-in could not be checked. Reload the page to sign in again." }, 401);
  }
  return context.next();
}

async function verify(token, env) {
  const team = String(env.ACCESS_TEAM_DOMAIN).replace(/^https?:\/\//, "").replace(/\/+$/, "");
  const parts = token.split(".");
  if (parts.length !== 3) throw new Error("malformed token");
  const [h, p, s] = parts;
  const header = JSON.parse(text(b64url(h)));
  const payload = JSON.parse(text(b64url(p)));
  if (header.alg !== "RS256") throw new Error("unexpected algorithm");

  let jwk = (await keys(team)).find(k => k.kid === header.kid);
  if (!jwk) jwk = (await keys(team, true)).find(k => k.kid === header.kid); // keys rotate: refetch once
  if (!jwk) throw new Error("unknown signing key");

  const key = await crypto.subtle.importKey("jwk", jwk, { name: "RSASSA-PKCS1-v1_5", hash: "SHA-256" }, false, ["verify"]);
  const ok = await crypto.subtle.verify("RSASSA-PKCS1-v1_5", key, b64url(s), new TextEncoder().encode(`${h}.${p}`));
  if (!ok) throw new Error("bad signature");

  const aud = Array.isArray(payload.aud) ? payload.aud : [payload.aud];
  const allowed = String(env.ACCESS_AUD).split(",").map(a => a.trim()).filter(Boolean); // production tag, optionally the previews' too
  const now = Math.floor(Date.now() / 1000);
  if (!aud.some(a => allowed.includes(a))) throw new Error("wrong audience");
  if (payload.iss !== `https://${team}`) throw new Error("wrong issuer");
  if (!payload.exp || payload.exp < now) throw new Error("expired");
  if (payload.nbf && payload.nbf > now + 60) throw new Error("not yet valid");
  if (!payload.email) throw new Error("no email in token");
  return String(payload.email).toLowerCase();
}

async function keys(team, refresh = false) {
  if (!refresh && certs.keys.length && Date.now() - certs.at < 3600_000) return certs.keys;
  const res = await fetch(`https://${team}/cdn-cgi/access/certs`);
  if (!res.ok) throw new Error("could not fetch Access keys");
  certs = { at: Date.now(), keys: (await res.json()).keys || [] };
  return certs.keys;
}

function b64url(str) {
  let s = str.replace(/-/g, "+").replace(/_/g, "/");
  while (s.length % 4) s += "=";
  return Uint8Array.from(atob(s), c => c.charCodeAt(0));
}
const text = bytes => new TextDecoder().decode(bytes);

function cookie(request, name) {
  const m = (request.headers.get("Cookie") || "").match(new RegExp(`(?:^|;\\s*)${name}=([^;]+)`));
  return m ? decodeURIComponent(m[1]) : null;
}

export function json(body, status = 200) {
  return new Response(JSON.stringify(body), {
    status,
    headers: { "Content-Type": "application/json; charset=utf-8", "Cache-Control": "no-store" },
  });
}
