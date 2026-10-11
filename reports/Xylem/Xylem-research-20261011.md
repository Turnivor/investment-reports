# Xylem (NYSE: XYL): Four-Masters Investment Research

> Research date: 2026-10-11 · Price at research: **$102.71** (close 9 Oct 2026, StockAnalysis and Finviz) · Currency: USD
> Framework: AI Berkshire `/investment-research` (Buffett · Munger · Duan Yongping · Li Lu). Written in English at the reader's request.
> Companion reports: [Pentair research](../Pentair/Pentair-research-20261011.md) · [Xylem vs Pentair quality screen](../Water/Xylem-vs-Pentair-quality-screen-20261011.md) · [Water technology funnel](../industry/WaterTechnology-funnel-20261011.md)
> **Educational research only. Not investment advice.**

> **Currency and your money:** this report is written in US dollars. Price $103 ≈ €91.55 ≈ 489 lei. National Bank of Romania reference rates of 9 Oct 2026: 1 EUR = 5.3414 lei, 1 USD = 4.7612 lei. Figures in lei and euros are conversions at that day's rate and move with it.


---

## 0. Information richness rating and AI limitations

| Item | Assessment |
|---|---|
| **Information richness** | **Grade A.** S&P 500 member, 21 to 23 sell-side analysts, 15 years of filings since the 2011 spin-off from ITT. |
| Main AI research trap | Consensus is strong ("water is a secular winner, 80/20 is lifting margins"). An AI summary tends to repeat it. The bear case and the return-on-capital problem get extra weight below. |
| Data gaps | macrotrends.net blocked automated access, so the 11-year table uses SEC XBRL filings as the primary source and StockAnalysis / Finviz as the second. Not found: market shares by segment, a company-wide end-market split, 10-year average multiples, ROIC before 2021. |
| Bias self-check | The feeling of safety comes from the theme (water) and the amount of coverage. The numbers that matter for an owner are less comfortable: ROE has been below 9% for three years and the free cash flow yield is 4%. |

---

## 1. Data collection and cross-validation

### 1.1 Key facts

| Metric | Value | Source |
|---|---|---|
| Share price (9 Oct 2026) | $102.71 | StockAnalysis / Finviz |
| Shares outstanding | 233.49M (24 Jul 2026) | Q2 2026 10-Q cover / StockAnalysis |
| Market cap | $23.98bn | Tool check, see 1.2 |
| 52-week range | $98.58 to $154.27 | StockAnalysis / Finviz |
| 1-year / YTD price change | about -31% / about -25% | StockAnalysis / Finviz |
| FY2025 revenue | $9,035m (+6% reported, +5% organic) | 10-K / Q4 2025 release |
| FY2025 GAAP operating income | $1,223m (13.5% margin) | SEC XBRL |
| FY2025 adjusted EBITDA margin | 22.2% | Q4 2025 release |
| FY2025 net income | $957m | SEC XBRL / StockAnalysis |
| FY2025 GAAP EPS / adjusted EPS | $3.92 / $5.08 | Q4 2025 release |
| FY2025 free cash flow (OCF minus capex) | $910m | SEC XBRL (StockAnalysis: $873m) |
| Trailing GAAP EPS (to Jun 2026) | $4.20 | StockAnalysis / Finviz ($4.21) |
| FY2026 guidance | Revenue about $9.2bn, organic growth 2 to 3%, adj. EBITDA margin 23.1 to 23.5%, adj. EPS $5.55 to $5.70 | Q2 2026 release (28 Jul 2026) |
| Consensus EPS 2026E / 2027E | $5.66 / $6.23 | StockAnalysis (Finviz 2027E: $6.21) |
| Net debt (30 Jun 2026) | $1,650m excluding leases, 0.8x adj. EBITDA | Q2 2026 release |
| Pending deals after 30 Jun | TriOS ($216m, closed), WaterFleet (about $200m), Cornell Pump + Roper Pump ($1.46bn cash, closing Q4 2026) | 10-Q, company release |
| Estimated net debt after the deals | about $3.5bn (estimate) | Calculated |
| Dividend | $1.72 a year (1.68% yield) | Q4 2025 release / StockAnalysis |
| Buybacks, H1 2026 | $1,243m (shares down 4.1% since year-end) | SEC XBRL |
| Analyst price target (avg) | about $151 to $155, range $112 to $180 | StockAnalysis / MarketBeat |
| Next results | Q3 2026 on 27 Oct 2026 | StockAnalysis / Finviz |

### 1.2 Tool-verified checks (`financial_rigor.py`)

| Check | Result |
|---|---|
| Market cap = $102.71 × 233.49M | **$23.98bn**. Matches reported $23.98bn, deviation 0.01%. ✅ |
| FY2025 revenue, 2 sources | $9,035m vs $9,035m. ✅ deviation 0.00% |
| FY2025 net income, 2 sources | $957m vs $957m. ✅ deviation 0.00% |
| FY2025 free cash flow, 2 sources | $910m vs $873m. ⚠️ 4.1% apart. StockAnalysis counts extra capitalized items as capex. Company-filing basis ($910m) used. |
| Net debt 30 Jun 2026, 2 sources | $1,650m vs $1,779m. ⚠️ 7.8% apart. The difference is lease liabilities. Ex-lease figure used. |
| P/E on 2026 guidance midpoint ($5.625) | 102.71 / 5.625 = **18.26x** |
| P/E on trailing GAAP EPS ($4.20) | 102.71 / 4.20 = **24.45x** |
| Price to book ($49.17 a share) | **2.09x** |
| Price to free cash flow ($4.10 a share, trailing) | **25.05x**, free cash flow yield **3.99%** |
| Dividend yield | 1.72 / 102.71 = **1.67%** |

### 1.3 Eleven years of numbers (SEC XBRL, $m)

| Year | Revenue | Gross margin | GAAP op. margin | Net income | GAAP EPS | Adj. EPS | ROE | Free cash flow | Shares (M, year-end) |
|---|---|---|---|---|---|---|---|---|---|
| 2015 | 3,653 | 38.4% | 12.3% | 340 | 1.87 | 1.85 (est.) | 16.1% | 347 | 178.4 |
| 2016 | 3,771 | 38.8% | 10.8% | 260 | 1.45 | 2.03 | 12.2% | 373 | 179.4 |
| 2017 | 4,707 | 39.2% | 11.7% | 331 | 1.83 | 2.40 | 14.1% | 516 | 179.9 |
| 2018 | 5,207 | 38.9% | 12.6% | 549 | 3.03 | 2.88 | 20.8% | 349 | 179.7 |
| 2019 | 5,249 | 39.0% | 9.3% | 401 | 2.21 | 3.02 | 14.0% | 613 | 180.1 |
| 2020 | 4,876 | 37.5% | 7.5% | 254 | 1.40 | 2.06 | 8.6% | 641 | 180.4 |
| 2021 | 5,195 | 38.0% | 11.3% | 427 | 2.35 | 2.49 | 13.8% | 330 | 180.4 |
| 2022 | 5,522 | 37.7% | 11.3% | 355 | 1.96 | 2.85 | 10.6% | 388 | 180.3 |
| 2023 | 7,364 | 36.9% | 8.9% | 609 | 2.79 | 3.78 | 8.9% | 566 | 241.5 |
| 2024 | 8,562 | 37.5% | 11.8% | 890 | 3.65 | 4.27 | 8.6% | 942 | 243.0 |
| 2025 | 9,035 | 38.5% | 13.5% | 957 | 3.92 | 5.08 | 8.7% | 910 | 243.6 |

Notes: from 2023 the company's adjusted EPS also adds back the amortization of acquired intangibles ($0.90 a share in 2025), so the adjusted series is not like-for-like across 2023. Two deals reshaped the company: Sensus (2016, about $1.7bn) and Evoqua (May 2023, about $7.5bn, paid entirely in shares).

---

## 2. The business: Duan Yongping's "right business"

**One sentence:** Xylem sells the pumps, treatment systems, meters and services that move, clean and measure water for utilities, factories and buildings, and earns a steady stream from replacing and servicing a very large installed base.

### 2.1 Where the money comes from (FY2025)

| Segment | Revenue | Share | Organic growth | Adj. operating margin (2024) | What it sells |
|---|---|---|---|---|---|
| Water Infrastructure | $2,636m | 29% | +3% | 22.1% (17.8%) | Wastewater pumps (Flygt), treatment equipment, dewatering |
| Applied Water | $1,849m | 20% | +2% | 18.4% (16.0%) | Pumps for buildings and industry (Bell & Gossett, Goulds) |
| Measurement & Control | $2,086m | 23% | +9% | 16.9% (17.5%) | Smart meters (Sensus), analytics |
| Water Solutions & Services | $2,464m | 27% | +5% | 17.1% (15.7%) | Ex-Evoqua: industrial treatment, outsourced water, service |
| **Total** | **$9,035m** | | **+5%** | **17.8% (16.0%)** | |

Geography: United States 58%, Western Europe 20%, emerging markets 14%, other 8%. China was about 3% of sales in 2025 and is heading to about 2%. No customer is above 5% of revenue.

### 2.2 Is it a good business?

**What is good about it**

- **Demand is hard to postpone forever.** Wastewater has to be pumped and drinking water has to be treated whatever the economy does. Services are 41% of the Water Solutions segment.
- **Margins are rising.** Adjusted EBITDA margin went from 20.6% in 2024 to 22.2% in 2025, with 23.1 to 23.5% guided for 2026. The company's "80/20" programme (drop the unprofitable 20% of products and customers) is the cause.
- **Cash conversion is solid.** Operating cash flow has averaged 1.4 times net income over five years.
- **Customers are spread out.** No single customer matters.

**What is not so good**

- **Growth is slow right now.** Organic growth was 0% in Q1 2026 and +1% in Q2. Full-year guidance was trimmed to 2 to 3%, against a long-term target of 4 to 6%. Management says walking away from poor business costs about 2 points this year.
- **Returns on the owners' capital are low.** ROE has been 8.6 to 8.9% for three years. Evoqua was paid for with 59 million new shares, which put $6.5bn of goodwill and intangibles on the balance sheet. Goodwill and intangibles are 60% of total assets.
- **Gross margin has not moved in eleven years** (37 to 39%). The margin gains are coming from cost cuts and mix, not from pricing power showing up in gross margin.
- **Adjusted and reported profit are far apart.** 2025 adjusted EPS was $5.08 and GAAP EPS $3.92. Of the $1.16 gap, $0.90 is non-cash amortization (fair to add back) and $0.54 is restructuring, which has appeared every year since 2016.

**Operating leverage:** moderate. A 6% rise in revenue in 2025 produced a 21% rise in GAAP operating income, but much of that was restructuring savings and not volume.

> **Duan Yongping's question: what is good about this business, in one sentence?**
> It sells things cities cannot stop buying, and it gets paid again for parts and service. The honest caveat: it is a good business that was bought at a high price in 2023, and today's shareholders are still earning a single-digit return on that purchase.

---

## 3. Moat: Buffett's "economic moat"

| Moat type | Test | Evidence | Strength |
|---|---|---|---|
| Brand / pricing power | Can it raise prices without losing volume? | Flygt, Bell & Gossett, Goulds and Sensus are specified by name by engineers. Xylem offset an estimated $180m of annual tariff cost in 2025 with price. But gross margin has been flat for a decade. | ★★★ |
| Switching costs | How costly is it to move? | High in metering (Sensus runs on its own licensed radio network, and a utility that picks it stays for 15 to 20 years) and in installed pumps (like-for-like replacement). The $850m, 23-year Dow outsourcing contract is the extreme case. | ★★★★ |
| Network effects | Does it get better with more users? | Very little. The Xylem Vue software platform is growing 30 to 40% a year but is small. | ★ |
| Scale | Does size lower cost? | The largest pure-play water technology company. Scale helps in service coverage, distribution and purchasing. Competitors Grundfos, Sulzer, KSB and Veralto are also large. | ★★★ |
| Technology / regulation | Is it protected? | PFAS treatment know-how from Evoqua, regulatory approvals for meters and treatment. Useful, not exclusive. | ★★★ |

**Trend:** the moat is slowly widening. The exit from low-margin lines, the sale of the international metering business (about $250m of revenue at under 10% margin), and the move into services and outsourced water all push the mix toward stickier revenue. The risk to the trend is that management keeps buying growth: three deals in three months in 2026, including $1.46bn for Cornell and Roper pumps at about 11.6 times EBITDA after synergies and tax benefits.

> **Buffett's question: will the moat still be there in ten years, and what could destroy it?**
> Very likely yes. Nobody has found a substitute for pumping and treating water. The moat is not the worry. The worry is the price paid for adding to it. A wide moat around a business earning 8 to 9% on equity does not make shareholders rich.

---

## 4. Inversion and risk list: Munger's "invert, always invert"

### 4.1 How this investment could fail

| Path | Probability | Impact | Comment |
|---|---|---|---|
| Organic growth stays at 0 to 3% and the market stops paying a premium multiple | Medium-high | High | Already happening: forward P/E went from 25.1x at end-2025 to 17.5x. |
| Serial acquisitions at full prices keep ROE in single digits | Medium-high | Medium | $1.46bn Cornell/Roper deal funded with $1.5bn of notes at 5.25 to 5.85%. Management wants to deploy about $1bn a year. |
| Margin target missed once the easy 80/20 gains are taken | Medium | High | The 2024 plan promised about 100 basis points a year. 2026 guidance is on track. 2027 onward is unproven. |
| Smart-meter cycle disappoints | Medium | Medium | Electric-meter projects were delayed in 2026. Measurement & Control margin fell 200 basis points in Q2. |
| US municipal funding falls after federal infrastructure money runs down | Medium | Medium | Not modelled in the valuation. See limits in section 7.5. |
| China keeps shrinking | High | Low | Revenue down 27% in Q2 2026, but only about 2% of sales. |
| Goodwill write-down | Low-medium | Medium | $8.3bn of goodwill. A write-down would not cost cash but would confirm Evoqua was overpaid. Not modelled. |
| Finance leadership churn | Happened | Low-medium | CFO Bill Grogan left on 31 Aug 2026 for GE HealthCare. An internal successor took over. |

### 4.2 Historical analogy

The closest parallels are the industrial companies that applied 80/20 simplification. Illinois Tool Works did it from 2012 and lifted operating margin from about 16% to about 24% over six years. The share price followed. The less happy parallel is any "quality compounder" that made a large all-share deal near a peak in its own valuation: profit grows, but profit per share and return on equity lag for years. Xylem today is both stories at once.

### 4.3 Bias check

- **Narrative bias:** "water scarcity" is a compelling story. The story has been true for twenty years and Xylem's ROE averaged 12% over the last ten.
- **Anchoring:** the 52-week high of $154 and analyst targets near $151 make $103 look cheap. On trailing GAAP earnings it is still 24 times.
- **What the bears say:** UBS (Neutral, $112 target, the lowest on the Street) and Wolfe (Peer Perform). Oppenheimer described the bear thesis in February as "peaking demand and funding risk".

> **Munger's question: where am I most likely to be wrong, and why would smart people not buy?**
> Smart people would not buy because they can get a 4% cash yield from a business growing 2 to 3% organically almost anywhere. The likeliest mistake on the other side is underestimating how far margins can still rise. If Xylem reaches the mid-20s EBITDA margin that Pentair and IDEX already earn, today's price will look fair to low.

---

## 5. Management: "right people" (Duan) and integrity (Buffett)

### 5.1 Key decisions

| Date | Decision | Result so far | Score |
|---|---|---|---|
| 2016 | Bought Sensus for about $1.7bn | Created the metering franchise. It took years to earn its cost. | ★★★ |
| Jan 2023 | Agreed to buy Evoqua for about $7.5bn in shares (former CEO Patrick Decker) | Revenue up 64% from 2022 to 2025. Share count up 34%. ROE fell from about 11% to below 9%. | ★★ |
| Jan 2024 | Matthew Pine became CEO; launched 80/20 simplification | Adjusted EBITDA margin up from 20.6% (2024) to 22.2% (2025), with 23.1 to 23.5% guided for 2026. | ★★★★ |
| 2025 to 2026 | Sold or exited more than $400m of low-margin revenue | Lower sales, higher margin. | ★★★★ |
| H1 2026 | Bought back $1,243m of shares at an average of about $123 | The price is now $103. Early, not disastrous. First meaningful buyback in a decade. | ★★★ |
| Aug 2026 | Agreed to buy Cornell and Roper pumps for $1.46bn in cash | High-margin assets (EBITDA margin above 30%), full price, funded with new debt. Too early to judge. | ★★★ |

### 5.2 Alignment

- **Ownership is tiny.** Insiders own 0.16 to 0.34% of the company. CEO Pine holds about 79,000 shares, worth about $8m, against annual pay of $11.3m.
- **Pay is tied to adjusted EPS and relative shareholder return** (50% each for performance shares). Adjusted EPS excludes restructuring and deal amortization, so management is not penalized for the costs of its own deals.
- **Insider dealing in the last twelve months:** four sales by officers and directors and one small purchase (director Jerome Peribere, $141k at $116.61 in May 2026). No open-market purchase by the CEO.

> **Duan Yongping's question: if the CEO retired, would the company stay competitive?**
> Yes. The brands and installed base do not depend on one person. The 80/20 discipline does depend on the current team, and the CFO who helped design it has just left.

---

## 6. Industry and long-run trend: Li Lu's "civilization" lens

- **Is this a civilization-level shift?** No. Water infrastructure is a civilization-level *need*, which is different. It grows with population, regulation and the age of pipes, at roughly GDP plus a little. It is closer to railways in 1950 than to electricity in 1900: essential, permanent, slow.
- **Pockets of real growth exist.** Xylem's data-centre orders more than tripled in Q2 2026 and data centres should be about 2% of sales by year-end. PFAS ("forever chemicals") rules require US drinking-water compliance by 2029. Outsourced industrial water is growing, as the Dow contract shows.
- **Position in the value chain:** equipment and service supplier. It does not own the water or the pipes. It carries no regulated-utility risk and no commodity risk, but also has no monopoly.
- **Technology risk:** low. Pumps and membranes change slowly.
- **Concentration:** none on the customer side.

> **Li Lu's question: looking back from 2046, is this the Standard Oil of its era or a 3Com?**
> Neither. It is more like a well-run railway supplier: still there in twenty years, still earning a living, unlikely to produce an extraordinary return unless bought cheaply.

---

## 7. Valuation and margin of safety

### 7.1 What the market is paying today

| Measure | Now | End of 2025 | 5-year average (2021 to 2025 year-ends) |
|---|---|---|---|
| P/E (GAAP, trailing) | 24.4x | 34.7x | 43.7x |
| Forward P/E | 17.5x | 25.1x | 32.2x |
| EV/EBITDA | 13.0x | 18.1x | 22.6x |
| Price to free cash flow | 25.0x | 38.0x | 46.7x |
| Dividend yield | 1.68% | 1.19% | about 1.2% |

The share is far below its own history. That history was unusually rich: Xylem traded at 40 to 55 times earnings in 2021 to 2023 as a "water theme" favourite. The history is a poor guide to fair value.

**Peers (forward P/E, Finviz, 9 Oct 2026, single source):** Pentair 10.1x · A. O. Smith 13.8x · Mueller Water 13.7x · **Xylem 16.5x** · Franklin Electric 18.7x · Veralto 20.2x · IDEX 24.2x · Watts Water 25.1x · Badger Meter 26.7x · Ecolab 30.0x. Xylem is in the lower half.

### 7.2 Reverse check: what does $102.71 assume?

At 18.3 times 2026 adjusted earnings and a 4.0% free cash flow yield, a buyer needs free cash flow per share to grow about 6% a year for a decade just to earn roughly 10% a year, with the multiple unchanged. Consensus expects 10% EPS growth in 2027. Management's own target is mid-teens. The price assumes less than management promises, which is the main point in the stock's favour.

### 7.3 Three scenarios over three years (`financial_rigor.py three-scenario`)

Starting point: 2026 adjusted EPS guidance midpoint of $5.625.

| Scenario | EPS growth a year | 2029 EPS | P/E in 2029 | Price in 2029 | Change vs $102.71 | Value today (discounted at 10%) |
|---|---|---|---|---|---|---|
| Bull: margins reach the mid-20s, growth returns to 4 to 6% | 12% | $7.90 | 24x | $189.7 | +84.7% | **$142.5** |
| Base: roughly what consensus expects | 9% | $7.28 | 20x | $145.7 | +41.8% | **$109.5** |
| Bear: growth stalls, deals disappoint | 2% | $5.97 | 14x | $83.6 | -18.6% | **$62.8** |

The base case discounted to today is about $109, close to the current price. **A 25% margin of safety on the base case is about $82 to $85.**

### 7.4 Ten-year discounted view (`terminal_value.py`)

The framework requires the exit multiple to come from a perpetual-growth formula, not from what peers trade at today: exit P/E = (1 - g / ROIC) / (r - g).

**The three inputs and why**

| Input | Value | Reason |
|---|---|---|
| r, cost of capital | **10%** (USD) | Framework default for dollar cash flows (range 9 to 11.5%). |
| ROIC on new capital | **12%** | Between the reported ROIC of 8 to 9% (dragged down by Evoqua goodwill) and the high return on organic investment in a business that needs little physical capital. Recent deals at about 11.6 times EBITDA pull the blend down. This is a judgment. |
| g, growth after 2036 | **3%** base (2% bear, 4% bull) | Long-run nominal US growth. Capped at 4% for USD. |

**Audit result:** all three hard checks passed (currency match, r minus g of at least 5 points in every case, discrete risks kept out of the discount rate). Denominator width: 8, 7 and 6 points.

| Case | Profit growth to 2036 | 2036 profit | Exit P/E | 10-year return a year (incl. 2.7% dividend + buyback) |
|---|---|---|---|---|
| Bear | 4% | $1,944m | 10.4x | **+1.0%** |
| Base | 7% | $2,584m | 10.7x | **+4.1%** |
| Bull | 9% | $3,109m | 11.1x | **+6.4%** |

Starting profit is 2026 adjusted net income of about $1,313m ($5.625 × 233.49M shares). Market cap $23,981m.

**Sensitivity to r (base case):** at r = 8% the exit P/E is 15.0x and the return is +7.6% a year. At r = 12% the exit P/E is 8.3x and the return is +1.6%. In none of the three does the base case return reach the discount rate used. In all three, Pentair ranks above Xylem (see the Pentair report), so the ranking is stable even though the absolute numbers move a lot with r.

### 7.5 Limits of this valuation

- **Not modelled:** a cut in US municipal water funding, and a goodwill write-down. Both are flagged by the audit tool as outside the model.
- The 10-year numbers are harsh by construction. A 10% discount rate gives almost any steady industrial an exit multiple near 11 times. The absolute return figures depend heavily on r. The ranking between companies is the sturdier conclusion.
- Adjusted earnings are used as the starting profit. On GAAP earnings every return above would be lower.

> **Buffett's question: if r is wrong by two points, does the conclusion flip?**
> No. At 8%, 10% and 12% the base case stays below the hurdle. The conclusion is about the price, not about the discount rate.

> **Duan Yongping's question: if the market closed for five years, would you hold at this price?**
> Yes, without losing sleep. The business will be bigger and more profitable in five years. But "safe to hold" and "cheap enough to buy more" are different answers, and at $103 only the first is true.

### In your money: what this means in lei

- **Price:** one share $103 ≈ €91.55 ≈ 489 lei; the margin-of-safety level of $85 ≈ €75.77 ≈ 405 lei. National Bank of Romania reference rates of 9 Oct 2026: 1 EUR = 5.3414 lei, 1 USD = 4.7612 lei.
- **Return:** The base case is +4.1% a year over ten years in dollars, in a range of +1.0% to +6.4%. A return in lei is that figure plus or minus the change in the lei price of the dollar. Between 26 Feb and 9 Oct 2026 the leu lost 10.2% against the dollar and 4.8% against the euro (BNR reference rates), which shows how much the exchange rate alone can move a lei result.
- **Inflation:** Romanian inflation was 6.2% a year in August 2026 (INS). The National Bank of Romania forecasts 6.1% for end-2026 and 3.4% for end-2027. The base case is below current inflation and only slightly above the end-2027 forecast, before any exchange-rate effect.


---

## 8. Decision memo

| Dimension | Conclusion | Confidence |
|---|---|---|
| Business quality (Duan) | Good, essential, recurring. Slow organic growth. | High |
| Moat (Buffett) | Real and slowly widening: installed base, metering lock-in, service. | Medium-high |
| Management (Duan + Buffett) | Operators are executing well. Capital allocation record is mixed, ownership is tiny. | Medium |
| Biggest risk (Munger) | Paying full prices for growth while organic growth stays at 0 to 3%. | Medium-high |
| Long-run trend (Li Lu) | Permanent need, modest growth. Not a paradigm shift. | High |
| Valuation (Buffett + Duan) | Fair. About $109 base value against a $102.71 price. No margin of safety. | Medium |

| Strategy | Suggestion |
|---|---|
| No position | Wait. Interesting below about **$85** (25% under the base value, about 15 times 2026 earnings). |
| Already holding | Hold. The business is intact and the multiple has already fallen by a third. |
| Signals to sell | Organic growth still at or below 2% through 2027 once the 80/20 exits are done · adjusted EBITDA margin stalls below 23% · another large deal paid with shares · net debt above 2.5 times EBITDA. |
| Signals to add | Price near $85 · organic growth back to 4% or more with the margin intact · the CEO buying shares with his own money. |

**Verdict: hold / wait. A good business at a fair price, with no cushion.**

> **Buffett (simulated):** "The business I understand. People will need clean water long after we are gone. What I can't get around is that the owners earn under 9% on their equity. I'd want that to change, or the price to."
>
> **Munger (simulated):** "They issued a third more shares to buy a competitor at a full price, and now they adjust away the cost of it every quarter. I'm not saying it was stupid. I'm saying show me the return."
>
> **Duan Yongping (simulated):** "Right business, mostly right people. Not yet the right price. There is no hurry. The water will still be there."
>
> **Li Lu (simulated):** "This is a durable business in a slow-growing field. Durable is valuable only at a price that leaves room for error. Fair is not that price."

---

## 9. AI confidence versus investment certainty

| | Level | Why |
|---|---|---|
| **AI analysis confidence** | High | Grade A information. The financial history comes straight from SEC filings and was cross-checked. |
| **Investment certainty** | Medium | The business is predictable. The return from here depends on two things that are not: whether organic growth recovers after 2026, and whether management keeps paying full prices for acquisitions. |

**Based on solid data:** the 11-year financial table, the 2026 guidance, share count, buybacks, the deal terms, current multiples.
**Based on reasoning from limited information:** the 12% return assumed on new capital, the moat scores, growth rates beyond 2027, and the reasons given for the share price fall (taken from press and analyst commentary).

---

## Appendix: cross-validation record and sources

| Data point | Source 1 | Source 2 | Deviation | Status |
|---|---|---|---|---|
| Share price | $102.71 (StockAnalysis) | $102.71 (Finviz) | 0.00% | ✅ |
| Market cap | $23.98bn (calculated) | $23.98bn (StockAnalysis) | 0.01% | ✅ |
| FY2025 revenue | $9,035m (SEC XBRL) | $9,035m (StockAnalysis) | 0.00% | ✅ |
| FY2025 net income | $957m (SEC XBRL) | $957m (StockAnalysis) | 0.00% | ✅ |
| FY2025 free cash flow | $910m (OCF minus capex) | $873m (StockAnalysis) | 4.1% | ⚠️ capex definition |
| Net debt, 30 Jun 2026 | $1,650m (company) | $1,779m (StockAnalysis) | 7.8% | ⚠️ leases |
| 2027E EPS | $6.23 (StockAnalysis) | $6.21 (Finviz) | 0.3% | ✅ |
| Trailing GAAP EPS | $4.20 (StockAnalysis) | $4.21 (Finviz) | 0.2% | ✅ |

**Data audit (`report_audit.py`, 15% random sample):** 23 points sampled, 21 passed, 2 warnings, 0 failed. **Cleared for release.** The two warnings are second-source differences above 1% (5-year average P/E: 43.7 vs 43.2 from another vendor; price to free cash flow: 25.0 vs 26.0 on Finviz). Prices, market cap, revenue, net income, buybacks, debt and guidance were re-fetched from StockAnalysis and the SEC press release for the audit. About a third of the sampled points were model assumptions or tool outputs, which the audit can only confirm were copied correctly. Valuation inputs were re-run through `terminal_value.py audit` after the final draft: passed, unchanged.

**Sources**

- SEC XBRL company facts (CIK 1524472): https://data.sec.gov/api/xbrl/companyfacts/CIK0001524472.json
- FY2025 Form 10-K: https://www.sec.gov/Archives/edgar/data/1524472/000152447226000012/xyl-20251231.htm
- Q2 2026 press release: https://www.sec.gov/Archives/edgar/data/0001524472/000152447226000108/xyl07282026ex991.htm
- Q2 2026 Form 10-Q: https://www.sec.gov/Archives/edgar/data/0001524472/000152447226000110/xyl-20260630.htm
- Q4 2025 press release: https://www.sec.gov/Archives/edgar/data/1524472/000152447226000008/xyl02102026ex991.htm
- 2026 proxy statement: https://www.sec.gov/Archives/edgar/data/1524472/000110465926036678/xyl-20260514xdef14a.htm
- 2024 Investor Day release: https://www.xylem.com/en-ae/resources/press-releases/xylem-unveils-multi-year-growth-strategy-at-2024-investor-day/
- StockAnalysis: https://stockanalysis.com/stocks/xyl/statistics/ and /financials/ and /forecast/
- Finviz: https://finviz.com/quote.ashx?t=XYL
- Q2 2026 call summary: https://www.investing.com/news/transcripts/earnings-call-transcript-xylem-beats-on-q2-2026-eps-raises-outlook-93CH-4817144
- Cornell / Roper deal: https://www.waterworld.com/drinking-water-treatment/distribution/news/55397171/xylem-to-acquire-cornell-pump-and-roper-pump-businesses-for-146b
- CFO change: https://nasdaq.com/articles/xylem-promotes-andrea-van-der-berg-succeed-william-grogan-cfo
- February 2026 sell-off: https://seekingalpha.com/news/4549509-xylem-shares-slide-after-cautious-2026-outlook

*macrotrends.net could not be read (access blocked), so SEC filings replaced it as the primary source.*
