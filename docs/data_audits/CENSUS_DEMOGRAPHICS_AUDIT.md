# Niagara Succession Signal — Census Demographics Data Audit

## Week 3 — Data Collection and Audit

This audit covers two approved Statistics Canada Census datasets:

- **Part A:** Statistics Canada Table 98-10-0022-01 — Census Age Data
- **Part B:** Statistics Canada Table 98-10-0592-01 — Class of Worker / Self-Employment

The two datasets are audited separately because they contain different variables and have different strengths, limitations and outstanding checks.

Where a finding was not established from the audit evidence, it is marked **Not established** rather than guessed.

---

# PART A — Table 98-10-0022-01 (Census Age Data)

## 1. Dataset Identification

| Field | Value |
|---|---|
| Dataset name | Age (in single years), average age and median age and gender: Canada, provinces and territories, census divisions and census subdivisions (2021 Census, 100% data) |
| Provider | Statistics Canada |
| Table/Dataset number | 98-10-0022-01 |
| Official source link | https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=9810002201 |
| Original filename | `98-10-0022-01.csv` |
| File format | CSV |
| SHA-256 of audited file (`98100022.csv`, 95,336,523 bytes) | `b7a6a987157c2617fee59a38c18086b0bcc72fd6c832f09d0804af49fb001ec1` |
| Date downloaded | 2026-10-01 |
| Downloaded/Audited by | Precious and Lucky |
| Repository location | `data/raw/statcan/census/` |
| Licence | Statistics Canada Open Licence |

---

## 2. Basic Dataset Information

| Check | Finding |
|---|---|
| Number of rows | 1,399,808 |
| Number of columns | 12 |
| Reference year/period | Census years 2016 and 2021 (699,904 rows each) |
| Geographic coverage | 5,468 geographies, 256 rows each |
| Smallest geographic level available | Census subdivision (CSD) |
| Industry classification | None |
| NAICS version, if stated | Not applicable |
| Business-size classification | None |
| Metadata available? | Yes: `98100022_MetaData.csv` |
| Documentation available? | Yes: metadata file |

---

## 3. Column Review

| Column Name | Meaning | Data Type | Example Value | Important for Project? |
|---|---|---|---|---|
| `REF_DATE` | Reference year | Integer | 2021 | No. Use `Census year (2)` instead |
| `GEO` | Geography name | String | Canada, Piney | Yes |
| `DGUID` | Dynamic Geographic Unique Identifier | String | 2021A00051001101 | Yes |
| `Census year (2)` | Census reference year | Integer | 2016, 2021 | Yes |
| `Age (in single years), average age and median age (128)` | Age category | String | 0 to 14 years | Yes |
| `Coordinate` | Statistics Canada member-position index | String | 1.1.2 | No |
| `Gender (3a):Total - Gender[1]` | Count of persons, all genders; average/median on statistic rows | Numeric | 6012795 | Yes |
| `Symbol` | Status flag for Total value | String | blank | Yes |
| `Gender (3a):Men+[2]` | Count of Men+ | Numeric | 3086510 | Yes |
| `Symbol.1` | Status flag for Men+ value | String | blank | Yes |
| `Gender (3a):Women+[3]` | Count of Women+ | Numeric | 2926285 | Yes |
| `Symbol.2` | Status flag for Women+ value | String | blank | Yes |

`Symbol.1` and `Symbol.2` are the names pandas gives to the second and third `Symbol` columns. In the raw file, all three are called `Symbol`.

---

## 4. Missing Values

Nothing was deleted or filled.

| Variable | Missing Count | Missing % | Possible Meaning / Note |
|---|---:|---:|---|
| `REF_DATE`, `GEO`, `DGUID`, `Census year (2)`, Age, `Coordinate` | 0 | 0% | Fully populated |
| Total - Gender | 77,696 | 5.550% | All carry symbol `x`, likely confidentiality suppression |
| Men+ | 77,704 | 5.551% | 8 more than Total, only on Median age row |
| Women+ | 77,744 | 5.554% | 48 more than Total, only on Median age row |
| `Symbol` (blank) | 1,235,328 | 88.25% | Blank status field |
| `Symbol.1` (blank) | 1,235,320 | 88.25% | Blank status field |
| `Symbol.2` (blank) | 1,235,280 | 88.25% | Blank status field |

Suppressed and status-coded observations must not automatically be treated as zero.

---

## 5. Duplicate Check

| Item | Result |
|---|---|
| Total duplicate rows | 0 |
| Possible duplicate business records | Not applicable — no business records |
| Fields used | Full-row match; `DGUID` + `Census year (2)` + Age; `Coordinate` |
| Result | 0 duplicates on every test |

`Coordinate` is unique across all 1,399,808 rows.

There are 290 geography names shared by more than one DGUID. This represents distinct places sharing names rather than duplicated rows.

**Joining rule:** use `DGUID`, not `GEO` name.

---

## 6. Geographic Audit

| Level | Geographies |
|---|---:|
| Canada | 1 |
| Province / territory | 13 |
| Census division | 293 |
| Census subdivision | 5,161 |
| **Total** | **5,468** |

All DGUIDs carry the 2021 vintage, and every geography has exactly 256 rows.

| Item | Finding |
|---|---|
| Geographic fields | `GEO` and `DGUID` |
| Geographic levels | Canada, province/territory, CD and CSD |
| Does Niagara appear directly? | Yes — Niagara CD 3526, DGUID `2021A00033526` |
| Are Niagara municipalities available? | Yes — all 12 CSDs |
| Niagara internal consistency | The 12 CSDs sum exactly to the CD total in both years: 447,890 in 2016 and 477,940 in 2021 |

The 12 municipalities are:

- Fort Erie
- Port Colborne
- Wainfleet
- West Lincoln
- Pelham
- Welland
- Thorold
- Niagara Falls
- Niagara-on-the-Lake
- St. Catharines
- Lincoln
- Grimsby

None is suppressed or flagged.

---

## 7. Time Coverage

| Item | Finding |
|---|---|
| Earliest year | 2016 |
| Latest year | 2021 |
| Frequency | Census year — every 5 years |
| Multiple years? | Yes, but only two points |

### Limitations

1. `REF_DATE` is 2021 on all 1,399,808 rows, including rows where `Census year (2)` is 2016. Use `Census year (2)` for the actual census period.
2. Two time points cannot support trend modelling.
3. The file contains no annual data.
4. 2021 counts reflect the May 2021 census reference period during the pandemic.

---

## 8. Industry / NAICS Review

| Question | Answer |
|---|---|
| Contains industry information? | No |
| Contains NAICS? | No |
| NAICS version / level | Not applicable |
| Important industry fields | None |

This table cannot be analysed or compared by industry.

---

## 9. Business Size / Employment Review

| Question | Answer |
|---|---|
| Contains employment information? | No |
| Contains business-size categories? | No |
| Size variable / categories / definition | Not applicable |

There is no labour-force, class-of-worker or self-employment variable in this dataset.

---

## 10. Succession-Related Variable Check

| Variable | Present? | Actual Column Name | Notes |
|---|:---:|---|---|
| Owner age | No | None | Population age is not business-owner age |
| Retirement intention | No | None | |
| Intended exit timeline | No | None | |
| Successor identified | No | None | |
| Succession plan | No | None | |
| Reason for closure | No | None | |
| Business status | No | None | |
| Business opening year | No | None | |

---

## 11. Direct, Proxy and Context Variables

| Type | Variables Found |
|---|---|
| **Direct** | None |
| **Proxy** | Population age bands, particularly 45–64, 55–64 and 65+; median age; average age; change between 2016 and 2021 |
| **Context** | Total population, gender, CD/CSD geography and population change |

> **Caution:** Population age structure is a weak proxy for business-owner age. Treating population age as owner age would create an ecological-fallacy problem.

---

## 12. Possible Joining Keys

| Possible Key | Present? | Example | Notes |
|---|:---:|---|---|
| Geography | Yes | DGUID `2021A00053526053` | Confirm partner dataset uses compatible geography and boundary vintage |
| Year | Yes | 2016 / 2021 | Use `Census year (2)`, not `REF_DATE` |
| NAICS | No | — | |
| Industry | No | — | |
| Business size | No | — | |
| Business identifier | No | — | |

A shared variable does not automatically make a join valid. Geography level and coding must first be verified.

---

## 13. Unusual Values / Quality Issues

| # | Issue | Evidence | Impact |
|---|---|---|---|
| 1 | `REF_DATE` mislabels 2016 rows as 2021 | 699,904 rows | Period errors if `REF_DATE` is used |
| 2 | `...` rows hold numeric `0` | 86,784 rows | False zeros if status ignored |
| 3 | `x` rows are blank | 77,696 rows | Missing/suppressed, not zero |
| 4 | Gender-only suppression | 8 Men+ and 48 Women+ cells | Small CSDs only |
| 5 | Random rounding | Populated counts are multiples of 5 | Limits small-area precision |
| 6 | Components do not always sum exactly | Differences within 10 | Consistent with rounding |
| 7 | Age label contains trailing space | `"64 "` | Could cause parsing error |
| 8 | Nested age categories | 128 labels mix multiple levels | Risk of double counting |
| 9 | Non-unique geography names | 290 names | Wrong joins if using name |
| 10 | CSD totals do not equal Canada | Small shortfalls | Do not construct national totals from CSDs |

---

## 14. Dataset Strengths

1. Complete and consistent coverage of 5,468 census geographies.
2. No row duplication.
3. Niagara and all 12 municipalities are available in both census years.
4. Single-year age detail enables custom age bands.
5. Two census periods allow change measurement.
6. `DGUID` provides a stable geographic identifier.

---

## 15. Dataset Limitations

1. Cannot directly measure succession, ownership, closure, employment or business size.
2. Population age is not owner age.
3. Only two time points are available.
4. There is no annual forecasting signal.
5. Gender is limited to Men+ and Women+.

---

## 16. Relevance to the Challenge

| Deliverable | Support? | How the Dataset Could Help |
|---|---|---|
| 4.1 Aggregated data layer | Yes — context layer | Population and age structure by CD/CSD |
| 4.2 Research report | Yes | Local demographic context |
| 4.3 Infographics & visual assets | Yes | Age pyramids and aging maps |
| 4.4 Graphs & exploratory visuals | Yes | Median age, age shares and 2016–2021 change |
| 4.5 Predictive model | Weak | Possible municipal aging covariate only |
| 4.6 Business acquisition / succession playbook | Minimal | Background only |
| 4.7 Local-economy impact analysis | Yes | Population denominators |
| 4.8 Government & private-sector remediation report | Minimal | Supporting context |
| 4.9 Nice-to-have extensions | Possible | Municipal aging index |

---

## 17. Dataset Decision

- [ ] KEEP — Core
- [x] **KEEP — Supporting**
- [ ] CONDITIONAL
- [ ] DO NOT USE

### Reason for Decision

The dataset has strong data quality and complete Niagara coverage, making it useful for demographic context and population denominators.

However, it contains no business, industry, business-size or direct succession variables and therefore cannot serve as the core succession dataset.

---

## 18. Actions Required Before Cleaning

- [ ] Ensure the raw file and metadata are preserved unchanged in `data/raw/statcan/census/`.
- [ ] Ensure the source entry is recorded in `data/raw/DATA_SOURCES.md`.
- [ ] Confirm the meanings of `x` and `...` and the rounding rules against the metadata.
- [ ] Decide how `"64 "` will be handled during cleaning.
- [ ] Ensure `Census year (2)` rather than `REF_DATE` is used as the actual census period.
- [ ] Do not convert population age into owner age.
- [ ] Peer review this audit.

---

## 19. New Risks or Data Gaps

**New risk identified:** Yes.

### Risk / Gap

The dataset contains no business, business-owner or succession variables. Population age could be incorrectly interpreted as owner age.

### Why It Matters

The project's succession question cannot be answered directly from this dataset.

### Action Required

Use this dataset as a demographic/context layer and clearly distinguish population demographics from business-owner characteristics.

---

## 20. Audit Sign-Off

| Field | Value |
|---|---|
| Dataset audited by | Precious and Lucky |
| Date audit completed | 2026-10-01 |
| Reviewed by | Pending |
| Review date | Pending |
| Audit status | Draft — reviewed findings to be confirmed by team |

---

# PART B — Table 98-10-0592-01 (Class of Worker / Self-Employment)

## 1. Dataset Identification

**Dataset name:** Statistics Canada Table 98-10-0592-01 — Class of worker and self-employment information  
**Provider:** Statistics Canada  
**Table/Dataset number:** 98-10-0592-01 (reference 98100592)  
**Official source link:** https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=9810059201  
**Original filename:** Statistics Canada Table 98-10-0592-01  
**File format:** CSV  
**Date downloaded:** 2026-10-01  
**Downloaded/Audited by:** Precious Ubanwa and Lucky  
**Repository location:** `data/raw/statcan/census/`  
**Licence:** Statistics Canada Open Licence

---

## 2. Basic Dataset Information

| Check | Finding |
|---|---|
| Number of rows | 53,215,380 |
| Number of columns | 23 |
| Reference year/period | `REF_DATE` field present; actual values not established |
| Geographic coverage | 251 unique geographic names; 307 unique geographic codes. Includes Canada, Ontario and Niagara |
| Smallest geographic level available | Not established |
| Industry classification | NAICS 2017 |
| NAICS version | NAICS 2017 |
| Business-size classification | None identified |
| Metadata available? | To be confirmed |
| Documentation available? | To be confirmed |

---

## 3. Column Review

All 23 columns were identified. Meanings of the `Symbol` fields and the exact interpretation of some class-of-worker measures have not yet been confirmed against official metadata.

| Column Name | Meaning | Important for Project? |
|---|---|---|
| `REF_DATE` | Reference period | Yes |
| `GEO` | Geographic name | Yes |
| `DGUID` | Dissemination geography identifier | Yes |
| `Statistics (3)` | Statistic type | To be confirmed |
| `Labour force status (3)` | Labour-force status dimension | Yes |
| `Age (15A)` | Population age group | Proxy/context only |
| `Gender (3)` | Gender dimension | Context |
| `Industry - Groups - NAICS 2017 (428A)` | NAICS 2017 industry group | Yes |
| `Coordinate` | Table coordinate | Unlikely |
| `Class of worker (7A): Total - Class of worker[1]` | Class-of-worker measure | To be confirmed |
| `Symbol` | Status flag | Check before use |
| `Class of worker (7A): Class of worker - not applicable[2]` | Class-of-worker measure | To be confirmed |
| `Symbol.1` | Status flag | Check before use |
| `Class of worker (7A): All classes of workers[3]` | Class-of-worker measure | Yes |
| `Symbol.2` | Status flag | Check before use |
| `Class of worker (7A): Employee[4]` | Employee measure | Yes |
| `Symbol.3` | Status flag | Check before use |
| `Class of worker (7A): Self-employed[5]` | Self-employed measure | Yes — proxy |
| `Symbol.4` | Status flag | Check before use |
| `Class of worker (7A): Self-employed[6]` | Second self-employed measure; exact difference from [5] not established | Yes — proxy |
| `Symbol.5` | Status flag | Check before use |
| `Class of worker (7A): Unpaid family worker[7]` | Unpaid family-worker measure | Context |
| `Symbol.6` | Status flag | Check before use |

---

## 4. Missing Values

Rows checked: **53,215,380**.

| Variable | Missing Count | Missing % |
|---|---:|---:|
| `REF_DATE` | 0 | 0.00% |
| `GEO` | 0 | 0.00% |
| `DGUID` | 0 | 0.00% |
| `Statistics (3)` | 0 | 0.00% |
| `Labour force status (3)` | 0 | 0.00% |
| `Age (15A)` | 0 | 0.00% |
| `Gender (3)` | 0 | 0.00% |
| `Industry - Groups - NAICS 2017 (428A)` | 0 | 0.00% |
| All classes of workers | 0 | 0.00% |
| Employee | 0 | 0.00% |
| Self-employed [5] | 0 | 0.00% |
| Self-employed [6] | 0 | 0.00% |
| Unpaid family worker | 0 | 0.00% |
| Total - Class of worker | Not established | Not established |
| Class of worker - not applicable | Not established | Not established |
| `Symbol`, `Symbol.1`–`Symbol.6` | Not established | Not established |

### Important Limitation

The audit does **not** establish that all 23 columns contain zero missing values.

Missing-value checks for the Symbol fields and the two class-of-worker fields identified above are still required.

No values were deleted or filled.

---

## 5. Duplicate Check

**Total duplicate rows:** Not established  
**Possible duplicate business records:** Not applicable — no business identifier  
**Fields used to check duplicates:** Not established

A formal duplicate analysis was not included in the supplied findings and must still be completed without changing the raw file.

---

## 6. Geographic Audit

**Geographic fields:** `GEO`, `DGUID`

**Confirmed geographic coverage:** Canada, Ontario and Niagara.

**Does Niagara appear directly?** Yes.

**Are Niagara municipalities available?** Not established.

### Geographic Limitations

- 251 unique geographic names and 307 unique geographic codes were identified.
- The reason for the difference has not yet been established.
- Exact geographic levels represented by the 307 codes have not been confirmed.
- Niagara municipalities/CSD availability must therefore not be assumed.

---

## 7. Time Coverage

**Earliest year/date:** Not established  
**Latest year/date:** Not established  
**Frequency:** Not established  
**Multiple years:** Not established

`REF_DATE` exists, but its actual values were not established in the supplied audit findings.

Geographic codes beginning with `2021A` must not by themselves be treated as proof of the dataset's reference period.

---

## 8. Industry / NAICS Review

**Contains industry information?** Yes  
**Contains NAICS?** Yes  
**NAICS version:** NAICS 2017  
**NAICS level/digits available:** Not established

**Important industry field:**

`Industry - Groups - North American Industry Classification System (NAICS) 2017 (428A)`

Industry analysis may be possible, but the exact aggregation level and category mapping must be confirmed from the metadata before use.

---

## 9. Business Size / Employment Review

**Contains employment information?** Yes.

Available class-of-worker information includes:

- employee;
- self-employed;
- unpaid family worker;
- all classes of workers; and
- not applicable.

**Contains business-size categories?** No.

No employee-count bands or enterprise-size classifications were identified.

> Self-employed persons must not automatically be classified as business owners or employers.

---

## 10. Succession-Related Variable Check

| Variable | Present? | Notes |
|---|:---:|---|
| Owner age | No | `Age (15A)` is population age, not identified as owner age |
| Retirement intention | No | |
| Intended exit timeline | No | |
| Successor identified | No | |
| Succession plan | No | |
| Reason for closure | No | |
| Business status | No | |
| Business opening year | No | |
| Ownership transfer | No | |
| Confirmed succession closure | No | |

---

## 11. Direct, Proxy and Context Variables

### Direct Variables

**None identified.**

### Proxy Variables

- Self-employed [5]
- Self-employed [6]
- Class of worker
- Employee
- Labour force status
- Age (15A)

These variables may provide context or proxy information but do not directly measure succession risk.

Self-employment does not establish business ownership, retirement intention or succession risk.

### Context Variables

- `GEO`
- `DGUID`
- Industry / NAICS 2017
- Gender
- `REF_DATE`

---

## 12. Possible Joining Keys

| Possible Key | Present? | Notes |
|---|:---:|---|
| Geography | Yes | Level and coding must be confirmed |
| DGUID | Yes | Exact geographic levels not established |
| Year | Yes | `REF_DATE` exists, but actual values need confirmation |
| NAICS | Yes | Exact level not established |
| Industry | Yes | Same NAICS 2017 field |
| Business size | No | |
| Business identifier | No | |
| Municipality/CSD | Not confirmed | Requires metadata review |

### Important Rule

A shared variable does **not** automatically mean that two datasets can be validly joined.

Meaning, geographic level, time period and coding must first be checked.

No merging or joining was performed during this audit.

---

## 13. Unusual Values / Quality Issues

1. Large unique-value counts occur in the class-of-worker fields.
2. Integer values in the self-employed/class-of-worker fields require metadata interpretation.
3. The exact meaning of Self-employed [5] versus Self-employed [6] has not been confirmed.
4. Missing-value coverage is incomplete for the Symbol fields and two class-of-worker fields.
5. Duplicate status has not been established.
6. Niagara is present, but Niagara municipality/CSD availability has not been established.
7. The difference between 251 geographic names and 307 geographic codes remains unexplained.
8. Time coverage has not yet been established.
9. NAICS granularity has not been confirmed.

---

## 14. Dataset Strengths

1. Very large dataset with 53,215,380 rows.
2. Contains multiple analytical dimensions including geography, labour-force status, age, gender, industry and class of worker.
3. Contains employee, self-employed and unpaid family-worker measures.
4. Contains NAICS 2017 industry information.
5. Niagara appears directly.
6. The substantive fields checked in the supplied audit showed no missing values.

---

## 15. Dataset Limitations

1. No direct succession variables.
2. Self-employed does not automatically mean business owner.
3. `Age (15A)` is not business-owner age.
4. No business-size classification.
5. No business identifier.
6. Cannot support business-level succession analysis.
7. Time coverage remains unconfirmed.
8. NAICS level remains unconfirmed.
9. Exact geographic levels remain unconfirmed.
10. Some class-of-worker definitions remain unconfirmed.

The dataset is highly aggregated/statistical in structure.

---

## 16. Relevance to the Challenge

- [x] 4.1 Aggregated data layer
- [x] 4.2 Research report
- [ ] 4.3 Infographics & visual assets
- [x] 4.4 Graphs & exploratory visuals
- [x] 4.5 Predictive model — proxy/context features only
- [ ] 4.6 Business acquisition / succession playbook
- [x] 4.7 Local-economy impact analysis
- [ ] 4.8 Government & private-sector remediation report
- [ ] 4.9 Nice-to-have extensions

### How Could This Dataset Help?

The dataset can provide aggregated context on self-employment and class-of-worker patterns by geography and industry.

It may support the aggregated data layer, research report, exploratory analysis and local-economy analysis after the outstanding definitions and metadata checks are completed.

For modelling, it may supply proxy/context features only because it contains no direct succession labels.

---

## 17. Dataset Decision

- [ ] KEEP — Core
- [x] **KEEP — Supporting**
- [ ] CONDITIONAL
- [ ] DO NOT USE

### Reason for Decision

The dataset provides potentially useful class-of-worker, self-employment, geography and industry context.

However, it contains no direct succession variables. Its use should remain aggregated, contextual and proxy-based.

Self-employment must not be treated as direct evidence of business ownership or succession risk.

---

## 18. Actions Required Before Cleaning

1. Confirm definitions of all class-of-worker variables.
2. Confirm the exact difference between Self-employed [5] and Self-employed [6].
3. Confirm the meaning of the integer values.
4. Confirm actual `REF_DATE` values and time coverage.
5. Confirm geographic levels in `GEO`/`DGUID`.
6. Confirm whether Niagara municipalities/CSDs are separately represented.
7. Confirm the NAICS 2017 level represented.
8. Run a formal duplicate check.
9. Check missingness across all 23 columns, including Symbol fields.
10. Preserve the raw dataset unchanged.
11. Do not classify all self-employed observations as business owners.
12. Do not create succession labels that the source data does not support.

---

## 19. New Risks or Data Gaps

**New risks identified:** Yes.

1. Self-employed ≠ business owner.
2. No direct succession outcomes.
3. Some class-of-worker values are not yet fully interpretable.
4. Niagara municipal geographic granularity is unconfirmed.
5. Time coverage is not established.
6. Duplicate status is not documented.
7. NAICS granularity is unconfirmed.
8. No business identifier is available.

### Why It Matters

These issues could result in self-employment being incorrectly treated as succession evidence or lead to invalid joins, comparisons or interpretations.

### Action Required

Resolve the outstanding items in Section 18 before cleaning and later analysis.

Relevant risks should also be reflected in `RISK_REGISTER.md`.

---

## 20. Audit Sign-Off

| Field | Value |
|---|---|
| Dataset audited by | Precious Ubanwa and Lucky |
| Date audit completed | To be recorded |
| Reviewed by | Pending |
| Review date | Pending |
| Audit status | Draft |

---

# Week 3 Audit Completion Status

## Table 98-10-0022-01 — Census Age Data

- [x] Dataset identified
- [x] Rows and columns recorded
- [x] Columns reviewed
- [x] Missing values checked
- [x] Duplicates checked
- [x] Geography checked
- [x] Niagara and its 12 municipalities confirmed
- [x] Time coverage checked
- [x] Industry/NAICS absence confirmed
- [x] Business-size information checked
- [x] Succession-related variables checked
- [x] Possible joining keys identified
- [x] Data-quality issues documented
- [x] Strengths and limitations recorded
- [x] Dataset relevance assessed
- [x] Dataset decision recorded
- [ ] Final peer review/sign-off

## Table 98-10-0592-01 — Class of Worker / Self-Employment

- [x] Dataset identified
- [x] Raw file preserved unchanged
- [x] Rows and columns recorded
- [ ] Column definitions fully confirmed
- [ ] Missing values checked across all 23 columns
- [ ] Duplicates checked
- [ ] Exact geographic levels confirmed
- [x] Niagara presence confirmed
- [ ] Niagara municipalities/CSDs confirmed
- [ ] Time coverage confirmed
- [ ] Exact NAICS level confirmed
- [x] Business-size information checked
- [x] Succession-related variables checked
- [x] Possible joining keys identified
- [x] Data-quality issues documented
- [x] Strengths and limitations recorded
- [x] Dataset relevance assessed
- [x] Dataset decision recorded
- [ ] Relevant new risks added/updated in `RISK_REGISTER.md`
- [ ] Final peer review/sign-off

---

# Overall Census Demographics Audit Conclusion

Both Census datasets should be retained as **supporting datasets**, not treated as direct succession datasets.

**98-10-0022-01** provides detailed Niagara demographic and population-age context, including all 12 municipalities, but population age must not be interpreted as business-owner age.

**98-10-0592-01** provides potentially valuable self-employment, class-of-worker and industry context, but self-employment must not be interpreted automatically as business ownership or succession risk. Several metadata, geography, time, missingness and duplicate checks remain outstanding before this dataset is ready for cleaning and analytical use.

Neither dataset contains direct evidence of:

- owner retirement intention;
- succession-plan status;
- identified successor;
- intended ownership-transfer timeline;
- reason for business closure; or
- confirmed succession-related closure.

These limitations must remain explicit throughout the project.
