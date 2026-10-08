# Data Cleaning Report: Statistics Canada Business Succession Tables
- **Project:** Niagara Succession Signal
- **Sprint / Milestone:** Week 4 - Succession Risk Signal Data Cleaning
- **Issue Reference:** #20 (Clean and Validate Statistics Canada Succession Data)
- **Branch:** week4-statcan-succession-cleaning
- **Target Geography:** Ontario (DGUID: 2021A000235)

## 1. Overview & General Cleaning Protocol

1. Protected raw files in data/raw/statcan/succession/ remain unmodified.
2. Filtered strictly to Ontario (DGUID == 2021A000235).
3. Preserved 2026 reference period and Percent unit of measure.
4. Preserved missing VALUE suppression codes (F and ..) without zero-filling or imputation.
5. Dropped empty SYMBOL column (100 percent NaN).

## 2. Table-by-Table Breakdown

### Table 33-10-1196-01
- **Before Cleaning:** 6,664 rows, 16 cols, 2,194 missing VALUE
- **Cleaning Actions:** Filtered Ontario (2021A000235), trimmed text padding, dropped SYMBOL
- **After Cleaning:** 476 rows, 15 cols, 107 missing VALUE
- **Status Breakdown:** B: 99, C: 80, A: 76, F: 71, E: 58, D: 56, ..: 36

### Table 33-10-1197-01
- **Before Cleaning:** 6,664 rows, 16 cols, 3,129 missing VALUE
- **Cleaning Actions:** Filtered Ontario, trimmed whitespace, dropped SYMBOL
- **After Cleaning:** 476 rows, 15 cols, 162 missing VALUE
- **Status Breakdown:** A: 150, F: 85, ..: 77, C: 62, E: 62, D: 22, B: 18

### Table 33-10-1198-01
- **Before Cleaning:** 19,040 rows, 17 cols, 8,488 missing VALUE
- **Cleaning Actions:** Filtered Ontario, trimmed whitespace, preserved importance levels, dropped SYMBOL
- **After Cleaning:** 1,360 rows, 16 cols, 477 missing VALUE
- **Status Breakdown:** A: 419, F: 257, ..: 220, C: 157, E: 146, B: 101, D: 60

### Table 33-10-1199-01
- **Before Cleaning:** 14,280 rows, 17 cols, 6,493 missing VALUE (F: 1,813 + ..: 4,680 = 6,493)
- **Cleaning Actions:** Filtered Ontario, trimmed whitespace, preserved scenarios and likelihoods, dropped SYMBOL
- **After Cleaning:** 1,020 rows, 16 cols, 344 missing VALUE (F: 179 + ..: 165 = 344)
- **Status Breakdown:** A: 285, F: 179, C: 171, ..: 165, E: 101, B: 72, D: 47

## 3. Remaining Limitations
- No Niagara-specific geography (Ontario benchmark only).
- Survey percentages are aggregate context and must not be converted into individual firm probabilities.
- Suppressed records (F and ..) cannot be filled or imputed.
