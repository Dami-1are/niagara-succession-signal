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

This creates a historical coverage gap for 2020â€“2021 that should be considered when comparing observations across years.

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

- `312120` â€” Breweries
- `621210` â€” Offices of dentists
- `541212` â€” Offices of accountants
- `722511` â€” Full-service restaurants
- `458112` â€” Women's clothing retailers

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

Additional categories â€” `Aggregate`, `Micro`, `Small`, `Medium`, `Large`, and `Zero Employees` â€” occur only in the 2025 records.

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
- historical coverage gap for 2020â€“2021

No data cleaning, recoding, filtering, deduplication or correction was performed.

---

## 11. Unique Business Identifier

The dataset contains:

`NEI_ID`

However, `NEI_ID` is not unique at the row level.

Audit results:

- Total records: 98,065
- Unique NEI_ID values: 15,846
- NEI_ID values occurring more than once: 15,199
- Rows belonging to NEI_ID values that occur more than once: 97,418

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

Repeated `NEI_ID` values across years suggest that `NEI_ID` may support longitudinal tracking of businesses across historical NEI observations. However, this should be confirmed before using `NEI_ID` as a business-level identifier across years.

Therefore, `NEI_ID` should not be treated as a unique row-level key, and its suitability as a business-level identifier across years should be confirmed before use.

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
2. Historical records cover 2016â€“2019 and 2022â€“2025, with no 2020â€“2021 observations.
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

> Acquire â†’ Preserve â†’ Document â†’ Audit â†’ Review
---

## 16. Follow-up Identifier and Record-Consistency Checks

Additional checks were performed on the 98,065-row dataset after the initial audit.

### 16.1 Identifier counts

| Check | Result |
|---|---:|
| Total records | 98,065 |
| Unique `NEI_ID` values | 15,846 |
| `NEI_ID` values appearing in multiple years | 15,199 |
| Repeated `NEI_ID`â€“`Year` groups | 141 |
| Repeated `NEI_ID`â€“`Year` groups with one distinct business name | 2 |
| Repeated `NEI_ID`â€“`Year` groups with multiple business names | 139 |
| Repeated `NEI_ID`â€“`Year` groups with multiple municipalities | 100 |
| `NEI_ID` values associated with multiple business names across the dataset | 6,099 |

The initial duplicate check counted 82,219 rows as repeated occurrences of an existing `NEI_ID`. This count represents occurrences beyond the first appearance of each ID; it does not mean that 82,219 rows are erroneous duplicates.

### 16.2 Interpretation and limitations

The repeated ID-year groups require further investigation. Some contain the same business name more than once, while others associate a single ID and year with different business names or municipalities.

These patterns may reflect duplicated records, ID reuse, changes in business names, multiple establishments, or other source-specific conventions. The available checks alone do not establish the cause.

Consequently:

- Do not deduplicate the dataset using `NEI_ID` alone.
- Do not assume that every `NEI_ID` represents one consistently identified business across all years.
- Do not remove records solely because an ID-year combination repeats.
- Confirm the provider's identifier definitions and record structure before conducting longitudinal business-level analysis.
- Preserve the original CSV and carry out any future cleaning in a separate derived dataset.

### 16.3 Audit status

These are follow-up findings from additional validation checks. They do not establish that every flagged record is invalid. The dataset remains **KEEP WITH LIMITATIONS**, pending further verification of identifier consistency and investigation of the 147 nonblank postal-code values that failed the format check.

### 16.4 Postal-Code Format Validation

A format check was performed on the `Business Postal Code` field across all 98,065 records.

| Check | Result |
|---|---:|
| Blank postal codes | 127 |
| Nonblank postal codes | 97,938 |
| Values matching the typical Canadian postal-code pattern | 97,791 |
| Nonblank values not matching that pattern | 147 |
| Unusual values containing line breaks | 13 |

Examples of values that did not match the expected format include partial entries such as `L3B` and `L2V`, values containing line breaks such as `L2R2R2` followed by `L2R2N3`, and values that may contain character substitutions or invisible characters.

These results are format-validation flags, not confirmation that all 147 values are incorrect. Some may represent partial postal codes or other source-specific conventions. No postal codes were corrected, recoded, or removed.

Before postal codes are used for geographic matching or joining, the flagged values should be investigated in a separate derived dataset. The original CSV remains unchanged.

### 16.5 Coordinate Validation and Reference System

A numeric validation check was performed on the `x` and `y` coordinate fields across all 98,065 records.

| Check | Result |
|---|---:|
| Total records | 98,065 |
| Blank `x` values | 3 |
| Blank `y` values | 3 |
| Non-numeric nonblank `x` values | 0 |
| Non-numeric nonblank `y` values | 0 |
| Rows within ordinary longitude/latitude numeric bounds | 0 |

The observed coordinate ranges were:

- `x`: approximately -8,876,398 to -8,783,699
- `y`: approximately 5,288,713 to 5,351,545

The official Niagara Region ArcGIS Feature Layer metadata identifies the spatial reference as **102100 (3857)**, corresponding to **WGS 84 / Pseudo-Mercator (Web Mercator), EPSG:3857**. The layer uses projected coordinates in metres.

Official metadata: https://services1.arcgis.com/WxiLK82TWf8W3O3f/arcgis/rest/services/OpenData_Consolidated_NEI_Opendata/FeatureServer/45

The coordinate values are therefore not longitude and latitude in degrees. Any future geographic analysis should account for the projected coordinate system and use appropriate transformations when another CRS is required.

No coordinates were modified, transformed, or removed during this audit. The three records with missing coordinate values should be handled explicitly in any subsequent spatial analysis.
