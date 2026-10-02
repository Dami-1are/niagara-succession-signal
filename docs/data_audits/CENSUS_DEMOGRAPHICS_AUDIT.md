# Census Demographics Dataset Audit: Statistics Canada Table 98-10-0022-01

| Audit status | Draft, needs review |
|---|---|
| Audited by | Precious and Lucky |
| Date | 2026-10-01 |

---

## 1. Dataset Identification

| Field | Value |
|---|---|
| Dataset name | Age (in single years), average age and median age and gender: Canada, provinces and territories, census divisions and census subdivisions (2021 Census, 100% data) |
| Provider | Statistics Canada |
| Table/Dataset number | 98-10-0022-01 |
| Official source link | <https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=9810002201> |
| Original filename | `98-10-0022-01.csv` |
| File format | CSV |
| SHA-256 of the audited file (`98100022.csv`, 95,336,523 bytes) | `b7a6a987157c2617fee59a38c18086b0bcc72fd6c832f09d0804af49fb001ec1` |
| Date downloaded | 2026-10-01 |
| Downloaded/Audited by | Precious and Lucky |
| Repository location | `docs/data_audits/CENSUS_DEMOGRAPHICS.md` |
| Licence | **[To confirm]** (Statistics Canada Open Licence expected) |

---

## 2. Basic Dataset Information

Record what is actually present in the downloaded file.

| Check | Finding |
|---|---|
| Number of rows | 1,399,808 rows |
| Number of columns | 12 columns |
| Reference year/period | Census years 2016 and 2021 (699,904 rows each) |
| Geographic coverage | 5,468 geographies, 256 rows each |
| Smallest geographic level available | Census subdivision (CSD) |
| Industry classification | None |
| NAICS version, if stated | Not applicable |
| Business-size classification, if available | None |
| Metadata available? | Yes: `98100022_MetaData.csv` |
| Documentation available? | Yes: the metadata file |

---

## 3. Column Review

| Column Name | Meaning | Data Type | Example Value | Important for Project? |
|---|---|---|---|---|
| `REF_DATE` | Reference year | Integer | 2021 | No. Use `Census year (2)` instead |
| `GEO` | Geography name | String (5,107 distinct names) | Canada, Piney | Yes |
| `DGUID` | Dynamic Geographic Unique Identifier | String (5,468 distinct) | 2021A00051001101 | Yes. Use as the geography key |
| `Census year (2)` | Census reference year | Integer | 2016, 2021 | Yes |
| `Age (in single years), average age and median age (128)` | Age category: 1 total, 3 broad groups, 1 aggregate (85 and over), 20 five-year bands, 101 single-year values (including 100 and over), plus Average age and Median age | String (128 distinct) | 0 to 14 years | Yes |
| `Coordinate` | StatCan member-position index in the form geography.year.age. `5468.2.128` is the last geography, 2016, Median age | String (unique per row) | 1.1.2 | No |
| `Gender (3a):Total - Gender[1]` | Count of persons, all genders (average or median age on the two statistic rows) | Numeric (decimal on the Average and Median age rows) | 6012795 | Yes |
| `Symbol` | Status flag for the Total value | String | blank (NaN in pandas) | Yes. Needed to interpret `x` and `...` |
| `Gender (3a):Men+[2]` | Count of Men+ | Numeric | 3086510 | Yes |
| `Symbol.1` | Status flag for the Men+ value | String | blank (NaN in pandas) | Yes |
| `Gender (3a):Women+[3]` | Count of Women+ | Numeric | 2926285 | Yes |
| `Symbol.2` | Status flag for the Women+ value | String | blank (NaN in pandas) | Yes |

`Symbol.1` and `Symbol.2` are the names pandas gives to the second and third `Symbol` columns. In the raw file all three are called `Symbol`.

---

## 4. Missing Values

Nothing was deleted or filled.

| Variable | Missing Count | Missing % | Possible Meaning / Note |
|---|---:|---:|---|
| `REF_DATE`, `GEO`, `DGUID`, `Census year (2)`, Age, `Coordinate` | 0 | 0% | Fully populated |
| Total - Gender | 77,696 | 5.550% | All carry symbol `x`, likely confidentiality suppression |
| Men+ | 77,704 | 5.551% | 8 more than Total, but only on the Median age row |
| Women+ | 77,744 | 5.554% | 48 more than Total, again only on the Median age row |
| `Symbol` (blank) | 1,235,328 | 88.25% |  missing data |
| `Symbol.1` (blank) | 1,235,320 | 88.25% | missing data |
| `Symbol.2` (blank) | 1,235,280 | 88.25% | missing data |

---

## 5. Duplicate Check

| Item | Result |
|---|---|
| Total duplicate rows | 0 |
| Possible duplicate business records | Not applicable (no business records) |
| Fields used | Full-row match; key `DGUID` + `Census year (2)` + Age; `Coordinate` |
| Result | 0 duplicates on every test. `Coordinate` is unique across all 1,399,808 rows |

**Notes:** duplicate geography **names** exist: 290 names are shared by more than one DGUID (for example Aberdeen, Amherst, Alma). No DGUID has more than one name, so this is not row duplication. The cause is distinct places sharing a name, for example Aberdeen in New Brunswick and Aberdeen in Saskatchewan. It is not caused by census years or boundary versions, because all 5,468 DGUIDs carry the 2021 vintage. Some names recur within one province and some span different geographic levels. Join on `DGUID`, never on `GEO`.

---

## 6. Geographic Audit

| Level | Geographies |
|---|---:|
| Canada | 1 |
| Province / territory | 13 (all, codes 10 to 62) |
| Census division | 293 |
| Census subdivision | 5,161 |
| **Total** | **5,468** |

All DGUIDs carry the 2021 vintage, and every geography has exactly 256 rows.

| Item | Finding |
|---|---|
| Geographic field(s) | `GEO` (name) and `DGUID`. The code is the part of the `DGUID` after position 9 |
| Geographic level(s) | Canada, province/territory, CD, CSD. The level is identifiable from the DGUID schema digits (0000, 0002, 0003, 0005) |
| Does Niagara appear directly? | **Yes.** Niagara (CD 3526, DGUID `2021A00033526`) |
| Are Niagara municipalities available? | **Yes, all 12 CSDs:** Fort Erie, Port Colborne, Wainfleet, West Lincoln, Pelham, Welland, Thorold, Niagara Falls, Niagara-on-the-Lake, St. Catharines, Lincoln, Grimsby (DGUIDs `2021A00053526xxx`). None is suppressed or flagged |
| Niagara internal consistency | The 12 CSDs sum exactly to the CD total in both years (447,890 in 2016; 477,940 in 2021) |

---

## 7. Time Coverage

| Item | Finding |
|---|---|
| Earliest year | 2016 (Census) |
| Latest year | 2021 (Census) |
| Frequency | Census year (every 5 years) |
| Multiple years? | Yes, but only two points |

**Limitations**

| # | Limitation |
|---|---|
| 1 | `REF_DATE` is 2021 on all 1,399,808 rows, even where `Census year (2)` is 2016. Any analysis that treats `REF_DATE` as the period will merge the two censuses. Use `Census year (2)` |
| 2 | Two time points cannot support trend modelling. The file has no annual data |
| 3 | 2021 counts reflect the census reference date (May 2021), during the pandemic |

---

## 8. Industry / NAICS Review

| Question | Answer |
|---|---|
| Contains industry information? | No |
| Contains NAICS? | No |
| NAICS version / level | Not applicable |
| Important industry fields | None |
| Notes | All 12 columns are geography, period, age and gender. This table cannot be aggregated or compared by industry |

---

## 9. Business Size / Employment Review

| Question | Answer |
|---|---|
| Contains employment information? | No. There is no labour-force, class-of-worker or self-employment variable |
| Contains business-size categories? | No |
| Size variable / categories / definition / source | Not applicable |

---

## 10. Succession-Related Variable Check

Checked against the actual columns of the acquired file.

| Variable | Present? | Actual Column Name | Notes |
|---|:---:|---|---|
| Owner age | No | none | Age here is population age, not business-owner age |
| Retirement intention | No | none | |
| Intended exit timeline | No | none | |
| Successor identified | No | none | |
| Succession plan | No | none | |
| Reason for closure | No | none | |
| Business status | No | none | |
| Business opening year | No | none | |

---

## 11. Direct, Proxy and Context Variables

| Type | Variables found |
|---|---|
| **Direct** | None |
| **Proxy** (population aging only, not business owners) | Age bands, especially 45-64, 55-64 and 65 and over, as a share of population; median age and average age; change between 2016 and 2021 in those measures |
| **Context** | Total population and gender split; geography and hierarchy (CD and CSD); 2016 to 2021 population change |

> **Caution:** population age structure is a weak proxy for owner age. Treating it as owner age would be an ecological fallacy.

---

## 12. Possible Joining Keys

| Possible Key | Present? | Example | Notes |
|---|:---:|---|---|
| Geography | Yes | `DGUID` 2021A00053526053 (St. Catharines) | Join on `DGUID`, never on `GEO` name (290 names repeat). Confirm the other dataset uses the same boundary vintage and level |
| Year | Yes | `Census year (2)` = 2016 / 2021 | Do not use `REF_DATE` |
| NAICS | No | none | |
| Industry | No | none | |
| Business size | No | none | |
| Business identifier | No | none | |

**Rule applied:** a shared variable does not make a join valid. Here, geography is the only possible key. Its coding and level must be verified in the partner dataset before any join.

---

## 13. Unusual Values / Quality Issues

| # | Issue | Evidence | Impact |
|---|---|---|---|
| 1 | `REF_DATE` mislabels the 2016 rows as 2021 | 699,904 rows with census year 2016 carry `REF_DATE` 2021 | Period errors if `REF_DATE` is used |
| 2 | `...` rows hold a numeric `0` | 86,784 rows (678 CSDs, all 2016) | **False zeros** if the symbol is ignored |
| 3 | `x` rows are blank | 77,696 rows (607 CSDs, all 2021) | Missing, not zero |
| 4 | Gender-only suppression | 8 Men+ and 48 Women+ cells blank while Total is shown, all on the Median age row | Small CSDs only |
| 5 | Random rounding | Every populated count is a multiple of 5 | Limits small-area precision |
| 6 | Components do not sum to totals | Total differs from Men+ plus Women+ in 410,515 of 1,301,454 count cells, always within 10 | Consistent with rounding. Do not sum across levels |
| 7 | Age label with a trailing space | `"64 "` | Naive parsing drops age 64 |
| 8 | Nested categories in one column | 128 age labels mix five levels | Double counting if summed |
| 9 | Non-unique geography names | 290 names | Wrong joins on name |
| 10 | CSD totals do not equal Canada | 2021 short by 4,935; 2016 short by 42,995 | Use CD or province level for national totals |

---

## 14. Dataset Strengths

- Complete and consistent coverage of all 5,468 census geographies, with exactly 256 rows each and no row duplication.
- Niagara and all 12 municipalities are present in both years.
- Single-year age detail, enabling any age band to be built.
- Two census points (2016 and 2021) for change measurement.
- A stable, well-formed identifier (`DGUID`) for joining to other StatCan products.

---

## 15. Dataset Limitations

- Cannot measure succession, ownership, closure, employment or business size. None of those variables exist here.
- Population age is not owner age.
- Only two time points, five years apart. No annual or forecasting signal.
- Gender is limited to Men+ and Women+.

---

## 16. Relevance to the Challenge

| Deliverable | Support? | How the dataset could help |
|---|---|---|
| 4.1 Aggregated data layer | Yes (context layer) | Population and age structure by CD/CSD, keyed by `DGUID` |
| 4.2 Research report | Yes | Local demographic context and aging narrative |
| 4.3 Infographics & visual assets | Yes | Age pyramids, aging maps by municipality |
| 4.4 Graphs & exploratory visuals | Yes | Median age, 55-64 and 65+ shares, 2016-2021 change |
| 4.5 Predictive model for forecasting business closures | Weak | At most a covariate (municipal aging). No outcome or business variables |
| 4.6 Business acquisition / succession playbook | Minimal | Background only |
| 4.7 Local-economy impact analysis | Yes (denominators) | Population base for per-capita measures |
| 4.8 Government & private-sector remediation report | Minimal | Supporting context |
| 4.9 Nice-to-have extension(s) | Possible | A municipal "aging index" for Niagara |

---

## 17. Dataset Decision

- [ ] KEEP: Core
- [x] **KEEP: Supporting**
- [ ] CONDITIONAL
- [ ] DO NOT USE

**Reason for decision:** data quality is high and Niagara coverage is complete, so the dataset is reliable as demographic context and denominators. It contains no business, industry, size or succession variables, so it cannot be core to a succession analysis.

---

## 18. Actions Required Before Cleaning

- [ ] Record the download date and repository location, and place the raw file read-only in `data/raw/`.
- [ ] Add the source entry to `data/raw/DATA_SOURCES.md`.
- [ ] Confirm the licence on the table page.
- [ ] Confirm the meanings of `x` and `...` and the rounding rule in the metadata.
- [ ] Decide how to handle the `"64 "` label and the `REF_DATE` column during cleaning.
- [ ] Find or obtain a table or dataset that actually contains business and succession variables.
- [ ] Peer review of this audit.

---

## 19. New Risks or Data Gaps

**New risk identified:** Yes

| Item | Description |
|---|---|
| Risk / gap | This dataset has no business, owner-age or succession variables. If the team treats it as a succession dataset, population age could be misread as owner age |
| Why it matters | The project's central question (succession and closure risk) cannot be answered from it, and any model built on it would rest on a proxy with an ecological-fallacy problem |
| Action required | Label it as a context layer, source a business dataset for the core analysis, and add the entries to `RISK_REGISTER.md` |

---

## 20. Audit Sign-Off

| Field | Value |
|---|---|
| Dataset audited by | Precious and Lucky |
| Date audit completed | 2026-10-01 |
| Reviewed by | [pending] |
| Review date | [pending] |
| Audit status | Draft, needs review |
