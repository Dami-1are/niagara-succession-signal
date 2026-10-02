# Business Dynamics Data Audit

## 1. Dataset Identification

### Dataset 1 — Business Dynamics by Industry

- **Statistics Canada table:** 33-10-0087-01
- **Raw file:** data/raw/statcan/business_dynamics/33100087.csv
- **Metadata file:** data/raw/statcan/business_dynamics/33100087_MetaData.csv
- **Format:** CSV
- **Reference period:** 2001–2023
- **Geography:** Canadian provinces and territories
- **Relevant geography:** Ontario is included, but Niagara is not separately identified.
- **Primary dimensions:** Reference date, geography, business dynamics measure, NAICS industry
- **Measures:** Active employer businesses, entrants, incumbents, exits, entry rate, exit rate

### Dataset 2 — Business Dynamics by Firm Size

- **Statistics Canada table:** 33-10-0088-01
- **Raw file:** data/raw/statcan/business_dynamics/33100088.csv
- **Metadata file:** data/raw/statcan/business_dynamics/33100088_MetaData.csv
- **Format:** CSV
- **Reference period:** 2001–2023
- **Geography:** Canadian provinces and territories
- **Relevant geography:** Ontario is included, but Niagara is not separately identified.
- **Primary dimensions:** Reference date, geography, employment dynamics, firm size
- **Measures:** Active employer businesses, entrants, incumbents, exits

---

## 2. Source and Preservation Check

Both approved Statistics Canada Business Dynamics datasets were acquired in their original CSV form and preserved in:

data/raw/statcan/business_dynamics/

The corresponding Statistics Canada metadata files were also preserved alongside the data files.

The raw files have not been cleaned, transformed, merged, or feature-engineered as part of this audit.

---

# 3. Dataset 33-10-0087-01 — Business Dynamics by Industry

## 3.1 Structure

- **Rows:** 27,324
- **Columns:** 16
- **Data type of VALUE:** float64
- **Non-numeric VALUE entries:** 0
- **Duplicate rows:** 0

### Columns

1. REF_DATE
2. GEO
3. DGUID
4. Business dynamics measure
5. North American Industry Classification System (NAICS)
6. UOM
7. UOM_ID
8. SCALAR_FACTOR
9. SCALAR_ID
10. VECTOR
11. COORDINATE
12. VALUE
13. STATUS
14. SYMBOL
15. TERMINATED
16. DECIMALS

## 3.2 Time Coverage

The dataset covers **2001 through 2023**, inclusive.

The data are annual.

## 3.3 Geography

The dataset contains 11 geographic categories:

- Newfoundland and Labrador
- Prince Edward Island
- Nova Scotia
- New Brunswick
- Quebec
- Ontario
- Manitoba
- Saskatchewan
- Alberta
- British Columbia
- Territories

Ontario is available, but **Niagara is not directly identified**.

The dataset therefore provides provincial/territorial context rather than Niagara-specific business dynamics.

## 3.4 Business Dynamics Measures

The dataset contains:

- Number of active employer businesses in the private sector
- Number of entrants
- Number of incumbents
- Number of exits
- Entry rate
- Exit rate

According to the metadata, entrants are businesses with employees in the current year but none in the previous year. Incumbents have employees in both years. Exits have employees in the previous year but none in the current year.

Therefore, **business exit is an employee-based operational measure and should not be interpreted as evidence of business succession, owner retirement, ownership transfer, or succession-related closure.**

## 3.5 Industry / NAICS Coverage

The dataset contains 18 industry categories, including:

- Private sector
- Agriculture, forestry, fishing and hunting [11]
- Mining, quarrying, and oil and gas extraction [21]
- Construction [23]
- Manufacturing [31-33]
- Wholesale trade [41]
- Retail trade [44-45]
- Transportation and warehousing [48-49]
- Information and cultural industries [51]
- Finance and insurance [52]
- Real estate and rental and leasing [53]
- Professional, scientific and technical services [54]
- Management of companies and enterprises [55]
- Administrative and support, waste management and remediation services [56]
- Arts, entertainment and recreation [71]
- Accommodation and food services [72]
- Other services (except public administration) [81]
- Unclassified businesses

The metadata indicates that different NAICS versions apply across the historical period:

- 1997 NAICS — 2001
- 2002 NAICS — 2002–2006
- 2007 NAICS — 2007–2011
- 2012 NAICS — 2012 onward

Longitudinal industry comparisons must therefore account for classification changes.

## 3.6 Missing and Status Values

VALUE is numeric where values are provided.

The dataset contains status-coded observations. STATUS contains:

- Missing/blank status
- x
- ..

SYMBOL and TERMINATED are entirely missing in the extracted data.

Status-coded observations must not automatically be converted to zero. Their meaning should be determined from the official Statistics Canada metadata before any future analytical use.

## 3.7 Data Characteristics and Limitations

The metadata indicates that business counts are rounded to units of ten.

The metadata also notes that counts are not necessarily additive across years because of business structure variations.

The private-sector total may not equal the sum of all industry categories.

The definition of the business entity is provincial/territorial. An enterprise operating with employees in two provinces may therefore be represented as business entities in both provinces.

The private-sector coverage also excludes certain sectors, including utilities, educational services, health care and social assistance, and public administration, while including unclassified businesses.

## 3.8 Direct Succession Variables

The dataset does **not** provide direct variables for:

- Owner age
- Retirement intention
- Planned exit date
- Succession plan
- Identified successor
- Ownership transfer
- Reason for closure
- Succession-related closure

These variables must therefore be recorded as **not available in this dataset**, rather than inferred from business exits.

## 3.9 Potential Joining Keys

Potential fields for future alignment with other project datasets include:

- REF_DATE
- GEO
- DGUID
- North American Industry Classification System (NAICS) / industry

REF_DATE, GEO, and DGUID may support alignment with 33-10-0088-01, while NAICS/industry may support future comparison or alignment with other project datasets that contain compatible industry classifications.

These are only potential joining or alignment fields. Compatibility must be verified before any future merge.

No merge is performed during this audit.

## 3.10 Audit Decision

**KEEP WITH LIMITATIONS**

The dataset provides useful contextual information about business entry, exit, active businesses, and industry-level dynamics.

However, its provincial/territorial geography prevents direct Niagara-level analysis, and its definition of business exit does not identify succession events.

---

# 4. Dataset 33-10-0088-01 — Business Dynamics by Firm Size

## 4.1 Structure

- **Rows:** 9,108
- **Columns:** 16
- **Data type of VALUE:** float64
- **Non-numeric VALUE entries:** 0
- **Duplicate rows:** 0

### Columns

1. REF_DATE
2. GEO
3. DGUID
4. Employment dynamics
5. Firm size
6. UOM
7. UOM_ID
8. SCALAR_FACTOR
9. SCALAR_ID
10. VECTOR
11. COORDINATE
12. VALUE
13. STATUS
14. SYMBOL
15. TERMINATED
16. DECIMALS

## 4.2 Time Coverage

The dataset covers **2001 through 2023**, inclusive, with annual observations.

## 4.3 Geography

The same 11 provincial/territorial geographic categories are present as in 33-10-0087-01.

Ontario is included, but Niagara is not separately identified.

## 4.4 Employment Dynamics

The dataset contains:

- Number of active employer businesses in the private sector
- Number of entrants
- Number of incumbents
- Number of exits

As with 33-10-0087-01, exit is defined using employee presence across consecutive years.

Therefore, an exit cannot by itself establish that a business owner retired, transferred ownership, implemented a succession plan, or closed specifically because of succession.

## 4.5 Firm-Size Coverage

The dataset contains nine firm-size categories:

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

For example, 50 employees or more overlaps with the more detailed categories 50 to less than 100 employees and 100 employees or more.

Similarly, 100 employees or more overlaps with 100 to less than 500 employees and 500 employees or more.

These categories must not be summed together as though they represented separate, non-overlapping populations.

## 4.6 Missing and Status Values

There are **4,179 missing VALUE observations**.

There are **4,179 observations with STATUS = x**.

According to the Statistics Canada metadata, `x` means the value was suppressed to meet the confidentiality requirements of the Statistics Act. Therefore, the 4,179 missing VALUE observations associated with `STATUS = x` are suppressed values and must not be treated as zero.

SYMBOL and TERMINATED are entirely missing.

## 4.7 Direct Succession Variables

The dataset does **not** contain direct measures of:

- Owner age
- Retirement intention
- Planned exit date
- Succession plan
- Successor identification
- Ownership transfer
- Reason for closure
- Succession-related closure

These should not be inferred from firm size, entry, or exit measures.

## 4.8 Potential Joining Keys

Potential fields for future alignment with other project datasets include:

- REF_DATE
- GEO
- DGUID
- Firm size

REF_DATE, GEO, and DGUID may support alignment with 33-10-0087-01, while firm-size categories may support future comparison or alignment with other project datasets that contain compatible business-size classifications.

These are only potential joining or alignment fields. Compatibility must be verified before any future merge.

No merge is performed during this audit.

## 4.9 Audit Decision

**KEEP WITH LIMITATIONS**

The dataset provides useful context on business entry, exit, and firm-size dynamics.

However, it is not Niagara-specific and does not contain direct succession variables. Its overlapping firm-size categories also require careful selection of categories in any later analysis.

---

# 5. Comparison of the Two Business Dynamics Datasets

| Dimension | 33-10-0087-01 | 33-10-0088-01 |
|---|---|---|
| Focus | Industry | Firm size |
| Rows | 27,324 | 9,108 |
| Columns | 16 | 16 |
| Years | 2001–2023 | 2001–2023 |
| Geography | Provinces/territories | Provinces/territories |
| Niagara directly identified | No | No |
| Entry data | Yes | Yes |
| Exit data | Yes | Yes |
| Incumbent data | Yes | Yes |
| Industry detail | Yes | No |
| Firm-size detail | No | Yes |
| Direct succession variables | No | No |
| Duplicate rows | 0 | 0 |
| Potential alignment fields | REF_DATE, GEO/DGUID, NAICS/industry | REF_DATE, GEO/DGUID, firm-size category |
| Audit decision | KEEP WITH LIMITATIONS | KEEP WITH LIMITATIONS |

---

# 6. Succession Relevance Assessment

Both datasets provide **indirect business-dynamics context** that may be useful later in the project.

Neither dataset directly measures business succession.

In particular, the presence of business exits should not be treated as evidence that an owner is approaching retirement or that ownership transfer is likely.

The datasets should therefore be used only where their documented measures support the specific analytical question, with their geographic, temporal, classification, and definitional limitations preserved.

---

# 7. New Findings and Limitations

The audit identified the following important limitations:

1. Neither dataset provides Niagara-specific geography.
2. Business exit is defined operationally through employee presence across years and is not a succession measure.
3. Direct succession variables are absent.
4. 33-10-0087-01 contains historical NAICS classification changes.
5. 33-10-0088-01 contains nested firm-size categories.
6. Some observations are status-coded rather than numeric.
7. Business counts are rounded to units of ten.
8. Provincial business-entity definitions affect interpretation of geographic counts.
9. The datasets provide historical context rather than direct evidence of individual business succession.

---

# 8. Final Audit Decision

### 33-10-0087-01 — Business Dynamics by Industry

**Decision: KEEP WITH LIMITATIONS**

Retain as contextual evidence of business entry, exit, active businesses, and industry dynamics. Do not treat business exits as direct succession events or use the dataset as though it provides Niagara-level observations.

### 33-10-0088-01 — Business Dynamics by Firm Size

**Decision: KEEP WITH LIMITATIONS**

Retain as contextual evidence of business entry, exit, active businesses, and firm-size dynamics. Do not treat business exits as direct succession events. Firm-size categories must be selected carefully because several categories overlap.

---

# 9. Audit Review Checklist

- [x] Source recorded
- [x] Raw files preserved
- [x] Rows and columns checked
- [x] Column names reviewed
- [x] Missing values/status fields reviewed
- [x] Duplicates checked
- [x] Geography confirmed
- [x] Time coverage confirmed
- [x] Industry/NAICS information checked
- [x] Business-size information checked
- [x] Succession-related variables checked
- [x] Possible joining keys identified
- [x] Data-quality problems documented
- [x] Strengths and limitations recorded
- [x] Dataset relevance assessed
- [x] Keep/conditional/do-not-use decision recorded
- [x] New risks added to the risk register
- [x] Final audit reviewed by project team

---

## 10. Week 3 Boundary

This audit does not perform data cleaning, merging, feature engineering, exploratory data analysis, modelling, succession scoring, or final project conclusions.

The datasets remain preserved in their raw form. Any later analytical use must respect the limitations documented in this audit.
