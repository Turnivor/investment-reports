// /api/requests: the friends' side of the request queue.
//   GET     → the signed-in friend's own requests, plus the list of report types they can ask for
//   POST    → add a request  { topic, skill, note }
//   DELETE  → cancel one of their own waiting requests  ?id=123
// Who is asking comes from the Access sign-in (see _middleware.js), never from the page.
// Nothing here runs research: requests wait until he reviews them with /queue in Claude Code.
//
// Needs the D1 database bound to the Pages project as DB.
// Optional: GITHUB_TOKEN (secret) + GITHUB_REPO ("Turnivor/investment-reports") to open an issue
// for each new request, which GitHub emails to him.

import { json } from "./_middleware.js";

// What friends can pick. The heaviest multi-agent commands are left out on purpose;
// he can still choose one himself when he runs a request.
const SKILLS = [
  { cmd: "", label: "Let him choose" },
  { cmd: "/investment-research", label: "Full company deep dive" },
  { cmd: "/investment-checklist", label: "Buffett checklist, quicker" },
  { cmd: "/quality-screen", label: "Quick quality screen of a few companies" },
  { cmd: "/earnings-review", label: "Latest earnings results" },
  { cmd: "/industry-research", label: "Map of a whole industry" },
  { cmd: "/industry-funnel", label: "Best 3 companies in an industry" },
  { cmd: "/news-pulse", label: "Why a share moved today" },
];
const MAX_WAITING = 3;

export async function onRequestGet({ env, data }) {
  const { results } = await env.DB.prepare(
    `SELECT id, topic, skill, note, status, report_id, reply, created_at, completed_at
       FROM requests WHERE requested_by = ? ORDER BY created_at DESC LIMIT 50`
  ).bind(data.email).all();
  return json({ email: data.email, skills: SKILLS, maxWaiting: MAX_WAITING, requests: results });
}

export async function onRequestPost({ request, env, data, waitUntil }) {
  let body;
  try { body = await request.json(); } catch { return json({ error: "Send the form as JSON." }, 400); }

  const topic = clean(body.topic, 200);
  const skill = clean(body.skill, 60);
  const note = clean(body.note, 1000);
  if (topic.length < 2) return json({ error: "Say what you would like researched." }, 400);
  if (!SKILLS.some(s => s.cmd === skill)) return json({ error: "Pick one of the report types in the list." }, 400);

  const { waiting } = await env.DB.prepare(
    `SELECT COUNT(*) AS waiting FROM requests WHERE requested_by = ? AND status = 'pending'`
  ).bind(data.email).first();
  if (waiting >= MAX_WAITING) {
    return json({ error: `You already have ${waiting} requests waiting. Cancel one or wait for a report first.` }, 429);
  }

  const created = new Date().toISOString();
  const row = await env.DB.prepare(
    `INSERT INTO requests (requested_by, topic, skill, note, created_at) VALUES (?, ?, ?, ?, ?) RETURNING id`
  ).bind(data.email, topic, skill, note, created).first();

  if (env.GITHUB_TOKEN && env.GITHUB_REPO) {
    waitUntil(notify(env, { id: row.id, email: data.email, topic, skill, note }).catch(() => {}));
  }
  return json({ ok: true, id: row.id }, 201);
}

export async function onRequestDelete({ request, env, data }) {
  const id = Number(new URL(request.url).searchParams.get("id"));
  if (!Number.isInteger(id) || id <= 0) return json({ error: "Which request?" }, 400);
  const res = await env.DB.prepare(
    `UPDATE requests SET status = 'cancelled', completed_at = ?
      WHERE id = ? AND requested_by = ? AND status = 'pending'`
  ).bind(new Date().toISOString(), id, data.email).run();
  if (!res.meta.changes) return json({ error: "That request is not waiting any more." }, 409);
  return json({ ok: true });
}

function clean(value, max) {
  return String(value ?? "").replace(/[\u0000-\u0008\u000B\u000C\u000E-\u001F]/g, "").trim().slice(0, max);
}

async function notify(env, r) {
  const lines = [
    `**From:** ${r.email}`,
    `**Topic:** ${r.topic}`,
    `**Report type:** ${r.skill || "his choice"}`,
    r.note ? `**Note:** ${r.note}` : null,
    "",
    `Request #${r.id}. Open Claude Code in this repo and run \`/queue\` to review it.`,
  ];
  await fetch(`https://api.github.com/repos/${env.GITHUB_REPO}/issues`, {
    method: "POST",
    headers: {
      Authorization: `Bearer ${env.GITHUB_TOKEN}`,
      Accept: "application/vnd.github+json",
      "User-Agent": "investment-reports-requests",
    },
    body: JSON.stringify({ title: `Report request #${r.id}: ${r.topic}`, body: lines.filter(l => l !== null).join("\n") }),
  });
}
