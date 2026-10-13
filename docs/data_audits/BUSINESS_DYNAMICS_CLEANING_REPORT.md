# Business Dynamics Cleaning Report

## 1. Purpose

This report documents the cleaning and validation of two Statistics Canada Business Dynamics datasets used for the Niagara succession-signal project:

1. **Business Dynamics by Industry** — Statistics Canada table 33-10-0087-01
2. **Business Dynamics by Firm Size** — Statistics Canada table 33-10-0088-01

The cleaning focused on producing separate Ontario-level analytical datasets while preserving the source data, maintaining the complete 2001–2023 historical period, documenting missing and suppressed observations, preparing NAICS information, validating firm-size categories, and documenting limitations relevant to future succession-related analysis.

No Niagara-level observations were manufactured or inferred from the Ontario data.

---

# 2. Dataset 1 — Business Dynamics by Industry

## 2.1 Source dataset

**Statistics Canada table:** 33-10-0087-01  
**Raw file:**

`data/raw/statcan/business_dynamics/33100087.csv`

### Before cleaning

| Validation item | Result |
|---|---:|
| Rows | 27,324 |
| Columns | 16 |
| Geography coverage | 11 geographies |
| Historical period | 2001–2023 |
| Ontario records | 2,484 |
| Exact duplicate rows | 0 |

The raw dataset contains six business-dynamics measures:

- Number of active employer businesses in the private sector
- Number of entrants
- Number of incumbents
- Number of exits
- Entry rate
- Exit rate

It contains 18 NAICS categories.

## 2.2 Ontario filtering

The cleaned dataset is restricted to Ontario using the Statistics Canada geography identifier:

`DGUID = 2016A000235`

The resulting dataset contains:

**2,484 rows × 18 columns**

The cleaned dataset is explicitly an **Ontario** dataset. It is not labelled as a Niagara dataset because the source table does not provide Niagara-level observations for this analysis.

The full historical period from **2001 through 2023** was retained.

No source records were deleted from the raw dataset. Records belonging to other geographies were excluded from the Ontario analytical output because the deliverable is specifically an Ontario dataset.

## 2.3 Missing and status-coded observations

The raw industry dataset contains the following status codes:

- `x` — suppressed to meet confidentiality requirements
- `..` — not available for a specific reference period
- blank/NaN status — observed numeric value where a numeric `VALUE` is available

For Ontario:

| Status | Records |
|---|---:|
| Blank/NaN | 2,448 |
| `..` | 36 |
| `x` | 0 |

The 36 observations with `..` have missing `VALUE` values.

Suppressed or unavailable observations were **not replaced with zero** and were **not imputed**.

A `status_interpretation` field was added to make the treatment of these observations explicit.

## 2.4 Duplicate validation

No exact duplicate rows were identified in the raw dataset or the Ontario subset.

No records were removed through deduplication.

**Duplicate validation: PASS**

## 2.5 NAICS preparation

The original NAICS field was retained and prepared for analytical use.

The cleaning added:

- `industry_label`
- `naics_code`
- `naics_version`

The `industry_label` field separates the readable industry description from the bracketed NAICS code.

The `naics_code` field extracts the source code, including range-based codes such as:

- `31-33`
- `44-45`
- `48-49`

Two source categories do not contain a specific NAICS code:

- Private sector
- Unclassified businesses

These categories were preserved rather than artificially assigning NAICS codes.

## 2.6 Historical NAICS-version limitation

The source data spans multiple historical NAICS versions:

| NAICS version | Years |
|---|---|
| 1997 NAICS | 2001 |
| 2002 NAICS | 2002–2006 |
| 2007 NAICS | 2007–2011 |
| 2012 NAICS | 2012–2023 |

The cleaning process documents these historical versions but **does not silently harmonize or force all observations into a single NAICS classification**.

This is an important limitation for longitudinal industry comparisons because an industry category may not represent exactly the same classification boundaries across all historical NAICS versions.

Any future cross-year industry trend analysis requiring strict comparability should apply an appropriate Statistics Canada NAICS concordance or crosswalk.

## 2.7 Columns renamed, added, or removed

The original source columns were converted to consistent snake_case names.

Examples include:

- `REF_DATE` → `ref_date`
- `GEO` → `geo`
- `DGUID` → `dguid`
- `Business dynamics measure` → `business_dynamics_measure`
- `North American Industry Classification System (NAICS)` → `naics`
- `VALUE` → `value`
- `STATUS` → `status`

Additional analytical fields were created:

- `industry_label`
- `naics_code`
- `naics_version`
- `status_interpretation`

The following technically empty source fields were removed from the cleaned output:

- `SYMBOL`
- `TERMINATED`

These fields were not deleted from the raw dataset.

## 2.8 VALUE validation

The cleaned `value` field was validated for:

- numeric consistency
- non-numeric values
- negative values
- missing values
- UOM consistency
- percentage validity

Results:

- Numeric conversion issues: 0
- Negative values: 0
- Missing values: 36
- Invalid percentage values: 0

Count measures use `Number` as the unit of measure, while entry and exit rates use `Percent`.

The source business-count values are reported at the source's stated precision; unrounded values were not manufactured or inferred.

## 2.9 Business exits and succession interpretation

The **Number of exits** measure was retained as a business-dynamics measure.

An exit represents the operational Statistics Canada business-dynamics concept based on changes in employer-business activity across consecutive periods.

It should **not** be interpreted as:

- owner retirement
- owner death
- business succession
- ownership transfer
- business failure for a specific known reason
- voluntary closure
- succession-related closure

No succession variable was created from the exit measure.

## 2.10 Remaining limitations

The industry dataset has several important limitations:

1. The data is available at the Ontario level for this analysis, not the Niagara level.
2. The dataset does not contain direct owner-level succession variables.
3. Owner age, retirement intention, succession plans, successor identification, ownership transfer, and reason for closure are not available.
4. Historical NAICS classifications change over time and were not harmonized during cleaning.
5. Some observations are unavailable because of source status coding.
6. Business counts are subject to the precision reported by Statistics Canada.
7. Business exits cannot be treated as direct evidence of succession.
8. The dataset does not support direct succession-risk scoring without additional evidence and appropriately defined variables.

---

# 3. Dataset 2 — Business Dynamics by Firm Size

## 3.1 Source dataset

**Statistics Canada table:** 33-10-0088-01  
**Raw file:**

`data/raw/statcan/business_dynamics/33100088.csv`

### Before cleaning

| Validation item | Result |
|---|---:|
| Rows | 9,108 |
| Columns | 16 |
| Geography coverage | 11 geographies |
| Historical period | 2001–2023 |
| Ontario records | 828 |
| Exact duplicate rows | 0 |

The dataset contains four employment-dynamics measures:

- Number of active employer businesses in the private sector
- Number of entrants
- Number of incumbents
- Number of exits

The dataset contains nine firm-size categories.

## 3.2 Ontario filtering

The cleaned dataset is restricted to Ontario using:

`DGUID = 2016A000235`

The resulting dataset contains:

**828 rows × 15 columns**

The complete historical period from **2001 through 2023** was retained.

Each of the nine firm-size categories contains 92 observations in the Ontario subset.

No source records were deleted from the raw dataset. Non-Ontario observations were excluded from the Ontario analytical output because the cleaning requirement is an Ontario-focused dataset.

## 3.3 Missing and suppressed observations

The firm-size dataset uses `x` to indicate observations suppressed to meet confidentiality requirements.

For the Ontario subset:

| Status | Records |
|---|---:|
| Observed numeric value | 632 |
| Suppressed (`x`) | 196 |

The 196 suppressed Ontario observations remain missing in the cleaned `value` field.

They were:

- not converted to zero
- not imputed
- not estimated
- not inferred from other firm-size categories

A `status_interpretation` field was added to make this treatment transparent.

## 3.4 Duplicate validation

No exact duplicate rows were identified in the raw dataset or Ontario subset.

No observations were removed through deduplication.

**Duplicate validation: PASS**

## 3.5 Firm-size categories and overlap

The source contains the following firm-size categories:

- Private sector
- Less than 5 employees
- 5 to less than 20 employees
- 20 to less than 50 employees
- 50 employees or more
- 50 to less than 100 employees
- 100 employees or more
- 100 to less than 500 employees
- 500 employees or more

These categories are **not all mutually exclusive**.

In particular:

- `50 employees or more` overlaps with `50 to less than 100 employees` and `100 employees or more`.
- `100 employees or more` overlaps with `100 to less than 500 employees` and `500 employees or more`.

Therefore, the cleaning process does **not sum these categories** and does not treat them as mutually exclusive groups.

The original firm-size categories were preserved rather than recoding them into unsupported categories such as Micro, Small, Medium, or Large.

The source metadata expresses firm size using Average Labour Units (ALUs). The source classification was preserved rather than replacing it with a different firm-size definition.

## 3.6 Columns renamed, added, or removed

The firm-size cleaned dataset retains the source fields required for analysis and validation.

The original source columns were standardized to lowercase snake_case names for consistency with the cleaned industry dataset.

Examples of renamed columns include:

- `REF_DATE` → `ref_date`
- `GEO` → `geo`
- `DGUID` → `dguid`
- `Employment dynamics` → `business_dynamics_measure`
- `Firm size` → `firm_size`
- `UOM` → `uom`
- `VALUE` → `value`
- `STATUS` → `status`

A `status_interpretation` field was added to document whether an observation represents an observed numeric value or a confidentiality-suppressed value.

The following technically empty source fields were removed from the cleaned output:

- `SYMBOL`
- `TERMINATED`

These fields were not removed from the raw source file.

`TERMINATED` was not interpreted as a business-closure indicator because it is a technical source field rather than a direct succession or exit variable.

## 3.7 Value validation

The cleaned `value` field was validated for:

- Numeric consistency
- Non-numeric values
- Negative values
- Missing values
- Unit consistency

**Validation results:**

- Numeric conversion issues: 0
- Negative values: 0
- Missing/suppressed values: 196
- Unit of measure (`uom`): Number
- Scalar factor (`scalar_factor`): units

The 196 confidentiality-suppressed observations, identified by the status code `x`, were retained with missing values in the `value` column.

Suppressed observations were not replaced with zero, imputed, or estimated.

No values were manufactured to complete the dataset.

## 3.8 Business exits and succession interpretation

The firm-size dataset's exit measure was retained as an operational business-dynamics measure.

It does not identify whether an exit occurred because of:

- owner retirement
- owner death
- succession
- ownership transfer
- business failure
- voluntary closure
- another specific reason

Therefore, exit counts were not renamed as succession events and were not converted into succession-risk variables.

## 3.9 Remaining limitations

The firm-size dataset has the following limitations:

1. It provides Ontario-level information rather than Niagara-level observations.
2. Firm-size categories overlap and must not be summed as if mutually exclusive.
3. Some observations are suppressed for confidentiality.
4. The dataset does not identify individual businesses or owners.
5. The dataset does not contain owner age, succession plans, retirement intentions, ownership transfers, or reasons for business exits.
6. The source firm-size classification should be interpreted according to its Statistics Canada methodology and Average Labour Unit basis.
7. Business exits cannot be treated as direct succession events.

---

# 4. Records Removed and Reasons

The cleaning process did **not delete observations from the raw datasets**.

The distinction between filtering and deletion is important:

### Geographic filtering

The cleaned deliverables are Ontario-specific. Therefore, observations belonging to other geographies were excluded from the cleaned Ontario outputs.

This was an analytical filtering step and did not modify the raw source files.

### Duplicate records

No duplicate observations were identified.

Therefore, no records were removed for duplication.

### Missing or suppressed values

No observations were removed because they contained missing, unavailable, or suppressed values.

Instead:

- Industry `..` observations were retained and documented as unavailable.
- Firm-size `x` observations were retained and documented as confidentiality-suppressed.
- Suppressed or unavailable values were not replaced with zero or imputed.

### Technical fields

The `SYMBOL` and `TERMINATED` columns were removed from the cleaned outputs because they were completely empty in the relevant Ontario subsets and did not provide analytical value.

These columns remain unchanged in the raw files.

---

# 5. Before-and-After Validation

| Dataset | Before | After | Years | Ontario rows | Duplicates |
|---|---:|---:|---|---:|---:|
| Business Dynamics by Industry | 27,324 × 16 | 2,484 × 18 | 2001–2023 | 2,484 | 0 |
| Business Dynamics by Firm Size | 9,108 × 16 | 828 × 15 | 2001–2023 | 828 | 0 |

Both cleaned datasets:

- retain the complete 2001–2023 period;
- contain Ontario observations only;
- preserve source suppression and unavailable statuses;
- contain no duplicate records;
- do not replace suppressed values with zero;
- do not infer succession events;
- remain separate;
- do not merge with each other or other project datasets.

---

# 6. Reproducibility

The cleaning process is implemented in:

`scripts/02_business_dynamics_cleaning.py`

The script reads the raw Statistics Canada files from:

`data/raw/statcan/business_dynamics/`

and writes the cleaned outputs to:

`data/processed/statcan/business_dynamics/`

Final outputs:

1. `business_dynamics_industry_ontario_cleaned.csv`
2. `business_dynamics_firm_size_ontario_cleaned.csv`

The script also validates that the raw source files remain present after processing.

The cleaning process is therefore reproducible without modifying the source datasets.

---

# 7. Final Cleaned Outputs

### Business Dynamics by Industry

`data/processed/statcan/business_dynamics/business_dynamics_industry_ontario_cleaned.csv`

**Final dimensions:** 2,484 × 18

### Business Dynamics by Firm Size

`data/processed/statcan/business_dynamics/business_dynamics_firm_size_ontario_cleaned.csv`

**Final dimensions:** 828 × 15

---

# 8. Overall Limitations and Analytical Boundaries

The cleaned datasets provide useful Ontario-level evidence on business dynamics by industry and firm size, but they do not constitute direct succession data.

In particular, the datasets do not contain the variables required to directly identify business succession, including owner age, retirement intention, succession planning, successor identification, ownership transfer, or succession-related closure.

The Business Dynamics exit measure should therefore be treated as an operational indicator of business exits rather than a direct measure of succession.

The data also cannot be used to manufacture Niagara-level observations. Any future Niagara-focused analysis must rely on an appropriate source containing Niagara-level information.

Historical industry analysis must account for changes between NAICS versions, and firm-size analysis must account for overlapping source categories.

These limitations should remain explicit in any subsequent analysis, dashboard, modelling, or research using these datasets.

---

# 9. Cleaning Decision

**Decision: KEEP WITH LIMITATIONS**

The two datasets are suitable for continued project use as cleaned Ontario-level business-dynamics reference datasets, provided that:

- their Ontario geography is maintained;
- historical NAICS changes are acknowledged;
- suppressed observations remain missing;
- firm-size overlaps are respected;
- exits are not interpreted as succession;
- no unsupported Niagara-level observations are created;
- no direct succession conclusions are drawn from these datasets alone.
