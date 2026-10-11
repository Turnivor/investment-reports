"""Build the site's data from the reports themselves.

Every report in reports/ starts with a block between two `---` lines that holds its card: verdict, reasons,
signals, checkpoint and value range, written as JSON. This script reads those blocks and writes

  reports.js   the list the site shows, the links between reports and the exchange rates
  calendar/    one .ics file per dated reminder (checkpoints, and the day a verdict turns 90 days old)
  README.md    the table of reports, between the two `reports:` markers

Run it after adding or changing a report:  python tools/build.py
It stops with a message if a block is missing something. Standard library only.
Every report must also have its PDF; python tools/make_pdf.py makes the missing ones and then runs this build.

Exchange rates are the National Bank of Romania reference rates (lei per 1 unit) of the last banking day on or
before each report's date. They are fetched once and kept in tools/fx.json, so later runs need no network.
"""
import json
import re
import sys
import urllib.request
import xml.etree.ElementTree as ET
from datetime import date, timedelta
from decimal import ROUND_HALF_UP, Decimal
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
FX_CACHE = ROOT / "tools" / "fx.json"
BNR = "https://curs.bnr.ro/files/xml/years/nbrfxrates{}.xml"
CURRENCIES = {"$": "USD", "€": "EUR", "₹": "INR", "£": "GBP"}  # symbol used in a report -> National Bank code
TONES = ("bad", "warn", "good")
SITE = "https://turnivor.github.io/investment-reports/"
STALE_DAYS = 90  # same as the site
START, END = "<!-- reports:start -->", "<!-- reports:end -->"

REQUIRE_PDF = True  # tools/make_pdf.py turns this off for the build it runs before printing

problems = []


def read_block(path):
    """The JSON block at the top of a report, or None if the file has none."""
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        return None
    end = text.find("\n---\n", 4)
    if end < 0:
        problems.append(f"{path.name}: the block at the top is never closed with ---")
        return None
    try:
        return json.loads(text[4:end])
    except json.JSONDecodeError as err:
        problems.append(f"{path.name}: the block at the top is not valid JSON ({err})")
        return None


def check(r, path):
    """Collect everything wrong with one report's block."""
    where = path.name
    def need(obj, keys, label=""):
        for key in keys:
            if obj.get(key) in (None, "", []):
                problems.append(f"{where}: {label}{key} is missing")
    need(r, ["id", "date", "ticker", "venue", "kind", "title", "px", "blurb", "verdict", "tone", "headline", "reasons", "watch"])
    if r.get("tone") not in TONES:
        problems.append(f"{where}: tone must be one of {', '.join(TONES)}")
    if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", str(r.get("date", ""))):
        problems.append(f"{where}: date must look like 2026-10-06")
    if len(r.get("reasons") or []) != 3:
        problems.append(f"{where}: reasons needs exactly 3 lines")
    nxt = r.get("next")
    if nxt:
        need(nxt, ["text"], "next.")
        if nxt.get("until") and not re.fullmatch(r"\d{4}-\d{2}-\d{2}", nxt["until"]):
            problems.append(f"{where}: next.until must look like 2026-10-27")
    b = r.get("bands")
    if b:
        need(b, ["cur", "bear", "base", "bull", "price"], "bands.")
        if b.get("cur") not in CURRENCIES:
            problems.append(f"{where}: bands.cur {b.get('cur')!r} is not a known currency; add it to CURRENCIES in tools/build.py")
        if all(isinstance(b.get(k), (int, float)) for k in ("bear", "base", "bull")) and not b["bear"] <= b["base"] <= b["bull"]:
            problems.append(f"{where}: bands should run bear <= base <= bull")
        if b.get("zone") and not b.get("zoneLabel"):
            problems.append(f"{where}: bands.zone needs a zoneLabel")
    q = r.get("quote")
    if q:
        need(q, ["cur", "price"], "quote.")
    if (b or q) and r.get("kind") == "Company" and not r.get("sym"):
        problems.append(f"{where}: a company report needs sym (its Yahoo Finance symbol) for prices and the scorecard")
    bench = r.get("benchmark")
    if r.get("sym") and not bench:
        problems.append(f"{where}: a report with sym needs benchmark (sym, name, fund, day, price) so the scorecard can compare it with its sector")
    if bench:
        need(bench, ["sym", "name", "price"], "benchmark.")
        if not isinstance(bench.get("price"), (int, float)):
            problems.append(f"{where}: benchmark.price must be a number (python tools/fetch_prices.py --base prints it)")
    if r.get("sym") and not (b or q):
        problems.append(f"{where}: sym needs either bands or quote, so the site knows the price at research")
    if r.get("pdf") and not (path.parent / r["pdf"]).exists():
        problems.append(f"{where}: pdf {r['pdf']} is not next to the report")
    if REQUIRE_PDF and not r.get("pdf"):
        problems.append(f"{where}: no PDF yet; run  python tools/make_pdf.py  to make it")
    for u in r.get("updates") or []:
        need(u, ["date", "title", "text"], "updates.")
    plan = r.get("plan")
    if plan:
        for key in ("none", "holding"):
            if key in plan and not isinstance(plan[key], str):
                problems.append(f"{where}: plan.{key} must be one line of text")
        for key in ("add", "sell"):
            if key in plan and not (isinstance(plan[key], list) and plan[key]):
                problems.append(f"{where}: plan.{key} must be a list of signals")
    for c in r.get("calendar") or []:
        need(c, ["date", "what"], "calendar.")
        if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", str(c.get("date", ""))):
            problems.append(f"{where}: calendar.date must look like 2026-10-27 (add approx when the report only gives a rough time)")


def bnr_rates(day, codes):
    """(banking day, {code: lei per 1 unit}) for the last National Bank fixing on or before `day`."""
    for year in (day.year, day.year - 1):
        with urllib.request.urlopen(BNR.format(year), timeout=30) as res:
            tree = ET.parse(res)
        cubes = [c for c in tree.iter() if c.tag.endswith("Cube") and c.get("date") and c.get("date") <= day.isoformat()]
        if cubes:
            cube = max(cubes, key=lambda c: c.get("date"))
            rates = {}
            for rate in cube:
                if rate.get("currency") in codes:
                    rates[rate.get("currency")] = round(float(rate.text) / float(rate.get("multiplier") or 1), 4)
            return cube.get("date"), rates
    raise RuntimeError(f"no National Bank rates on or before {day}")


def exchange_rates(reports):
    """The FX table for the site: {banking day: {code: lei}}, covering every report that shows a value range."""
    cache = json.loads(FX_CACHE.read_text(encoding="utf-8")) if FX_CACHE.exists() else {"days": {}, "for": {}}
    changed = False
    for r in reports:
        if not r.get("bands") or r["bands"].get("cur") not in CURRENCIES:
            continue
        codes = {"EUR", CURRENCIES[r["bands"]["cur"]]}
        day = cache["for"].get(r["date"])
        if day and codes <= set(cache["days"].get(day, {})):
            continue
        try:
            day, rates = bnr_rates(date.fromisoformat(r["date"]), codes)
        except Exception as err:
            problems.append(f"{r['id']}: could not get National Bank rates for {r['date']} ({err})")
            continue
        if not codes <= set(rates):
            problems.append(f"{r['id']}: the National Bank lists no rate for {', '.join(sorted(codes - set(rates)))} on {day}")
            continue
        cache["days"].setdefault(day, {}).update(rates)
        cache["for"][r["date"]] = day
        changed = True
        print(f"Fetched National Bank rates of {day} for {r['id']}")
    if changed:
        FX_CACHE.write_text(json.dumps(cache, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    used = {cache["for"][r["date"]] for r in reports if r.get("bands") and r["date"] in cache["for"]}
    return {day: cache["days"][day] for day in sorted(used)}


def money(cur, v):
    """Same rounding as the site: two decimals under 100, none from 100 up."""
    if v < 100:
        return cur + f"{v:,.2f}".rstrip("0").rstrip(".")
    return cur + f"{int(Decimal(str(v)).quantize(Decimal('1'), ROUND_HALF_UP)):,}"


def day_text(iso):
    return date.fromisoformat(iso).strftime("%d %b %Y")


def notes(r, intro):
    """What a reminder carries: what to check, where the report stood, its own rules, and where to go afterwards."""
    b, p = r.get("bands"), r.get("plan") or {}
    lines = [*intro, "", f"WHERE THE REPORT STOOD ({day_text(r['date'])})", f"Verdict: {r['verdict']}"]
    if b:
        lines.append(f"Price then {money(b['cur'], b['price'])} · bear {money(b['cur'], b['bear'])} · base {money(b['cur'], b['base'])} · bull {money(b['cur'], b['bull'])}")
        if b.get("zoneLabel"):
            lines.append(b["zoneLabel"])
    else:
        lines.append(f"Price then {r['px']}")
    if p.get("holding"):
        lines += ["", "IF YOU HOLD IT", p["holding"]]
    if p.get("add"):
        lines += ["", "SIGNALS TO ADD", *("• " + x for x in p["add"])]
    if p.get("sell"):
        lines += ["", "SIGNALS TO SELL", *("• " + x for x in p["sell"])]
    if not p:
        lines += ["", "SIGNALS TO WATCH", *("• " + x for x in r["watch"])]
    lines += ["", "AFTERWARDS", f"Report: {SITE}#{r['id']}"]
    if r.get("pdf"):
        lines.append(f"PDF: {SITE}{r['pdf']}")
    lines += ["To update the report, copy the request on its page into Claude Code.", "", "Research notes, not investment advice."]
    return "\n".join(lines)


def events_of(r):
    """Every dated reminder of a report: its checkpoints and the day its verdict turns 90 days old."""
    dated = r.get("calendar") or ([{"date": r["next"]["until"], "what": "Checkpoint", "check": r["next"]["text"]}] if (r.get("next") or {}).get("until") else [])
    out = []
    for c in dated:
        intro = [f"Date not confirmed. The report says: {c['approx']}."] if c.get("approx") else []
        if c.get("check"):
            intro += ["WHAT TO CHECK", c["check"]]
        out.append({**c, "title": f"{r['title']}: {c['what']}" + (" (date to confirm)" if c.get("approx") else ""), "notes": notes(r, intro)})
    refresh = (date.fromisoformat(r["date"]) + timedelta(days=STALE_DAYS + 1)).isoformat()
    out.append({"date": refresh, "what": "Refresh the verdict", "check": f"It turns {STALE_DAYS} days old.", "refresh": True, "title": f"{r['title']}: refresh the verdict",
                "notes": notes(r, [f"The verdict of {day_text(r['date'])} turns {STALE_DAYS} days old. Rerun the research before relying on it."])})
    out.sort(key=lambda e: e["date"])
    for e in out:
        slug = re.sub(r"[^a-z0-9]+", "-", e["what"].lower()).strip("-")[:40]
        e["ics"] = f"calendar/{r['id']}-{e['date']}-{slug}.ics"
    return out


def ics(r, e):
    """One all-day event as a calendar file, which a phone or computer opens in its own calendar app."""
    def text(value):
        return value.replace("\\", "\\\\").replace(";", "\\;").replace(",", "\\,").replace("\n", "\\n")

    def fold(line):  # lines are at most 75 bytes; longer ones continue on the next line after a space
        raw, parts = line.encode("utf-8"), []
        while len(raw) > (75 if not parts else 74):
            cut = 75 if not parts else 74
            while (raw[cut] & 0xC0) == 0x80:  # never split a character
                cut -= 1
            parts.append(raw[:cut]); raw = raw[cut:]
        parts.append(raw)
        return b"\r\n ".join(parts).decode("utf-8")

    start = date.fromisoformat(e["date"])
    lines = [
        "BEGIN:VCALENDAR", "VERSION:2.0", "PRODID:-//Officium Advocati Diaboli//Reports//EN", "CALSCALE:GREGORIAN",
        "BEGIN:VEVENT",
        f"UID:{Path(e['ics']).stem}@turnivor.github.io",
        f"DTSTAMP:{r['date'].replace('-', '')}T000000Z",
        f"DTSTART;VALUE=DATE:{start:%Y%m%d}",
        f"DTEND;VALUE=DATE:{start + timedelta(days=1):%Y%m%d}",
        f"SUMMARY:{text(e['title'])}",
        f"DESCRIPTION:{text(e['notes'])}",
        f"URL:{SITE}#{r['id']}",
        "TRANSP:TRANSPARENT",
        "BEGIN:VALARM", "ACTION:DISPLAY", f"DESCRIPTION:{text(e['title'])}", "TRIGGER:-PT15H", "END:VALARM",  # 09:00 the day before
        "END:VEVENT", "END:VCALENDAR",
    ]
    return "\r\n".join(fold(line) for line in lines) + "\r\n"


def write_calendar(reports):
    """Write one .ics file per reminder into calendar/, and clear out the ones no report asks for any more."""
    folder = ROOT / "calendar"
    folder.mkdir(exist_ok=True)
    wanted = set()
    for r in reports:
        for e in r["events"]:
            path = ROOT / e["ics"]
            wanted.add(path.name)
            body = ics(r, e).encode("utf-8")
            if not path.exists() or path.read_bytes() != body:
                path.write_bytes(body)
    for old in folder.glob("*.ics"):
        if old.name not in wanted:
            old.unlink()


def readme_table(reports):
    rows = ["| Date | Report | Type | Verdict |", "|---|---|---|---|"]
    for r in reports:
        name = f"{r['title']} ({r['ticker']})" if r.get("sym") else r["title"]
        pdf = f" ([PDF]({r['pdf']}))" if r.get("pdf") else ""
        rows.append(f"| {r['date']} | [{name}]({r['file']}){pdf} | {r['kind']} | {r['verdict']} |")
    return "\n".join(rows)


def main():
    reports = []
    for path in sorted((ROOT / "reports").rglob("*.md")):
        block = read_block(path)
        if block is None:
            if not any(path.name in p for p in problems):
                problems.append(f"{path.name}: no block at the top, so it would not appear on the site")
            continue
        check(block, path)
        folder = path.parent.relative_to(ROOT).as_posix()
        entry = {"id": block.get("id"), "file": f"{folder}/{path.name}", **{k: v for k, v in block.items() if k != "id"}}
        if entry.get("pdf"):
            entry["pdf"] = f"{folder}/{entry['pdf']}"
        reports.append(entry)
    ids = [r["id"] for r in reports]
    for dup in sorted({i for i in ids if ids.count(i) > 1}):
        problems.append(f"id {dup!r} is used by more than one report")
    reports.sort(key=lambda r: (r.get("date") or "", r.get("id") or ""), reverse=True)
    fx = exchange_rates(reports) if not problems else {}

    if problems:
        print("Not built. Fix these first:", file=sys.stderr)
        for p in problems:
            print("  - " + p, file=sys.stderr)
        sys.exit(1)

    for r in reports:
        r["events"] = events_of(r)
    write_calendar(reports)

    data = {
        "reports": reports,
        # a link from one report to another is recognised by the other report's file name
        "links": [[Path(r["file"]).stem, r["id"]] for r in reports],
        "fx": fx,
        "currencies": CURRENCIES,
    }
    (ROOT / "reports.js").write_text(
        "/* Made by tools/build.py from the block at the top of each report. Do not edit by hand. */\n"
        "window.SITE_DATA = " + json.dumps(data, indent=1, ensure_ascii=False) + ";\n", encoding="utf-8")

    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    if START in readme and END in readme:
        head, rest = readme.split(START, 1)
        readme = head + START + "\n" + readme_table(reports) + "\n" + END + rest.split(END, 1)[1]
        (ROOT / "README.md").write_text(readme, encoding="utf-8")
    else:
        print("README.md has no reports markers, so its table was left alone", file=sys.stderr)
    print(f"Built reports.js and the README table from {len(reports)} reports")


if __name__ == "__main__":
    main()
