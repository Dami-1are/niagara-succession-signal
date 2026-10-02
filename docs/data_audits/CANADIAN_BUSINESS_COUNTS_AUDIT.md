# Canadian Business Counts — Data Audit

**How the findings were produced:** every number below comes from `audit_script.py`, run against the unmodified raw CSV in `data/raw/`. The full output is saved in `docs/data_audits/audit_script_output.txt`. The raw files were not cleaned, filtered or changed.

---

# 1. Dataset Identification

**Dataset name:** Canadian Business Counts, with employees, census metropolitan areas and census subdivisions, June 2026 (cube title in the downloaded metadata)  
**Provider:** Statistics Canada  
**Table/Dataset number:** 33-10-1176-01  
**Official source link:** https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=3310117601  
**Original filename:** `33101176.csv` (metadata file: `33101176_MetaData.csv`)  
**File format:** CSV, plus cube metadata (CSV)  
**Date downloaded:** October 1, 2026  
**Downloaded/Audited by:** Theophilus and Ruth  
**Repository location:** `data/raw/` (stored with Git LFS)  
**Licence:** Statistics Canada Open Licence  

---

# 2. Basic Dataset Information

| Check | Finding |
|---|---|
| Number of rows | 1,047,957 (excluding the header row) |
| Number of columns | 16 |
| Reference year/period | One value only: `REF_DATE` = 2026-01 (metadata start and end reference period: 2026-01-01). The cube title says "June 2026"; the file does not explain the difference. |
| Geographic coverage | 3,348 unique DGUIDs: 3,307 census subdivisions and 41 census metropolitan areas. Not limited to Niagara. |
| Smallest geographic level available | Census subdivision (CSD) |
| Industry classification | NAICS, hierarchical, with the code written inside the label in brackets (for example `Accommodation and food services [72]`) |
| NAICS version, if stated | NAICS 2022 (stated in the cube metadata, footnote 5) |
| Business-size classification, if available | `Employment size`: 9 categories (employee-count bands plus a total) |
| Metadata available? | Yes (`33101176_MetaData.csv`) |
| Documentation available? | Yes (Statistics Canada table page and the cube notes in the metadata) |

---

# 3. Column Review

Meanings follow Statistics Canada's standard column layout for table downloads.

| Column Name | Meaning | Data Type | Example Value | Important for Project? |
|---|---|---|---|---|
| `REF_DATE` | Reference period | Text (year-month) | 2026-01 | Yes |
| `GEO` | Geography name | Text | Niagara Falls | Yes |
| `DGUID` | Dissemination geography unique identifier | Text | 2021A00053526043 | Yes (the reliable geography key) |
| `Employment size` | Employee-count band of the business | Text | 1 to 4 employees | Yes |
| `North American Industry Classification System (NAICS)` | Industry, with NAICS code in brackets | Text | Accommodation and food services [72] | Yes |
| `UOM` | Unit of measure | Text | Number (the only value) | No |
| `UOM_ID` | Code for the unit of measure | Numeric code | 223 | No |
| `SCALAR_FACTOR` | Scale of the value | Text | units (the only value) | No |
| `SCALAR_ID` | Code for the scalar factor | Numeric code | 0 | No |
| `VECTOR` | Statistics Canada series identifier | Text | v1918450229 | No (unique per series) |
| `COORDINATE` | Position of the series across the table's dimensions (three parts, matching the 3 dimensions reported in the metadata) | Text | 1.1.2 | No |
| `VALUE` | Number of businesses | Numeric | Range 1 to 262,535 | Yes (the measure) |
| `STATUS` | Statistics Canada status flag | Text | (empty in all rows) | No |
| `SYMBOL` | Statistics Canada symbol | Text | (empty in all rows) | No |
| `TERMINATED` | Flag for terminated series | Text | (empty in all rows) | No |
| `DECIMALS` | Number of decimals of `VALUE` | Numeric code | 0 | No |

---

# 4. Missing Values

| Variable | Missing Count | Missing % | Possible Meaning / Note |
|---|---:|---:|---|
| `REF_DATE` | 0 | 0% | |
| `GEO` | 0 | 0% | |
| `DGUID` | 0 | 0% | |
| `Employment size` | 0 | 0% | |
| NAICS | 0 | 0% | |
| `VALUE` | 0 | 0% | |
| `UOM`, `UOM_ID`, `SCALAR_FACTOR`, `SCALAR_ID`, `VECTOR`, `COORDINATE`, `DECIMALS` | 0 each | 0% | |
| `STATUS` | 1,047,957 | 100% | The file uses no status flags. |
| `SYMBOL` | 1,047,957 | 100% | The file uses no symbols. |
| `TERMINATED` | 1,047,957 | 100% | The file flags no terminated series. |

Nothing was deleted or filled.

---

# 5. Duplicate Check

**Total duplicate rows:** 0 (entire row identical)  

**Possible duplicate business records:** Not applicable. The file holds aggregate counts, not individual business records.  

**Fields used to check duplicates:** the entire row; `REF_DATE + GEO + DGUID + NAICS + Employment size` (0 duplicates); `VECTOR + COORDINATE` (0 duplicates); and `REF_DATE + GEO + NAICS + Employment size` without `DGUID` (83,212 duplicates).  

**Notes:** the 83,212 figure appears only when `DGUID` is left out of the key. 167 `GEO` names map to more than one `DGUID`, and adding `DGUID` removes every duplicate. A row is therefore uniquely identified by `REF_DATE + GEO + DGUID + NAICS + Employment size`. No duplicates were removed.

---

# 6. Geographic Audit

### Findings

**Geographic field(s):** `GEO` (name) and `DGUID` (code)  

**Geographic level(s):** by DGUID type prefix, 3,307 DGUIDs begin `2021A0005` (census subdivisions) and 41 begin `2021S0503` (census metropolitan areas). These match the table title. No province, census-division or national rows appear.  

**Does Niagara appear directly?** No. There is no Niagara Region (census division) row. The St. Catharines - Niagara CMA is present, and a regional total would have to be built from the municipalities.  

**Are Niagara municipalities available?** Yes, all 12, plus the CMA. Every Niagara subdivision DGUID contains the Niagara census division code 3526.  

| Municipality (`GEO`) | `DGUID` |
|---|---|
| Fort Erie | 2021A00053526003 |
| Grimsby | 2021A00053526065 |
| Lincoln | 2021A00053526057 |
| Niagara Falls | 2021A00053526043 |
| Niagara-on-the-Lake | 2021A00053526047 |
| Pelham | 2021A00053526028 |
| Port Colborne | 2021A00053526011 |
| St. Catharines | 2021A00053526053 |
| Thorold | 2021A00053526037 |
| Wainfleet | 2021A00053526014 |
| Welland | 2021A00053526032 |
| West Lincoln | 2021A00053526021 |
| *CMA:* St. Catharines - Niagara | 2021S0503539 |

None of the 12 are missing.

**Geographic limitations:** a second `GEO` called "Lincoln" exists (`DGUID` 2021A00051303008). Its code starts with 13, a different province, so it is not Niagara. Niagara must be selected by `DGUID`, never by the `GEO` name. The CMA overlaps the municipal subdivisions.

---

# 7. Time Coverage

**Earliest year/date:** 2026-01  

**Latest year/date:** 2026-01  

**Frequency:** Semi-annual (from the `Frequency` field of `33101176_MetaData.csv`)  

**Does the dataset cover multiple years?** No. It is a single snapshot (all 1,047,957 rows share `REF_DATE` 2026-01).  

**Important time-related limitations:** a metadata note says counts can shift between reference periods because of method changes (for example how inactive units are identified), so the figures do not only reflect changes in the business population, and Statistics Canada advises against using them as a time series. The cube title says June 2026 while the data say 2026-01.

### Historical CBC data

No historical CBC files were acquired in Week 3, so no comparison of columns, geography, NAICS, employment-size definitions or reference periods was made. No historical tables were combined.

---

# 8. Industry / NAICS Review

**Does the dataset contain industry information?** Yes  

**Does it contain NAICS?** Yes  

**NAICS version:** NAICS 2022 (stated in the cube metadata, footnote 5)  

**NAICS level/digits available:** 445 unique NAICS values. Code depth: 3 values with a 1-digit code, 20 with 2-digit, 99 with 3-digit, 323 with 4-digit. No 5- or 6-digit codes. Every value has a bracketed code.  

**Important industry fields:** `North American Industry Classification System (NAICS)`  

**Notes / limitations:**
- The three 1-digit values are aggregate or catch-all categories: Total, all industries [1], Unclassified [2] and Sub-total, classified [3].
- The code is inside the label text, so it must be extracted before NAICS can be used as a join key.
- 22 industry names appear under more than one code (a parent and a child level share the same name), for example "Educational services" [61] and [611], "Heritage institutions" [712] and [7121], and "Business-to-business electronic markets, and agents and brokers" [419] and [4191]. The full list is in the script output.
- Examples of sectors: Agriculture, forestry, fishing and hunting [11]; Arts, entertainment and recreation [71]; Accommodation and food services [72].

---

# 9. Business Size / Employment Review

**Does the dataset contain employment information?** Yes, as employee-count bands. It does not contain employee counts.  

**Does it contain business-size categories?** Yes  

**Size variable:** `Employment size`  

**Available categories (9, with row counts):**

| Category | Rows |
|---|---|
| Total, with employees | 333,598 |
| 1 to 4 employees | 233,140 |
| 5 to 9 employees | 154,851 |
| 10 to 19 employees | 124,786 |
| 20 to 49 employees | 95,784 |
| 50 to 99 employees | 50,891 |
| 100 to 199 employees | 28,886 |
| 200 to 499 employees | 17,288 |
| 500 plus employees | 8,733 |

**Definition of categories:** employee-count bands as labelled in the file. "Total, with employees" is an aggregate; the other eight are size bands. The row counts reconcile: 333,598 + 714,359 = 1,047,957.  

**Source of definition:** the category labels in the downloaded file. The CSV gives no separate definition.  

**Notes / limitations:** no category is labelled "micro" or "small"; the smallest band is "1 to 4 employees". How micro and small businesses are defined from these bands is a later project decision. "Without employees" and "Indeterminate" categories are absent (confirmed by the script), so the table covers employer businesses only.

---

# 10. Succession-Related Variable Check

Checked against the 16 actual column names (script section 7) and the data values.

| Variable | Present? | Actual Column Name | Notes |
|---|---|---|---|
| Owner age | No | None | |
| Retirement intention | No | None | |
| Intended exit timeline (planned exit) | No | None | |
| Successor identified | No | None | |
| Succession plan | No | None | |
| Ownership transfer information | No | None | |
| Reason for closure | No | None | `TERMINATED` is a Statistics Canada series flag, not a closure reason, and is empty in every row. |
| Business status | No | None | `STATUS` is a data-quality flag column, not business status, and is empty in every row. |
| Business opening year | No | None | |

This confirms the Week 2 expectation that CBC does not directly measure succession. No such variables were created or inferred.

---

# 11. Direct, Proxy and Context Variables

### Direct Variables

**Found:** none.

### Proxy Variables

**Found:** none identified in this file.

### Context Variables

**Found:** business counts (`VALUE`) by geography (`GEO`, `DGUID`), industry (NAICS) and employment size (`Employment size`) at one reference period.

---
# 12. Possible Joining Keys

| Possible Key | Present? | Example | Notes |
|---|---|---|---|
| Geography | Yes | `DGUID` 2021A00053526043 (Niagara Falls) | Use `DGUID`, not `GEO`: 167 names map to more than one `DGUID`. The CBC uses 2021-vintage DGUIDs, which may support alignment with Statistics Canada Census datasets using compatible 2021 geography. |
| Year / reference period | Yes | `2026-01` | A single value. Datasets from other periods, such as the 2021 Census, cannot be treated as representing the same point in time. |
| NAICS | Yes | `Accommodation and food services [72]` | The NAICS code is embedded in the label and must be extracted before joining. Other datasets must be aligned to a compatible NAICS level and classification before comparison or joining. |
| Industry | Yes | The NAICS label | Industry labels may support comparison, but the same industry name can occur at more than one NAICS hierarchy level. |
| Business size | Yes | `1 to 4 employees` | Other datasets' employment-size categories must be checked and mapped before comparison or joining. |
| Business identifier | No | None | The file contains aggregate counts, not individual business records. |

### Potential connections with other project datasets

- **2021 Census datasets:** compatible 2021 geographic identifiers may support geographic alignment through `DGUID`, subject to checking that the geographic level is the same.
- **Niagara Employment Inventory (NEI):** municipality, NAICS/industry and employment-size information may support future comparison. A direct join should not be assumed; geographic and category definitions must first be aligned.
- **Business Dynamics datasets:** NAICS/industry, firm-size categories and reference period may support broader comparison where definitions align. However, the Business Dynamics datasets use provincial/territorial geography. Provincial `GEO`/`DGUID` therefore cannot be directly joined to Niagara-level CBC records and should be treated as broader Ontario context unless an appropriate aggregation strategy is established.

### Important Rule

A common variable does not automatically mean two datasets can be joined. Geographic level, meaning, coding, category definitions and reference period must be checked first.

No datasets were merged during Week 3.

### Important Rule

A common variable does not automatically mean two datasets can be joined. Meaning, level and coding must be checked first. No datasets were merged.

---

# 13. Unusual Values / Quality Issues

### Findings

1. **Reference-period discrepancy:** the cube title says June 2026, but the data and metadata say 2026-01.
2. **Not suitable as a time series** per the Statistics Canada metadata note, and only one period is present.
3. **`GEO` names are not unique:** 167 names map to more than one `DGUID`. Filtering and joining must use `DGUID`, and the Niagara DGUIDs in Section 6 are the ones to use in Week 4 (data cleaning). No filtering was done in Week 3.
4. **NAICS structure:** the code is embedded in the label, depth is 1 to 4 digits only, and 22 industry names appear at two hierarchy levels.
5. **No suppression or quality flags are recorded in the relevant fields:** `STATUS`, `SYMBOL` and `TERMINATED` are entirely empty, while the minimum `VALUE` is 1. Therefore, based on this file alone, an absent combination cannot be distinguished from a true zero or an unpublished combination. This is not proof that nothing was withheld.
6. **Aggregate and overlapping rows:** "Total, with employees" with the size bands, the NAICS levels (including "Total, all industries [1]", "Sub-total, classified [3]" and "Unclassified [2]"), and CMA with subdivision rows overlap. The labels indicate overlap that was not tested in Week 3 and must be handled in Week 4.
7. **No unusual values** in `VALUE` (0 non-numeric, 0 negative, 0 zero). `UOM` and `SCALAR_FACTOR` each have one value.

New findings (not previously documented in Week 2): items 1, 2, 3, 4 and 5. Confirmed from Week 2: CBC contains no direct succession variables.

---

# 14. Dataset Strengths

1. Covers all 12 Niagara municipalities and the St. Catharines - Niagara CMA with stable `DGUID` codes.
2. Gives business counts by NAICS industry (up to 4 digits) and employment size, a baseline picture of the local business structure.
3. Clean structure: no missing values in key fields, no duplicates, numeric counts, and an official source with downloadable metadata.

---

# 15. Dataset Limitations

1. Contains no direct succession variables, so it cannot by itself identify succession risk in Niagara businesses.
2. Covers employer businesses only; businesses without employees and indeterminate businesses are not included.
3. A single reference period, and the metadata advises against using it as a time series.
4. Aggregate counts only: no individual business records, owners or business identifiers.
5. No Niagara Region total row, and geography, industry and size levels overlap.

---

# 16. Relevance to the Challenge

- [x] 4.1 Aggregated data layer
- [ ] 4.2 Research report
- [ ] 4.3 Infographics & visual assets
- [x] 4.4 Graphs & exploratory visuals
- [ ] 4.5 Predictive model for forecasting business closures
- [ ] 4.6 Business acquisition / succession playbook
- [x] 4.7 Local-economy impact analysis
- [ ] 4.8 Government & private-sector remediation report
- [ ] 4.9 Nice-to-have extension(s)

### Explain briefly

**How could this dataset help?** It can supply business counts by municipality, industry and employment size as baseline context for the aggregated data layer, exploratory visuals and local-economy analysis.

---
# 17. Dataset Decision

After completing the audit, select one:

- [x] **KEEP — Core:** Important dataset for the main analysis
- [ ] **KEEP — Supporting:** Useful for context or validation
- [ ] **CONDITIONAL:** May be useful depending on later analysis
- [ ] **DO NOT USE:** Not suitable for the project

### Reason for decision

**Decision: KEEP — Core**

The Canadian Business Counts dataset is retained as a core dataset because it provides business counts by geography, NAICS industry and employment size, including coverage of all 12 Niagara Region municipalities and the St. Catharines - Niagara CMA.

It can support the project's main analysis by providing an aggregate view of the Niagara business population across industries and employment-size categories.

However, the dataset contains no direct succession variables and cannot independently identify succession risk. Its documented limitations — including the single reference period, employer-business-only coverage, non-unique `GEO` names, NAICS hierarchy issues and the unresolved June 2026 versus `2026-01` reference-period discrepancy — must be considered in later analysis.

---

# 18. Actions Required Before Cleaning

1. Resolve or note the June 2026 (cube title) versus 2026-01 (data) reference-period difference.
2. Filter by the 12 Niagara DGUIDs listed in Section 6 (not by `GEO` name) in Week 4 (data cleaning).
3. Extract the NAICS code from the label text and decide how to treat the aggregate and overlapping rows (totals, sub-totals, unclassified, parent and child levels, CMA versus subdivisions).
4. Decide how micro and small businesses will be defined from the employment-size bands.

---

# 19. New Risks or Data Gaps

**Yes**

**Risk / gap:** The dataset is a single snapshot, and its metadata advises against using Canadian Business Counts as a time series. It contains no direct succession variables and covers employer businesses only. There is also an unresolved reference-period discrepancy: the cube title says "June 2026", while the downloaded data and metadata report `2026-01`.

**Why it matters:** Trends in Niagara business counts cannot be measured reliably from this file alone, and succession risk cannot be derived from it directly. The employer-business-only coverage also means businesses without employees are not represented. The unresolved reference-period discrepancy must be considered when aligning this dataset with other sources.

**Action required:** Use this dataset as a core aggregate business-count source within its documented limitations. Do not use it alone to infer succession risk or business-count trends. Use other approved datasets for succession-related indicators and document the reference-period discrepancy when the CBC data is used or compared with other datasets. Record the relevant data limitations in `RISK_REGISTER.md` where they affect later analysis.

---

# 20. Audit Sign-Off

**Dataset audited by:** Theophilus and Ruth  

**Date audit completed:** October 2, 2026  

**Reviewed by:** Joyce Ebruphiyo Etata (Team Lead)  

**Review date:** October 2, 2026  

**Audit status:** Reviewed — Approved with documented limitations

---

# Week 3 Audit Completion Criteria

- [x] Dataset source has been recorded in `data/raw/DATA_SOURCES.md`
- [x] Raw file has been preserved unchanged
- [x] Rows and columns have been recorded
- [x] Columns have been reviewed
- [x] Missing values have been checked
- [x] Duplicates have been checked
- [x] Geography has been confirmed
- [x] Time coverage has been confirmed
- [x] Industry/NAICS information has been checked
- [x] Business-size information has been checked
- [x] Succession-related variables have been checked
- [x] Possible joining keys have been identified
- [x] Data-quality problems have been documented
- [x] Strengths and limitations have been recorded
- [x] Dataset relevance has been assessed
- [x] Keep/conditional/do-not-use decision has been recorded
- [ ] New risks have been added to the risk register where necessary (pending team lead)
- [ ] Audit has been reviewed
