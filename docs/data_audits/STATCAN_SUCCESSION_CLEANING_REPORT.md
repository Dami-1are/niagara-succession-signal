# Data Cleaning Report: Statistics Canada Business Succession Tables

- **Project:** Niagara Succession Signal
- **Sprint / Milestone:** Week 4 — Succession Risk Signal Data Cleaning
- **Branch:** week4-statcan-succession-cleaning
- **Source Tables:** 33-10-1196, 33-10-1197, 33-10-1198, 33-10-1199

---

## 1. Scope & Geographic Normalization

All tables were filtered to Ontario:
- **Target Geography:** GEO == 'Ontario'
- **DGUID:** 2021A000235

---

## 2. Audit & Quality Metrics

| Table ID | Raw Rows | Ontario Rows | Missing VALUE | Status Breakdown (Ontario) |
| :--- | :--- | :--- | :--- | :--- |
| **33-10-1196** | 6,664 | 476 | 107 | B: 99, C: 80, A: 76, F: 71, E: 58, D: 56, ..: 36 |
| **33-10-1197** | 6,664 | 476 | 162 | A: 150, F: 85, ..: 77, C: 62, E: 62, D: 22, B: 18 |
| **33-10-1198** | 19,040 | 1,360 | 477 | A: 419, F: 257, ..: 220, C: 157, E: 146, B: 101, D: 60 |
| **33-10-1199** | 14,280 | 1,020 | 344 | A: 285, F: 179, C: 171, ..: 165, E: 101, B: 72, D: 47 |

---

## 3. Transformations Applied

1. Filtered by Ontario DGUID (2021A000235).
2. Stripped whitespace from categorical string fields.
3. Removed unpopulated SYMBOL column (100% NaN).
4. Verified suppression flags (F and .. correspond exactly to missing numeric values).

---

## 4. Deliverables

- data/interim/statcan_33101196_ontario_cleaned.csv
- data/interim/statcan_33101197_ontario_cleaned.csv
- data/interim/statcan_33101198_ontario_cleaned.csv
- data/interim/statcan_33101199_ontario_cleaned.csv
- notebooks/02_data_cleaning/02_statcan_succession_cleaning.ipynb
