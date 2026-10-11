# Officium Advocati Diaboli

*Fortuna vitrea est.* Fortune is glass: just when it shines, it shatters.

Personal stock and industry research, made with Claude Code and the [ai-berkshire](https://github.com/xbtlin/ai-berkshire) framework (Buffett / Munger / Duan Yongping / Li Lu).

> Not investment advice. AI-assisted research; verify before acting.

**Website:** https://turnivor.github.io/investment-reports/

<!-- reports:start -->
| Date | Report | Type | Verdict |
|---|---|---|---|
| 2026-10-11 | [Xylem (XYL)](reports/Xylem/Xylem-research-20261011.md) ([PDF](reports/Xylem/Xylem-research-20261011.pdf)) | Company | Hold · buy < $85 |
| 2026-10-11 | [Xylem vs Pentair: Quality Screen](reports/Water/Xylem-vs-Pentair-quality-screen-20261011.md) ([PDF](reports/Water/Xylem-vs-Pentair-quality-screen-20261011.pdf)) | Comparison | Both pass · Pentair cheaper |
| 2026-10-11 | [Water Technology Funnel](reports/industry/WaterTechnology-funnel-20261011.md) ([PDF](reports/industry/WaterTechnology-funnel-20261011.pdf)) | Industry | Favor VLTO · AOS · PNR |
| 2026-10-11 | [Pentair (PNR)](reports/Pentair/Pentair-research-20261011.md) ([PDF](reports/Pentair/Pentair-research-20261011.pdf)) | Company | Hold · buy < $47 |
| 2026-10-11 | [India Financial Services Funnel](reports/industry/IndiaFinancials-funnel-20261011.md) ([PDF](reports/industry/IndiaFinancials-funnel-20261011.pdf)) | Industry | Favor ICICI · HDFC Bank · HDFC AMC |
| 2026-10-11 | [India Financial Services](reports/industry/IndiaFinancials-industry-20261011.md) ([PDF](reports/industry/IndiaFinancials-industry-20261011.pdf)) | Industry | Favor private banks · AMCs |
| 2026-10-11 | [HDFC Bank (HDB)](reports/HDFC-Bank/HDFC-Bank-research-20261011.md) ([PDF](reports/HDFC-Bank/HDFC-Bank-research-20261011.pdf)) | Company | Small staged buy · better < ₹600 |
| 2026-10-09 | [Oklo (OKLO)](reports/Oklo/Oklo-research-20261009.md) ([PDF](reports/Oklo/Oklo-research-20261009.pdf)) | Company | Avoid · speculative < $20 |
| 2026-10-09 | [Advanced Nuclear & SMR Value Chain](reports/industry/AdvancedNuclear-SMR-industry-20261009.md) ([PDF](reports/industry/AdvancedNuclear-SMR-industry-20261009.pdf)) | Industry | Favor BWXT · CCJ · CEG |
| 2026-10-06 | [Rheinmetall (RHM)](reports/Rheinmetall/Rheinmetall-research-20261006.md) ([PDF](reports/Rheinmetall/Rheinmetall-research-20261006.pdf)) | Company | Gray zone · buy < €700 |
| 2026-02-26 | [Flutter Entertainment (FLUT)](reports/FLUT/FLUT-pre-earnings-20260226.md) ([PDF](reports/FLUT/FLUT-pre-earnings-20260226.pdf)) | Pre-earnings trade | Hold · wait for guidance |
<!-- reports:end -->

Charts: [`charts/`](charts/)

## The site

| File | What it is |
|---|---|
| [`index.html`](index.html) | Reports page: the list, filters, and the reader with a summary card |
| [`commands.html`](commands.html) | [Command cheat sheet](https://turnivor.github.io/investment-reports/commands.html) for the ai-berkshire commands |
| [`reports.js`](reports.js) | The list of reports the site shows. Made by [`tools/build.py`](tools/build.py) from the block at the top of each report; not edited by hand |
| [`print.html`](print.html) | The paper version of a report, at `print.html#<id>`. [`tools/make_pdf.py`](tools/make_pdf.py) prints it to the PDF offered on each report |
| [`prices.json`](prices.json) | Latest prices, rewritten each weekday at 16:00 UTC by [`tools/fetch_prices.py`](tools/fetch_prices.py) through a GitHub Action. Feeds the "Now" line on each card and the scorecard |
| [`site.css`](site.css) | Shared look for both pages (colours, fonts, top menu) |
| [`og.png`](og.png) | Preview image shown when the link is shared |
| [`brand/`](brand/) | Emblem, seal and browser-tab icons |

GitHub Pages serves the site from `main` / root. There is no build step.

## Adding a report

1. Put the `.md` file in `reports/<Company>/` (and the PDF next to it, if there is one).
2. Start the file with its card: a block between two `---` lines, written as JSON. Copy one from an existing report and change it.
   - **Always:** `id`, `date`, `ticker`, `venue`, `kind`, `title`, `px`, `blurb`, `verdict`, `tone` (`bad`, `warn` or `good`)
   - **Summary card:** `headline`, `reasons` (3 lines), `watch` (signals), `next` (`text`, plus `until` if it has a date)
   - **A single company:** `sym` (its Yahoo Finance symbol), so the site can show today's price and score the verdict, and `benchmark` (`sym`, `name`, `fund`, `day`, `price`): a fund or index for its sector, with its level on the research day. `python tools/fetch_prices.py --base <share sym> <benchmark sym> <report date> <research price>` prints that day and level
   - **What to do next:** `plan` (`none`, `holding`, `add`, `sell`: the report's own rules for someone who does not or does own the share) and `calendar` (a list of `date`, `what`, `check`, plus `approx` when the report only gives a rough time). Both come from the report's decision memo and feed the calendar reminders and the PDF
   - **Optional:** `bands` (`cur`, `bear`, `base`, `bull`, `price`, `zone`, `zoneLabel`, `note`) for the value range, `quote` (`cur`, `price`) when there are no bands, `updates` (dated notes added after the report)
3. Every line in the card must come from the report itself.
4. Run `python tools/make_pdf.py`. It prints the report's paper version (`print.html#<id>`: a working sheet with the verdict, plan and dates, then the full report) to a PDF next to the report, notes it in the card, and then runs `python tools/build.py`, which rebuilds `reports.js` and the table above, fetches the National Bank of Romania rates for the report's date, and stops with a message if the card is missing something. After changing a card later, run `python tools/make_pdf.py <id>` to remake that PDF.
5. Commit and push.

The age tag ("12 days old", "needs a refresh" after 90 days) is worked out from `date`, so it needs no upkeep. If a newer Romanian inflation figure is out, refresh `INFLATION` in `index.html`.
