// /api/inbox: the owner's side of the queue, for inbox.html (works from a phone).
//   GET   → every waiting request (oldest first) and the 15 most recently closed ones
//   POST  → { id, action: "pick" | "unpick" | "decline", reply? }
// Only emails in the ADMIN_EMAILS setting may use it. Picking does not run anything:
// it marks the request so /queue offers it first, in Claude Code on his computer or in a cloud session.

import { json, isAdmin } from "./_middleware.js";

const forbidden = () => json({ error: "This page is only for the site owner." }, 403);

export async function onRequestGet({ env, data }) {
  if (!isAdmin(env, data.email)) return forbidden();
  const [waiting, recent] = await env.DB.batch([
    env.DB.prepare(
      `SELECT id, requested_by, topic, skill, note, picked_at, created_at
         FROM requests WHERE status = 'pending' ORDER BY created_at`
    ),
    env.DB.prepare(
      `SELECT id, requested_by, topic, skill, status, report_id, reply, created_at, completed_at
         FROM requests WHERE status <> 'pending' ORDER BY COALESCE(completed_at, created_at) DESC LIMIT 15`
    ),
  ]);
  return json({ email: data.email, waiting: waiting.results, recent: recent.results });
}

export async function onRequestPost({ request, env, data }) {
  if (!isAdmin(env, data.email)) return forbidden();
  let body;
  try { body = await request.json(); } catch { return json({ error: "Send JSON." }, 400); }
  const id = Number(body.id);
  if (!Number.isInteger(id) || id <= 0) return json({ error: "Which request?" }, 400);
  const now = new Date().toISOString();
  const reply = String(body.reply ?? "").trim().slice(0, 1000);

  let stmt;
  if (body.action === "pick") {
    stmt = env.DB.prepare(`UPDATE requests SET picked_at = ? WHERE id = ? AND status = 'pending'`).bind(now, id);
  } else if (body.action === "unpick") {
    stmt = env.DB.prepare(`UPDATE requests SET picked_at = NULL WHERE id = ? AND status = 'pending'`).bind(id);
  } else if (body.action === "decline") {
    stmt = env.DB.prepare(
      `UPDATE requests SET status = 'declined', reply = ?, picked_at = NULL, completed_at = ?
        WHERE id = ? AND status = 'pending'`
    ).bind(reply, now, id);
  } else {
    return json({ error: "Unknown action." }, 400);
  }
  const res = await stmt.run();
  if (!res.meta.changes) return json({ error: "That request is not waiting any more." }, 409);
  return json({ ok: true });
}
