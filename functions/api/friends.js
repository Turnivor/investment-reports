// /api/friends: the owner manages who can sign in, from the Inbox (works on a phone).
//   GET     → the email addresses on the Cloudflare Access "Friends" policy
//   POST    → { email }  add someone
//   DELETE  → ?email=…   remove someone, and sign them out
// Only emails in ADMIN_EMAILS may use it, and those can never be removed here.
//
// Settings on the Pages project (FRIENDS-SETUP.md, step 10):
//   CLOUDFLARE_ACCOUNT_ID  the account id (text)
//   ACCESS_POLICY_ID       the Friends policy id (text; optional: without it the policy named "Friends" is used)
//   ACCESS_ADMIN_TOKEN     a Cloudflare API token (secret) with "Access: Apps and Policies Write",
//                          plus "Access: Organizations, Identity Providers, and Groups Write" to sign removed friends out

import { json, isAdmin } from "./_middleware.js";

const API = "https://api.cloudflare.com/client/v4";
// Fields a reusable policy keeps when it is written back; everything else in the GET result is read-only.
const WRITABLE = ["name", "decision", "include", "exclude", "require", "session_duration", "approval_required",
  "approval_groups", "isolation_required", "purpose_justification_required", "purpose_justification_prompt",
  "mfa_config", "connection_rules"];
const EMAIL = /^[^\s@<>"',;]+@[^\s@<>"',;]+\.[^\s@<>"',;]{2,}$/;

class SetupError extends Error {}

export async function onRequest(context) {
  const { request, env, data } = context;
  if (!isAdmin(env, data.email)) return json({ error: "This page is only for the site owner." }, 403);
  if (!env.ACCESS_ADMIN_TOKEN || !env.CLOUDFLARE_ACCOUNT_ID) {
    return json({ error: "Managing friends here is not set up yet (FRIENDS-SETUP.md, step 10).", setup: true }, 501);
  }
  try {
    if (request.method === "GET") return await list(env);
    if (request.method === "POST") return await add(request, env);
    if (request.method === "DELETE") return await remove(request, env);
    return json({ error: "Method not allowed." }, 405);
  } catch (err) {
    return json({ error: err.message, setup: err instanceof SetupError }, err instanceof SetupError ? 501 : 502);
  }
}

async function list(env) {
  const policy = await getPolicy(env);
  return json({ emails: emailsOf(policy), admins: admins(env), policy: policy.name });
}

async function add(request, env) {
  let body;
  try { body = await request.json(); } catch { return json({ error: "Send JSON." }, 400); }
  const email = String(body.email || "").trim().toLowerCase();
  if (!EMAIL.test(email) || email.length > 254) return json({ error: "That does not look like an email address." }, 400);
  const policy = await getPolicy(env);
  if (emailsOf(policy).includes(email)) return json({ error: `${email} is already on the list.` }, 409);
  policy.include = [...(policy.include || []), { email: { email } }];
  await putPolicy(env, policy);
  return json({ ok: true, emails: emailsOf(policy) }, 201);
}

async function remove(request, env) {
  const email = String(new URL(request.url).searchParams.get("email") || "").trim().toLowerCase();
  if (!email) return json({ error: "Whose access should be removed?" }, 400);
  if (admins(env).includes(email)) return json({ error: "The site owner cannot be removed here." }, 400);
  const policy = await getPolicy(env);
  const before = (policy.include || []).length;
  policy.include = (policy.include || []).filter(r => String(r?.email?.email || "").toLowerCase() !== email);
  if (policy.include.length === before) return json({ error: `${email} is not on the list.` }, 404);
  if (!policy.include.length) return json({ error: "The list cannot be left empty." }, 400);
  await putPolicy(env, policy);
  // Sign them out now rather than when their session runs out. Needs the second token permission; skipped if missing.
  const revoked = await cf(env, "POST", "/access/organizations/revoke_user", { email }).then(() => true, () => false);
  return json({ ok: true, revoked, emails: emailsOf(policy) });
}

const admins = env => String(env.ADMIN_EMAILS || "").toLowerCase().split(",").map(e => e.trim()).filter(Boolean);
const emailsOf = policy => (policy.include || []).map(r => r?.email?.email).filter(Boolean).map(e => String(e).toLowerCase()).sort();

async function getPolicy(env) {
  if (env.ACCESS_POLICY_ID) return cf(env, "GET", `/access/policies/${encodeURIComponent(env.ACCESS_POLICY_ID)}`);
  const all = await cf(env, "GET", "/access/policies?per_page=100");
  const found = (all || []).filter(p => String(p.name).toLowerCase() === "friends");
  if (found.length !== 1) {
    throw new SetupError(found.length ? "Several policies are named Friends. Set ACCESS_POLICY_ID (FRIENDS-SETUP.md, step 10)."
                                      : "No Access policy named Friends was found. Set ACCESS_POLICY_ID (FRIENDS-SETUP.md, step 10).");
  }
  return cf(env, "GET", `/access/policies/${encodeURIComponent(found[0].id)}`); // the full policy, as the list may be abridged
}

async function putPolicy(env, policy) {
  const body = Object.fromEntries(WRITABLE.filter(k => policy[k] !== undefined).map(k => [k, policy[k]]));
  await cf(env, "PUT", `/access/policies/${encodeURIComponent(policy.id)}`, body);
}

async function cf(env, method, path, body) {
  const res = await fetch(`${env.CLOUDFLARE_API_BASE || API}/accounts/${env.CLOUDFLARE_ACCOUNT_ID}${path}`, {
    method,
    headers: { Authorization: `Bearer ${env.ACCESS_ADMIN_TOKEN}`, "Content-Type": "application/json" },
    body: body === undefined ? undefined : JSON.stringify(body),
  });
  let out = {};
  try { out = await res.json(); } catch {}
  if (!res.ok || out.success === false) {
    const msg = (out.errors || []).map(e => e.message).join("; ") || `HTTP ${res.status}`;
    if (res.status === 401 || res.status === 403) throw new SetupError(`Cloudflare refused the friends token (${msg}). Check its permissions (FRIENDS-SETUP.md, step 10).`);
    throw new Error(`Cloudflare said: ${msg}`);
  }
  return out.result;
}
