# Data Cleaning & Validation Report: Statistics Canada Business Succession Tables

- **Project:** Niagara Succession Signal
- **Sprint / Milestone:** Week 4 - Succession Risk Signal Data Cleaning
- **Issue Reference:** #20 (Clean and Validate Statistics Canada Succession Data)
- **Branch:** week4-statcan-succession-cleaning
- **Target Geography:** Ontario (DGUID: 2021A000235)

---

## 1. Executive Validation Summary

All four Statistics Canada succession tables were cleaned and programmatically validated end-to-end in 
otebooks/02_data_cleaning/02_statcan_succession_cleaning.ipynb.

| Table ID | Raw Rows | Ontario Rows | Duplicates (Raw / Cleaned) | Missing VALUE | Suppression Codes (F + ..) | Metadata Validations (GEO, REF_DATE, UOM) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **33-10-1196-01** | 6,664 | 476 | 0 / 0 | 107 | F: 71, ..: 36 (Sum: 107) | PASSED (Ontario, 2026, Percent) |
| **33-10-1197-01** | 6,664 | 476 | 0 / 0 | 162 | F: 85, ..: 77 (Sum: 162) | PASSED (Ontario, 2026, Percent) |
| **33-10-1198-01** | 19,040 | 1,360 | 0 / 0 | 477 | F: 257, ..: 220 (Sum: 477) | PASSED (Ontario, 2026, Percent) |
| **33-10-1199-01** | 14,280 | 1,020 | 0 / 0 | 344 | F: 179, ..: 165 (Sum: 344) | PASSED (Ontario, 2026, Percent) |

---

## 2. Feedback Implementation & Audit Verification

### 1. Duplicate Checks (Item 1)
- Programmatic assertions confirmed **0 duplicate rows** in the raw national tables and **0 duplicate rows** in the filtered Ontario datasets.

### 2. Missing VALUE vs. STATUS Code Integrity (Item 2)
- Across all tables, 100% of missing VALUE cells correspond to either:
  - F: Too unreliable to be published (confidentiality / sampling variability).
  - ..: Not available for a specific reference period.
- **Table 1199 Equivalence Audit:**
  - Raw national level: 1,813 (F) + 4,680 (..) = 6,493 missing VALUE records.
  - Ontario slice: 179 (F) + 165 (..) = 344 missing VALUE records.
- Missing values were strictly preserved without zero-filling or imputation.

### 3. Explicit Metadata Confirmations (Item 3)
- **Geography:** Asserted GEO == 'Ontario' and DGUID == '2021A000235' across all rows.
- **Reference Period:** Asserted REF_DATE == 2026 across all records.
- **Unit of Measure:** Asserted UOM == 'Percent' (UOM_ID: 239, SCALAR_FACTOR: units).

### 4. Preservation of Source Categories (Item 4)
- **NAICS:** Preserved original industry descriptions and coding strings without arbitrary re-grouping.
- **Employment Size (Table 1196):** Maintained exact source classes: 1 to 4 employees, 5 to 19 employees, 20 to 99 employees, and 100 or more employees.
- **Intention Timelines (Table 1196):** Preserved distinct timelines: Within 2 years, Within 3 to 5 years, Within 6 to 10 years, Timeline unknown, No intention within 10 years, Intention unknown.
- **Expectations (Table 1197):** Kept separate categories for buyer availability, fair market price, sufficient time/resources, professional advice, and government support.
- **Importance Levels (Table 1198):** Maintained ratings (Very important, Somewhat important, Not important, Level of importance, unknown).
- **Scenarios & Likelihoods (Table 1199):** Preserved 3 scenarios (continue operating, sell at reduced value, scale down/close operations) and 5 likelihood levels (Very likely, Somewhat likely, Somewhat unlikely, Very unlikely, Likelihood, unknown).

---

## 3. Deliverables Summary

- data/interim/statcan_33101196_ontario_cleaned.csv (476 rows, 15 cols)
- data/interim/statcan_33101197_ontario_cleaned.csv (476 rows, 15 cols)
- data/interim/statcan_33101198_ontario_cleaned.csv (1,360 rows, 16 cols)
- data/interim/statcan_33101199_ontario_cleaned.csv (1,020 rows, 16 cols)
- 
otebooks/02_data_cleaning/02_statcan_succession_cleaning.ipynb (Fully executed with outputs)
- docs/data_audits/STATCAN_SUCCESSION_CLEANING_REPORT.md (Updated audit report)