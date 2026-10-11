"""Fetch the latest price for every report that names a Yahoo Finance symbol and save them to prices.json.

The site reads prices.json to show "now" prices on the report cards and to fill the scorecard.
Symbols come from the `sym: "..."` fields of the REPORTS list in index.html, so there is one list to keep.
Standard library only. A symbol that fails keeps its previous price; the file is rewritten only when a price changed.
"""
import json
import re
import sys
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "prices.json"
URL = "https://query1.finance.yahoo.com/v8/finance/chart/{}?range=5d&interval=1d"
AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0 Safari/537.36"


def fetch(sym):
    req = urllib.request.Request(URL.format(sym), headers={"User-Agent": AGENT})
    with urllib.request.urlopen(req, timeout=20) as res:
        meta = json.load(res)["chart"]["result"][0]["meta"]
    day = datetime.fromtimestamp(meta["regularMarketTime"], timezone.utc).strftime("%Y-%m-%d")
    return {"price": round(float(meta["regularMarketPrice"]), 4), "currency": meta["currency"], "date": day}


def main():
    syms = sorted(set(re.findall(r'\bsym: "([A-Za-z0-9.^=-]+)"', (ROOT / "index.html").read_text(encoding="utf-8"))))
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
