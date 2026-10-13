"""
Request queue for Claude Code: lets Claude read and update the friends' report requests.

Runs on his own computer, started by Claude Code (never on the website). It talks to the
Cloudflare D1 database behind request.html through Cloudflare's API. It only reads the queue
and records outcomes: research is always started by him, from /queue, one request at a time.

Setup (details in FRIENDS-SETUP.md, step 6), from the repo folder:
    pip install "mcp[cli]"
    claude mcp add research-queue \
        -e CLOUDFLARE_ACCOUNT_ID=<account id> \
        -e CLOUDFLARE_D1_ID=<database id> \
        -e CLOUDFLARE_API_TOKEN=<token with D1 Edit> \
        -- python3 tools/queue_mcp.py
The token stays in his local Claude Code settings. Never commit it.
"""

import json
import os
import re
import urllib.error
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

try:  # MCP Python SDK 2.x
    from mcp.server.mcpserver import MCPServer as Server
    from mcp.server.mcpserver.exceptions import ToolError
except ImportError:  # 1.x
    from mcp.server.fastmcp import FastMCP as Server
    from mcp.server.fastmcp.exceptions import ToolError

ROOT = Path(__file__).resolve().parent.parent
mcp = Server("research-queue")


def query(sql: str, params: list | None = None) -> dict:
    """Run one SQL statement on the D1 database and return its first result block."""
    try:
        account, db, token = (os.environ[k] for k in ("CLOUDFLARE_ACCOUNT_ID", "CLOUDFLARE_D1_ID", "CLOUDFLARE_API_TOKEN"))
    except KeyError as missing:
        raise ToolError(f"{missing} is not set. Add it with `claude mcp add ... -e` (see FRIENDS-SETUP.md).") from None
    req = urllib.request.Request(
        f"https://api.cloudflare.com/client/v4/accounts/{account}/d1/database/{db}/query",
        data=json.dumps({"sql": sql, "params": [str(v) for v in (params or [])]}).encode(),  # the API takes text params
        headers={"Authorization": f"Bearer {token}", "Content-Type": "application/json"},
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=30) as res:
            body = json.load(res)
    except urllib.error.HTTPError as err:
        detail = err.read().decode(errors="replace")[:300]
        raise ToolError(f"Cloudflare API error {err.code}: {detail}") from None
    except (urllib.error.URLError, TimeoutError) as err:
        raise ToolError(f"Could not reach Cloudflare: {err}") from None
    if not body.get("success"):
        raise ToolError(f"Cloudflare API error: {body.get('errors')}")
    return body["result"][0]


def now() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds").replace("+00:00", "Z")


def report_ids() -> dict[str, str]:
    """Report ids and titles currently in reports.js (made by tools/build.py)."""
    text = (ROOT / "reports.js").read_text(encoding="utf-8")
    data = json.loads(re.search(r"window\.SITE_DATA\s*=\s*(\{.*\});?\s*$", text, re.S).group(1))
    return {r["id"]: r.get("title", r["id"]) for r in data.get("reports", [])}


@mcp.tool()
def list_pending() -> list[dict]:
    """List friends' report requests that are waiting for a decision, oldest first."""
    return query(
        "SELECT id, requested_by, topic, skill, note, created_at FROM requests "
        "WHERE status = 'pending' ORDER BY created_at"
    )["results"]


@mcp.tool()
def get_request(request_id: int) -> dict:
    """Show everything about one request, whatever its status."""
    rows = query("SELECT * FROM requests WHERE id = ?", [request_id])["results"]
    return rows[0] if rows else {"error": f"No request #{request_id}."}


@mcp.tool()
def list_recent(limit: int = 15) -> list[dict]:
    """List the most recent requests of every status (done, declined, cancelled, pending)."""
    limit = max(1, min(int(limit), 100))
    return query(
        "SELECT id, requested_by, topic, skill, status, report_id, created_at, completed_at "
        f"FROM requests ORDER BY created_at DESC LIMIT {limit}"  # limit is a clamped int, safe to inline
    )["results"]


@mcp.tool()
def mark_done(request_id: int, report_id: str, reply: str = "") -> str:
    """Close a waiting request with the finished report. report_id is the report's `id` from its card,
    which must already be in reports.js (run tools/make_pdf.py / tools/build.py first). The friend sees
    a link to it on request.html once the site is pushed. `reply` is an optional short note to them."""
    known = report_ids()
    if report_id not in known:
        return (f"No report with id '{report_id}' in reports.js. Build it first (python tools/make_pdf.py), "
                f"then try again. Known ids include: {', '.join(list(known)[:12])}")
    res = query(
        "UPDATE requests SET status = 'done', report_id = ?, reply = ?, completed_at = ? "
        "WHERE id = ? AND status = 'pending'",
        [report_id, reply.strip()[:1000], now(), request_id],
    )
    if not res["meta"].get("changes"):
        return f"Request #{request_id} is not waiting (already handled, cancelled, or it does not exist)."
    return f"Request #{request_id} marked done with report '{known[report_id]}'. Push the site so the friend can open it."


@mcp.tool()
def decline(request_id: int, reply: str = "") -> str:
    """Decline a waiting request. `reply` is shown to the friend, e.g. why or what to ask instead."""
    res = query(
        "UPDATE requests SET status = 'declined', reply = ?, completed_at = ? WHERE id = ? AND status = 'pending'",
        [reply.strip()[:1000], now(), request_id],
    )
    if not res["meta"].get("changes"):
        return f"Request #{request_id} is not waiting (already handled, cancelled, or it does not exist)."
    return f"Request #{request_id} declined."


if __name__ == "__main__":
    mcp.run()  # stdio: only the Claude Code session that started it can talk to it
