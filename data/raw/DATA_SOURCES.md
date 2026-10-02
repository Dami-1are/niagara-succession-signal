# Niagara Succession Signal — Raw Data Source Log

## Purpose

This file records the origin of every raw dataset collected for the Niagara Succession Signal project.

It allows us to trace each file back to its original source and supports transparency and reproducibility.

This log will be completed during **Week 3 — Data Collection and Audit** as datasets are actually downloaded.

---

# Raw Data Rule

Files stored in `data/raw/` must represent the original downloaded data.

**Do not clean, rename columns, remove rows, fill missing values, merge datasets or otherwise modify the contents of a raw data file.**

Any cleaned or transformed version should be saved later in the appropriate `data/interim/` or `data/processed/` location.

---

# Information Required for Every Dataset

For every raw dataset collected, record:

- Dataset name
- Provider
- Official source link
- Table/dataset number, where applicable
- Original downloaded filename
- File format
- Reference period
- Geographic coverage
- Date downloaded
- Downloaded by
- Licence
- Repository location
- Whether the raw file was modified
- Notes or known limitations

---

# 1. Consolidated Niagara Employment Inventory (NEI)

**Provider:** Niagara Region  
**Dataset:** Consolidated Niagara Employment Inventory  
**Official source link:** https://open.niagararegion.ca/datasets/d23f4f781add4584904bc78b94c869b3_45/explore 
**Original filename:** OpenData_Consolidated_NEI_Opendata_-482263215789080610.csv 
**File format:** CSV 
**Reference period:** 2016–2019 and 2022–2025
**Geographic coverage:** Niagara Region  
**Date downloaded:** September 28, 2026  
**Downloaded by:** Stephen Ayankoso 
**Licence:** No license provided on the Consolidated NEI dataset page at the time of download 
**Repository location:** `data/raw/OpenData_Consolidated_NEI_Opendata_-482263215789080610.csv` 
**Raw file modified:** No  
**Status:** Acquired for Week 3 audit

### Notes

The Consolidated NEI provides local business information including municipality, business information, NAICS, sector, industry, business opening information, and employee-size categories.

The actual record count, fields, categories, missing values, geographic coverage, identifiers, and succession-related variables will be verified during the Week 3 data audit.

The downloaded CSV has been preserved in its original form in `data/raw/`.

---

# 2. Canadian Business Counts — 33-10-1176-01

**Provider:** Statistics Canada  
**Table:** 33-10-1176-01  
**Official source link:** To be recorded at download  
**Original filename:** To be recorded  
**File format:** CSV + metadata planned  
**Reference period:** To be recorded  
**Geographic coverage:** To be confirmed from downloaded table/metadata  
**Date downloaded:** To be recorded  
**Downloaded by:** To be recorded  
**Licence:** Statistics Canada Open Licence  
**Repository location:** `data/raw/statcan/business_counts/`  
**Raw file modified:** No  
**Status:** Planned for Week 3 acquisition

---

# 3. Business Dynamics by Industry — 33-10-0087-01

**Provider:** Statistics Canada  
**Table:** 33-10-0087-01  
**Official source link:** To be recorded at download  
**Original filename:** To be recorded  
**File format:** CSV + metadata planned  
**Reference period:** To be recorded  
**Geographic coverage:** To be confirmed from metadata  
**Date downloaded:** To be recorded  
**Downloaded by:** To be recorded  
**Licence:** Statistics Canada Open Licence  
**Repository location:** `data/raw/statcan/business_dynamics/`  
**Raw file modified:** No  
**Status:** Planned for Week 3 acquisition

### Important Limitation

A recorded business exit must not automatically be interpreted as a succession-related closure.

---

# 4. Business Dynamics by Firm Size — 33-10-0088-01

**Provider:** Statistics Canada  
**Table:** 33-10-0088-01  
**Official source link:** To be recorded at download  
**Original filename:** To be recorded  
**File format:** CSV + metadata planned  
**Reference period:** To be recorded  
**Geographic coverage:** To be confirmed from metadata  
**Date downloaded:** To be recorded  
**Downloaded by:** To be recorded  
**Licence:** Statistics Canada Open Licence  
**Repository location:** `data/raw/statcan/business_dynamics/`  
**Raw file modified:** No  
**Status:** Planned for Week 3 acquisition

---

# 5. Census Age Data — 98-10-0022-01

**Provider:** Statistics Canada
**Table:** 98-10-0022-01
**Official source link:** https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=9810002201
**Original filename:** 98100022.csv (metadata file: 9810002201_MetaData.csv)
**File format:** CSV + metadata
**Reference period:** 2021 Census (2016 Census also included)
**Geographic coverage:** Canada, 13 provinces/territories, 293 census divisions, 5,161 census subdivisions (5,468 geographies). **Niagara (CD 3526) and its 12 municipalities are included.
**Date downloaded:** October 1, 2026
**Downloaded by:** Precious and Lucky
**Licence:** Statistics Canada Open Licence
**Repository location:** data/raw/statcan/census/98100022.csv
**Raw file modified:** No
**Status:** Acquired for Week 3 audit

**Important Limitation**
Population age must not automatically be treated as business-owner age.

**Notes**
Population counts by single year of age, with average age and median age, for Total, Men+ and Women+. 1,399,808 rows and 12 columns. SHA-256: b7a6a987157c2617fee59a38c18086b0bcc72fd6c832f09d0804af49fb001ec1.
REF_DATE is 2021 on every row, including the 2016 rows, so use the "Census year (2)" column for the period. Symbol x marks suppressed values (blank) and symbol ... marks not-applicable values, which are shown as 0. The full findings are in docs/data_audits/CENSUS_DEMOGRAPHICS_AUDIT.md.

### Important Limitation

Population age must not automatically be treated as business-owner age.

---

# 6. Census Class of Worker / Self-Employment — 98-10-0592-01

**Dataset name:** Statistics Canada Table 98-10-0592-01 — Class of worker and self-employment information  
**Provider:** Statistics Canada  
**Table/Dataset number:** 98-10-0592-01 (reference 98100592)  
**Official source link:** <https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=9810059201>  
**Original filename:**Statistics Canada Table 98-10-0592-01  
**File format:** CSV  + metadata 
**Date downloaded:** 01/10/2026  
**Downloaded/Audited by:** Precious Ubanwa and Lucky  
**Repository location:** data/raw/statcan/census/98100592-eng.zip
**Licence:** Statistics Canada Open Licence  
**Repository location:** `data/raw/statcan/census/`  
**Raw file modified:** No  
**Status:** Acquired for Week 3 audit

### Important Limitation

Self-employment is a proxy and must not automatically be treated as direct evidence of business ownership or succession risk.

---

# Additional Dataset Template

Copy this section whenever another dataset is approved and collected.

## Dataset Name

**Provider:**  
**Table/Dataset Number:**  
**Official source link:**  
**Original filename:**  
**File format:**  
**Reference period:**  
**Geographic coverage:**  
**Date downloaded:**  
**Downloaded by:**  
**Licence:**  
**Repository location:**  
**Raw file modified:** No  
**Status:**  

### Notes / Limitations

Add any important information about the dataset here.

---

# Week 3 Update Rule

Immediately after downloading a dataset, the team member responsible should update this file with the **actual**:

1. source link;
2. filename;
3. format;
4. reference period;
5. geographic coverage;
6. download date;
7. name of the person who downloaded it; and
8. repository location.

Do not leave these fields as **"To be recorded"** after the dataset has been collected.

---

# Traceability Rule

Every dataset used in the final **4.1 Aggregated Data Layer** must be traceable from:

**Original Source → Raw File → Interim/Cleaned Data → Processed/Aggregated Data → Analysis/Model**

This ensures that another person can understand where our data came from and reproduce the major stages of our work.
