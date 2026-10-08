report = """
# Census Age Cleaning Report

## 1. Dataset Overview

This report documents the cleaning and validation of the Statistics Canada Census Age dataset used for the Niagara-focused analysis.

Raw dataset:
- `98100022.csv`

Cleaned dataset:
- `census_age_niagara_cleaned.csv`

The raw Census file was not overwritten.

---

## 2. Before Cleaning

### Dataset dimensions

- Rows: 1,399,808
- Columns: 14

### Census periods
# Census Age Data Cleaning Report — Niagara

## 1. Overview

This report documents the cleaning and validation of the Statistics Canada Census Age dataset for the Niagara Census Division and its 12 municipalities.

**Raw dataset:** `data/98100022.csv`
**Cleaned dataset:** `census_age_niagara_cleaned.csv`
**Census years:** 2016 and 2021

The raw dataset was not overwritten.

---

## 2. Before Cleaning

The raw dataset contained:

* **Rows:** 1,399,808
* **Columns:** 14
* Multiple Canadian geographies
* Census years including 2016 and 2021
* 128 age labels
* Total-Gender, Men+, and Women+ measures
* Statistics Canada status/suppression fields

The age field contains individual ages, age groups, broad age groups, total age, average age, and median age.

---

## 3. Niagara Geography Filtering

The dataset was restricted to the Niagara Census Division and its 12 municipalities:

1. Fort Erie
2. Port Colborne
3. Wainfleet
4. West Lincoln
5. Pelham
6. Welland
7. Thorold
8. Niagara Falls
9. Niagara-on-the-Lake
10. St. Catharines
11. Lincoln
12. Grimsby

The Niagara Census Division itself was also retained.

This gives **13 geography levels** in total.

### DGUID validation

DGUID was used together with GEO to correctly identify the Niagara municipalities.

During validation, two different geographic units were found with the GEO name **Lincoln**. They had different DGUIDs:

* `2021A00051303008`
* `2021A00053526057`

The correct Niagara municipality of Lincoln was identified as:

`2021A00053526057`

The other Lincoln geography was excluded.

After correction, each of the 13 Niagara geography levels contained 256 records, giving:

**13 × 256 = 3,328 rows**

---

## 4. Census-Year Treatment

Both Census years were retained:

* 2016
* 2021

Each year contains 1,664 Niagara records.

No annual values were created.

No interpolation, annualization, or forecasting was performed.

---

## 5. Age-Label Cleaning and Hierarchy

The age field contains 128 different labels.

These include:

* Individual ages
* Age groups
* Broad age groups
* Total age
* Under 1 year
* Average age
* Median age

Age labels were reviewed and whitespace was handled during classification.

The age hierarchy was preserved.

Overlapping age categories were **not added together** because doing so would double-count the population.

For example, a person aged 64 can be represented within both a single-year category and broader age-group categories.

No attempt was made to create one combined population total from all age categories.

---

## 6. Suppression and Status Codes

The dataset contains corresponding Symbol fields for the gender measures.

Status information was preserved as provided by Statistics Canada.

The following principles were applied:

* `x` was treated as a suppression/status indicator.
* `...` was preserved as a status indicator.
* Suppressed values were not replaced with zero.
* Status-coded observations were not imputed or estimated.
* Blank Symbol fields were not treated as population values.

The Niagara subset did not contain `x` or `...` status codes.

---

## 7. Gender Fields

The following measures were retained:

* Total-Gender
* Men+
* Women+

The original numeric values were preserved.

No attempt was made to force Men+ and Women+ to sum exactly to Total-Gender because Statistics Canada applies random rounding and confidentiality treatment.

---

## 8. Missing-Value Validation

Missing values were checked after filtering to Niagara.

The following core fields contained no missing values:

* GEO
* DGUID
* Census year
* Age
* Total-Gender
* Men+
* Women+

The Symbol fields were blank throughout the Niagara subset because there were no applicable status symbols in those records.

Blank Symbol fields were therefore preserved rather than converted into population values.

---

## 9. Duplicate Validation

Two duplicate checks were performed:

1. Exact duplicate rows
2. Duplicate combinations of:

   * DGUID
   * Census year
   * Age category

Both checks returned zero duplicates.

---

## 10. Geographic Validation

The final dataset contains exactly **13 geography levels**:

* Niagara
* Fort Erie
* Port Colborne
* Wainfleet
* West Lincoln
* Pelham
* Welland
* Thorold
* Niagara Falls
* Niagara-on-the-Lake
* St. Catharines
* Lincoln
* Grimsby

All 12 Niagara municipalities are present.

---

## 11. Census Total Validation

The Niagara Census Division total population was validated using the `Total - Age` category.

| Census Year | Niagara Total Population |
| ----------- | -----------------------: |
| 2016        |                  447,890 |
| 2021        |                  477,940 |

These totals match the expected Census totals.

---

## 12. Final Dataset

The final cleaned dataset contains:

* **Rows:** 3,328
* **Columns:** 12
* **Geography levels:** 13
* **Census years:** 2016 and 2021
* **2016 records:** 1,664
* **2021 records:** 1,664
* **Exact duplicates:** 0

The cleaned file was saved separately as:

`census_age_niagara_cleaned.csv`

The original raw file `98100022.csv` was not overwritten.

---

## 13. Project Restrictions

This cleaning stage does **not** create or infer:

* Business-owner age
* Entrepreneur age
* Retiring-owner age
* Owner retirement intention
* Succession plans
* Successor information
* Business closure reasons
* Business opening years
* Ownership transfers
* Business status
* Succession-related closures

The Census Age dataset describes the general population and should not be presented as direct business-owner information.

Population age may be used later as contextual or proxy information, but its limitations must be clearly stated.

No business datasets were merged during this cleaning stage.

No trends or forecasts were created because only the 2016 and 2021 Census periods are available in this dataset.

---

## 14. Limitations

The cleaned dataset has several limitations:

* Population age is not the same as business-owner age.
* Only two Census periods are available.
* The data does not provide annual observations between 2016 and 2021.
* Statistics Canada applies random rounding.
* Some observations may contain suppression or status information.
* Age categories overlap and cannot be summed across the hierarchy.
* The dataset does not provide business-level information.
* The dataset does not directly measure succession planning or retirement intentions.
* Industry-specific business information is not included in this dataset.

---

## 15. Deliverables

The completed cleaning stage produces:

1. `census_age_niagara_cleaned.csv`
2. `02_census_age_cleaning.ipynb`
3. `census_age_cleaning_report.md`

The notebook provides a reproducible record of:

* Raw dataset loading
* Initial validation
* Census-year selection
* Niagara geography filtering
* DGUID validation
* Age-category review
* Age hierarchy handling
* Status/suppression handling
* Missing-value validation
* Duplicate validation
* Geographic validation
* Census total validation
* Saving the cleaned dataset
