# Niagara Census Self-Employment Data Cleaning Report

## 1. Introduction

This report documents the cleaning and validation of the 2021 Statistics Canada Census Class of Worker and Self-Employment dataset for Niagara Census Division.

The purpose of this cleaning process is to prepare a reliable dataset for analysing self-employment patterns by age, gender, industry, and labour force status.

The cleaned dataset will support the Niagara Succession Signal project. However, self-employment statistics alone cannot identify business owners who are retiring or businesses at risk of closure due to succession challenges.

## 2. Data Source

- **Source:** Statistics Canada
- **Table:** 98-10-0592-01
- **Census year:** 2021
- **Sample:** 25% Census sample
- **Geography:** Niagara Census Division
- **DGUID:** 2021A00033526
- **Original dataset:** `data/raw/9810059201_databaseLoadingData.csv`
- **Cleaning notebook:** `notebooks/02_data_cleaning/02_census_self_employment_cleaning.ipynb`
- **Cleaned dataset:** `data/interim/census_self_employment_niagara_cleaned.csv`

## 3. Dataset Dimensions

| Metric | Original Dataset | Cleaned Dataset |
|---|---:|---:|
| Number of rows | 125,714 | 125,714 |
| Number of columns | 20 | 21 |
| Records lost | — | 0 |
| Missing values | 628,570 | 0 |
| Exact duplicate records | 0 | 0 |

The original dataset contained five completely empty columns, accounting for 628,570 missing cells. These columns were removed during cleaning.

Six additional columns were created to make the Census categories easier to identify and analyse.

## 4. Cleaning Steps Performed

### 4.1 Created a Working Copy

A separate DataFrame named `clean_df` was created from the original dataset using Pandas. This ensured that cleaning operations did not modify the original source data.

### 4.2 Removed Empty Columns

Five completely empty columns were removed:

- `UOM`
- `VECTOR`
- `STATUS`
- `SYMBOL`
- `TERMINATED`

No records were deleted.

### 4.3 Added Category Identifiers

The following identifiers were extracted from the Statistics Canada `COORDINATE` field:

- `class_worker_id`
- `industry_id`
- `age_id`
- `gender_id`
- `labour_status_id`

These identifiers preserve the original category distinctions and support accurate filtering.

### 4.4 Clarified Self-Employment Categories

A new column, `class_worker_label`, was created to distinguish two categories that share the original label `Self-employed`.

- **ID 5:** Self-employed, including unpaid family workers.
- **ID 6:** Self-employed, excluding unpaid family workers.

Both categories were retained without combining their counts.

### 4.5 Preserved Census Counts

The `VALUE` column was retained as an integer. No census counts were changed, estimated, or replaced.

The original `COORDINATE` values were also preserved.

## 5. Data Validation Results

The following checks were performed to verify the quality and consistency of the cleaned dataset.

| Validation Check | Result | Status |
|---|---|---|
| Census year | 2021 only | Passed |
| Geography | Niagara Census Division only | Passed |
| Census Division ID | 2021A00033526 | Passed |
| Total records | 125,714 | Passed |
| Missing values after cleaning | 0 | Passed |
| Exact duplicate records | 0 | Passed |
| Duplicate census coordinates | 0 | Passed |
| Invalid or negative census counts | 0 | Passed |
| Decimal census counts | 0 | Passed |
| Original census values preserved | True | Passed |
| Original coordinates preserved | True | Passed |
| Exported CSV successfully reopened | Yes | Passed |

### 5.1 Category Validation

The cleaned dataset contains:

| Category | Number of Unique IDs |
|---|---:|
| Age | 15 |
| Gender | 3 |
| Labour force status | 3 |
| Industry | 400 |
| Class of worker | 7 |

All category identifiers were extracted from the original Statistics Canada `COORDINATE` field.

### 5.2 Export Verification

The cleaned dataset was exported to:

`data/interim/census_self_employment_niagara_cleaned.csv`

The exported CSV was successfully reopened using Pandas.

Verification confirmed:

- 125,714 rows and 21 columns.
- All original census counts preserved.
- All original census coordinates preserved.
- No records lost during cleaning.

## 6. Dataset Limitations

### 6.1 Missing Industry Categories

The Statistics Canada industry classification contains identifiers ranging from 1 to 428.

However, the downloaded dataset contains 400 unique industry identifiers.

The following 28 identifiers are absent:

8, 10, 11, 15, 23, 63, 67, 70, 72, 74, 76, 132, 135, 138, 164, 165, 241, 247, 252, 253, 254, 255, 257, 259, 286, 308, 319, 320.

The reason for these absent categories has not yet been confirmed. They must not automatically be treated as zero or replaced with invented values.

### 6.2 Overlapping Age Categories

The dataset contains overlapping age groups.

For example, `25 to 64 years` includes smaller age groups such as `25 to 34 years`, `35 to 44 years`, and `45 to 54 years`.

Adding overlapping age groups together would result in double-counting.

Future analysis must select appropriate non-overlapping age categories.

### 6.3 Hierarchical Industry Categories

The NAICS industry classification contains broad sectors and smaller industry categories.

For example, `Farms` is included within the broader `Agriculture, forestry, fishing and hunting` sector.

These categories must not be added together without considering their hierarchical relationships.

### 6.4 Self-Employment Is Not the Same as Business Ownership

The Census identifies self-employed individuals, but it does not directly identify all business owners or their succession plans.

The dataset does not provide individual-level information about:

- Business owners' retirement intentions.
- Whether a successor has been identified.
- Whether a business has a succession plan.
- Whether a business is at risk of closure because of succession challenges.

Therefore, self-employment patterns should be treated as contextual evidence rather than direct measurements of succession risk.

### 6.5 Geographic and Time Limitations

The cleaned dataset covers Niagara Census Division for the 2021 Census only.

It cannot independently establish changes in self-employment over time or differences between Niagara municipalities.

### 6.6 Census Data Interpretation

The dataset contains aggregate Census counts from the 2021 Census 25% sample.

The data should not be interpreted as individual-level records, and aggregate counts should not be used to infer the circumstances of specific business owners.

## 7. Conclusion

The 2021 Niagara Census Class of Worker and Self-Employment dataset was successfully cleaned and validated using Python and Pandas.

The cleaning process preserved all 125,714 records and original Census counts while removing five completely empty columns and adding six columns to improve category identification.

The final dataset contains 125,714 rows and 21 columns.

Key achievements include:

- Confirmed the dataset covers Niagara Census Division and the 2021 Census.
- Verified that no exact duplicate records or duplicate Census coordinates exist.
- Preserved all original Census counts and category identifiers.
- Distinguished the two self-employment categories.
- Identified and documented 28 absent industry identifiers.
- Exported and verified the cleaned CSV.

The cleaned dataset is ready for further exploratory analysis, subject to the limitations documented in Section 6.

It can support the Niagara Succession Signal project by providing evidence about self-employment patterns across age groups, gender and industries.

However, the dataset does not directly measure business succession risk, retirement intentions or succession planning.

**Final output:** `data/interim/census_self_employment_niagara_cleaned.csv`

**Reproducible notebook:** `notebooks/02_data_cleaning/02_census_self_employment_cleaning.ipynb`