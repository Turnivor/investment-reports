-- One-time change for a database created before the Inbox existed: adds the "picked" mark.
-- Run once in the Cloudflare dashboard: D1 → investment-requests → Console.
-- (A database created from the current schema.sql already has it; running this there fails harmlessly with "duplicate column".)
ALTER TABLE requests ADD COLUMN picked_at TEXT;
