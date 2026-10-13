-- Request queue for the friends' "Request a report" page.
-- Run once in the Cloudflare dashboard: Storage & Databases → D1 → your database → Console.
-- Safe to run again: it only creates what is missing.

CREATE TABLE IF NOT EXISTS requests (
  id           INTEGER PRIMARY KEY AUTOINCREMENT,
  requested_by TEXT NOT NULL,                  -- the friend's email, as Cloudflare Access saw it
  topic        TEXT NOT NULL,                  -- what they want researched, e.g. "Nvidia"
  skill        TEXT NOT NULL DEFAULT '',       -- the ai-berkshire command they picked, or '' to leave it to him
  note         TEXT NOT NULL DEFAULT '',       -- anything else they wrote
  status       TEXT NOT NULL DEFAULT 'pending'
               CHECK (status IN ('pending', 'done', 'declined', 'cancelled')),
  report_id    TEXT,                           -- the report's id in reports.js once done (opens at ./#<id>)
  reply        TEXT NOT NULL DEFAULT '',       -- his note back, e.g. why it was declined
  picked_at    TEXT,                           -- set when he picks it in the Inbox; /queue runs picked ones first
  created_at   TEXT NOT NULL,                  -- ISO 8601, UTC
  completed_at TEXT
);

CREATE INDEX IF NOT EXISTS requests_by_user ON requests (requested_by, created_at);
CREATE INDEX IF NOT EXISTS requests_by_status ON requests (status, created_at);
