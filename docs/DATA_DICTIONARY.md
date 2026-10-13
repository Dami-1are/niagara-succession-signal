# Niagara Succession Signal — Data Dictionary

## Purpose

This document describes the variables used in the Niagara Succession Signal project. It is the single project data dictionary.

Only variables confirmed in the actual datasets are documented as available. Nothing is added because we expect it to exist. Anything not confirmed in a cleaning report, audit or file is marked **To confirm**; no row counts, column counts, filenames or cleaning results are guessed.

---

# 1. Data Dictionary Status

**Current Stage:** Week 4 — Data Dictionary and Cleaning Documentation (updated 2026-10-11)

Dataset status, sources, geography, time, units, aggregates, NAICS, proxies, conflicts and traceability are in `WEEK4_DATA_DOCUMENTATION.md`. Per-dataset status, PR author and approval are in Section 1 of that file. Conflicts between documents are listed in Section 10 of that file for team-lead review; none was resolved by changing methodology.

Cleaning reports read: Canadian Business Counts, Business Dynamics, census age, census self-employment and Statistics Canada succession, plus the root README and the CFIB CSV header. No NEI cleaning report file exists on `main`; NEI cleaning results are taken from the description of PR #24, which contains the cleaning report. The NEI notebook was not read. Cells not stated in a report or file are marked To confirm.

---

# 2. Variable Documentation Template

For every variable that enters our analysis, we record the 14 fields below. Every table in Sections 3 to 9 uses them, in this order.

| Field | Description |
|---|---|
| Dataset | Dataset where the variable comes from |
| Original Column Name | Exact name used in the source file |
| Standardised Name | Name used in our processed dataset, if changed |
| Description | What the variable represents |
| Data Type | Text, integer, decimal, date, category, etc. |
| Unit | Unit of measurement where applicable |
| Example | Example value |
| Geographic Level | Canada, Ontario, CMA, CD, CSD, Niagara Region, municipality, etc. |
| Reference Period | Year/date represented |
| Missing Values | Number or percentage missing |
| Source | Original organisation/dataset |
| Direct / Proxy / Context | How the variable relates to succession risk |
| Transformation | Any cleaning or transformation applied |
| Notes / Limitations | Important cautions about interpretation |

The issue's Step 4 names map onto this template as follows: Cleaned column name = Standardised Name; Cleaning action = Transformation; Missing/suppression treatment = stated in Missing Values and Transformation. The template's structure is unchanged.

---

# 3. Consolidated Niagara Employment Inventory

Provider: Niagara Region Open Data. Raw: `data/raw/OpenData_Consolidated_NEI_Opendata_-482263215789080610.csv`. Cleaned: `data/interim/nei_cleaned.csv` (98,065 rows x 20 columns). PR #24. Cleaning results are taken from the description of PR #24 (merged and approved), which contains the NEI cleaning report; no report file is tracked. The dataset was 98,065 rows x 20 columns before and after cleaning; no rows or columns were removed; there were no exact duplicate rows; all 20 columns were renamed to snake_case; text fields had whitespace stripped and blank text converted to missing. The coordinate system EPSG:3857 is described as likely (inferred), not confirmed from metadata. Data types are To confirm except where PR #24 states them (opening year numeric; NAICS codes stored as digit strings). Succession variables (owner age, retirement intention, exit timeline, successor, succession plan, closure reason) are not in these columns.

| Dataset | Original Column Name | Standardised Name | Description | Data Type | Unit | Example | Geographic Level | Reference Period | Missing Values | Source | Direct / Proxy / Context | Transformation | Notes / Limitations |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| NEI | `OBJECTID` | `objectid` | Dataset record identifier | To confirm | n/a | To confirm | Individual Niagara business, 12 municipalities | 2016-2019, 2022-2025 | Raw (audit): Not reported; cleaned: not listed as missing in PR #24 | Niagara Region | Contextual | Renamed (PR #24); no column-specific action listed | Suitability as a cross-dataset key not established |
| NEI | `NEI_ID` | `nei_id` | Business identifier | To confirm | n/a | To confirm | Individual Niagara business, 12 municipalities | 2016-2019, 2022-2025 | Raw (audit): 0; cleaned: not listed as missing in PR #24 | Niagara Region | Direct / business-level (not a succession variable) | Renamed; all 82,219 repeated `nei_id` observations across years retained (PR #24) | 15,846 distinct values; repeats across years |
| NEI | `Year` | `year` | Observation year | To confirm | Year | To confirm | Individual Niagara business, 12 municipalities | 2016-2019, 2022-2025 | Raw (audit): 0; cleaned: not listed as missing in PR #24 | Niagara Region | Contextual | Renamed (PR #24); no column-specific action listed | No 2020 or 2021; PR #24 preserves these as unobserved, with no interpolation |
| NEI | `Municipality` | `municipality` | Niagara Region municipality | To confirm | n/a | To confirm | Individual Niagara business, 12 municipalities | 2016-2019, 2022-2025 | Raw (audit): 0; cleaned: not listed as missing in PR #24 | Niagara Region | Contextual | Renamed; names and punctuation harmonised, for example St. Catharines and Niagara-on-the-Lake (PR #24) | Raw spelling differs from Canadian Business Counts (Section 10, item 10); the cleaned file uses the harmonised spellings (checked 2026-10-11) |
| NEI | `Business Name` | `business_name` | Business name | To confirm | n/a | Not shown (identifies a business) | Individual Niagara business, 12 municipalities | 2016-2019, 2022-2025 | Raw (audit): Not reported; cleaned: not listed as missing in PR #24 | Niagara Region | Direct / business-level (not a succession variable) | Renamed; whitespace stripped and internal whitespace collapsed (PR #24) | Do not reproduce records in documentation |
| NEI | `Business Street Number` | `business_street_number` | Street number | To confirm | n/a | Not shown | Individual Niagara business, 12 municipalities | 2016-2019, 2022-2025 | Raw (audit): Not reported; cleaned: not listed as missing in PR #24 | Niagara Region | Direct / business-level (not a succession variable) | Renamed; whitespace stripped (PR #24) |  |
| NEI | `Business Street Name` | `business_street_name` | Street name | To confirm | n/a | Not shown | Individual Niagara business, 12 municipalities | 2016-2019, 2022-2025 | Raw (audit): Not reported; cleaned: not listed as missing in PR #24 | Niagara Region | Direct / business-level (not a succession variable) | Renamed; whitespace stripped and internal whitespace collapsed (PR #24 refers to street addresses) |  |
| NEI | `Business Unit` | `business_unit` | Unit | To confirm | n/a | Not shown | Individual Niagara business, 12 municipalities | 2016-2019, 2022-2025 | Raw (PR #24): 74,541 missing; cleaned: 74,541 missing | Niagara Region | Direct / business-level (not a succession variable) | Renamed; whitespace stripped; blank text converted to missing (PR #24) | Optional field with many nulls (PR #24) |
| NEI | `Business PO Box` | `business_po_box` | PO box | To confirm | n/a | Not shown | Individual Niagara business, 12 municipalities | 2016-2019, 2022-2025 | Raw (PR #24): 94,275 missing; cleaned: 94,275 missing | Niagara Region | Direct / business-level (not a succession variable) | Renamed; whitespace stripped; blank text converted to missing (PR #24) | Optional field with many nulls (PR #24) |
| NEI | `Business Postal Code` | `business_postal_code` | Postal code | To confirm | n/a | Not shown | Individual Niagara business, 12 municipalities | 2016-2019, 2022-2025 | Raw (PR #24): 127 missing; cleaned: 127 missing | Niagara Region | Direct / business-level (not a succession variable) | Renamed; standardised to A1A 1A1 format per PR #24 (only 133 rows in the cleaned file as read contain a space; Week 4 documentation, Section 10, item 47) | Possible future matching field (audit) |
| NEI | `Business Website` | `business_website` | Website | To confirm | n/a | Not shown | Individual Niagara business, 12 municipalities | 2016-2019, 2022-2025 | Raw (PR #24): 34,573 missing; cleaned: 34,573 missing | Niagara Region | Direct / business-level (not a succession variable) | Renamed; lower-cased and trailing slashes trimmed (PR #24) |  |
| NEI | `Primary NAICS` | `primary_naics` | Primary NAICS code | Text (digit string; PR #24) | NAICS code | 312120 (format only) | Individual Niagara business, 12 municipalities | 2016-2019, 2022-2025 | Raw (audit): 0; cleaned: not listed as missing in PR #24 | Niagara Region | Direct / business-level (not a succession variable) | Renamed; stored as digit strings with trailing `.0` removed and leading zeros kept (PR #24) | Six-digit codes; NAICS version not stated; not harmonised |
| NEI | `Secondary NAICS` | `secondary_naics` | Secondary NAICS code | Text (digit string; PR #24) | NAICS code | To confirm | Individual Niagara business, 12 municipalities | 2016-2019, 2022-2025 | Raw (audit and PR #24): 19,404; cleaned: 19,404 blank (kept as missing, not imputed); the cleaned file also holds 0 in 68,237 rows (Week 4 documentation, Section 10, item 48) | Niagara Region | Direct / business-level (not a succession variable) | Renamed; stored as digit strings with trailing `.0` removed and leading zeros kept (PR #24) |  |
| NEI | `Primary Sector` | `primary_sector` | Primary sector | To confirm | n/a | To confirm | Individual Niagara business, 12 municipalities | 2016-2019, 2022-2025 | Raw (audit): 0; cleaned: not listed as missing in PR #24 | Niagara Region | Direct / business-level (not a succession variable) | Renamed; whitespace stripped (PR #24) |  |
| NEI | `Industry` | `industry` | Industry | To confirm | n/a | To confirm | Individual Niagara business, 12 municipalities | 2016-2019, 2022-2025 | Raw (audit): 0; cleaned: not listed as missing in PR #24 | Niagara Region | Direct / business-level (not a succession variable) | Renamed; whitespace stripped (PR #24) |  |
| NEI | `What year did this business open in Niagara?` | `opening_year` | Year the business opened in Niagara | Numeric (cast, PR #24) | Year | To confirm | Individual Niagara business, 12 municipalities | 2016-2019, 2022-2025 | Raw (audit and PR #24): 199 blank and 31,306 rows holding `0`; cleaned: 31,505 missing per PR #24 (the cleaned file as read on 2026-10-11 holds 199 blank and 31,306 0; Week 4 documentation, Section 10, item 47) | Niagara Region | Direct / business-level; potential proxy for business age (requires validation; not a confirmed succession-risk predictor) | Renamed; cast to numeric; values of 1800 or less, which includes the 31,306 `0` values, converted to missing; no business age calculated (PR #24) | The cleaner treated `0` as a placeholder; the audit had not established its meaning. PR #24 reports no valid values between 1 and 1800. Not owner age |
| NEI | `What is the indoor floor size (in square feet) of this business?` | `floor_size_sqft` | Indoor floor size (per column name) | To confirm | Square feet | To confirm | Individual Niagara business, 12 municipalities | 2016-2019, 2022-2025 | Raw (PR #24): 2,695 null plus more than 53,000 rows holding `0`; cleaned: 55,836 missing per PR #24 (the cleaned file as read on 2026-10-11 holds 2,695 blank and 53,181 0; Week 4 documentation, Section 10, item 47) | Niagara Region | Direct / business-level (not a succession variable) | Renamed; the treatment of the `0` values is not described in the PR #24 action list | Check the notebook if the treatment of `0` matters |
| NEI | `Size Range of Employees` | `size_range_of_employees` | Employee-size category | To confirm | Employee-size category | To confirm | Individual Niagara business, 12 municipalities | 2016-2019, 2022-2025 | Raw (audit): 0; cleaned: not listed as missing in PR #24 | Niagara Region | Direct / business-level; potential proxy for business size (requires validation; not a confirmed succession-risk predictor) | Renamed; raw categories (Micro, Small, Medium, Large, Aggregate, Zero Employees) kept separate from the descriptive ranges and not merged or recoded (PR #24) | 12 labels; `Aggregate` (22 rows, 2025) and short labels (2025 only) not explained in the audit |
| NEI | `x` | `x` | Coordinate | To confirm | Coordinate units; EPSG:3857 is likely (inferred, not confirmed from metadata; PR #24) | To confirm | Individual Niagara business, 12 municipalities | 2016-2019, 2022-2025 | Raw (audit and PR #24): 3; cleaned: 3 (2016 records, kept as missing, not removed) | Niagara Region | Direct / business-level (not a succession variable) | Renamed (PR #24); no other column-specific action listed | Coordinate reference system inferred, not confirmed; the 3 records cannot be mapped without geocoding |
| NEI | `y` | `y` | Coordinate | To confirm | Coordinate units; EPSG:3857 is likely (inferred, not confirmed from metadata; PR #24) | To confirm | Individual Niagara business, 12 municipalities | 2016-2019, 2022-2025 | Raw (audit and PR #24): 3; cleaned: 3 (2016 records, kept as missing, not removed) | Niagara Region | Direct / business-level (not a succession variable) | Renamed (PR #24); no other column-specific action listed | Coordinate reference system inferred, not confirmed; the 3 records cannot be mapped without geocoding |

---

# 4. Canadian Business Counts

Provider: Statistics Canada, Table 33-10-1176-01. Raw: `data/raw/33101176.csv` (1,047,957 rows x 16 columns, unchanged). Cleaned: `data/interim/canadian_business_counts_niagara_cleaned.csv` (10,462 x 14) and `canadian_business_counts_niagara_cma_reference.csv` (2,121 x 14). PR #29. Source: `reports/cbc_cleaning_report.md`. Column count: 16 raw − 9 removed = 7; NAICS split into two = 8; 6 added = 14.

| Dataset | Original Column Name | Standardised Name | Description | Data Type | Unit | Example | Geographic Level | Reference Period | Missing Values | Source | Direct / Proxy / Context | Transformation | Notes / Limitations |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Canadian Business Counts | `REF_DATE` | `ref_date` | Reference period | To confirm | Date | 2026-01 | 12 Niagara municipalities (CMA in a separate reference file) | 2026-01 | 0 | Statistics Canada, 33-10-1176-01 | Contextual | Renamed | Cube title says June 2026 (Section 10, item 1) |
| Canadian Business Counts | `GEO` | `geo` | Geography name | Text | n/a | Niagara Falls | 12 Niagara municipalities (CMA in a separate reference file) | 2026-01 | 0 | Statistics Canada, 33-10-1176-01 | Contextual | Renamed; kept as a label only | 167 names map to more than one DGUID |
| Canadian Business Counts | `DGUID` | `dguid` | Geography unique identifier | Text | n/a | 2021A00053526043 | 12 Niagara municipalities (CMA in a separate reference file) | 2026-01 | 0 | Statistics Canada, 33-10-1176-01 | Contextual | Renamed; used to select the 12 municipalities | Use instead of `GEO` |
| Canadian Business Counts | (added) | `geo_level` | Geography level flag | Text | n/a | `cma_reference_only` (CMA file) | 12 Niagara municipalities (CMA in a separate reference file) | 2026-01 | 0 | Statistics Canada, 33-10-1176-01 | Contextual | Added by cleaning | Value for municipality rows: to confirm from the file |
| Canadian Business Counts | `Employment size` | `employment_size` | Employee-count band | Text | Employee-size band | 1 to 4 employees | 12 Niagara municipalities (CMA in a separate reference file) | 2026-01 | 0 | Statistics Canada, 33-10-1176-01 | Contextual | Renamed; 9 categories kept with original wording | No micro/small/medium/large recoding |
| Canadian Business Counts | (added) | `employment_size_type` | `aggregate_total` or `size_band` | Text | n/a | size_band | 12 Niagara municipalities (CMA in a separate reference file) | 2026-01 | 0 | Statistics Canada, 33-10-1176-01 | Contextual | Added by cleaning | "Total, with employees" overlaps the bands |
| Canadian Business Counts | `North American Industry Classification System (NAICS)` | `naics_code` | NAICS code extracted from the label | Text | NAICS code | 72 | 12 Niagara municipalities (CMA in a separate reference file) | 2026-01 | 0 | Statistics Canada, 33-10-1176-01 | Contextual | Split from the raw label; stored as text | NAICS 2022; 403 distinct codes in the 12 municipalities |
| Canadian Business Counts | (same source column) | `naics_label` | Industry label | Text | n/a | Accommodation and food services | 12 Niagara municipalities (CMA in a separate reference file) | 2026-01 | 0 | Statistics Canada, 33-10-1176-01 | Contextual | Split from the raw label |  |
| Canadian Business Counts | (added) | `naics_digit_length` | Code length, 1 to 4 | To confirm | Digits | 2 | 12 Niagara municipalities (CMA in a separate reference file) | 2026-01 | 0 | Statistics Canada, 33-10-1176-01 | Contextual | Added by cleaning |  |
| Canadian Business Counts | (added) | `naics_level_name` | Level name (`aggregate_not_a_naics_level`, `sector`, `subsector`, `industry_group`) | Text | n/a | sector | 12 Niagara municipalities (CMA in a separate reference file) | 2026-01 | 0 | Statistics Canada, 33-10-1176-01 | Contextual | Added by cleaning | Levels nested; do not sum across levels |
| Canadian Business Counts | (added) | `naics_is_range` | Marks range codes such as 31-33 | Boolean (to confirm) | n/a | To confirm | 12 Niagara municipalities (CMA in a separate reference file) | 2026-01 | 0 | Statistics Canada, 33-10-1176-01 | Contextual | Added by cleaning | Range codes treated as 2-digit sectors |
| Canadian Business Counts | (added) | `naics_category_type` | `aggregate_total`, `unclassified`, `aggregate_subtotal_classified` or `industry` | Text | n/a | industry | 12 Niagara municipalities (CMA in a separate reference file) | 2026-01 | 0 | Statistics Canada, 33-10-1176-01 | Contextual | Added by cleaning | Nothing deleted; filter before analysing industries |
| Canadian Business Counts | `VALUE` | `business_count` | Number of employer businesses | Integer | Number of businesses | Range 1 to 262,535 (raw) | 12 Niagara municipalities (CMA in a separate reference file) | 2026-01 | 0 | Statistics Canada, 33-10-1176-01 | Contextual | Converted to integer; no zero fill | Employer businesses only; absent combinations are not zeros |
| Canadian Business Counts | `VECTOR` | `vector` | Statistics Canada series identifier | Text | n/a | v1918450229 | 12 Niagara municipalities (CMA in a separate reference file) | 2026-01 | 0 | Statistics Canada, 33-10-1176-01 | Contextual | Renamed |  |
| Canadian Business Counts | `UOM`, `UOM_ID`, `SCALAR_FACTOR`, `SCALAR_ID`, `DECIMALS` | (removed) | Constants: 'Number', 223, 'units', 0, 0 | n/a | n/a | n/a | 12 Niagara municipalities (CMA in a separate reference file) | 2026-01 | 0 | Statistics Canada, 33-10-1176-01 | Contextual | Removed from the analytical file; kept in raw | Constant in every raw row |
| Canadian Business Counts | `COORDINATE` | (removed) | Position index across table dimensions | Text | n/a | 1.1.2 | 12 Niagara municipalities (CMA in a separate reference file) | 2026-01 | 0 | Statistics Canada, 33-10-1176-01 | Contextual | Removed; redundant | Kept in raw |
| Canadian Business Counts | `STATUS`, `SYMBOL`, `TERMINATED` | (removed) | Status, symbol, terminated flags | Text | n/a | (blank) | 12 Niagara municipalities (CMA in a separate reference file) | 2026-01 | Empty in all 1,047,957 raw rows | Statistics Canada, 33-10-1176-01 | Contextual | Removed; empty | Not business status or closure information |

---

# 5. Business Dynamics

Provider: Statistics Canada, Tables 33-10-0087-01 (industry) and 33-10-0088-01 (firm size). Cleaned: `data/processed/statcan/business_dynamics/business_dynamics_industry_ontario_cleaned.csv` and `business_dynamics_firm_size_ontario_cleaned.csv`. PR #26. Source: `docs/data_audits/BUSINESS_DYNAMICS_CLEANING_REPORT.md`. Ontario only (2,484 and 828 rows). Business exits are not succession-related closures.

| Dataset | Original Column Name | Standardised Name | Description | Data Type | Unit | Example | Geographic Level | Reference Period | Missing Values | Source | Direct / Proxy / Context | Transformation | Notes / Limitations |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Business Dynamics | `REF_DATE` | `ref_date` | Reference year | To confirm | Year | 2001 to 2023 | Province (Ontario only in cleaned files) | 2001-2023 | To confirm | Statistics Canada, 33-10-0087-01 / 33-10-0088-01 | Contextual | Renamed |  |
| Business Dynamics | `GEO` | `geo` | Province or territory | Text | n/a | Ontario | Province (Ontario only in cleaned files) | 2001-2023 | To confirm | Statistics Canada, 33-10-0087-01 / 33-10-0088-01 | Contextual | Renamed; Ontario selected | Not Niagara |
| Business Dynamics | `DGUID` | `dguid` | Geography identifier | Text | n/a | 2016A000235 | Province (Ontario only in cleaned files) | 2001-2023 | To confirm | Statistics Canada, 33-10-0087-01 / 33-10-0088-01 | Contextual | Renamed | 2016 vintage; CBC uses 2021 vintage (Section 10, item 19) |
| Business Dynamics | `Business dynamics measure` (0087) / `Employment dynamics` (0088) | `business_dynamics_measure` | Measure reported on the row (active, entrants, incumbents, exits; rates in 0087 only) | Text | Businesses or percent | Exits | Province (Ontario only in cleaned files) | 2001-2023 | To confirm | Statistics Canada, 33-10-0087-01 / 33-10-0088-01 | Proxy (exits only; not succession closures) | Renamed | An exit is not evidence of succession or retirement |
| Business Dynamics | `North American Industry Classification System (NAICS)` (0087) | `naics` (+ `industry_label`, `naics_code`, `naics_version` added) | Industry category | Text | n/a | To confirm | Province (Ontario only in cleaned files) | 2001-2023 | To confirm | Statistics Canada, 33-10-0087-01 / 33-10-0088-01 | Contextual | Label and code split; version added by year | Four NAICS versions over 2001-2023; not harmonised |
| Business Dynamics | `Firm size` (0088) | `firm_size` | Firm-size category | Text | n/a | To confirm | Province (Ontario only in cleaned files) | 2001-2023 | To confirm | Statistics Canada, 33-10-0087-01 / 33-10-0088-01 | Contextual | Renamed; source categories kept | Nine nested, overlapping categories; do not sum |
| Business Dynamics | `VALUE` | `value` | Businesses or a rate | Decimal | Number or percent | To confirm | Province (Ontario only in cleaned files) | 2001-2023 | 0087: 36 missing (all `..`); 0088: 196 missing (all `x`) in the Ontario outputs | Statistics Canada, 33-10-0087-01 / 33-10-0088-01 | Contextual | Not imputed or zero-filled | Counts rounded to units of ten |
| Business Dynamics | `STATUS` | `status` (+ `status_interpretation` added) | Status flag | Text | n/a | `x`, `..`, blank | Province (Ontario only in cleaned files) | 2001-2023 | To confirm | Statistics Canada, 33-10-0087-01 / 33-10-0088-01 | Contextual | Kept; interpretation column added |  |
| Business Dynamics | `UOM`, `SCALAR_FACTOR` | `uom`, `scalar_factor` | Unit and scale | Text | n/a | Number, units | Province (Ontario only in cleaned files) | 2001-2023 | To confirm | Statistics Canada, 33-10-0087-01 / 33-10-0088-01 | Contextual | Renamed | Other metadata columns' cleaned names: to confirm |
| Business Dynamics | `UOM_ID`, `SCALAR_ID`, `VECTOR`, `COORDINATE`, `DECIMALS` | To confirm | Series metadata | Text / code | n/a | To confirm | Province (Ontario only in cleaned files) | 2001-2023 | To confirm | Statistics Canada, 33-10-0087-01 / 33-10-0088-01 | Contextual | To confirm | Not listed in the cleaning report |
| Business Dynamics | `SYMBOL`, `TERMINATED` | (removed) | Empty columns | n/a | n/a | n/a | Province (Ontario only in cleaned files) | 2001-2023 | Empty | Statistics Canada, 33-10-0087-01 / 33-10-0088-01 | Contextual | Removed from cleaned outputs | Unchanged in raw |

---

# 6. Census Age Data

Provider: Statistics Canada, Table 98-10-0022-01. Cleaned: `census_age_niagara_cleaned.csv` (repository root; 3,328 rows x 12 columns = 13 geographies x 256). PR #28. Source: `census_age_cleaning_report.md`. All 12 column names are kept as in the raw file. Population age describes the population, not business owners.

| Dataset | Original Column Name | Standardised Name | Description | Data Type | Unit | Example | Geographic Level | Reference Period | Missing Values | Source | Direct / Proxy / Context | Transformation | Notes / Limitations |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Census age | `REF_DATE` | `REF_DATE` | Reference year | Integer | Year | 2021 | Niagara census division and 12 CSDs | Census years 2016 and 2021 | 0 | Statistics Canada, 98-10-0022-01 | Contextual | None (name kept) | Reads 2021 on every raw row; use `Census year (2)` |
| Census age | `GEO` | `GEO` | Geography name | Text | n/a | Fort Erie | Niagara census division and 12 CSDs | Census years 2016 and 2021 | 0 | Statistics Canada, 98-10-0022-01 | Contextual | Filtered to Niagara by DGUID | Names shared across DGUIDs |
| Census age | `DGUID` | `DGUID` | Geography identifier | Text | n/a | 2021A00053526057 (Lincoln) | Niagara census division and 12 CSDs | Census years 2016 and 2021 | 0 | Statistics Canada, 98-10-0022-01 | Contextual | Used for filtering | Other Lincoln (2021A00051303008) excluded |
| Census age | `Census year (2)` | `Census year (2)` | Census reference year | Integer | Year | 2016, 2021 | Niagara census division and 12 CSDs | Census years 2016 and 2021 | 0 | Statistics Canada, 98-10-0022-01 | Contextual | None; both years kept | No annual values created |
| Census age | `Age (in single years), average age and median age (128)` | same | Age category or statistic | Text | Years | 0 to 14 years | Niagara census division and 12 CSDs | Census years 2016 and 2021 | 0 | Statistics Canada, 98-10-0022-01 | Proxy (population age; not owner age) | Whitespace trimmed; hierarchy not summed | 128 nested labels; do not sum |
| Census age | `Coordinate` | `Coordinate` | Member-position index | Text | n/a | 1.1.2 | Niagara census division and 12 CSDs | Census years 2016 and 2021 | To confirm | Statistics Canada, 98-10-0022-01 | Contextual | None |  |
| Census age | `Gender (3a):Total - Gender[1]` | same | Persons, all genders | Numeric | Persons | Not shown (Niagara values not read here) | Niagara census division and 12 CSDs | Census years 2016 and 2021 | 0 in cleaned file | Statistics Canada, 98-10-0022-01 | Proxy (population age; not owner age) | Values unchanged | Randomly rounded to multiples of 5; population, not owners |
| Census age | `Symbol` | `Symbol` | Status flag for Total | Text | n/a | blank | Niagara census division and 12 CSDs | Census years 2016 and 2021 | Blank on all 3,328 rows | Statistics Canada, 98-10-0022-01 | Contextual | Preserved | No `x` or `...` in the Niagara subset |
| Census age | `Gender (3a):Men+[2]` | same | Persons, Men+ | Numeric | Persons | Not shown | Niagara census division and 12 CSDs | Census years 2016 and 2021 | 0 in cleaned file | Statistics Canada, 98-10-0022-01 | Proxy (population age; not owner age) | Values unchanged | Not forced to sum to Total |
| Census age | `Symbol` (second) | `Symbol.1` | Status flag for Men+ | Text | n/a | blank | Niagara census division and 12 CSDs | Census years 2016 and 2021 | Blank on all rows | Statistics Canada, 98-10-0022-01 | Contextual | Preserved | Automatic pandas name |
| Census age | `Gender (3a):Women+[3]` | same | Persons, Women+ | Numeric | Persons | Not shown | Niagara census division and 12 CSDs | Census years 2016 and 2021 | 0 in cleaned file | Statistics Canada, 98-10-0022-01 | Proxy (population age; not owner age) | Values unchanged | Not forced to sum to Total |
| Census age | `Symbol` (third) | `Symbol.2` | Status flag for Women+ | Text | n/a | blank | Niagara census division and 12 CSDs | Census years 2016 and 2021 | Blank on all rows | Statistics Canada, 98-10-0022-01 | Contextual | Preserved | Automatic pandas name |

---

# 7. Census Class of Worker / Self-Employment

Provider: Statistics Canada, Table 98-10-0592-01 (2021 Census, 25% sample). Cleaned: `data/interim/census_self_employment_niagara_cleaned.csv` (125,714 rows x 21 columns; Niagara census division `2021A00033526`). PR #30. Source: `docs/data_audits/CENSUS_SELF_EMPLOYMENT_CLEANING_REPORT.md`. Column count: 20 raw − 5 removed = 15; plus 6 added = 21. The cleaned header was not read, so original columns other than `DGUID`, `COORDINATE` and `VALUE` are named only generically below. The report's raw file (125,714 rows, 20 columns) does not match the Week 3 audit's file (53,215,380 rows, 23 columns), so the audit's column list is not used here (`WEEK4_DATA_DOCUMENTATION.md`, Section 10, item 43). Self-employment is not treated as direct evidence of business ownership.

| Dataset | Original Column Name | Standardised Name | Description | Data Type | Unit | Example | Geographic Level | Reference Period | Missing Values | Source | Direct / Proxy / Context | Transformation | Notes / Limitations |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Census class of worker | `DGUID` | `DGUID` (to confirm) | Geography identifier: Niagara census division | Text | n/a | 2021A00033526 | Niagara census division | 2021 Census (25% sample) | 0 (cleaned file has no missing values) | Statistics Canada, 98-10-0592-01 | Contextual | Filtered to Niagara; kept | Not a municipality |
| Census class of worker | Original dimension columns (age, gender, labour force status, industry, class of worker) | To confirm from header | Category labels for the census dimensions | Text | n/a | To confirm | Niagara census division | 2021 Census (25% sample) | 0 | Statistics Canada, 98-10-0592-01 | Contextual | Kept | Names not listed in the report. Age groups overlap; industries are hierarchical; do not sum |
| Census class of worker | Other retained original columns (for example reference year and geography name) | To confirm from header | To confirm | To confirm | n/a | To confirm | Niagara census division | 2021 Census (25% sample) | 0 | Statistics Canada, 98-10-0592-01 | Contextual | Kept | Not named in the report; 12 of the 15 retained originals are not named in the report; to confirm from the header |
| Census class of worker | `COORDINATE` | `COORDINATE` | Statistics Canada position index across the five dimensions | Text | n/a | To confirm | Niagara census division | 2021 Census (25% sample) | 0 | Statistics Canada, 98-10-0592-01 | Contextual | Preserved unchanged; the five identifiers below are extracted from it | No duplicate coordinates |
| Census class of worker | `VALUE` | `VALUE` | Census count of persons | Integer | Persons | To confirm | Niagara census division | 2021 Census (25% sample) | 0 (no negative or decimal counts) | Statistics Canada, 98-10-0592-01 | Proxy for the self-employed categories (not a business owner); Contextual otherwise | Kept as integer; counts not changed or estimated | Aggregate 25% sample counts, not individual records |
| Census class of worker | (added from `COORDINATE`) | `class_worker_id` | Class of worker identifier (7 values) | Integer (to confirm) | n/a | To confirm | Niagara census division | 2021 Census (25% sample) | 0 | Statistics Canada, 98-10-0592-01 | Proxy / Contextual | Added by cleaning | ID 5 = self-employed including unpaid family workers; ID 6 = excluding them |
| Census class of worker | (added) | `class_worker_label` | Label separating the two categories both named `Self-employed` | Text | n/a | To confirm | Niagara census division | 2021 Census (25% sample) | 0 | Statistics Canada, 98-10-0592-01 | Proxy / Contextual | Added by cleaning | Both kept; not combined |
| Census class of worker | (added from `COORDINATE`) | `industry_id` | Industry identifier (400 unique) | Integer (to confirm) | n/a | To confirm | Niagara census division | 2021 Census (25% sample) | 0 | Statistics Canada, 98-10-0592-01 | Contextual | Added by cleaning | 28 of the 1 to 428 identifiers are absent for an unconfirmed reason; absent is not zero |
| Census class of worker | (added from `COORDINATE`) | `age_id` | Age identifier (15 unique) | Integer (to confirm) | n/a | To confirm | Niagara census division | 2021 Census (25% sample) | 0 | Statistics Canada, 98-10-0592-01 | Proxy (population age; not owner age) | Added by cleaning | Overlapping age groups |
| Census class of worker | (added from `COORDINATE`) | `gender_id` | Gender identifier (3 unique) | Integer (to confirm) | n/a | To confirm | Niagara census division | 2021 Census (25% sample) | 0 | Statistics Canada, 98-10-0592-01 | Contextual | Added by cleaning |  |
| Census class of worker | (added from `COORDINATE`) | `labour_status_id` | Labour force status identifier (3 unique) | Integer (to confirm) | n/a | To confirm | Niagara census division | 2021 Census (25% sample) | 0 | Statistics Canada, 98-10-0592-01 | Contextual | Added by cleaning |  |
| Census class of worker | `UOM`, `VECTOR`, `STATUS`, `SYMBOL`, `TERMINATED` | (removed) | Five columns that were empty in the raw file | n/a | n/a | n/a | Niagara census division | 2021 Census (25% sample) | Empty (628,570 missing cells in total) | Statistics Canada, 98-10-0592-01 | Contextual | Removed; kept in raw | The cleaned file has no status column |

---

# 8. Statistics Canada Succession Tables (33-10-1196-01 to 33-10-1199-01)

Provider: Statistics Canada. Cleaned: `data/interim/statcan_33101196_ontario_cleaned.csv` (476 x 15), `...1197...` (476 x 15), `...1198...` (1,360 x 16), `...1199...` (1,020 x 16). PR #27. Source: `docs/data_audits/STATCAN_SUCCESSION_CLEANING_REPORT.md`. Ontario contextual benchmark only, not Niagara data. Percentages are aggregate survey results, not individual-business probabilities.

| Dataset | Original Column Name | Standardised Name | Description | Data Type | Unit | Example | Geographic Level | Reference Period | Missing Values | Source | Direct / Proxy / Context | Transformation | Notes / Limitations |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Succession tables | `REF_DATE` | `REF_DATE` | Reference year | Integer | Year | 2026 | Ontario | 2026 | 0 | Statistics Canada, 33-10-1196-01 to 1199-01 | Contextual | None | 2026 on all rows |
| Succession tables | `GEO` | `GEO` | Geography name | Text | n/a | Ontario | Ontario | 2026 | 0 | Statistics Canada, 33-10-1196-01 to 1199-01 | Contextual | Filtered to Ontario | No Niagara geography |
| Succession tables | `DGUID` | `DGUID` | Geography identifier | Text | n/a | 2021A000235 | Ontario | 2026 | 0 | Statistics Canada, 33-10-1196-01 to 1199-01 | Contextual | Filtered to Ontario | Differs from the 2016-vintage Ontario DGUID in Business Dynamics |
| Succession tables | Dimension columns: `Business characteristics` and `Intentions for businesses to sell or transfer ownership within the next 10 years` (1196); `Expectations related to selling or transferring of the business` (1197); `Considerations related to the sale or transfer of the business` and `Level of importance` (1198); `Various scenarios if business is unable to find a suitable buyer or successor` and `Likelihood` (1199) | same | Survey category (industry, size, intention, expectation, consideration, scenario) | Text | n/a | To confirm | Ontario | 2026 | 0 | Statistics Canada, 33-10-1196-01 to 1199-01 | Contextual | Original categories preserved; no cross-dataset aggregation | Other breakdown columns: to confirm from the file headers. Aggregate and overlapping categories possible |
| Succession tables | `UOM`, `UOM_ID`, `SCALAR_FACTOR`, `SCALAR_ID`, `VECTOR`, `COORDINATE`, `DECIMALS` | same | Unit, scale and series metadata | Text / code | Percent | Percent | Ontario | 2026 | 0 | Statistics Canada, 33-10-1196-01 to 1199-01 | Contextual | Kept | `UOM` is Percent on all rows; no conversion to counts |
| Succession tables | `VALUE` | `VALUE` | Percentage of businesses giving the answer | Numeric | Percent | To confirm | Ontario | 2026 | 1196: 107; 1197: 162; 1198: 477; 1199: 344 (all `F` or `..`) | Statistics Canada, 33-10-1196-01 to 1199-01 | Contextual | Not imputed or zero-filled | Aggregate survey percentage for Ontario; not an individual probability |
| Succession tables | `STATUS` | `STATUS` | Quality or availability flag | Text | n/a | `F`, `..`, `A` to `E` (to confirm which appear) | Ontario | 2026 | n/a | Statistics Canada, 33-10-1196-01 to 1199-01 | Contextual | Kept | `F` = too unreliable to be published; `..` = not available for the period |
| Succession tables | `SYMBOL` | (absent) | Symbol | n/a | n/a | n/a | Ontario | 2026 | Empty in the audit | Statistics Canada, 33-10-1196-01 to 1199-01 | Contextual | Absent from cleaned files; removal not stated in the report | Section 10, item 39 |
| Succession tables | `TERMINATED` | `TERMINATED` | Terminated-series flag | Text | n/a | To confirm | Ontario | 2026 | To confirm | Statistics Canada, 33-10-1196-01 to 1199-01 | Contextual | Kept |  |

---

# 9. CFIB Succession Evidence

Provider: CFIB, *Succession Tsunami* (survey fielded June 27 to August 17, 2022; 2,479 owners; Canada). Structured file: `data/processed/cfib/cfib_succession_evidence_structured.csv` (PR #25). The 13 evidence records are listed in `docs/data_audits/CFIB_SUCCESSION_EVIDENCE_NOTES.md`. The 11 column names are from the CSV header (read 2026-10-11); column contents and types are To confirm because only the header was read.

| Dataset | Original Column Name | Standardised Name | Description | Data Type | Unit | Example | Geographic Level | Reference Period | Missing Values | Source | Direct / Proxy / Context | Transformation | Notes / Limitations |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| CFIB evidence | `source` | `source` | Source organisation or report | Text | n/a | To confirm | Canada | Survey fielded 2022-06-27 to 2022-08-17 | To confirm | CFIB, Succession Tsunami | Contextual | None recorded |  |
| CFIB evidence | `source_year` | `source_year` | Year of the source | Integer (to confirm) | Year | 2022 (survey fielded 2022) | Canada | Survey fielded 2022-06-27 to 2022-08-17 | To confirm | CFIB, Succession Tsunami | Contextual | None recorded |  |
| CFIB evidence | `topic` | `topic` | Topic of the evidence record (contents to confirm) | Text | n/a | To confirm | Canada | Survey fielded 2022-06-27 to 2022-08-17 | To confirm | CFIB, Succession Tsunami | Contextual | None recorded | Five measures: exit intention, exit method, succession planning, planning by timeline, barriers |
| CFIB evidence | `measure` | `measure` | Measure reported (contents to confirm) | Text | n/a | To confirm | Canada | Survey fielded 2022-06-27 to 2022-08-17 | To confirm | CFIB, Succession Tsunami | Contextual | None recorded | Keep measures separate |
| CFIB evidence | `category` | `category` | Answer category (contents to confirm) | Text | n/a | To confirm | Canada | Survey fielded 2022-06-27 to 2022-08-17 | To confirm | CFIB, Succession Tsunami | Contextual | None recorded | Exit-method percentages are not mutually exclusive |
| CFIB evidence | `value` | `value` | Reported percentage | Numeric (to confirm) | Percent (per notes) | 76 (exit-intention record in the notes) | Canada | Survey fielded 2022-06-27 to 2022-08-17 | To confirm | CFIB, Succession Tsunami | Contextual | None recorded | Survey percentage of owners; not a probability of closure |
| CFIB evidence | `unit` | `unit` | Unit of `value` | Text | n/a | To confirm | Canada | Survey fielded 2022-06-27 to 2022-08-17 | To confirm | CFIB, Succession Tsunami | Contextual | None recorded |  |
| CFIB evidence | `population` | `population` | Population the percentage applies to | Text | n/a | To confirm | Canada | Survey fielded 2022-06-27 to 2022-08-17 | To confirm | CFIB, Succession Tsunami | Contextual | None recorded | Timeline-specific plan percentages apply only to owners exiting in that timeline |
| CFIB evidence | `geography` | `geography` | Geography of the evidence | Text | n/a | Canada | Canada | Survey fielded 2022-06-27 to 2022-08-17 | To confirm | CFIB, Succession Tsunami | Contextual | None recorded | No Niagara or Ontario breakdown |
| CFIB evidence | `source_page` | `source_page` | Page (and figure) in the report | Text / integer (to confirm) | n/a | To confirm | Canada | Survey fielded 2022-06-27 to 2022-08-17 | To confirm | CFIB, Succession Tsunami | Contextual | None recorded |  |
| CFIB evidence | `notes` | `notes` | Notes on the record | Text | n/a | To confirm | Canada | Survey fielded 2022-06-27 to 2022-08-17 | To confirm | CFIB, Succession Tsunami | Contextual | None recorded |  |

---
# 10. Variable Classification

- **Direct / business-level:** Variables observed for individual Niagara businesses in NEI, including location, municipality, industry, NAICS, opening year and employee-size category. These are business characteristics, not direct evidence of succession risk.

- **Proxy:** Population age, self-employment and business exits may provide indirect evidence relevant to succession vulnerability. NEI opening year and employee-size category are directly observed business-level fields that may also be used as potential proxies for business age and size, subject to validation. None is a confirmed predictor of succession-related closure.

- **Contextual:** Canadian Business Counts, Ontario Business Dynamics, Ontario Statistics Canada succession tables and Canada-level CFIB evidence provide broader business and succession context. They do not establish individual Niagara business succession-risk probabilities.

**Important:** No available dataset directly identifies whether an individual Niagara business has a succession plan, an identified successor, a retirement intention or a succession-related closure.

The suitability of proxy variables for modelling requires team-lead confirmation and validation. See `WEEK4_DATA_DOCUMENTATION.md`, Sections 7, 8 and 10.

# 11. Standardisation Rules

1. Original column names are recorded first; any renamed column has both names documented.
2. Data types, units, missing values and category mappings are recorded.
3. NAICS versions, business-size definitions and geographic transformations are documented, not harmonised.
4. Derived variables are documented with how they were calculated.
5. Missing values are measured before treatment.
6. A variable is not added because we expect or want it to exist; only variables confirmed in the actual downloaded datasets are documented as available.

---

# 12. Derived Variables

| Derived Variable | Created From | Formula / Rule | Purpose | Limitation |
|---|---|---|---|---|
| None created in this documentation | n/a | n/a | n/a | Columns added by cleaning notebooks (for example the six added Canadian Business Counts columns) are listed in their dataset tables |

A derived succession-risk feature will not be presented as an observed variable.

---

# 13. Data Dictionary Completion Checklist

- [ ] Every dataset used in the aggregated data layer is documented (class of worker header and CFIB column contents To confirm).
- [ ] Original column names are recorded for audited datasets (some Census Class of Worker column names still need confirmation).
- [ ] Standardised names recorded where applicable (class of worker, part of Business Dynamics To confirm).
- [ ] Data types, units and examples recorded (many NEI data type cells, and many Business Dynamics and class-of-worker cells, To confirm).
- [x] Geographic levels and reference periods recorded.
- [ ] Missingness documented for every variable.
- [ ] Transformations documented (NEI from the PR #24 description; class of worker header not read).
- [x] Direct, proxy and contextual variables distinguished.
- [ ] Definitions checked against official source metadata.
- [ ] Every retained variable is documented (many cells To confirm).
- [ ] Variable definitions are recorded (many cells To confirm).
- [ ] Derived variables are documented (none created in this documentation; columns added by cleaning are in the dataset tables).
- [x] Important limitations are documented.

---

# Relationship to Required Deliverable 4.1

The challenge requires an **Aggregated Data Layer**: a cleaned, documented, aggregated dataset joining relevant open sources at appropriate sector and municipal levels. This dictionary, with `WEEK4_DATA_DOCUMENTATION.md`, documents the datasets that feed it.

---

## Week 4 additions (added 2026-10-13)

### NEI cleaned file: `data/interim/nei_cleaned.csv` (98,065 rows x 22 columns)
Two flag columns were added to the 20 original NEI columns. Flags only mark records; no rows were removed or altered.

| Column | Type | Meaning | Counts |
|---|---|---|---|
| `postal_code_status` | text | Quality flag for `business_postal_code`. Includes `Missing` and `Invalid - Review`; the validation rule is in `notebooks/02_data_cleaning/02_nei_cleaning.ipynb`. | 127 Missing; 153 Invalid - Review |
| `nei_id_conflict` | True/False | True when the same `nei_id` in the same survey `year` appears under more than one distinct `business_name`. Every row in such a group is flagged. Missing names count as their own value. | 278 True; 97,787 False |

Note: repeated `nei_id` values across different years are longitudinal observations of the same business and are not flagged.

### Raw files not stored in the repository
| File | Used by | How to obtain |
|---|---|---|
| `data/raw/98100022.csv` (Census Table 98-10-0022-01) | Census Age cleaning (Precious) | Download from Statistics Canada; see `data/raw/DATA_SOURCES.md` |
| `data/raw/9810059201_databaseLoadingData.csv` (Census Table 98-10-0592-01) | Self-employment cleaning (Ruth) | Download the database-loading CSV from Statistics Canada; see `data/raw/DATA_SOURCES.md` |
