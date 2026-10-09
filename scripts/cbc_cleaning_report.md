# Cleaning Report - Canadian Business Counts (Niagara), Week 4

**Source:** Statistics Canada table 33-10-1176-01 | **Raw file:** `data/raw/33101176.csv` (unchanged; SHA-256 `25900b137bf79991719bb4516014317807255338936f59e9ddc1566282f1c8d8`)
**Notebook:** `notebooks/02_cbc_cleaning.ipynb` | **Outputs:** `canadian_business_counts_niagara_cleaned.csv`, `canadian_business_counts_niagara_cma_reference.csv`

## 1. Before cleaning
| Check | Result | Week 3 audit |
|---|---|---|
| Rows | 1,047,957 | 1,047,957 |
| Columns | 16 | 16 |
| REF_DATE values | 2026-01 | 2026-01 |
| Unique DGUIDs | 3,348 | 3,348 |
| Unique GEO names | 3,163 | - |
| GEO names mapping to >1 DGUID | 167 | names are not unique |
| Exact duplicate rows | 0 | 0 |
| Duplicates on REF_DATE+GEO+DGUID+NAICS+Employment size | 0 | 0 |
| Fully empty columns | STATUS, SYMBOL, TERMINATED | STATUS, SYMBOL, TERMINATED |
| Missing values in REF_DATE, GEO, DGUID, Employment size, NAICS, VALUE | 0 | 0 |

**Geographic coverage:** all of Canada (3,348 geographies: census metropolitan areas and census subdivisions).

## 2. Cleaning actions
1. **Niagara filtering - by DGUID.** Rows were selected with the 12 municipality DGUIDs supplied in the task. `GEO` was not used, because 167 names occur under more than one DGUID (e.g. another *Lincoln* exists outside Niagara). All 12 municipalities were confirmed present.
2. **DGUID treatment.** DGUID is the geography key. The `GEO` name was kept only as a readable label and was checked against the expected name for each DGUID.
3. **CMA treatment.** The St. Catharines - Niagara CMA (`2021S0503539`) overlaps the municipalities. It is saved in a separate file (`canadian_business_counts_niagara_cma_reference.csv`, 2,121 rows, `geo_level = cma_reference_only`) and **must never be added to municipality totals**.
4. **NAICS extraction.** `NAICS` was split into `naics_label` and `naics_code`. `naics_code` is stored as text.
5. **NAICS hierarchy.** `naics_digit_length` and `naics_level_name` identify the level (1, 2, 3 or 4 digits). `naics_is_range` marks range codes such as `31-33` (treated as 2-digit sectors). Parent and child categories are **not** combined; for example Educational services `[61]` and `[611]` both remain.
6. **Aggregate categories.** `naics_category_type` flags `[1]` Total, all industries (`aggregate_total`), `[2]` Unclassified (`unclassified`) and `[3]` Sub-total, classified (`aggregate_subtotal_classified`). Every other code is `industry`. Nothing was deleted; filter on this column before analysing industries.
7. **Employment size.** All nine source categories are retained with original wording. `employment_size_type` marks `Total, with employees` as `aggregate_total` and the eight others as `size_band`. No micro/small/medium/large recoding was applied.
8. **Reference period.** `REF_DATE` is preserved as published (`2026-01`). It was not changed to June 2026.
9. **VALUE.** Converted to integer `business_count`; no missing, negative or non-numeric values. No absent combination was filled with zero.
10. **Renamed columns:** REF_DATE->ref_date, GEO->geo, DGUID->dguid, Employment size->employment_size, VECTOR->vector, VALUE->business_count; NAICS -> naics_label + naics_code.
11. **Columns removed from the analytical dataset** (they remain in the raw file):

| raw column | reason removed |
|---|---|
| STATUS | completely empty in the raw file (not business status / closure information) |
| SYMBOL | completely empty in the raw file (not business status / closure information) |
| TERMINATED | completely empty in the raw file (not business status / closure information) |
| UOM | constant for every row: 'Number' |
| UOM_ID | constant for every row: '223' |
| SCALAR_FACTOR | constant for every row: 'units' |
| SCALAR_ID | constant for every row: '0' |
| DECIMALS | constant for every row: '0' |
| COORDINATE | positional index of geography/size/NAICS - redundant |

## 3. After cleaning
| Item | Result |
|---|---|
| Final rows (12 municipalities) | 10,462 |
| Final columns | 14 |
| Municipalities | 12 |
| Unique DGUIDs | 12 |
| NAICS digit lengths retained | 1, 2, 3, 4 |
| Distinct NAICS codes | 403 |
| Employment-size categories retained | 9 |
| Missing values in analytical fields | 0 |
| Exact duplicate rows | 0 |
| Duplicates on REF_DATE+GEO+DGUID+NAICS+Employment size | 0 |
| CMA reference rows (separate file) | 2,121 |

**Rows per municipality**

| geo | dguid | rows |
|---|---|---|
| Fort Erie | 2021A00053526003 | 824 |
| Grimsby | 2021A00053526065 | 811 |
| Lincoln | 2021A00053526057 | 971 |
| Niagara Falls | 2021A00053526043 | 1285 |
| Niagara-on-the-Lake | 2021A00053526047 | 870 |
| Pelham | 2021A00053526028 | 662 |
| Port Colborne | 2021A00053526011 | 704 |
| St. Catharines | 2021A00053526053 | 1496 |
| Thorold | 2021A00053526037 | 804 |
| Wainfleet | 2021A00053526014 | 434 |
| Welland | 2021A00053526032 | 941 |
| West Lincoln | 2021A00053526021 | 660 |

**NAICS levels retained**

| naics_digit_length | naics_level_name | rows | codes |
|---|---|---|---|
| 1 | aggregate_not_a_naics_level | 253 | 3 |
| 2 | sector | 1242 | 20 |
| 3 | subsector | 3189 | 95 |
| 4 | industry_group | 5778 | 285 |

**Employment-size categories retained:** Total, with employees; 1 to 4 employees; 5 to 9 employees; 10 to 19 employees; 20 to 49 employees; 50 to 99 employees; 100 to 199 employees; 200 to 499 employees; 500 plus employees.

**Reconciliation check (validation only):** across 2,933 municipality x NAICS cells, 0 had a published Total that differed from the sum of its published bands; 0 had a Total with no band rows and 0 had band rows with no Total. Totals were not added to bands anywhere in the output.

## 4. Remaining limitations
- **Single reference period.** All rows are `2026-01`; the file cannot show trends and must not be used for business-count trends on its own.
- **Reference-period discrepancy.** The cube title says June 2026 but the data say 2026-01. The Week 3 audit could not resolve this; the raw value was preserved and no date was invented.
- **Employer businesses only.** The table counts businesses *with employees*; businesses without employees are not represented.
- **No direct succession variables.** There is no owner age, retirement intention, successor, ownership transfer, closure reason or opening year. Nothing of this kind was created or inferred.
- **Aggregate data.** Rows are counts of businesses per geography x NAICS x employment-size cell, not individual businesses.
- **Overlapping hierarchy and categories.** NAICS levels are nested, aggregate NAICS rows overlap detailed ones, and `Total, with employees` overlaps the size bands. Filter on `naics_level_name`, `naics_category_type` and `employment_size_type` before summing, or businesses will be double counted.
- **Absent rows are not zeros.** A missing geography / NAICS / size combination cannot be assumed to mean zero businesses.
- **CMA overlaps the municipalities.** Do not add the CMA file to municipality totals.
- **STATUS, SYMBOL and TERMINATED** were empty in the raw file. They are not business status or closure information.
- **Size definitions.** Micro/small/medium/large are not defined by the source; any grouping requires a project-level definition documented before use.
