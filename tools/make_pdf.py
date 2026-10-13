"""Make the PDF that sits next to each report, then rebuild the site data.

  python tools/make_pdf.py              every report that has no PDF yet
  python tools/make_pdf.py oklo xylem   these reports again (after changing a card or filing an update)
  python tools/make_pdf.py --all        every report again

The PDF is the page print.html#<id> printed by Microsoft Edge or Chrome without a window: the working sheet
(verdict, value range, the report's plan, dates to tick off) followed by the full report. The report's card gets
`"pdf": "<file name>"` so the site offers it for download. Needs Edge or Chrome on this computer and a network
connection for the fonts.
"""
import functools
import http.server
import json
import os
import subprocess
import sys
import tempfile
import threading
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import build

ROOT = build.ROOT
BROWSERS = [
    os.environ.get("PDF_BROWSER", ""),
    r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
    r"C:\Program Files\Microsoft\Edge\Application\msedge.exe",
    r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    "/usr/bin/google-chrome", "/usr/bin/chromium", "/usr/bin/chromium-browser",
    "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
]


class Quiet(http.server.SimpleHTTPRequestHandler):
    def log_message(self, *args):
        pass


def cards():
    """(path, card) for every report that has a card."""
    out = []
    for path in sorted((ROOT / "reports").rglob("*.md")):
        text = path.read_text(encoding="utf-8")
        end = text.find("\n---\n", 4)
        if text.startswith("---\n") and end > 0:
            out.append((path, json.loads(text[4:end])))
    return out


def set_pdf(path, name):
    """Write `"pdf": name` into the report's card, right after its id."""
    text = path.read_text(encoding="utf-8")
    end = text.find("\n---\n", 4)
    card = json.loads(text[4:end])
    if card.get("pdf") == name:
        return
    out = {}
    for key, value in card.items():
        if key != "pdf":
            out[key] = value
        if key == "id":
            out["pdf"] = name
    path.write_text("---\n" + json.dumps(out, indent=2, ensure_ascii=False) + text[end:], encoding="utf-8", newline="")


def rebuild(require_pdf):
    build.REQUIRE_PDF = require_pdf
    build.problems.clear()
    build.main()


def main():
    args = sys.argv[1:]
    browser = next((b for b in BROWSERS if b and Path(b).exists()), None)
    if not browser:
        sys.exit("No Edge or Chrome found. Set PDF_BROWSER to the browser's path.")
    everything = cards()
    known = {card["id"] for _, card in everything}
    for unknown in [a for a in args if a != "--all" and a not in known]:
        sys.exit(f"No report with id {unknown!r}. Known: {', '.join(sorted(known))}")
    wanted = [(p, c) for p, c in everything
              if "--all" in args or c["id"] in args or (not args and not (c.get("pdf") and (p.parent / c["pdf"]).exists()))]
    if not wanted:
        print("Every report already has its PDF.")
        rebuild(True)
        return

    rebuild(False)  # print.html reads reports.js, so it has to be current first
    server = http.server.ThreadingHTTPServer(("127.0.0.1", 0), functools.partial(Quiet, directory=str(ROOT)))
    threading.Thread(target=server.serve_forever, daemon=True).start()
    try:
        with tempfile.TemporaryDirectory() as profile:
            for path, card in wanted:
                target = path.with_suffix(".pdf")
                url = f"http://127.0.0.1:{server.server_address[1]}/print.html#{card['id']}"
                # Chrome refuses to start as root (cloud sessions run as root) unless its sandbox is off.
                sandbox = ["--no-sandbox"] if getattr(os, "geteuid", lambda: 1)() == 0 else []
                subprocess.run([browser, *sandbox, "--headless=new", "--disable-gpu", "--no-first-run", "--no-pdf-header-footer",
                                f"--user-data-dir={profile}", "--virtual-time-budget=25000", "--run-all-compositor-stages-before-draw",
                                f"--print-to-pdf={target}", url], check=True, timeout=180, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
                size = target.stat().st_size if target.exists() else 0
                if size < 30_000:
                    sys.exit(f"{card['id']}: the PDF came out empty or too small ({size} bytes). Nothing else was changed.")
                set_pdf(path, target.name)
                print(f"{card['id']}: {target.relative_to(ROOT).as_posix()} ({size // 1024} KB)")
    finally:
        server.shutdown()
    missing = [c["id"] for p, c in cards() if not c.get("pdf")]
    rebuild(not missing)
    if missing:
        print("Still without a PDF: " + ", ".join(missing) + ". Run this again with no names to make them.")


if __name__ == "__main__":
    main()
