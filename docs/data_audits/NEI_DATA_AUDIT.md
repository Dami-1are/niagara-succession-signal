# NEI Data Audit

## 1. Dataset Identification

**Dataset name:** Consolidated Niagara Employment Inventory (Consolidated NEI Opendata)

**Provider:** Niagara Region

**Official source:**  
https://open.niagararegion.ca/datasets/d23f4f781add4584904bc78b94c869b3_45/explore

**Original filename:**  
`OpenData_Consolidated_NEI_Opendata_-482263215789080610.csv`

**File format:** CSV

**Date downloaded:** September 28, 2026

**Downloaded by:** Stephen Ayankoso

**Repository location:**  
`data/raw/OpenData_Consolidated_NEI_Opendata_-482263215789080610.csv`

**Licence:** No license provided on the Consolidated NEI dataset page at the time of download.

**Raw file modified:** No

---

## 2. Dataset Structure

The downloaded CSV contains:

- **Records:** 98,065
- **Columns:** 20

### Actual columns

1. `OBJECTID`
2. `NEI_ID`
3. `Year`
4. `Municipality`
5. `Business Name`
6. `Business Street Number`
7. `Business Street Name`
8. `Business Unit`
9. `Business PO Box`
10. `Business Postal Code`
11. `Business Website`
12. `Primary NAICS`
13. `Secondary NAICS`
14. `Primary Sector`
15. `Industry`
16. `What year did this business open in Niagara?`
17. `What is the indoor floor size (in square feet) of this business?`
18. `Size Range of Employees`
19. `x`
20. `y`

The actual downloaded record count confirms the approximate 98,065 records identified during the Week 2 research.

---

## 3. Historical Year Coverage

The `Year` field contains the following observations:

| Year | Records |
|---|---:|
| 2016 | 10,403 |
| 2017 | 11,198 |
| 2018 | 11,664 |
| 2019 | 12,016 |
| 2022 | 13,033 |
| 2023 | 12,692 |
| 2024 | 13,335 |
| 2025 | 13,724 |
| **Total** | **98,065** |

No records with `Year` values of 2020 or 2021 were observed.

This creates a historical coverage gap for 2020–2021 that should be considered when comparing observations across years.

The downloaded consolidated dataset contains records through 2025. Although the Niagara Region confirmed that a 2026 NEI survey was conducted, a dedicated 2026 dataset was not identified through the public Open Data search during the Week 2 research.

---

## 4. Geographic Coverage

The dataset contains all 12 municipalities in Niagara Region.

| Municipality | Records |
|---|---:|
| Fort Erie | 6,224 |
| Grimsby | 4,009 |
| Lincoln | 4,644 |
| Niagara Falls | 22,430 |
| Niagara on the Lake | 4,863 |
| Pelham | 2,815 |
| Port Colborne | 3,874 |
| St Catharines | 32,885 |
| Thorold | 4,443 |
| Wainfleet | 537 |
| Welland | 9,741 |
| West Lincoln | 1,600 |
| **Total** | **98,065** |

The dataset also contains:

- `Business Street Number`
- `Business Street Name`
- `Business Unit`
- `Business PO Box`
- `Business Postal Code`
- `x`
- `y`

Three records have blank values for each of the `x` and `y` coordinate fields.

The coordinate fields may support future geographic or spatial analysis, but the coordinate reference system should be confirmed from the dataset metadata before use.

No municipality values were blank in the audited data.

---

## 5. NAICS, Sector and Industry

The dataset contains:

- `Primary NAICS`
- `Secondary NAICS`
- `Primary Sector`
- `Industry`

Non-empty counts:

| Field | Non-empty records |
|---|---:|
| Primary NAICS | 98,065 |
| Secondary NAICS | 78,661 |
| Primary Sector | 98,065 |
| Industry | 98,065 |

Therefore, all records have a Primary NAICS, Primary Sector and Industry value in the audited CSV.

Secondary NAICS is not populated for 19,404 records.

Primary NAICS values observed include six-digit classifications, for example:

- `312120` — Breweries
- `621210` — Offices of dentists
- `541212` — Offices of accountants
- `722511` — Full-service restaurants
- `458112` — Women's clothing retailers

NAICS values were not recoded or standardized during the audit.

These fields may support future comparison with Statistics Canada datasets, subject to checking classification year, level of aggregation, geography and compatibility before joining.

---

## 6. Business Opening Information

The dataset contains the field:

`What year did this business open in Niagara?`

Audit findings:

- Non-empty records: 97,866
- Blank records: 199
- Earliest observed value: `0`
- Latest observed value: `2026`
- Records with value `0`: 31,306

Other unusually early historical values are also present.

The field therefore requires clarification before it can safely be used for business-age calculations.

No values were changed during the audit.

Business age was **not calculated** during Week 3.

---

## 7. Employee-Size Information

The employee-size field is:

`Size Range of Employees`

The exact categories and record counts are:

| Employee-size category | Records |
|---|---:|
| Small (5-99 Employees) | 37,584 |
| Micro (1-4 Employees) | 26,606 |
| Permanently Closed or Vacant | 17,809 |
| Undetermined | 14,075 |
| Medium (100-499 Employees) | 1,700 |
| Large (500 + Employees) | 209 |
| Zero Employees | 32 |
| Aggregate | 22 |
| Small | 15 |
| Micro | 9 |
| Medium | 3 |
| Large | 1 |
| **Total** | **98,065** |

The expected detailed categories are present:

- Micro (1-4 Employees)
- Small (5-99 Employees)
- Medium (100-499 Employees)
- Large (500 + Employees)
- Undetermined
- Permanently Closed or Vacant

Additional categories — `Aggregate`, `Micro`, `Small`, `Medium`, `Large`, and `Zero Employees` — occur only in the 2025 records.

The metadata inspected does not establish whether these additional categories represent a classification change, aggregation, or another reporting convention.

These categories were not recoded or combined during the audit.

---

## 8. Permanently Closed or Vacant

There are **17,809 records** classified as:

`Permanently Closed or Vacant`

Inspection of the available 20 fields did not identify:

- a separate closure date
- a closure reason
- a vacancy reason
- a succession-related closure field

Therefore, this category cannot be interpreted as evidence of succession-driven closure.

`Permanently Closed or Vacant` is treated as a status indicator only.

The audit did not classify these records as:

- succession failures
- retirement-related closures
- businesses without successors
- businesses without buyers
- business failures

No such inference was made from the dataset.

---

## 9. Direct Succession Variables

The actual downloaded CSV was checked for direct succession-related variables.

No direct variables were identified for:

- owner age
- owner birth year
- owner retirement intention
- planned exit date
- succession-plan status
- identified successor
- ownership transfer
- closure reason
- succession-related closure

Therefore:

> No direct succession-related variables were identified in the 20 columns of the downloaded Consolidated NEI CSV.

This confirms the succession-data limitation identified during Week 2 for the publicly available consolidated dataset.

This does not establish that the 2026 NEI survey did not collect succession information. Rather, the succession-specific information was not identified in the publicly downloaded Consolidated NEI CSV.

---

## 10. Data Quality Checks

The following fields were checked for blank values:

- `NEI_ID`
- `Year`
- `Municipality`
- `Primary NAICS`
- `Primary Sector`
- `Industry`
- `Size Range of Employees`

No blank values were identified in these fields.

Other data-quality observations include:

- 199 blank business opening-year values
- 31,306 opening-year values recorded as `0`
- 19,404 records without a non-empty Secondary NAICS
- 3 blank `x` coordinate values
- 3 blank `y` coordinate values
- additional employee-size categories appearing only in 2025
- repeated `NEI_ID` values across historical observations
- historical coverage gap for 2020–2021

No data cleaning, recoding, filtering, deduplication or correction was performed.

---

## 11. Unique Business Identifier

The dataset contains:

`NEI_ID`

However, `NEI_ID` is not unique at the row level.

Audit results:

- Total records: 98,065
- Unique NEI_ID values: 15,846
- Duplicate NEI_ID values: 15,199
- Records involved in duplicate NEI_ID values: 97,418

Repeated NEI_ID values occur across different `Year` values.

For example, some NEI_ID values were observed across:

- 2016
- 2017
- 2018
- 2019
- 2022
- 2023
- 2024
- 2025

This indicates that `NEI_ID` can function as a reference to a business across historical NEI observations rather than uniquely identifying each row.

Therefore, `NEI_ID` should not be treated as a unique row-level key without incorporating the observation year or another appropriate field.

No new identifier was created.

---

## 12. Potential Future Joining Keys

The following fields may support future joins or comparisons:

- `Municipality`
- `Business Postal Code`
- `Primary NAICS`
- `Secondary NAICS`
- `Primary Sector`
- `Industry`
- `Year`
- `Size Range of Employees`
- `x`
- `y`
- `NEI_ID`

Potential uses include:

- municipality-level comparisons
- industry/sector comparisons
- historical year alignment
- employment-size comparisons
- geographic matching
- longitudinal business analysis

`NEI_ID` requires caution because it is not unique at the row level.

`OBJECTID` is present as a dataset identifier, but its suitability as a cross-dataset joining key has not been established.

The presence of a field with the same name in another dataset does not automatically mean that the datasets can be safely joined.

No datasets were merged during Week 3.

---

## 13. New Findings and Limitations

Inspection of the actual downloaded dataset revealed several findings that required confirmation beyond the Week 2 research:

1. The exact dataset contains 98,065 records and 20 columns.
2. Historical records cover 2016–2019 and 2022–2025, with no 2020–2021 observations.
3. `NEI_ID` is repeated across years and is not a unique row-level identifier.
4. The employee-size field contains additional categories appearing only in 2025.
5. The business-opening-year field contains 31,306 values of `0` and 199 blanks.
6. The dataset contains 17,809 `Permanently Closed or Vacant` records, but no closure reason or succession-related closure field.
7. No direct succession variables were identified in the 20 downloaded columns.
8. All 12 Niagara municipalities are represented.
9. Three records have blank `x` and `y` coordinate values.
10. Secondary NAICS is not populated for 19,404 records.
11. The downloaded consolidated dataset ends at 2025, while a dedicated 2026 public dataset was not located during the Week 2 Open Data search.

These limitations should be considered before using the NEI for later analysis or modelling.

---

## 14. Suitability for Project

### Final decision: KEEP WITH LIMITATIONS

The Consolidated NEI is suitable to carry forward because it provides valuable local information on:

- businesses
- municipalities
- sectors
- industries
- NAICS classifications
- employee-size categories
- historical observations
- geographic information

However, it has important limitations for the Niagara Succession Signal project.

Most importantly, the dataset does not directly identify:

- owner retirement intention
- successor availability
- succession-plan status
- ownership-transfer plans
- succession-related closure reasons

Therefore, the NEI should not be used alone to identify businesses as being at risk of succession-driven closure.

It can instead provide supporting information for understanding **where businesses are located, which sectors they operate in, the employment size of businesses, and historical business patterns**.

The NEI will need to be considered alongside other approved datasets and evidence for the broader project analysis.

---

## 15. Week 3 Audit Conclusion

The approved Consolidated NEI dataset was acquired and preserved in its original CSV format.

The audit verified:

- dataset structure
- record count
- geographic coverage
- NAICS and sector fields
- business opening information
- employee-size categories
- closed/vacant status
- data-quality issues
- business identifiers
- potential future joining fields
- direct succession-variable availability
- dataset limitations

No cleaning, recoding, merging, feature engineering, risk scoring, business-age calculation or modelling was performed during this audit.

**Week 3 process completed:**

> Acquire → Preserve → Document → Audit → Review