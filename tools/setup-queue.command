#!/bin/bash
# One-time setup of /queue in Claude Code on this Mac. Double-click it in Finder
# (or run: bash tools/setup-queue.command). It asks for one paste: the three lines
#   ACCOUNT=...
#   DATABASE=...
#   TOKEN=...
# that were sent to you. Nothing is stored in the repo; the values go into your own Claude Code settings.

cd "$(dirname "$0")/.." || exit 1
REPO="$(pwd)"
pause() { echo; read -r -n 1 -s -p "Press any key to close this window." </dev/tty; echo; }
fail() { echo; echo "✘ $1"; pause; exit 1; }

echo "Setting up /queue for Claude Code"
echo "================================="
echo

# 1. Claude Code must be installed
CLAUDE="$(command -v claude || true)"
[ -z "$CLAUDE" ] && [ -x "$HOME/.claude/local/claude" ] && CLAUDE="$HOME/.claude/local/claude"
[ -z "$CLAUDE" ] && [ -x "$HOME/.local/bin/claude" ] && CLAUDE="$HOME/.local/bin/claude"
[ -z "$CLAUDE" ] && fail "Claude Code was not found. Install it first, then double-click this file again."
echo "✔ Claude Code found"

# 2. uv runs the queue script with the right Python and its one library, without touching your Python setup
UV="$(command -v uv || true)"
[ -z "$UV" ] && [ -x "$HOME/.local/bin/uv" ] && UV="$HOME/.local/bin/uv"
if [ -z "$UV" ]; then
  echo "… installing uv (a small Python helper, about 20 seconds)"
  curl -LsSf https://astral.sh/uv/install.sh | sh >/dev/null 2>&1 || fail "Could not install uv. Check the internet connection and try again."
  UV="$HOME/.local/bin/uv"
  [ -x "$UV" ] || fail "uv was installed but not found at $UV."
fi
echo "✔ uv ready"

# 3. The three values
echo
echo "Paste the three lines you were sent (ACCOUNT=…, DATABASE=…, TOKEN=…)."
echo "Nothing will show while you paste. Then press Enter."
ACCOUNT="" DATABASE="" TOKEN=""
stty -echo </dev/tty
while [ -z "$ACCOUNT" ] || [ -z "$DATABASE" ] || [ -z "$TOKEN" ]; do
  IFS= read -r line </dev/tty || break
  line="$(printf '%s' "$line" | tr -d '\r' | sed 's/^[[:space:]]*//; s/[[:space:]]*$//')"
  case "$line" in
    ACCOUNT=*)  ACCOUNT="${line#ACCOUNT=}" ;;
    DATABASE=*) DATABASE="${line#DATABASE=}" ;;
    TOKEN=*)    TOKEN="${line#TOKEN=}" ;;
  esac
done
stty echo </dev/tty
echo
[ -n "$ACCOUNT" ] && [ -n "$DATABASE" ] && [ -n "$TOKEN" ] || fail "Not all three lines arrived. Double-click the file again and paste all three."
echo "✔ Got the three values"

# 4. Check they work before saving anything
echo "… checking the connection to the request queue"
CHECK="$(CLOUDFLARE_ACCOUNT_ID="$ACCOUNT" CLOUDFLARE_D1_ID="$DATABASE" CLOUDFLARE_API_TOKEN="$TOKEN" \
  "$UV" run --quiet --no-project --python ">=3.10" --with "mcp[cli]" python - "$REPO/tools" <<'PY' 2>&1
import sys
sys.path.insert(0, sys.argv[1])
import queue_mcp
r = queue_mcp.query("SELECT COUNT(*) AS n FROM requests WHERE status = 'pending'")
print(f"OK {r['results'][0]['n']}")
PY
)"
case "$CHECK" in
  *"OK "*) echo "✔ Connected. Requests waiting right now: ${CHECK##*OK }" ;;
  *) echo "$CHECK" | tail -3; fail "The connection check failed. Ask for the three lines again (the token may be wrong or expired)." ;;
esac

# 5. Register the queue tools with Claude Code, for every folder
"$CLAUDE" mcp remove research-queue --scope user >/dev/null 2>&1
"$CLAUDE" mcp add --scope user research-queue \
  -e CLOUDFLARE_ACCOUNT_ID="$ACCOUNT" \
  -e CLOUDFLARE_D1_ID="$DATABASE" \
  -e CLOUDFLARE_API_TOKEN="$TOKEN" \
  -- "$UV" run --quiet --no-project --python ">=3.10" --with "mcp[cli]" python "$REPO/tools/queue_mcp.py" >/dev/null \
  || fail "Claude Code did not accept the queue tools."
echo "✔ Queue tools added to Claude Code"

# 6. The /queue command, for every folder
mkdir -p "$HOME/.claude/commands"
cp "$REPO/.claude/commands/queue.md" "$HOME/.claude/commands/queue.md" || fail "Could not copy the /queue command."
echo "✔ /queue command installed"

echo
echo "All set. Open Claude Code (in any folder) and type:  /queue"
echo "If you move this folder ($REPO), run this file again from its new place."
pause
