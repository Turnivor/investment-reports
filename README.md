# Officium Advocati Diaboli

*Fortuna vitrea est.* Fortune is glass: just when it shines, it shatters.

Personal stock and industry research, made with Claude Code and the [ai-berkshire](https://github.com/xbtlin/ai-berkshire) framework (Buffett / Munger / Duan Yongping / Li Lu).

> Not investment advice. AI-assisted research; verify before acting.

**Website:** https://turnivor.github.io/investment-reports/

| Date | Report | Type | Verdict |
|---|---|---|---|
| 2026-10-11 | [HDFC Bank (HDB)](reports/HDFC-Bank/HDFC-Bank-research-20261011.md) | Company | Small staged buy; better < ₹600 |
| 2026-10-11 | [India financial services funnel](reports/industry/IndiaFinancials-funnel-20261011.md) | Industry | Favor ICICI Bank, HDFC Bank, HDFC AMC |
| 2026-10-11 | [India financial services](reports/industry/IndiaFinancials-industry-20261011.md) | Industry | Favor private banks and asset managers |
| 2026-10-11 | [Xylem (XYL)](reports/Xylem/Xylem-research-20261011.md) | Company | Hold; buy < $85 |
| 2026-10-11 | [Pentair (PNR)](reports/Pentair/Pentair-research-20261011.md) | Company | Hold; buy < $47 |
| 2026-10-11 | [Xylem vs Pentair quality screen](reports/Water/Xylem-vs-Pentair-quality-screen-20261011.md) | Comparison | Both pass; Pentair cheaper |
| 2026-10-11 | [Water technology funnel](reports/industry/WaterTechnology-funnel-20261011.md) | Industry | Favor Veralto, A. O. Smith, Pentair |
| 2026-10-09 | [Oklo (OKLO)](reports/Oklo/Oklo-research-20261009.md) | Company | Avoid at $34; speculative only < $20 |
| 2026-10-09 | [Advanced Nuclear & SMR value chain](reports/industry/AdvancedNuclear-SMR-industry-20261009.md) | Industry | Favor fuel-cycle chokepoints & existing fleets (BWXT, CCJ, CEG) |
| 2026-10-06 | [Rheinmetall](reports/Rheinmetall/Rheinmetall-research-20261006.md) ([PDF](reports/Rheinmetall/Rheinmetall-research-20261006.pdf)) | Company | Gray zone; buy < €700 |
| 2026-02-26 | [Flutter Entertainment (FLUT)](reports/FLUT/FLUT-pre-earnings-20260226.md) ([PDF](reports/FLUT/FLUT_Analysis_20260226.pdf)) | Pre-earnings trade | Hold; wait for guidance |

Charts: [`charts/`](charts/)

## The site

| File | What it is |
|---|---|
| [`index.html`](index.html) | Reports page: the list, filters, and the reader with a summary card |
| [`commands.html`](commands.html) | [Command cheat sheet](https://turnivor.github.io/investment-reports/commands.html) for the ai-berkshire commands |
| [`site.css`](site.css) | Shared look for both pages (colours, fonts, top menu) |
| [`og.png`](og.png) | Preview image shown when the link is shared |
| [`brand/`](brand/) | Emblem, seal and browser-tab icons |

GitHub Pages serves the site from `main` / root. There is no build step.

## Adding a report

1. Put the `.md` file in `reports/<Company>/` (and the PDF next to it, if there is one).
2. Add one entry to the `REPORTS` list at the top of the script in `index.html`:
   - **Always:** `id`, `file`, `date`, `ticker`, `venue`, `kind`, `title`, `px`, `blurb`, `verdict`, `tone` (`bad`, `warn` or `good`)
   - **Summary card:** `headline`, `reasons` (3 lines), `watch` (signals), `next` (`text`, plus `until` if it has a date)
   - **Optional:** `pdf`, and `bands` (`cur`, `bear`, `base`, `bull`, `price`, `zone`, `zoneLabel`, `note`) for the value-range bar
3. Every line in the summary must come from the report itself.
   - **Currency:** add the National Bank of Romania rates for the research date to the `FX` table (lei per 1 unit) so the card can show the price in euros and lei, and refresh `INFLATION` if a newer figure is out.
4. Add a row to the table above, commit and push.

The age tag ("12 days old", "needs a refresh" after 90 days) is worked out from `date`, so it needs no upkeep.
