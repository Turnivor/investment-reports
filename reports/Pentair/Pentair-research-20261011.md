---
{
  "id": "pentair",
  "date": "2026-10-11",
  "ticker": "PNR",
  "sym": "PNR",
  "benchmark": {
    "sym": "XLI",
    "name": "US industrials",
    "fund": "Industrial Select Sector SPDR ETF",
    "day": "2026-10-09",
    "price": 169.25
  },
  "venue": "NYSE",
  "kind": "Company",
  "title": "Pentair",
  "px": "$52.47",
  "blurb": "Pool, filtration and pump maker with 25% margins. Down 53% in a year after pool distributors cut inventory and guidance was cut.",
  "verdict": "Hold · buy < $47",
  "tone": "warn",
  "headline": "Hold or wait. Cheap, but trust has to be re-earned.",
  "reasons": [
    "Pool sales fell 42% in Q2 2026 as distributors cut about $170m of inventory. Full-year EPS guidance was cut to $4.60 to $4.80.",
    "Management admitted a modest loss of share in pool replacement equipment, and there were three people in the CFO seat in 2026.",
    "The price is 11 times 2026 earnings with an 8% free cash flow yield. The base case is worth about $63 today, the bear case about $30."
  ],
  "watch": [
    "A third pool guidance cut",
    "Pool margin guided below 30% for 2027",
    "Further admitted share loss",
    "Net debt staying above 2.5 times EBITDA into 2028"
  ],
  "next": {
    "text": "Q3 2026 results, expected 23 October 2026. They show whether the pool destock is over.",
    "until": "2026-10-23"
  },
  "bands": {
    "cur": "$",
    "bear": 30.3,
    "base": 63.1,
    "bull": 84.6,
    "price": 52.47,
    "zone": 47,
    "zoneLabel": "Margin of safety below $47",
    "note": "3-year scenario targets, discounted to today at 10%."
  }
}
---

# Pentair (NYSE: PNR): Four-Masters Investment Research

> Research date: 2026-10-11 · Price at research: **$52.47** (close 9 Oct 2026, StockAnalysis and MarketBeat) · Currency: USD
> Framework: AI Berkshire `/investment-research` (Buffett · Munger · Duan Yongping · Li Lu). Written in English at the reader's request.
> Companion reports: [Xylem research](../Xylem/Xylem-research-20261011.md) · [Xylem vs Pentair quality screen](../Water/Xylem-vs-Pentair-quality-screen-20261011.md) · [Water technology funnel](../industry/WaterTechnology-funnel-20261011.md)
> **Educational research only. Not investment advice.**

> **Currency and your money:** this report is written in US dollars. Price $52.47 ≈ €46.77 ≈ 250 lei. National Bank of Romania reference rates of 9 Oct 2026: 1 EUR = 5.3414 lei, 1 USD = 4.7612 lei. Figures in lei and euros are conversions at that day's rate and move with it.


---

## 0. Information richness rating and AI limitations

| Item | Assessment |
|---|---|
| **Information richness** | **Grade A.** S&P 500 member, 17 to 18 analysts, decades of filings, 50 straight years of dividend increases. |
| Main AI research trap | Two opposite traps. Before July 2026 the consensus was "margin-expansion compounder". After July it flipped to "broken story". An AI summary will echo whichever is louder. This report tries to separate what actually broke (pool channel, forecasting, trust) from what did not (two of three segments, cash generation). |
| Data gaps | macrotrends.net blocked automated access, so SEC XBRL filings are the primary source and StockAnalysis the second. Not found: Pentair's own pool market share, its replacement share of sales, the 2028 targets from the March 2026 Investor Day, any insider purchases since July. Figures before 2018 are distorted by the nVent spin-off and are shown on a continuing-operations basis where available. |
| Bias self-check | A 53% fall in a year makes anything look cheap. The test used here is whether the 2025 pool profit was real or was inflated by distributors stocking up. Part of it was inflated. |

---

## 1. Data collection and cross-validation

### 1.1 Key facts

| Metric | Value | Source |
|---|---|---|
| Share price (9 Oct 2026) | $52.47 | StockAnalysis / MarketBeat |
| Shares outstanding | 159.64M | StockAnalysis (161.61M at 31 Mar 2026 per 10-Q, before Q2 buybacks) |
| Market cap | $8.38bn | Tool check, see 1.2 |
| 52-week range | $51.13 to $112.26 | StockAnalysis / Investing.com |
| 1-year / YTD price change | about -53% / about -50% | StockAnalysis / calculated |
| FY2025 revenue | $4,176m (+2.3%) | SEC XBRL / StockAnalysis |
| FY2025 GAAP operating income | $857.5m (20.5% margin) | SEC XBRL |
| FY2025 adjusted operating margin | 25.2% | Q4 2025 release |
| FY2025 net income | $653.8m | SEC XBRL / StockAnalysis |
| FY2025 GAAP EPS (continuing) / adjusted EPS | $3.93 / $4.92 | Q4 2025 release |
| FY2025 free cash flow | $748.4m | Company (StockAnalysis: $746.0m) |
| Q2 2026 sales | $932.6m (-17.0%); Pool segment -42% | Q2 2026 release |
| FY2026 guidance (cut in July) | Sales -4% to -7%, adjusted EPS **$4.60 to $4.80** (was $5.30 to $5.40), Pool sales -18% to -22% | Q2 2026 release (28 Jul 2026) |
| Consensus EPS 2026E / 2027E | $4.64 / $5.22 | StockAnalysis |
| Net debt (30 Jun 2026) | $1,514m excluding leases | Q2 2026 release |
| Taco acquisition | About $1.4bn cash, closed 1 Oct 2026, funded with term loans | Company releases |
| Estimated net debt after Taco | about $3.0bn to $3.1bn, about 2.4x EBITDA (estimate; company figure for leverage) | Q2 2026 slides |
| Dividend | $1.08 a year (2.06% yield), 50th consecutive annual increase | Company |
| Buybacks, H1 2026 | $348m (4.0M shares at about $100 and about $75) | Q2 2026 release |
| Analyst price target (avg) | $75.33 (StockAnalysis) or $86.44 (MarketBeat, includes stale targets) | Both |
| Next results | Q3 2026, expected 23 Oct 2026 | StockAnalysis (estimated date) |

### 1.2 Tool-verified checks (`financial_rigor.py`)

| Check | Result |
|---|---|
| Market cap = $52.47 × 159.64M | **$8.38bn**. Matches reported $8.38bn, deviation 0.04%. ✅ |
| FY2025 revenue, 2 sources | $4,176.0m vs $4,176m. ✅ deviation 0.00% |
| FY2025 net income, 2 sources | $653.8m vs $654m. ✅ deviation 0.03% |
| FY2025 free cash flow, 2 sources | $748.4m vs $746.0m. ✅ deviation 0.3% |
| Net debt 30 Jun 2026, 2 sources | $1,514m vs $1,670m. ⚠️ 10% apart. The difference is lease liabilities. Ex-lease figure used. |
| P/E on 2026 guidance midpoint ($4.70) | 52.47 / 4.70 = **11.16x** |
| P/E on trailing GAAP EPS ($3.98) | 52.47 / 3.98 = **13.18x** |
| Price to book ($23.49 a share) | **2.23x** |
| Price to free cash flow ($4.22 a share, trailing) | **12.43x**, free cash flow yield **8.04%** |
| Dividend yield | 1.08 / 52.47 = **2.06%** |
| Analyst price target, 2 sources | $75.33 vs $86.44. ❌ 15% apart. The lower, more recent figure is the better guide. |

### 1.3 The financial record (SEC XBRL, continuing operations, $m)

| Year | Revenue | Gross margin | GAAP op. margin | Adjusted op. margin | Net income (cont.) | GAAP EPS (cont.) | Adj. EPS | ROE | Free cash flow | Shares (M, year-end) |
|---|---|---|---|---|---|---|---|---|---|---|
| 2016 | 2,781 | 34.5% | 12.7% | n/a | 178 | 0.97 | n/a | distorted | about 337 | 181.8 |
| 2017 | 2,846 | 34.7% | 13.3% | 17.5% | 114 | 0.62 | 1.94 | distorted | 243 | 180.3 |
| 2018 | 2,965 | 35.3% | 14.7% | 18.1% | 322 | 1.81 | 2.35 | distorted | 410 | 171.4 |
| 2019 | 2,957 | 35.6% | 14.6% | 17.5% | 362 | 2.12 | 2.38 | 18.8% | 287 | 168.3 |
| 2020 | 3,018 | 35.0% | 15.3% | 17.2% | 357 | 2.13 | 2.50 | 17.7% | 512 | 166.1 |
| 2021 | 3,765 | 35.0% | 16.9% | 18.2% | 556 | 3.32 | 3.40 | 24.4% | 557 | 165.1 |
| 2022 | 4,122 | 33.1% | 14.4% | 18.6% | 483 | 2.92 | 3.68 | 18.7% | 283 | 164.5 |
| 2023 | 4,105 | 37.0% | 18.0% | 20.8% | 623 | 3.75 | 3.75 | 21.0% | 550 | 165.3 |
| 2024 | 4,083 | 39.2% | 19.7% | 23.5% | 626 | 3.74 | 4.33 | 18.4% | 693 | 164.8 |
| 2025 | 4,176 | 40.5% | 20.5% | 25.2% | 650 | 3.93 | 4.92 | 17.6% | 748 | 163.2 |

Notes: Pentair spun off its electrical business as nVent in April 2018 and sold its valves business in 2017, so equity and ROE before 2019 are not comparable. Revenue has barely grown since 2022 ($4.1bn to $4.2bn). Almost all profit growth since then came from margin: gross margin rose from 33.1% to 40.5%.

---

## 2. The business: Duan Yongping's "right business"

**One sentence:** Pentair makes pool pumps, filters and heaters, water filtration and ice machines, and industrial and commercial pumps, and most of what it sells replaces something that has worn out.

### 2.1 Where the money comes from (FY2025, as reported)

| Segment | Revenue | Share | Segment margin | What it sells | 2025 growth |
|---|---|---|---|---|---|
| Pool | $1,559m | 37% | **33.8%** | Pool pumps, filters, heaters, automation | +9% |
| Flow | $1,554m | 37% | 23.3% | Residential, commercial and industrial pumps | +3% |
| Water Solutions | $1,062m | 25% | 23.9% | Filtration (Everpure), commercial ice (Manitowoc), residential treatment | -6% |
| **Total** | **$4,176m** | | **25.2%** | | **+2.3%** |

Pool was 37% of sales but about **46% of segment profit**. About 70% of sales are in the United States. One pool distributor accounted for about **18% of total company sales** in 2025 (15% in 2024). With Taco included, the mix moves to about 48% Water Solutions, 28% Pool and 24% Flow (company slides, on the new 2026 segment basis).

### 2.2 What happened in 2026

| Date | Event |
|---|---|
| 3 Feb | Q4 2025 beat. 2026 guidance: sales +3 to 4%, adjusted EPS $5.25 to $5.40. |
| 28 Apr | Q1 fine, but management said pool distributors had bought early ahead of price rises. Shares fell about 10%. |
| 10 Jul | CFO Nicholas Brazis left after about four months in the job. |
| 14 Jul | Profit warning. Q2 sales came in 17% below last year against guidance of +1%. Pool distributors cut about $170m of inventory in one quarter. Full-year adjusted EPS guidance cut to $4.60 to $4.80. Shares fell 15% the next day to $64.33. |
| 28 Jul | CEO John Stauch: "We made some decisions that need to be reversed." He admitted a modest loss of share in replacement equipment and strained relations with smaller distributors and dealers. The same day Pentair announced the $1.4bn Taco acquisition. |
| Aug to Oct | Shareholder class actions filed. New CFO Bob Hau (ex-Fiserv) named, starting 1 Nov. Taco closed 1 Oct. Shares drifted to a low of $51.13. |

### 2.3 Is it a good business?

**What is good about it**

- **Replacement demand.** A pool pump that fails gets replaced that season. Peer Hayward says about 85% of its North American residential pool sales are aftermarket. Taco, the new acquisition, says the same of its hydronic products.
- **High margins and high returns.** Adjusted operating margin rose from 17.5% in 2019 to 25.2% in 2025. ROE has averaged about 19% since the spin-off. Capital spending is under 2% of sales.
- **Cash.** Free cash flow exceeded net income in three of the last five years, and operating cash flow has averaged 1.07 times net income.
- **A three-player pool market.** Pentair, Hayward and Fluidra supply most pool equipment in North America.

**What is not so good**

- **The pool profit was partly borrowed from the future.** Distributors stocked up in 2025 ahead of price increases. Pool sales grew 9% in 2025 and are guided down 18 to 22% in 2026. Management's "starting point" for 2027 is about $1.45bn, which is still below 2025.
- **Pricing was pushed too far.** Price added 5.1 points to pool growth in 2025 while volume added 1.4. Management has now admitted share loss and that some decisions need reversing. That is a sign that the margin gains leaned on customers, not only on efficiency.
- **Customer concentration.** A single distributor at 18% of company sales can change a quarter on its own, and just did.
- **No real growth for three years.** Sales were $4.12bn in 2022 and $4.18bn in 2025, and volume fell in 2025 (-2.1%).
- **The Q2 2026 margin was flattered.** The 25.4% adjusted margin included about $35m of one-off tariff refunds, worth about 3.8 points.

> **Duan Yongping's question: what is good about this business, in one sentence?**
> It replaces worn-out equipment in millions of pools and buildings at a 25% margin with little capital. The uncomfortable addition: management tried to squeeze the customer harder than the product justified, and "doing the right thing" for customers is the part of the business that just failed.

---

## 3. Moat: Buffett's "economic moat"

| Moat type | Test | Evidence | Strength |
|---|---|---|---|
| Brand / pricing power | Can it raise prices without losing volume? | Yes for years: gross margin went from 33% to 40.5%. In 2026 the limit was found. Price kept rising, volume fell, share was lost. | ★★★ (was ★★★★) |
| Switching costs | How costly is it to move? | Pool automation ties pumps, heaters and lights to one brand's controller. Dealers are trained on one brand. But a single failed pump can be swapped for a Hayward or Fluidra unit, which is where share was lost. | ★★★ |
| Network effects | Does it get better with more users? | Indirect only: a large dealer network makes the brand easier to buy and service. Relations with small dealers are now strained. | ★★ |
| Scale | Does size lower cost? | One of three large pool suppliers. Leader in commercial ice with Manitowoc. Scale in sourcing helped absorb tariffs. | ★★★ |
| Technology / regulation | Is it protected? | Variable-speed pump rules pushed upgrades and favoured the big three. Filtration certifications. Nothing exclusive. | ★★ |

**Trend:** narrower than a year ago, by management's own admission. The damage looks modest and specific to pool replacement equipment for older pools. Flow and Water Solutions posted record margins in Q2 2026. Whether the share loss stops or spreads is the single most important thing to watch.

> **Buffett's question: will the moat still be there in ten years, and what could destroy it?**
> The installed base will still be there, and so will the three-player structure. What could destroy the moat is exactly what 2026 revealed: treating pricing power as unlimited. A brand that dealers resent is a brand they stop recommending.

---

## 4. Inversion and risk list: Munger's "invert, always invert"

### 4.1 How this investment could fail

| Path | Probability | Impact | Comment |
|---|---|---|---|
| Pool share loss continues and the 2027 rebound to about $1.45bn does not arrive | Medium | High | Pool was 46% of segment profit. Q3 pool guidance is -23 to -25%. |
| Pool margins settle well below the old 33 to 34% because prices must be given back | Medium | High | Management says 2027 margins will "start with a three". Unproven. |
| Housing and consumer weakness keeps new pools and remodels depressed | Medium-high | Medium | Management assumes little or no US residential recovery in 2026. |
| Taco was the wrong deal at the wrong time | Medium | Medium | $1.4bn in cash while guidance was being cut and the CFO seat was empty. Leverage rises to about 2.4x. Paid about 10.5 times EBITDA after synergies and tax benefits. |
| More bad news in forecasting: another guidance cut | Medium | High | Two pool guidance cuts already in 2026. Credibility is low, so the reaction to a third would be severe. |
| Securities class actions | Certain to proceed, outcome unknown | Low-medium | Usually settled and insured, but a distraction. Not modelled. |
| Tariffs return or refunds are reversed | Low-medium | Low-medium | Not modelled. |
| Finance leadership instability | Happened | Medium | Three people in the CFO seat in 2026. Bob Hau starts 1 Nov. |

### 4.2 Historical analogy

Pool equipment has been through this before. In 2022 to 2023 distributors cut inventory after the pandemic boom. Hayward's sales fell about 25% in 2023 and its shares fell by about half, and then recovered as the channel normalized. The pattern (channel overstocks, a sharp one-year drop, demand from the installed base reasserting itself) favours patience.

The difference this time is that Pentair says it also lost share, which Hayward did not report in 2023. A closer parallel for that part is a consumer-products company that pushed price too hard and had to give some back. Those recoveries happen, but margins seldom return to the peak.

### 4.3 Bias check

- **Anchoring:** the 52-week high was $112. That price reflected 2025 profits that were partly pulled forward. It is not a target.
- **"Cheap" bias:** 11 times earnings looks cheap only if $4.70 of earnings is a floor. If pool margins reset lower, it is not.
- **What the bears say:** TD Cowen (Sell, $65), Bank of America (Underperform), BNP Paribas (Underperform, suspects the inventory problem is tied to the largest customer and doubts further margin expansion). RBC called the CFO change "an embarrassing development". Goldman cut its target to $60 on 9 Oct.
- **What the bulls say:** Wolfe upgraded on 15 Sep ($91). Oppenheimer, Baird, Mizuho, Citi, UBS, Deutsche Bank and JPMorgan keep positive ratings on the view that the destock is temporary.

> **Munger's question: where am I most likely to be wrong, and why would smart people not buy?**
> Smart people would not buy because management was surprised by its own largest customer, lost its CFO twice, and then spent $1.4bn. Each alone is forgivable. Together they say the controls were weaker than the margins suggested. The likeliest mistake on the other side is selling a 25%-margin replacement business at 11 times earnings in the worst quarter of a channel correction.

---

## 5. Management: "right people" (Duan) and integrity (Buffett)

### 5.1 Key decisions

| Date | Decision | Result so far | Score |
|---|---|---|---|
| 2018 | Spun off nVent; John Stauch became CEO (CFO since 2007) | Created a focused water company. nVent has done well on its own. | ★★★★ |
| 2021 on | Transformation programme: pricing, sourcing, 80/20 | Adjusted margin up from 17.2% to 25.2%. Part of the pricing has now proved excessive. | ★★★ |
| 2022 | Bought Manitowoc Ice for $1.6bn | Good business at about 30% margins. Standalone results are no longer disclosed. | ★★★ |
| 2025 | Pushed pool price increases and early-buy programmes | Pulled sales into 2025, strained dealer relations, lost share. | ★ |
| Q1 2026 | Bought back $200m of shares at about $100 | Three months before the profit warning. The price is now $52. | ★ |
| Jul 2026 | Admitted the pool mistakes publicly and said decisions would be reversed | Candid and fast. | ★★★★ |
| Jul to Oct 2026 | Bought Taco for about $1.4bn in cash | Diversifies away from Pool into commercial and hydronic markets. Adds debt at a weak moment. Too early to judge. | ★★ |

### 5.2 Alignment

- **CEO ownership is meaningful.** Stauch beneficially owns about 1.47 million shares including units and options (447,000 held directly). At $52.47 the direct holding is worth about $23m, against annual pay of $11.4m.
- **Insiders as a group own 0.6% to 1.3%** depending on whether options and units are counted.
- **No insider buying was found after the July fall.** Two insiders sold near $100 in February 2026. The search of filings was not exhaustive.
- **Dividend discipline is strong:** 50 consecutive annual increases, payout about 25% of earnings.

> **Duan Yongping's question: if the CEO retired, would the company stay competitive?**
> Yes. The more pointed question in 2026 is the reverse: is the current team the right one to repair dealer relationships it damaged? The admission in July was the right first step. The absence of insider buying at half the old price is not encouraging.

---

## 6. Industry and long-run trend: Li Lu's "civilization" lens

- **Is this a civilization-level shift?** No. Pool equipment and building water systems are mature replacement markets that grow with the installed base and with price.
- **The installed base is the asset.** North America has roughly 5 to 6 million residential in-ground pools. Equipment lasts about 8 to 11 years. That base does not shrink in a recession.
- **Tailwinds:** water-quality concerns (PFAS) for residential and commercial filtration, energy-efficiency rules, commercial building and data-centre demand in Flow, hydronic heating and cooling through Taco.
- **Headwinds:** housing turnover, interest rates, consumers repairing instead of upgrading.
- **Position in the value chain:** manufacturer selling through distributors. The distributor layer is concentrated, which gives the largest distributor leverage over inventory and, in time, over price.

> **Li Lu's question: looking back from 2046, is this the Standard Oil of its era or a 3Com?**
> Neither. Pools and buildings will still need pumps and filters. This is a durable, ordinary business. The return will be decided by the price paid and by whether management relearns restraint on pricing.

---

## 7. Valuation and margin of safety

### 7.1 What the market is paying today

| Measure | Now | End of 2025 | 5-year average (2021 to 2025 year-ends) |
|---|---|---|---|
| P/E (GAAP, trailing) | 13.5x | 26.1x | 21.8x |
| Forward P/E | 10.9x | 19.8x | 18.4x |
| EV/EBITDA (before Taco debt) | 9.7x | 17.1x | 16.5x |
| Price to free cash flow | 12.5x | 22.8x | 23.5x |
| Dividend yield | 2.06% | about 1.0% | about 1.2% |

Including the Taco debt and no Taco profit, enterprise value is about $11.3bn, or about 10.8 times the roughly $1.05bn of EBITDA implied by 2026 guidance. Consensus 2026 EPS fell about 13% this year. The share price fell about 50%. Most of the fall is the multiple.

**Peers (StockAnalysis, 9 Oct 2026):** forward P/E for Pentair 10.9x · Fluidra 11.8x · Hayward 12.5x · A. O. Smith 14.5x · Xylem 17.5x · Franklin Electric 20.1x · IDEX 25.5x · Watts Water 26.5x · Badger Meter 27.6x. The three pool names are the three cheapest. The market is marking down pools as a category, not Pentair alone.

### 7.2 Reverse check: what does $52.47 assume?

An 8.0% free cash flow yield means a buyer earns about 10% a year if free cash flow per share grows only 2% a year, with no change in the multiple. The price therefore assumes that 2026's reduced cash flow is close to permanent and barely grows. Management claims a $200m pool rebound in 2027 alone.

### 7.3 Three scenarios over three years (`financial_rigor.py three-scenario`)

Starting point: 2026 adjusted EPS guidance midpoint of $4.70, which excludes Taco.

| Scenario | EPS growth a year | 2029 EPS | P/E in 2029 | Price in 2029 | Change vs $52.47 | Value today (discounted at 10%) |
|---|---|---|---|---|---|---|
| Bull: pool recovers fully, trust returns | 10% | $6.26 | 18x | $112.6 | +114.6% | **$84.6** |
| Base: partial pool recovery, margins hold | 6% | $5.60 | 15x | $84.0 | +60.0% | **$63.1** |
| Bear: share loss continues, pool margins reset | -5% | $4.03 | 10x | $40.3 | -23.2% | **$30.3** |

The base case discounted to today is about $63, roughly 20% above the current price. **A 25% margin of safety on the base case is about $47.** The base multiple of 15x is below Pentair's own five-year average of 18.4x on purpose, because trust has to be rebuilt.

### 7.4 Ten-year discounted view (`terminal_value.py`)

Exit multiple from the perpetual-growth formula only: exit P/E = (1 - g / ROIC) / (r - g).

**The three inputs and why**

| Input | Value | Reason |
|---|---|---|
| r, cost of capital | **10%** (USD) | Framework default for dollar cash flows (range 9 to 11.5%). |
| ROIC on new capital | **13%** | Between the reported ROIC of 14 to 15.6% and the lower return on acquisitions such as Taco at about 10.5 times EBITDA. A judgment. |
| g, growth after 2036 | **3%** base (2% bear, 4% bull) | Long-run nominal US growth. Capped at 4% for USD. |

**Audit result:** all three hard checks passed (currency match, r minus g of at least 5 points in every case, discrete risks kept out of the discount rate). Denominator width: 8, 7 and 6 points.

| Case | Profit growth to 2036 | 2036 profit | Exit P/E | 10-year return a year (incl. 3.5% dividend + buyback) |
|---|---|---|---|---|
| Bear | 2% | $915m | 10.6x | **+5.0%** |
| Base | 5.5% | $1,282m | 11.0x | **+8.9%** |
| Bull | 8% | $1,620m | 11.5x | **+11.8%** |

Starting profit is 2026 adjusted net income of about $750m ($4.70 × 159.64M shares). Market cap $8,376m.

**Sensitivity to r (base case):** at r = 8% the exit P/E is 15.4x and the return is +12.5% a year. At r = 12% the exit P/E is 8.5x and the return is +6.2%. The base case clears the hurdle at 8%, falls about one point short at 10%, and falls well short at 12%. At every r, Pentair's return is 4 to 5 points higher than Xylem's, so the ranking between the two is stable.

### 7.5 Limits of this valuation

- **Not modelled:** the outcome of the securities class actions, and a return of tariffs or a reversal of the refunds. Both are flagged by the audit tool as outside the model.
- Pool share loss and the Taco integration are handled as scenarios (the bear case), not through the discount rate.
- Adjusted EPS is the starting point. Pentair's adjustments include restructuring and "transformation" costs that have recurred every year since 2021 (about $87m forecast for 2026, or about $0.45 a share after tax, estimate). On GAAP earnings the multiples are about 18% higher and the returns lower.
- The bear case may not be bearish enough if pool margins fall to the mid-20s.

> **Buffett's question: if r is wrong by two points, does the conclusion flip?**
> Partly. At 8% this is a clear buy on the base case and at 12% it is not. What does not flip is that Pentair offers more return per dollar than Xylem at any rate tested. The honest reading is "reasonably priced with a wide range of outcomes", not "obviously cheap".

> **Duan Yongping's question: if the market closed for five years, would you hold at this price?**
> Probably yes, because the installed base keeps buying and the cash yield is 8%. The hesitation is not about the business. It is about whether the people running it have understood why the customers got angry.

### In your money: what this means in lei

- **Price:** one share $52.47 ≈ €46.77 ≈ 250 lei; the margin-of-safety level of $47 ≈ €41.89 ≈ 224 lei. National Bank of Romania reference rates of 9 Oct 2026: 1 EUR = 5.3414 lei, 1 USD = 4.7612 lei.
- **Return:** The base case is +8.9% a year over ten years in dollars, in a range of +5.0% to +11.8%. A return in lei is that figure plus or minus the change in the lei price of the dollar. Between 26 Feb and 9 Oct 2026 the leu lost 10.2% against the dollar and 4.8% against the euro (BNR reference rates), which shows how much the exchange rate alone can move a lei result.
- **Inflation:** Romanian inflation was 6.2% a year in August 2026 (INS). The National Bank of Romania forecasts 6.1% for end-2026 and 3.4% for end-2027. The base case is above both figures; the bear case (+5.0%) is below current inflation.


---

## 8. Decision memo

| Dimension | Conclusion | Confidence |
|---|---|---|
| Business quality (Duan) | Good replacement business with high margins. 2025 pool profit was overstated by channel stocking. | Medium-high |
| Moat (Buffett) | Real but narrower than a year ago. Pricing power was overused. | Medium |
| Management (Duan + Buffett) | Strong record to 2024, serious errors in 2025 to 2026, candid about them. Credibility is damaged. | Medium-low |
| Biggest risk (Munger) | Pool share loss and margin reset are not one-off, and a debt-funded deal sits on top. | Medium |
| Long-run trend (Li Lu) | Mature, durable, driven by the installed base. | High |
| Valuation (Buffett + Duan) | Low. About $63 base value against a $52.47 price, with a bear case near $30. | Medium |

| Strategy | Suggestion |
|---|---|
| No position | Wait for the Q3 results on 23 Oct. Interesting below about **$47** (25% under the base value, about 10 times 2026 earnings), or at today's price once the destock is confirmed finished. |
| Already holding | Hold. The price already reflects a poor outcome, and selling at 11 times earnings during a channel correction has historically been the wrong moment in this industry. |
| Signals to sell | A third pool guidance cut · pool margin guided below 30% for 2027 · further admitted share loss · net debt staying above 2.5 times EBITDA into 2028 · a dividend freeze after 50 years of increases. |
| Signals to add | Q3 confirms channel inventory is normal · 2027 pool sales guided at or above $1.45bn · insiders buying shares · the new CFO resets guidance conservatively and then meets it. |

**Verdict: hold / wait. Cheap, but trust has to be re-earned. The next data point is 23 October.**

> **Buffett (simulated):** "I like businesses where the customer has to come back because the pump broke. I don't like finding out that the customer was being charged more each year until he went next door. Price is what you pay. This price leaves room, though not as much as it looks."
>
> **Munger (simulated):** "They raised prices until the dealers revolted, bought back stock at a hundred, lost two CFOs and then did a $1.4 billion deal. I would want to see a year of dull, accurate forecasts before I believed anything they said."
>
> **Duan Yongping (simulated):** "The business is right. The price is close to right. The people made a mistake about the customer. Watch what they do, not what they say, and see whether they put the customer first again."
>
> **Li Lu (simulated):** "The installed base is a real asset and the market is pricing a temporary problem as if it were permanent. That is where opportunities come from. It is also where value traps come from. The difference will be visible in pool share within a year."

---

## 9. AI confidence versus investment certainty

| | Level | Why |
|---|---|---|
| **AI analysis confidence** | High on the numbers, medium on the diagnosis | Grade A information and filings-based data. But the key question (how much pool share was lost and whether it continues) is not answered in any public number. |
| **Investment certainty** | Medium-low for the next year, medium over five | The range between the bear and bull cases is very wide ($30 to $85 in today's money). |

**Based on solid data:** the financial history, the July guidance cut and its size, segment margins, the Taco terms, share count and buybacks, current multiples.
**Based on reasoning from limited information:** how permanent the pool share loss is, where pool margins settle, the 13% return assumed on new capital, the after-tax size of recurring adjustments, and the comparison with Hayward in 2023 (drawn from general knowledge of that episode, not re-verified for this report).

---

## Appendix: cross-validation record and sources

| Data point | Source 1 | Source 2 | Deviation | Status |
|---|---|---|---|---|
| Share price | $52.47 (StockAnalysis) | $52.47 (MarketBeat) | 0.00% | ✅ |
| Market cap | $8.38bn (calculated) | $8.38bn (StockAnalysis) | 0.04% | ✅ |
| FY2025 revenue | $4,176.0m (SEC XBRL) | $4,176m (StockAnalysis) | 0.00% | ✅ |
| FY2025 net income | $653.8m (SEC XBRL) | $654m (StockAnalysis) | 0.03% | ✅ |
| FY2025 free cash flow | $748.4m (company) | $746.0m (StockAnalysis) | 0.3% | ✅ |
| FY2025 GAAP operating income | $857.5m (SEC XBRL) | $973.4m (StockAnalysis) | 13.5% | ⚠️ StockAnalysis excludes unusual items; filings used |
| Net debt, 30 Jun 2026 | $1,514m (company) | $1,670m (StockAnalysis) | 10% | ⚠️ leases |
| Trailing P/E | 13.51 (StockAnalysis) | 13.1 (CompaniesMarketCap) | 3% | ⚠️ timing |
| Analyst price target | $75.33 (StockAnalysis) | $86.44 (MarketBeat) | 15% | ❌ stale targets in the higher figure |

**Data audit (`report_audit.py`, 15% random sample):** 23 points sampled, 23 passed, 0 failed. **Cleared for release.** Prices, market cap, net income, free cash flow, dividend, buybacks, debt and guidance were re-fetched from StockAnalysis and the SEC press release for the audit. About a third of the sampled points were model assumptions or tool outputs, which the audit can only confirm were copied correctly. Valuation inputs were re-run through `terminal_value.py audit` after the final draft: passed, unchanged.

**Sources**

- SEC XBRL company facts (CIK 77360): https://data.sec.gov/api/xbrl/companyfacts/CIK0000077360.json
- FY2025 Form 10-K: https://www.sec.gov/Archives/edgar/data/77360/000007736026000007/pnr-20251231.htm
- Q2 2026 press release: https://www.sec.gov/Archives/edgar/data/0000077360/000007736026000042/q22026pressrelease.htm
- 14 Jul 2026 pre-announcement: https://www.sec.gov/Archives/edgar/data/0000077360/000007736026000039/july2026pre-earningsexhibit.htm
- Q4 2025 press release: https://www.sec.gov/Archives/edgar/data/77360/000007736026000003/a2025q4pressrelease.htm
- 2026 proxy statement: https://www.sec.gov/Archives/edgar/data/77360/000007736026000014/pnr-20260317.htm
- Taco announcement: https://www.businesswire.com/news/home/20260728677398/en/
- New CFO announcement: https://secure.businesswire.com/news/home/20260922021792/en/Pentair-Announces-Bob-Hau-as-Executive-Vice-President-and-Chief-Financial-Officer
- Hayward Form 10-Q (June 2026): https://www.sec.gov/Archives/edgar/data/0001834622/000183462226000047/hayw-20260627.htm
- StockAnalysis: https://stockanalysis.com/stocks/pnr/statistics/ and /financials/ and /forecast/
- MarketBeat: https://www.marketbeat.com/stocks/NYSE/PNR/forecast/
- Q2 2026 call highlights: https://finance.yahoo.com/markets/stocks/articles/pentair-q2-earnings-call-highlights-200356202.html
- Q2 2026 slides summary: https://www.investing.com/news/company-news/pentair-q2-2026-slides-pool-drops-42-taco-deal-expands-platform-93CH-4817332
- Analyst reaction (RBC, BNP): https://finance.yahoo.com/markets/stocks/articles/pentair-shares-plummet-premarket-guidance-113920479.html
- CFO changes: https://www.cfodive.com/news/pentair-brings-back-cfo-interim-finance-chief/825452/

*macrotrends.net could not be read (access blocked), so SEC filings replaced it as the primary source.*
