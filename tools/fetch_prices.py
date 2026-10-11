"""Fetch the latest price for every report that names a Yahoo Finance symbol and save them to prices.json.

The site reads prices.json to show "now" prices on the report cards and to fill the scorecard.
Symbols come from the `sym: "..."` fields of the REPORTS list in index.html, so there is one list to keep.
Standard library only. A symbol that fails keeps its previous price; the file is rewritten only when a price changed.

It also works out alerts: a share that has just dropped to or under its report's level, a checkpoint date that has
arrived, and a verdict that has turned 90 days old. When ALERT_DIR is set, they are written there as alert_title.txt
and alert_body.md, and the workflow opens a GitHub issue from them, which GitHub emails to the repo owner.
"""
import json
import os
import re
import sys
import urllib.request
from datetime import date, datetime, timedelta, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "prices.json"
URL = "https://query1.finance.yahoo.com/v8/finance/chart/{}?range=5d&interval=1d"
AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0 Safari/537.36"
SITE = "https://turnivor.github.io/investment-reports/"
STALE_DAYS = 90  # same as the site


def fetch(sym):
    req = urllib.request.Request(URL.format(sym), headers={"User-Agent": AGENT})
    with urllib.request.urlopen(req, timeout=20) as res:
        meta = json.load(res)["chart"]["result"][0]["meta"]
    day = datetime.fromtimestamp(meta["regularMarketTime"], timezone.utc).strftime("%Y-%m-%d")
    return {"price": round(float(meta["regularMarketPrice"]), 4), "currency": meta["currency"], "date": day}


def reports(html):
    """The fields the alerts need from each entry of the REPORTS list in index.html."""
    body = html.split("const REPORTS = [", 1)[1].split("\n];", 1)[0]
    out = []
    for chunk in re.split(r'\n  \{ id: "', body)[1:]:
        def grab(pattern):
            m = re.search(pattern, chunk)
            return m.group(1) if m else None
        zone = grab(r"\bzone: ([0-9.]+)")
        out.append({
            "id": chunk.split('"', 1)[0], "title": grab(r'\btitle: "([^"]+)"'), "date": grab(r'\bdate: "([0-9-]{10})"'),
            "sym": grab(r'\bsym: "([^"]+)"'), "cur": grab(r'bands: \{ cur: "([^"]+)"'), "zone": float(zone) if zone else None,
            "next": grab(r'next: \{ text: "((?:[^"\\]|\\.)*)"'), "until": grab(r'\buntil: "([0-9-]{10})"'),
        })
    return out


def alerts(entries, old, new, today):
    """One line per thing worth a look today. A Monday run also covers the weekend."""
    span = 3 if today.weekday() == 0 else 1
    due = lambda day: 0 <= (today - day).days < span
    lines = []
    for r in entries:
        link = f"[{r['title']}]({SITE}#{r['id']})"
        was, now = old.get(r["sym"]), new.get(r["sym"])
        if r["zone"] and was and now and was["price"] > r["zone"] >= now["price"]:
            lines.append(f"**Price:** {link} is at {r['cur']}{now['price']:g}, at or under its {r['cur']}{r['zone']:g} level from the report.")
        if r["until"] and due(date.fromisoformat(r["until"])):
            lines.append(f"**Checkpoint:** {link}. {r['next']}")
        if r["date"] and due(date.fromisoformat(r["date"]) + timedelta(days=STALE_DAYS + 1)):
            lines.append(f"**Refresh:** the {link} verdict is now over {STALE_DAYS} days old." + (" The scorecard judges it from today." if r["sym"] else ""))
    return lines


def main():
    html = (ROOT / "index.html").read_text(encoding="utf-8")
    syms = sorted(set(re.findall(r'\bsym: "([A-Za-z0-9.^=-]+)"', html)))
    if not syms:
        sys.exit("No symbols found in index.html")
    old = json.loads(OUT.read_text(encoding="utf-8")).get("prices", {}) if OUT.exists() else {}
    prices, failed = {}, []
    for sym in syms:
        try:
            prices[sym] = fetch(sym)
            print(f"{sym}: {prices[sym]['price']} {prices[sym]['currency']} ({prices[sym]['date']})")
        except Exception as err:  # keep the last known price for this symbol
            failed.append(sym)
            print(f"{sym}: FAILED ({err})", file=sys.stderr)
            if sym in old:
                prices[sym] = old[sym]

    today = datetime.now(timezone.utc).date()
    found = alerts(reports(html), old, prices, today)
    for line in found:
        print("ALERT", line)
    if found and os.environ.get("ALERT_DIR"):
        out = Path(os.environ["ALERT_DIR"])
        plain = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", found[0]).replace("**", "")
        title = plain if len(found) == 1 else f"{len(found)} things to look at ({today:%d %b %Y})"
        (out / "alert_title.txt").write_text(title[:120], encoding="utf-8")
        (out / "alert_body.md").write_text("\n".join(f"- {line}" for line in found) + f"\n\nRaised by the daily price job. [Scorecard]({SITE}#scorecard)\n", encoding="utf-8")

    if len(failed) == len(syms):
        sys.exit("Every symbol failed; prices.json left as it was")
    if prices == old:
        print("No price changed")
        return
    doc = {"updated": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"), "source": "Yahoo Finance", "prices": prices}
    OUT.write_text(json.dumps(doc, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote {OUT.name}" + (f" ({len(failed)} failed: {', '.join(failed)})" if failed else ""))


if __name__ == "__main__":
    main()
