# Canadian Business Counts — Data Audit

**Auditors:** Theophilus and Ruth  
**Date downloaded:** October 1, 2026  
**Date audited:** October 2, 2026

**Dataset:** Statistics Canada Table 33-10-1176-01 — *Canadian Business Counts, with employees, census metropolitan areas and census subdivisions, June 2026* (cube title as given in the downloaded metadata).

**Files audited:** `33101176.csv` (raw data) and `33101176_MetaData.csv` (cube metadata), stored in `data/raw/`.

**How the findings were produced:** every number below comes from `audit_script.py`, run against the unmodified raw CSV. The full output is saved in `docs/data_audits/audit_script_output.txt`. The raw file was not cleaned, filtered or changed.

---

## 1. Dataset Structure

- **Rows:** 1,047,957 (excluding the header row)
- **Columns:** 16
- **Column names:** `REF_DATE`, `GEO`, `DGUID`, `Employment size`, `North American Industry Classification System (NAICS)`, `UOM`, `UOM_ID`, `SCALAR_FACTOR`, `SCALAR_ID`, `VECTOR`, `COORDINATE`, `VALUE`, `STATUS`, `SYMBOL`, `TERMINATED`, `DECIMALS`
- **Important identifiers:** `REF_DATE`, `GEO`, `DGUID`, `Employment size`, NAICS. A row is uniquely identified by the combination of these five fields (0 duplicates, see Section 4). `VECTOR` + `COORDINATE` is also unique per row (0 duplicates).
- **Important measure:** `VALUE` (number of businesses). Range 1 to 262,535. `UOM` is "Number" and `SCALAR_FACTOR` is "units" on every row.
- **Metadata:** the cube metadata reports 3 dimensions.

## 2. Geography

- **Unique `GEO` names:** 3,163. **Unique `DGUID` values:** 3,348. The two differ because 167 `GEO` names map to more than one `DGUID` (see Section 8).
- **Geographic levels present (by DGUID type prefix):**
  - `2021A0005`: 3,307 DGUIDs — census subdivisions
  - `2021S0503`: 41 DGUIDs — census metropolitan areas
  
  These two levels match the table title (census metropolitan areas and census subdivisions). No other level appears: there is **no census-division or Niagara Region total row** and no province or national row.
- **Can Niagara be identified?** Yes. All 12 Niagara Region municipalities are present as census subdivisions, plus the St. Catharines - Niagara CMA. Every Niagara subdivision DGUID contains the Niagara census division code 3526.

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

All 12 municipalities were found; none are missing.

- **Geographic limitations:** a second `GEO` called "Lincoln" exists (`DGUID` 2021A00051303008). Its code starts with 13, a different province, so it is not Niagara. Niagara must be selected by `DGUID`, never by the `GEO` name. The CMA overlaps the municipal subdivisions, so the two levels describe overlapping areas. Because there is no Niagara Region row, any regional total would have to be built from the 12 municipalities.

## 3. Business Information

- **Business counts:** present, in `VALUE`.
- **Employment-size categories (9, with row counts):**

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

  "Total, with employees" is an aggregate category; the other eight are size bands. The row counts reconcile: 333,598 + 714,359 = 1,047,957.
- **Micro / small businesses:** no category is labelled "micro" or "small". The smallest band in the file is "1 to 4 employees". How micro and small businesses are defined from these bands is a later project decision.
- **Indeterminate businesses / businesses without employees:** not present. The script confirmed that no category contains "without employees" or "indeterminate". The table covers employer businesses only.
- **NAICS / industry:** present. 445 unique NAICS values, hierarchical, with the code written inside the label in brackets (for example `Retail trade [44-45]`). Code depth: 3 values with a 1-digit code, 20 with 2-digit, 99 with 3-digit, 323 with 4-digit. **No 5- or 6-digit codes are present.** Every value has a bracketed code. The 3 values with a 1-digit code are Total, all industries [1], Unclassified [2] and Sub-total, classified [3]. These are aggregate or catch-all categories, not specific industries. Examples of sectors: Agriculture, forestry, fishing and hunting [11]; Arts, entertainment and recreation [71]; Accommodation and food services [72].
- 
## 4. Data Quality
- **Missing values:** 0 blank cells in `REF_DATE`, `GEO`, `DGUID`, `Employment size`, NAICS, `VALUE` and every other column except three. `STATUS`, `SYMBOL` and `TERMINATED` are blank in all 1,047,957 rows.
- **Suppressed values / quality flags:** `STATUS` and `SYMBOL` are empty in every row, so no suppression or quality-flag symbols are recorded in these fields in the downloaded file. This does not prove that nothing was withheld: there are no zero counts in `VALUE` (minimum 1), so a missing combination cannot be distinguished from a true zero or an unpublished value based on this file alone.
- **Duplicate records:** 0 exact duplicate rows (entire row identical). 0 duplicates on `REF_DATE + GEO + DGUID + NAICS + Employment size`. 0 on `VECTOR + COORDINATE`. Using only `REF_DATE + GEO + NAICS + Employment size` (leaving out `DGUID`) gives 83,212 duplicates, because 167 `GEO` names are shared by more than one `DGUID`; adding `DGUID` removes all of them.
- **Unusual values:** none found in `VALUE` (0 non-numeric, 0 negative, 0 zero). `UOM` and `SCALAR_FACTOR` have a single value each.
- **Unclear categories:** 22 industry names appear under more than one NAICS code (a parent and a child level share the same name), for example "Educational services" [61] and [611], "Heritage institutions" [712] and [7121], and "Business-to-business electronic markets, and agents and brokers" [419] and [4191]. The full list is in the script output.
- **Other concerns:** see Section 8
- 
## 5. Time Coverage

- **Reference period in the data:** one value only, `REF_DATE` = `2026-01` (all 1,047,957 rows). The metadata gives Start and End Reference Period both as 2026-01-01.
- **Cube title discrepancy:** the cube title says "June 2026", but the data and the metadata reference period are January 2026. This file does not explain the difference, so it is recorded here as unresolved.
- **Frequency:** "Semi-annual", from the `Frequency` field of `33101176_MetaData.csv`.
- **Time limitations:** the download is a single snapshot, so it contains no trend. In addition, a metadata note says counts can shift between reference periods because of method changes (for example how inactive units are identified), so the figures do not only reflect changes in the business population, and Statistics Canada advises against using them as a time series.

## 6. Possible Future Joining Keys

The following fields may support future comparison or joining with other Niagara Succession Signal datasets. These are potential keys only; compatibility must be checked during cleaning before any datasets are joined.

- **`DGUID` / geography** — `DGUID` is the reliable geography identifier in this dataset because `GEO` names are not unique. The CBC contains 2021-vintage DGUIDs for census subdivisions and census metropolitan areas. This may support geographic alignment with Statistics Canada Census datasets that use compatible 2021 geographic identifiers.

- **Niagara Employment Inventory (NEI)** — the NEI contains Niagara municipality information, but the CBC uses census-subdivision DGUIDs. A direct join should not be assumed. Municipality names or an approved municipality-to-DGUID crosswalk may be needed after geographic compatibility is verified.

- **NAICS / industry** — the CBC contains NAICS information embedded in the industry label and uses codes from 1 to 4 digits. NAICS may support future comparison with the NEI, Business Dynamics and other project datasets containing industry information. Before joining, the NAICS code must be extracted and the datasets must be aligned to a compatible NAICS level and classification.

- **`Employment size`** — the CBC contains nine text categories: one aggregate category (`Total, with employees`) and eight employment-size bands. This field may support comparison with the NEI or Business Dynamics firm-size information, but the category definitions are not automatically equivalent. Size bands must be checked and mapped before any comparison or join.

- **`REF_DATE`** — the CBC contains one reference period, `2026-01`. Year/reference period may support temporal alignment with other datasets, but datasets from different periods, such as the 2021 Census, cannot be treated as representing the same point in time.

- **Provincial Business Dynamics data** — the Business Dynamics datasets provide provincial/territorial geography, including Ontario, rather than Niagara census-subdivision geography. Their provincial geography therefore cannot be directly joined to Niagara-level CBC records. Any later use should treat them as broader Ontario context unless an appropriate aggregation strategy is established.

No datasets were merged during Week 3.

## 7. Succession-Data Gap

No column in the downloaded Canadian Business Counts file directly contains succession information. The following variables were checked and were not found:

- Owner age: absent
- Retirement intention: absent
- Planned exit: absent
- Succession-plan status: absent
- Identified successor: absent
- Ownership transfer information: absent
- Reason for closure: absent

`TERMINATED` is a Statistics Canada series-status field, not a business-closure reason, and it is empty in every row.

This confirms the Week 2 expectation that Canadian Business Counts does not directly measure business succession. No succession variables were created or inferred during Week 3.

## 8. New Findings and Limitations

New findings from inspecting the actual downloaded file include:

1. **Reference-period discrepancy:** the cube title says June 2026, while `REF_DATE` is `2026-01` and the metadata Start and End Reference Period are `2026-01-01`. The downloaded files do not explain this difference, so it remains documented as unresolved.

2. **Single-period dataset:** only one reference period is present. In addition, the Statistics Canada metadata advises against treating these data as a time series because methodological changes can affect counts between reference periods.

3. **`GEO` names are not unique:** 167 geographic names map to more than one `DGUID`. Therefore, `GEO` names alone should not be used as geographic joining keys. `DGUID` should be used where compatible geographic identifiers are available.

4. **NAICS structure:** NAICS codes are embedded in the industry labels and range from 1 to 4 digits. Twenty-two industry names occur at more than one hierarchy level. NAICS hierarchy must therefore be handled carefully during later cleaning and comparison.

5. **No suppression or quality flags are recorded in the relevant fields:** `STATUS`, `SYMBOL` and `TERMINATED` are empty in all rows, while the minimum `VALUE` is 1. Therefore, based on this file alone, an absent combination cannot be distinguished from a true zero or an unpublished combination.

6. **Employer businesses only:** the dataset does not contain categories for businesses without employees or indeterminate businesses. Businesses with no employees are therefore outside the scope of this table.

7. **No Niagara Region total row:** the dataset contains the 12 Niagara municipalities as census subdivisions and the St. Catharines - Niagara CMA, but no Niagara Region/census-division total row.

8. **Potential aggregation overlap:** the dataset includes aggregate and detailed categories, including `Total, with employees` alongside individual employment-size bands and broad NAICS totals alongside more detailed industries. These categories must not be summed without first accounting for their hierarchy and possible overlap.

Confirmed from Week 2: Canadian Business Counts contains no direct succession variables.

## 9. Historical CBC Data

No additional historical Canadian Business Counts files were acquired during Week 3.

Therefore, no comparison of historical columns, geography, NAICS classifications, employment-size definitions, reference periods or categories was performed, and no historical CBC tables were combined.

If historical CBC data are considered later, comparability must first be established before combining them with the current dataset.

## 10. Final Dataset Decision

**Decision: KEEP WITH LIMITATIONS**

**Reason:** The Canadian Business Counts dataset provides useful business-count information for all 12 Niagara Region municipalities and the St. Catharines - Niagara CMA, with industry information through NAICS and employment-size information for employer businesses.

However, the dataset contains only one reference period and no direct succession variables. It also has important limitations relating to geographic hierarchy, non-unique `GEO` names, NAICS hierarchy, employment-size aggregation, employer-business scope, and the absence of recorded suppression/quality flags.

The dataset can therefore contribute to the Niagara Succession Signal project as a source of business-population context, but it cannot by itself identify succession risk or succession-related business closures. Its documented limitations must be carried forward into later project phases.
