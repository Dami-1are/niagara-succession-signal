# Data Cleaning & Validation Report: Statistics Canada Business Succession Tables

- **Project:** Niagara Succession Signal
- **Sprint / Milestone:** Week 4 - Succession Risk Signal Data Cleaning
- **Issue Reference:** #20 (Clean and Validate Statistics Canada Succession Data)
- **Branch:** week4-statcan-succession-cleaning
- **Cleaning Notebook:** notebooks/02_data_cleaning/02_statcan_succession_cleaning.ipynb
- **Target Geography:** Ontario (DGUID: 2021A000235)

---

## 1. Executive Validation Summary

All four Statistics Canada succession tables were cleaned and programmatically validated end-to-end in `notebooks/02_data_cleaning/02_statcan_succession_cleaning.ipynb`.

| Table ID | Raw Rows | Ontario Rows | Duplicates (Raw / Cleaned) | Missing VALUE | Suppression Breakdown (F + ..) | Programmatic Validations (GEO, REF_DATE, UOM) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **33-10-1196-01** | 6,664 | 476 | 0 / 0 | 107 | F: 71, ..: 36 (Sum: 107) | PASSED (Ontario, 2026, Percent) |
| **33-10-1197-01** | 6,664 | 476 | 0 / 0 | 162 | F: 85, ..: 77 (Sum: 162) | PASSED (Ontario, 2026, Percent) |
| **33-10-1198-01** | 19,040 | 1,360 | 0 / 0 | 477 | F: 257, ..: 220 (Sum: 477) | PASSED (Ontario, 2026, Percent) |
| **33-10-1199-01** | 14,280 | 1,020 | 0 / 0 | 344 | F: 179, ..: 165 (Sum: 344) | PASSED (Ontario, 2026, Percent) |

---

## 2. Reviewer Feedback Implementation Details

### Item 1: Programmatic Duplicate Checks
- Both raw national tables and Ontario-filtered tables were verified via `assert df.duplicated().sum() == 0`.
- All four tables contain strictly **0 duplicate rows** before and after cleaning.

### Item 2: Missing VALUE vs. STATUS Codes Equivalence & Clarification of Status F
- **Statistics Canada Status Flag Definitions:**
  - **`STATUS == 'F'`**: Defined officially by Statistics Canada as **"Too unreliable to be published"**. This occurs when an estimate does not meet Statistics Canada's minimum data quality thresholds due to high sampling variability or coefficient of variation (CV), or when the cell is suppressed to protect confidentiality. **Status F records are NOT zero and must NOT be imputed or replaced with estimates.**
  - **`STATUS == '..'`**: Defined as **"Not available for a specific reference period"**.
- **Equivalence Validation:**
  - 100% of missing numeric `VALUE` cells in all four tables correspond strictly to `STATUS` codes `F` or `..`.
  - For Table 1199 (Ontario slice): Missing `VALUE` count is exactly 344 (`F: 179` + `..: 165` = 344). Programmatic assertions confirmed this strict equivalence.

### Item 3: Metadata Integrity Assertions
- Programmatic assertions in the notebook confirm:
  - `GEO == 'Ontario'` and `DGUID == '2021A000235'` across all rows.
  - `REF_DATE == 2026` across all rows (no historical or interpolated years).
  - `UOM == 'Percent'` across all rows (percentages preserved; no conversion to counts).

### Item 4: Category and Dimension Preservation
- **NAICS:** Preserved original industry labels and structure without cross-dataset aggregation or alteration.
- **Employment Size (Table 1196):** Source bins (`1 to 4 employees`, `5 to 19 employees`, `20 to 99 employees`, `100 or more employees`) remain unchanged.
- **Intention Timelines (Table 1196):** All original timelines preserved (`Within 2 years`, `Within 3 to 5 years`, `Within 6 to 10 years`, `Timeline unknown`, `No intention within 10 years`, `Intention unknown`).
- **Expectations (Table 1197):** Kept all distinct categories (fair market price, buyer availability, sufficient resources, advisory support, government programs).
- **Importance Levels (Table 1198):** Maintained source categories (`Very important`, `Somewhat important`, `Not important`, `Level of importance, unknown`).
- **Scenarios & Likelihoods (Table 1199):** Preserved 3 scenarios (continue operating, sell at reduced value, scale down/close operations) and all 5 likelihood ratings.

### Item 5: Reproducibility & Output Validation
- Cleaning notebook location: `notebooks/02_data_cleaning/02_statcan_succession_cleaning.ipynb`.
- The notebook executes sequentially from start to finish without errors and reproduces all four files in `data/interim/`:
  - `data/interim/statcan_33101196_ontario_cleaned.csv` (476 rows, 15 columns)
  - `data/interim/statcan_33101197_ontario_cleaned.csv` (476 rows, 15 columns)
  - `data/interim/statcan_33101198_ontario_cleaned.csv` (1,360 rows, 16 columns)
  - `data/interim/statcan_33101199_ontario_cleaned.csv` (1,020 rows, 16 columns)

---

## 3. Remaining Limitations & Boundaries
1. **Contextual Provincial Benchmark:** Survey data reflects Ontario as a whole. No Niagara-specific geography is present.
2. **Aggregate Survey Evidence:** These figures must not be interpreted as individual business probabilities or certainty scores.
3. **No Imputation of Suppressed Cells:** Values flagged with F and .. represent statistical suppression and cannot be reconstructed.