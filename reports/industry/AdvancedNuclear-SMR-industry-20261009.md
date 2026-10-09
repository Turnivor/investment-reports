# Advanced Nuclear & SMR Value Chain — Industry Investment Research

**Date:** 2026-10-09 · **Framework:** value-chain scan + Buffett / Munger / Duan Yongping / Li Lu
**Scope:** advanced reactors and SMRs, the fuel cycle that feeds them (uranium → conversion → enrichment/HALEU → fabrication), the component suppliers, and the operators that sell the power. Follows up on [Oklo research](../Oklo/Oklo-research-20261009.md). Builds on the broader April report 核电-industry-20260409.md (in the upstream ai-berkshire repo).
**Information richness:** **A for the fuel cycle and operators** (decades of data) · **B/C for SMR developers** (pre-revenue, cost data mostly undisclosed)

> **AI research limitations:** "AI needs nuclear" is one of the loudest narratives in the market, so an AI summary drifts toward the optimistic consensus. This report deliberately leans on *hard* numbers: signed contracts, permits actually issued, and disclosed construction costs. Forecasts are labeled as estimates. Not investment advice.

---

## 1. Investment Logic Chain and Validation

### 1.1 The chain

```
AI data centers + electrification + reshoring
    → US/global power demand grows again after 15 flat years
        → Buyers need FIRM, CARBON-FREE, 24/7 power (wind/solar + batteries don't fully solve this)
            → Existing nuclear is re-rated (restarts, uprates, PPAs) — NOW
            → New nuclear is ordered (large AP1000 + SMRs + microreactors) — 2030s
                → Fuel demand rises, especially for enriched uranium & HALEU (the bottleneck)
                    → Winners: (1) owners of existing reactors, (2) fuel cycle chokepoints,
                       (3) component makers with nuclear certifications, (4) maybe a few SMR developers
```

### 1.2 Link-by-link validation

| Link | Core assumption | Evidence | Strength |
|---|---|---|---|
| AI → power demand | Data-center load grows fast | Data-center electricity forecast ~1,300 TWh by 2035 (SMR Intel); hyperscalers signing GW-scale contracts | ★★★★★ |
| Demand → firm clean power | Buyers pay a premium for 24/7 carbon-free | Microsoft–Constellation TMI restart, ~$16B over 20 years; Meta 6.6 GW across Vistra/TerraPower/Oklo | ★★★★★ |
| → Existing nuclear re-rated | Old plants are worth more | CEG $104B market cap; Palisades restart (Holtec) | ★★★★★ |
| → New nuclear actually built | SMRs get built at competitive cost | **Permits: yes.** Kemmerer CP (Mar 2026), Clinch River CP (Sep 29 2026), Darlington under construction. **Cost: NOT yet.** Darlington = C$20.9B for 1.2 GW (≈C$17,400/kW) | ★★★☆☆ |
| → Fuel demand / HALEU | Enrichment is the chokepoint | Uranium term price $96.50/lb, the highest since the series began in 1996; Centrus is the only US HALEU producer (~900 kg/yr) | ★★★★☆ |
| → SMR developers make money | Developers earn returns | No SMR developer is profitable. XE −41% vs IPO, NuScale −81% (52w), Oklo −74% (52w), Holtec IPO withdrawn Sep 25 2026 | ★★☆☆☆ |

**The weak link is the last one.** Demand is real. Permits are coming faster than ever. But **nobody has proven an SMR can be built for less than large nuclear per kW**, and FOAK numbers so far say the opposite.

### 1.3 Validation events that have actually happened (not forecasts)

| Date | Event |
|---|---|
| Sep 2024 | Microsoft–Constellation 20-year PPA, Three Mile Island Unit 1 restart |
| Oct 2024 | Google–Kairos 500 MW; Amazon–X-energy (960 MW, 5 GW option by 2039) |
| Apr 2025 | Canada (CNSC) licenses BWRX-300 construction at Darlington |
| May 2025 | US executive orders: target 400 GW of nuclear by 2050; DOE Reactor Pilot Program; NRC reform |
| Oct 28 2025 | US government–Westinghouse (Cameco 49% / Brookfield) **$80B AP1000 framework**. Government gets 20% of distributions above $17.5B; Westinghouse IPO required by 2029 if valued above $30B |
| Jan 2026 | Meta: 6.6 GW across Vistra, TerraPower (2.8 GW) and Oklo (1.2 GW) |
| Mar 4 2026 | NRC issues TerraPower Natrium (Kemmerer) construction permit, the first Gen-IV CP |
| Apr 2026 | Kairos breaks ground on Hermes 2; **X-energy IPO** (largest nuclear IPO ever, $1B+) |
| Jun–Aug 2026 | Four DOE pilot reactors reach criticality by July 4 (Valar, Antares, Deployable Energy, Aalo); Oklo Groves on Aug 5 |
| Sep 25 2026 | **Holtec withdraws its $825M IPO** (market appetite cooling) |
| Sep 29 2026 | NRC issues TVA Clinch River BWRX-300 construction permit |

> **Duan Yongping's question:** *The chain looks perfect. What's different this time from the 2006–2011 "renaissance" that died?*
> This time the buyers are the richest companies on earth, signing real contracts, and permits really are moving faster. **What's the same as last time: construction costs.** Vogtle went from $14B to ~$35B, and Darlington's first SMR is ~C$25,700/kW including shared infrastructure. Demand doesn't fix cost.

---

## 2. Value-Chain Map

### 2.1 Structure

```
UPSTREAM — FUEL CYCLE
  Uranium mining ──► Conversion (UF6) ──► Enrichment ──► HALEU (5–20%) ──► Fuel fabrication
  (CCJ, KAP, NXE,     (Cameco, Orano,     (Urenco, Orano,  (Centrus = only    (BWXT, Framatome,
   UEC, UUUU, PDN)     ConverDyn)          TENEX, CNNC;     US producer;       Westinghouse, TRISO-X
                                           Centrus, GLE/    Orano, Urenco      [XE], Oklo Aurora fuel)
                                           Silex laser)     plans)
                                                 │
MIDSTREAM — REACTORS & EQUIPMENT                 ▼
  Large reactors: Westinghouse AP1000 (private: Cameco/Brookfield)
  SMRs (light water): GE Vernova-Hitachi BWRX-300 · NuScale · Holtec SMR-300 · Rolls-Royce SMR
  Advanced (Gen IV): TerraPower Natrium (private) · Kairos (private) · X-energy Xe-100 · Oklo Aurora
  Microreactors: Westinghouse eVinci · Radiant · Nano Nuclear · BWXT BANR
  Components: forgings & pressure vessels (Doosan, Japan Steel Works, BWXT), pumps/valves/I&C (Curtiss-Wright),
              steam generators, cooling, EPC (Fluor, Bechtel-private, Kiewit-private)
                                                 │
DOWNSTREAM — OWNERS / OPERATORS                  ▼
  Existing fleet: Constellation · Vistra · Talen · PSEG · Duke/Southern · CGN Power · CNNP · Fortum
  New-build owners: TVA · OPG · utilities · developers who own plants (Oklo, NuScale/ENTRA1)
  Buyers: Microsoft · Amazon · Google · Meta · Switch · Dow
                                                 │
BACK END & ANCILLARY                             ▼
  Spent-fuel storage & decommissioning (Holtec) · Recycling (Oklo, Orano) · Isotopes (Oklo, ASP Isotopes, BWXT Medical)
  ETFs: NLR · URA · URNM · NUKZ · physical uranium (Sprott SPUT, Yellow Cake)
```

### 2.2 Business characteristics by segment

| Segment | Model | Margins | Competition | Barrier | Cyclicality |
|---|---|---|---|---|---|
| Uranium mining | Sell a commodity | Op margin 14% (CCJ) – 41% (KAP) | Oligopoly (KAP + CCJ ≈ 40% of supply) | Resource + permits | **High** (uranium price) |
| Conversion / enrichment | Sell a processing service | High, long-term contracts | **4–5 global players**; Russia (TENEX) being cut out | Technology + licenses + national security | Low–medium |
| HALEU | Sell a scarce service | Not yet scaled | **Centrus is the only US producer** | Licenses + centrifuge tech + government contracts | Low (government-driven) |
| Fuel fabrication | Sell a specialty product | 20–35% | Oligopoly by fuel type | Licenses + qualification | Low |
| SMR / advanced developers | Sell designs, or own plants | Negative today | 6+ serious US designs, plus China/Russia/Korea | Licenses + FOAK experience | n/a (pre-revenue) |
| Nuclear components | Sell certified equipment | Op margin 10–20% (BWXT 10%, CW 20%) | Niche oligopolies | **N-stamp certification**, decades of qualification | Medium |
| Existing-fleet operators | Sell power (merchant + PPAs) | Op margin 15–20% | Few owners; no new supply until the 2030s | Assets can't be replicated | Medium (power prices) |
| Spent fuel / decommissioning | Services + casks | Steady | Near-monopoly niches (Holtec, Orano) | Licenses | Low |

### 2.3 Chokepoints

1. 🔴 **Enrichment and HALEU.** Almost every advanced reactor (Oklo, X-energy, Kairos, TerraPower) needs HALEU, and the US makes ~900 kg/yr against a need of many tonnes. Russia was the main supplier. **This is the tightest bottleneck in the chain.** Who benefits: Centrus (LEU), Urenco and Orano (not listed / state-owned), Silex/GLE (laser enrichment, pre-commercial).
2. 🟠 **Large forgings and N-stamped components.** Few factories can make reactor pressure vessels (Doosan, Japan Steel Works, BWXT). A real multi-GW build-out would sell out this capacity first.
3. 🟠 **Existing reactors.** There are ~94 US reactors and no new large ones before ~2031. Their owners hold a scarce asset that is being re-rated.
4. 🟡 **Skilled labor / EPC** (not investable directly; mostly private companies).

> **Buffett's question:** *Which segment is most like a toll bridge?*
> **Existing reactors** (sunk cost, ~20-year license extensions, PPAs with hyperscalers) and **enrichment** (very few licensed players, national-security protection). SMR developers are the opposite: they *pay* the tolls.

---

## 3. Global Company Scan (prices as of Oct 9 2026, StockAnalysis unless noted)

### 3.1 Upstream — uranium mining

| Company | Ticker | Market cap | EV | Key metrics | Pure-play | Tier | Info |
|---|---|---|---|---|---|---|---|
| **Kazatomprom** | KAP (LSE) | £13.0B | — | P/E 15.8x, EV/EBITDA 7.3x, op margin 41%, dividend 4.2% | Pure | **T1** | A |
| **Cameco** | CCJ | $37.9B | $37.9B | P/E 153x TTM / 61x fwd, EV/EBITDA 68x; also owns 49% of Westinghouse | Pure (+Westinghouse) | **T1** | A |
| NexGen Energy | NXE | $5.9B | $5.6B | Pre-production (Rook I) | Pure | T2 | B |
| Uranium Energy | UEC | $4.6B | $4.1B | Revenue $37M, P/S 122x | Pure | T2 | B |
| Energy Fuels | UUUU | $2.5B | $2.2B | Uranium + rare earths; revenue $106M | High | T2 | B |
| Paladin / Boss / Deep Yellow / Denison | PDN, BOE, DYL (ASX); DML (TSX) | — | — | Producers and developers | Pure | T2–T3 | B |
| CGN Mining | 1164.HK | — | — | CGN group's uranium arm | Pure | T3 | B |
| Physical uranium | SPUT (TSX), Yellow Cake (LSE) | — | — | Holds physical U3O8 | — | Special | A |

### 3.2 Upstream — conversion, enrichment, HALEU, fuel

| Company | Ticker | Market cap | Key metrics | Position | Tier | Info |
|---|---|---|---|---|---|---|
| **Centrus Energy** | LEU | $2.9B | EV $2.2B; revenue $474M; FCF −$164M; shares +31% YoY; short interest 26.5%; −61% (52w) | Only US HALEU producer; LEU broker | **T2** | B |
| Silex Systems | SLX (ASX) | A$1.1B | Revenue A$19M; loss A$39M; −43% (52w) | Laser enrichment (GLE JV with Cameco) | T3 | B |
| ASP Isotopes | ASPI | $0.41B | Revenue $31M; loss $132M | Isotope enrichment, HALEU ambitions | T3 | C |
| Lightbridge | LTBR | $0.22B | EV ≈ −$21M (cash > market cap); shares +66% YoY | Advanced metallic fuel (R&D) | T3 | C |
| Urenco / Orano / Framatome | private / state | — | — | Enrichment and fuel majors | (not listed) | — |

### 3.3 Midstream — reactor developers (SMR & advanced)

| Company | Ticker | Market cap | EV | TTM revenue | Status | Tier | Info |
|---|---|---|---|---|---|---|---|
| **GE Vernova** (GE-Hitachi BWRX-300) | GEV | $262B | $253B | $41.4B | Darlington under construction (grid ~2030); TVA Clinch River CP Sep 2026. Nuclear is a small share of revenue | **T4** (diversified) | A |
| **X-energy** | XE | $5.5B | $3.9B | $150M | Xe-100 HTGR + TRISO-X fuel; Dow Long Mott CP under review; Amazon. IPO Apr 2026 at $23, now $13.55 (−41%) | **T3** | B |
| **Oklo** | OKLO | $6.4–6.6B | ~$3.5B | $1.2M | Aurora fast reactor; Groves test reactor critical; INL 2028 target | **T3** | B |
| **NuScale** | SMR | $3.1B | $2.0B | $10.7M | Only NRC-certified SMR (77 MWe); ENTRA1/TVA up to 6 GW framework; shares +132% YoY | **T3** | B |
| NANO Nuclear | NNE | $0.81B | $0.23B | $0.2M | Microreactors, early stage | T3 | C |
| Rolls-Royce (RR SMR) | RR (LSE) | £113.8B | — | £23.2B | SMR is a tiny share; UK/Czech selection | T4 | A |
| Holtec Nuclear | HNUC (withdrawn) | (IPO pulled Sep 25 2026; was targeting ~$9.4–10.2B) | — | — | SMR-300 at Palisades; spent fuel; Palisades restart | Future IPO | B |
| TerraPower / Kairos / Radiant / Valar / Aalo | private | — | — | — | Natrium (CP Mar 2026) / Hermes 2 / microreactors / DOE pilots | Future IPO candidates (Kairos possibly Q4 2026) | C |
| Westinghouse | private (Cameco 49%, Brookfield 51%) | IPO required by 2029 if valued above $30B | — | — | AP1000 + eVinci microreactor | Future IPO | B |

### 3.4 Midstream — components and equipment

| Company | Ticker | Market cap | Key metrics | Nuclear role | Tier | Info |
|---|---|---|---|---|---|---|
| **BWX Technologies** | BWXT | $13.0B | P/E 37x / 29x fwd; EV/EBITDA 30x; ROIC 10.8%; FCF $317M | US Navy reactors (monopoly), commercial components, fuel, BANR microreactor, medical isotopes | **T1** | A |
| **Curtiss-Wright** | CW | $18.7B | P/E 35x / 32x fwd; op margin 20%; ROIC 16.5% | Reactor coolant pumps (AP1000), valves, I&C; also defense | **T2** | A |
| **Doosan Enerbility** | 034020.KS | ₩49.9T | P/E 276x / 105x fwd | Forgings, pressure vessels, NuScale/X-energy supplier | **T2** | B |
| KEPCO E&C | 052690.KS | — | — | Korean reactor design and engineering | T2 | B |
| Fluor | FLR | — | — | NuScale EPC, exiting its NuScale stake | T4 | A |
| China: Shanghai Electric, Dongfang Electric, Jiangsu Shentong, etc. | A-shares | see April report | — | Domestic equipment | T1–T2 (China) | A |

### 3.5 Downstream — operators

| Company | Ticker | Market cap | EV | Key metrics | Nuclear fleet | Tier | Info |
|---|---|---|---|---|---|---|---|
| **Constellation** | CEG | $103.6B | $127.6B | P/E 28x / 24x fwd; EV/EBITDA 15.7x; FCF only $295M (capex + Calpine deal) | Largest US nuclear fleet | **T1** | A |
| **Vistra** | VST | $52.4B | $72.5B | P/E 27x / 15x fwd; EV/EBITDA 10.9x; FCF $2.26B | Comanche Peak + ex-Energy Harbor; Meta deal | **T1** | A |
| Talen Energy | TLN | $17.5B | $26.8B | Fwd P/E 12x; net debt $9.3B | Susquehanna (Amazon) | T2 | A |
| PSEG | PEG | — | — | Regulated utility + NJ nuclear | T4 | A |
| **CGN Power** | 1816.HK / 003816 | HK$238.7B | — | P/E 14.4x; P/B 1.10x; dividend 3.1% | China's largest nuclear operator | **T1** | A |
| **China National Nuclear Power** | 601985.SS | ¥182.5B | — | P/E 25.7x; P/B 0.78x | CNNC's operating platform | **T1** | A |
| Fortum | FORTUM (HEL) | — | — | Finnish nuclear/hydro | T4 | A |

### 3.6 ETFs

| ETF | Focus | Note |
|---|---|---|
| **NLR** (VanEck) | Operators + uranium + SMRs, 28 holdings, AUM $3.7B | Top weights CEG 9.2%, CCJ 8.3%, PEG 7.8%, Fortum 6.7%, BWXT 6.3%, NXE 5.5%, OKLO 5.1%, XE 4.5% |
| URA (Global X) | Uranium miners + nuclear | Broadest |
| URNM (Sprott) | Pure miners | Highest uranium-price beta |
| NUKZ (Range) | Advanced nuclear tilt | Higher SMR exposure |

> **Anti-bias note:** I deliberately included small, poorly covered names (LTBR, ASPI, SLX, NNE) and private future IPO candidates (TerraPower, Kairos, Holtec, Westinghouse). Information richness for these is B/C, so short write-ups do not mean they are worse. They are simply less knowable.

---

## 4. Four-Master Analysis of Leading Companies

### 4.1 Constellation Energy (CEG): owner of the scarcest asset

- **Business:** owns the largest US nuclear fleet (~22 GW nuclear before Calpine) and sells power to grids and hyperscalers (Microsoft TMI restart, Meta).
- **Numbers:** revenue $31.3B; net income $3.47B; P/E 28x TTM / 23.7x forward; EV/EBITDA 15.7x; net debt $24B. TTM FCF of only $295M reflects capex and the Calpine acquisition. −21% over 52 weeks.
- **Is it a good business?** Yes, now. Its plants are paid for, nobody can add equivalent supply before the 2030s, and hyperscalers pay premiums. The cyclical part is wholesale power prices.

| Moat | ★ | Evidence |
|---|---|---|
| Pricing power | ★★★★ | Premium 20-year PPAs |
| Switching costs | ★★★ | Co-located data centers |
| Network effects | ★ | — |
| Scale | ★★★★ | Fleet-wide O&M and fuel purchasing |
| License / asset scarcity | ★★★★★ | Can't be replicated before the 2030s |

- **Risks (Munger):** power-price collapse (gas glut, demand disappointment); FERC/PJM limits on behind-the-meter deals; integration risk from Calpine; a single plant incident. Worst case: P/E falls back to utility levels (~15x), roughly −40%.
- **Management:** Joe Dominguez. Disciplined, early mover on hyperscaler deals. **A-**.
- **Valuation:** fair to slightly rich (24x forward for a cyclical power seller).
- **Rating: ★★★★☆ (core candidate on pullbacks)**

### 4.2 Cameco (CCJ): the fuel-cycle compounder with Westinghouse inside

- **Business:** #2 uranium miner (McArthur River/Cigar Lake), conversion, fuel services, plus **49% of Westinghouse** (AP1000, the US government's $80B framework).
- **Numbers:** revenue $2.45B; net income $250M; P/E 153x TTM / 61x forward; EV/EBITDA 68x; essentially no net debt; +1% over 52 weeks.
- **Is it a good business?** Tier-1 assets with long-term contracts, and the term price is at a record $96.50/lb. Westinghouse turns it into a reactor-vendor option as well.

| Moat | ★ | Evidence |
|---|---|---|
| Pricing power | ★★★ | Takes the market price, but its contract book smooths it |
| Switching costs | ★★★ | Utilities qualify suppliers over years |
| Network effects | ★ | — |
| Scale | ★★★★ | World-class ore grades |
| License / resources | ★★★★★ | Athabasca deposits; Western supply security |

- **Risks:** the valuation already assumes Westinghouse success; uranium price cycle; mine disruptions; AP1000 cost overruns. Smart sellers say the forward P/E of 61x already prices in the renaissance.
- **Management:** Tim Gitzel. Patient, disciplined in the downturn. **A**.
- **Valuation:** **expensive**. Buy only on a material pullback (forward P/E < ~40x).
- **Rating: ★★★★☆ (core quality, wait for price)**

### 4.3 Kazatomprom (KAP): the cheapest quality, with geopolitical risk

- **Business:** world's #1 uranium producer (~20–25% of supply), lowest-cost ISR mines.
- **Numbers:** P/E 15.8x; EV/EBITDA 7.3x; op margin 41%; dividend 4.2%; +18% over 52 weeks.
- **Moat:** cost position ★★★★★, scale ★★★★★, but sovereign control and logistics through Russia and China.
- **Risks:** Kazakhstan's state control (tax changes), sanctions spillover, sulfuric-acid shortages, sales tilted to China and Russia. Worst case: a Western sanctions issue makes it uninvestable for some holders.
- **Management:** state-controlled. **B**.
- **Valuation:** **cheap** relative to peers. The discount is the price of geopolitics.
- **Rating: ★★★★☆ (satellite; size for sovereign risk)**

### 4.4 BWX Technologies (BWXT): the nuclear "picks and shovels" with a monopoly core

- **Business:** sole supplier of US Navy nuclear reactors (submarines, carriers); commercial components (Canada CANDU); TRISO fuel; microreactors (BANR, Project Pele); medical isotopes.
- **Numbers:** revenue $3.51B; net income $355M; P/E 37x / 28.6x forward; ROIC 10.8%; FCF $317M; −28% over 52 weeks. (EV $14.5B > market cap $13.0B means ~$1.4B net debt.)
- **Good business?** Yes: a cost-plus government monopoly with decades of visibility, plus commercial upside.

| Moat | ★ | Evidence |
|---|---|---|
| Pricing power | ★★★ | Cost-plus contracts cap the upside |
| Switching costs | ★★★★★ | Navy has no alternative supplier |
| Network effects | ★ | — |
| Scale | ★★★ | — |
| License / security clearances | ★★★★★ | Category I nuclear materials licenses, classified work |

- **Risks:** defense-budget changes; commercial projects slipping; valuation.
- **Management:** Rex Geveden. Steady. **A-**.
- **Valuation:** reasonable-to-rich at 29x forward, but 28% cheaper than a year ago.
- **Rating: ★★★★★ (core; best risk/reward among quality names after the pullback)**

### 4.5 Centrus Energy (LEU): owns the bottleneck, but small and cash-burning

- **Business:** the only US company producing HALEU (Piketon, Ohio, ~900 kg/yr under DOE contract), plus LEU trading. Oklo's LOI covers up to 5 Aurora cores from 2029.
- **Numbers:** revenue $474M; net income $48.5M; FCF −$164M; net cash $691M; shares +31% YoY; short interest 26.5%; −61% over 52 weeks.
- **Good business?** A strategic chokepoint, but it relies on government money and still has to build a centrifuge plant at scale. Historically it bought Russian LEU for resale, a supply risk now being unwound.

| Moat | ★ | Evidence |
|---|---|---|
| License / technology | ★★★★ | US-origin centrifuge tech (AC100M), NRC license, DOE contracts |
| Scale | ★★ | Tiny today |
| Switching costs | ★★★ | Long-term contracts |

- **Risks:** execution of the centrifuge build-out; dependence on DOE funding; Urenco/Orano expanding in the US; dilution.
- **Management:** Amir Vexler. **B**.
- **Valuation:** EV/Sales 4.7x, after a −61% drop. **Reasonable for a strategic asset**, but speculative.
- **Rating: ★★★☆☆ (satellite / watch: the purest bottleneck play)**

### 4.6 GE Vernova (GEV): the most bankable SMR, wrapped in a mega-cap

- **Business:** gas turbines, grid, wind, plus GE-Hitachi's BWRX-300. That design has the most real-world traction: Darlington is under construction (grid ~2030) and TVA Clinch River received its CP on Sep 29 2026.
- **Numbers:** $262B market cap; revenue $41.4B; FCF $12.4B; P/E 28.6x TTM / 47.8x forward; +60% over 52 weeks.
- **Note:** nuclear is a small part of value. You buy GEV for gas turbines and grid; the SMR is a free option.
- **Key data point for the whole industry:** **Darlington costs C$20.9B for 4 × 300 MW, ≈ C$17,400/kW, and the first unit ≈ C$25,700/kW.** That is the most credible public SMR cost so far, and it is *not* cheaper than large nuclear.
- **Rating: ★★★☆☆ (good company, but rich, and not a nuclear pure-play)**

### 4.7 X-energy (XE): the best-backed listed advanced developer

- **Business:** Xe-100 (80 MWe high-temperature gas reactor, 4-pack = 320 MWe) plus TRISO-X fuel fabrication (TX-1, Oak Ridge, ~2027–28). Customers: Dow (Long Mott, CP under NRC review) and Amazon (up to 5 GW by 2039).
- **Numbers:** $5.5B market cap; EV $3.9B; revenue $150M (government cost-share and engineering); net loss −$449M; net cash $1.61B; 406M shares. IPO Apr 24 2026 at $23, now $13.55 (−41%).
- **Vs. Oklo:** X-energy has more revenue, stronger customers (Amazon, Dow, DOE ARDP cost-share) and its own fuel factory, but it burns ~3× Oklo's cash and has a lower EV. **XE looks better value than OKLO on almost every metric**, though both are high-risk.
- **Rating: ★★☆☆☆ (high-risk option)**

### 4.8 Oklo (OKLO): see the [full report](../Oklo/Oklo-research-20261009.md)

Summary: $6.6B market cap, EV ~$3.5B, revenue $1.2M, ~$3.1B liquidity, ~23% annual dilution. The current price implies ~7–8 GW operating by 2036. Probability-weighted value ~$5.5/share vs $34.44. **★★☆☆☆, avoid at the current price; speculative only below ~$20.** Oklo has the strongest liquidity of the group and a working reactor (Groves).

### 4.9 NuScale (SMR): certified design, missing customers

- Only NRC-certified SMR design (77 MWe uprate approved 2025); ENTRA1/TVA 6 GW is a framework, not a firm order; Fluor is exiting its stake; shares +132% YoY; −81% over 52 weeks; revenue $10.7M; burn ~$780M TTM (incl. ENTRA1-related payments); $1.07B cash.
- The 2023 UAMPS cancellation (costs rose to $89/MWh) remains the cautionary tale.
- **Rating: ★★☆☆☆**

### 4.10 Brief notes on others

| Company | Note | Rating |
|---|---|---|
| Vistra (VST) | Cheaper than CEG (15x fwd, FCF $2.3B), nuclear is ~1/4 of the fleet; Meta deal | ★★★★☆ |
| Talen (TLN) | Fwd P/E 12x, Amazon Susquehanna deal; high leverage (net debt $9.3B) | ★★★☆☆ |
| Curtiss-Wright (CW) | Best-quality component name (ROIC 16.5%), AP1000 pumps; 32x fwd | ★★★★☆ |
| Doosan Enerbility | Global forging chokepoint, but at 105x forward P/E | ★★★☆☆ |
| CGN Power (1816.HK) | P/E 14.4x, P/B 1.1x, 3.1% dividend. China is building the most reactors globally | ★★★★☆ |
| CNNP (601985) | P/B 0.78x; Linglong One (first commercial land SMR) is still under commissioning | ★★★☆☆ |
| NexGen (NXE) | World-class Rook I deposit; permitting/construction risk | ★★★☆☆ |
| UEC / UUUU | Expensive for their production levels | ★★☆☆☆ |
| Silex (SLX) | Laser-enrichment moonshot with Cameco | ★★☆☆☆ |
| NNE / LTBR / ASPI | Early-stage, cash-dependent | ★☆☆☆☆ – ★★☆☆☆ |
| Rolls-Royce | Great turnaround, but SMR is immaterial to the stock | n/a for this theme |

> **Buffett's question:** *Will these moats exist in 10 years?* Navy reactors (BWXT), Athabasca ore (Cameco), Kazakh ISR cost (KAP) and existing licensed reactors (CEG/VST): **yes, very likely**. SMR developers' moats: **unknown until they build several units at a known cost.**

---

## 5. Industry-Level Risks (Munger's Checklist)

### 5.1 Systemic risks

| Risk | Probability (10y) | Impact | Response |
|---|---|---|---|
| SMR costs stay at FOAK levels (>$10,000/kW) | **High (~50%)** | Kills most developer theses; operators and fuel are fine | Overweight existing assets and fuel; underweight developers |
| AI power demand disappoints (efficiency gains, capex cycle turns) | Medium (~30%) | Hurts operator multiples; uranium less affected | Keep operators at a reasonable P/E |
| Nuclear accident anywhere | Low (~3–5%) | Extreme: sector-wide de-rating (TMI 1979, Fukushima 2011) | Cap the theme weight |
| Policy reversal (after 2028 elections, NRC reform rolled back) | Low–medium (~15%) | High for developers | Prefer firms with non-US and defense revenue |
| Russia/Kazakhstan supply shock | Medium | Uranium/enrichment prices up (good for CCJ, LEU); bad for KAP and fuel buyers | Mix of KAP and CCJ hedges |
| Valuation bubble bursting | **Already happening** for developers (−40% to −80%) | — | Wait for capitulation; don't anchor on peaks |
| Equity dilution | Certain for developers | Per-share returns well below company growth | Treat developers as venture capital |
| Alternatives (geothermal, long-duration storage, gas + CCS, fusion) | Medium long-term | Caps the premium for firm power | Watch Fervo, storage costs |

### 5.2 Historical analogies

| Analogy | Who won? | Did most investors make money? | Lesson |
|---|---|---|---|
| **US nuclear wave, 1965–1980** | Utilities with regulated returns; GE/Westinghouse vendors suffered | No: cost overruns, cancellations, WPPSS default (1983) | Construction cost kills; owners of *finished* plants won later |
| **Nuclear "renaissance" 2005–2011** | Nobody: Westinghouse bankruptcy 2017, uranium crash | No | Narrative ≠ cash |
| **Shale 2010–2020** | Royalty and mineral owners, low-cost operators | Most E&P equity holders lost money despite huge growth | Growth with heavy capex destroys per-share value |
| **Solar 2005–2015** | Chinese scale manufacturers; buyers of cheap power | Most early pure-plays went bust | The industry can win while the pioneers lose |
| **Railroads, 1850s–1900** | Late buyers of bankrupt assets; Buffett buying BNSF in 2009 | Early investors often lost | Buy proven assets, not construction projects |

**Lesson for today:** value goes to (1) **scarce existing assets** and (2) **chokepoint suppliers**. Pioneers building first-of-a-kind plants mostly transfer value to customers and later owners.

### 5.3 Bias check
- **Narrative bias:** "AI + nuclear" is a perfect story. The cost data (Darlington, Vogtle, NuScale UAMPS) is what the story leaves out.
- **Anchoring:** OKLO −82%, NuScale −81%, XE −41% from IPO. "Cheaper than before" ≠ "cheap".
- **Herding:** ETF flows into NLR and URA made the whole sector move together in 2025; dispersion is now returning.

> **Munger's question:** *How do you lose money in a growing industry?* Pay a growth multiple for a company that must keep issuing shares to fund first-of-a-kind construction. Most SMR equity today fits that description.

---

## 6. Civilizational Trend (Li Lu)

- **Paradigm shift or phase?** **A real, multi-decade shift.** Electrification plus AI plus decarbonization plus energy security point the same way, and nuclear is the only scalable firm zero-carbon source. US, Chinese, European, Japanese and Korean policy all point the same way for the first time since the 1970s.
- **Closest analogy:** **electrification (1890–1930)** — utilities (regulated monopolies) and equipment makers (GE, Westinghouse) captured value — and **railroads** (essential, but brutal for early capital).
- **End state in 10–20 years:**
  - Large reactors (AP1000, Chinese Hualong) supply most new nuclear GW.
  - **2–4 SMR designs survive** with fleet orders; the rest fold or merge. BWRX-300 is the current front-runner (CPs in Canada and the US). X-energy, TerraPower and Kairos have the strongest backers; Oklo has the most cash.
  - Fuel cycle: a Western enrichment/HALEU build-out replaces Russian supply, through a few protected players.
- **Winner-take-most segments:** enrichment/HALEU (national-security oligopoly), naval/defense reactors (BWXT monopoly), and the dominant SMR design (a standardized design wins through learning effects).
- **Most likely to be disrupted:** high-cost uranium developers if supply responds; SMR designs that never reach a second unit; operators' premium if alternatives (geothermal, long-duration storage) scale.

> **Li Lu's question:** *Twenty years from now, who is Standard Oil and who is 3Com?* The "Standard Oil" candidates are the **fuel-cycle chokepoints and existing fleets** (Cameco/Westinghouse, BWXT, Constellation). Most SMR developers listed today are more likely to be the 3Coms, even if one becomes a giant. Picking that one today is a lottery, not an investment.

---

## 7. Portfolio Construction

### 7.1 Recommended theme portfolio (estimates; not advice)

| Layer | Weight of theme | Names | Segment | Logic | Entry guide |
|---|---|---|---|---|---|
| **Core** | 55% | **BWXT** (20%), **Cameco** (15%), **Constellation** (20%) | Components / fuel / operator | Widest moats; proven cash flows | BWXT < ~$150 (≤30x fwd) ✅ now; CCJ < ~$70 (fwd P/E ~45x); CEG < ~$280 (≤22x fwd) |
| **Satellite** | 30% | **Kazatomprom** (10%), **Vistra** (10%), **Centrus** (5%), **Curtiss-Wright** (5%) | Low-cost uranium / cheaper operator / HALEU chokepoint / pumps | Value plus bottleneck exposure | KAP at P/E < 16x ✅ now; VST < ~$160 ✅ now; LEU only below ~$150 and after Piketon expansion milestones |
| **Option** | ≤10% | **X-energy** (4%), **Oklo** (3%, only < $20), **NuScale** (≤2%) | SMR developers | Can go to zero; one may become a giant | XE < $15 ✅ now; OKLO < $20 ❌ not yet; SMR < $6 |
| **Lazy alternative** | 100% | **NLR** | Diversified ETF | CEG/CCJ/BWXT/PEG plus a sleeve of SMRs | Accumulate in tranches |

### 7.2 Signals

| Signal | Conditions |
|---|---|
| **Add** | Any SMR discloses an all-in cost < $8,000/kW for unit 2+; binding hyperscaler PPAs with prices; HALEU contracts beyond pilot volumes; sector-wide selloff with CEG < 20x forward or CCJ < 40x forward |
| **Reduce** | Developers re-rate on news without cost data (another 2025-style mania); uranium term > $130/lb with miners at peak multiples; AI capex cuts |
| **Exit** | Major nuclear incident; repeal of NRC reform / DOE pilot program; Darlington or Kemmerer costs blow out a further 50%+ |

### 7.3 Theme weight cap
**Max 10–15% of a total portfolio**, with SMR developers **≤1–2% of the total portfolio**. The logic chain is strong at the demand end and unproven at the cost end, and one accident can de-rate the whole sector overnight.

---

## 8. Decision Memo

| Dimension | Conclusion | Confidence |
|---|---|---|
| Logic chain | Demand ✓, permits ✓, **cost ✗ (unproven)** | High |
| Best business (Duan) | Existing licensed fleets and naval reactors (BWXT) | High |
| Widest moat (Buffett) | BWXT (Navy monopoly) and Cameco (ore plus Westinghouse) | High |
| Biggest risk (Munger) | SMR FOAK costs (Darlington ≈ C$17,400/kW) plus dilution; tail risk = an accident | High |
| Civilizational trend (Li Lu) | Real multi-decade shift; value goes to chokepoints and existing assets | Medium-high |
| Overall valuation | Quality names fair-to-rich (CCJ rich, BWXT fair after −28%); developers corrected 40–80% but still price in success | Medium |

### What the masters might say (simulated)

> **Buffett:** "I own utilities through Berkshire Hathaway Energy, so I like a toll bridge. Existing nuclear plants with 20-year contracts are toll bridges. A company that hasn't built its first plant isn't a toll bridge. It's a construction company asking for capital."

> **Munger:** "The money in a new industry usually goes to the customers and to whoever controls the bottleneck. Here, the bottleneck is enriched fuel and licensed plants. Ask who earns a return on capital, not who has the best press release."

> **Duan Yongping:** "Do I understand what Cameco or BWXT does? Yes. Do I understand what an SMR costs? No, and Ontario just told me it costs more than people said. I'll stick to what I understand."

> **Li Lu:** "This is a real civilizational trend, and it will last decades. That's why there's no hurry. The great opportunity comes when the first wave of hype collapses and the real winners trade at reasonable prices. Some SMR stocks have already fallen 80%. Watch for the companies that keep executing while their stock is down."

---

## 9. AI Confidence vs. Investment Certainty

| | Level |
|---|---|
| AI analysis confidence | **High** for prices, multiples, permits and contracts (sourced Oct 2026). **Low** for SMR costs and deployment pace |
| Investment certainty | **High** for "existing nuclear + fuel chokepoints benefit". **Low** for "which SMR wins" |

**Information-richness flags:** CEG/VST/CCJ/KAP/BWXT/CW/GEV = A · LEU/XE/OKLO/SMR/NXE/Doosan = B · NNE/LTBR/ASPI/private developers = C.

### Questions for first-hand verification
1. What are the real all-in $/kW for Kemmerer, Clinch River and Long Mott as construction proceeds?
2. How fast is US HALEU capacity really scaling (Centrus Piketon, Urenco USA, Orano Oak Ridge)?
3. Are hyperscaler nuclear agreements binding with fixed prices, or options?
4. How do utilities view SMR cost risk (talk to TVA/OPG/Dominion engineers)?
5. When do Westinghouse, TerraPower, Kairos and Holtec come to market, and at what valuations?

### Limitations
- Market data from StockAnalysis (Oct 9 2026). Chinese A-share/H-share details partly rely on the April 2026 report.
- No macrotrends cross-check for every ticker (HTTP 403). Key figures were cross-checked where possible (see appendix).
- GBP/KRW/HKD market caps are not converted to USD, to avoid FX estimation error.

## Appendix — Verification log

```
Darlington C$/kW: 20.9B / 1,200 MW = C$17,417/kW; unit 1: 7.7B / 300 MW = C$25,667/kW (Decimal)
Natrium: $4B / 345 MW ≈ $11,594/kW (press figure; excludes storage nuance)
EV/Sales: OKLO 2,917x · NNE 1,097x · SMR 191x · XE 26x · LEU 4.7x
XE vs IPO $23: −41.1% · CEG FCF yield 0.28% · KAP earnings yield 6.3%
cross-validate XE price 13.55 / 13.52 ✅ · uranium term $96.50 / $96.50 ✅
```

## Sources
- StockAnalysis statistics (CEG, VST, TLN, CCJ, LEU, BWXT, GEV, CW, XE, SMR, NNE, NXE, UEC, UUUU, LTBR, ASPI, RR, KAP, SLX, 034020, 1816, 601985) and NLR holdings: https://stockanalysis.com
- SMR Intel, State of SMR 2026: https://smrintel.com/state-of-smr-2026/
- World Nuclear News, Darlington C$20.9B budget: https://world-nuclear-news.org/articles/what-is-the-budget-for-canadas-first-smr-project
- GE Vernova, TVA Clinch River CP: https://www.gevernova.com/news/press-releases/nrc-issues-first-us-construction-permit-bwrx-300-small-modular-reactor-tva-clinch-river
- Westinghouse $80B framework: https://www.powermag.com/westinghouse-enters-partnership-for-80-billion-of-new-nuclear-reactors/
- Holtec IPO launch / withdrawal: https://finance.yahoo.com/markets/stocks/articles/holtec-nuclear-launches-900-million-172827133.html , https://www.renaissancecapital.com/Profile/HNUC
- X-energy Long Mott / TRISO-X: https://www.powermag.com/dow-and-x-energy-advance-landmark-nuclear-project-in-texas-with-construction-permit-filing
- Uranium prices: https://skillings.net/uranium-price-forecast-2026-spot-price-resistance-and-the-bull-cycle-warming-up
- TerraPower / Kairos: https://en.wikipedia.org/wiki/TerraPower , https://www.ans.org/news/2026-04-21/article-7964/kairos-power-breaks-ground-on-first-powerproducing-reactor-in-oak-ridge/
- Linglong One: https://wnn.world-nuclear.org/articles/chinese-smr-completes-non-nuclear-steam-start-up-test
- NuScale / ENTRA1 / Fluor: https://simplywall.st/stocks/us/capital-goods/nyse-smr/nuscale-power/news/nuscale-power-smr-is-up-59-after-tva-linked-6gw-pathway-and
