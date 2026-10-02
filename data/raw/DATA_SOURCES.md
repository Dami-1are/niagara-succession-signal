# Niagara Succession Signal â€” Raw Data Source Log

## Purpose

This file records the origin of every raw dataset collected for the Niagara Succession Signal project.

It allows us to trace each file back to its original source and supports transparency and reproducibility.

This log will be completed during **Week 3 â€” Data Collection and Audit** as datasets are actually downloaded.

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

# 2. Canadian Business Counts â€” 33-10-1176-01

**Provider:** Statistics Canada  
**Dataset:** Canadian Business Counts, with employees, census metropolitan areas and census subdivisions, June 2026  
**Table:** 33-10-1176-01  
**Official source link:** https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=3310117601  
**Original filename:** 33101176.csv (metadata file: 33101176_MetaData.csv)  
**File format:** CSV + cube metadata (CSV)  
**Reference period:** 2026-01 (REF_DATE; metadata start and end 2026-01-01). The cube title says "June 2026"; this difference is documented in the audit.  
**Frequency:** Semi-annual (from the downloaded metadata)  
**Geographic coverage:** 3,348 DGUIDs: 3,307 census subdivisions and 41 census metropolitan areas, including all 12 Niagara Region municipalities and the St. Catharines - Niagara CMA  
**Date downloaded:** October 1, 2026  
**Downloaded by:** Theophilus and Ruth  
**Licence:** Statistics Canada Open Licence  
**Repository location:** `data/raw/`  
**Raw file modified:** No  
**Status:** Downloaded and Audited (Week 3)

### Notes

Business counts for employer businesses by geography, NAICS industry and employment size (1,047,957 rows, 16 columns). The raw CSV and cube metadata are stored in `data/raw/` using Git LFS because of file size (run `git lfs pull` after cloning). Neither file has been modified. See `docs/data_audits/CANADIAN_BUSINESS_COUNTS_AUDIT.md` for findings and limitations.

---

# 3. Business Dynamics by Industry — 33-10-0087-01

**Provider:** Statistics Canada  
**Table:** 33-10-0087-01  
**Official source link:** https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=3310008701  
**Original downloaded filename:** 33100087-eng.zip  
**Extracted raw data:** 33100087.csv  
**Metadata:** 33100087_MetaData.csv  
**File format:** CSV + metadata CSV  
**Reference period:** 2001–2023  
**Geographic coverage:** Canadian provinces and territories, including Ontario; Niagara is not separately identified  
**Date downloaded:** 2026-10-01  
**Downloaded by:** Project team  
**Licence:** Statistics Canada Open Licence  
**Repository location:** data/raw/statcan/business_dynamics/  
**Raw file modified:** No  
**Status:** Acquired and audited

### Notes / Limitations

The dataset contains 27,324 rows and 16 columns.

It provides annual business-dynamics measures by industry and province/territory, including active employer businesses, entrants, incumbents, exits, entry rates and exit rates.

Business exits are defined using employee presence across consecutive years. An exit must not automatically be interpreted as owner retirement, ownership transfer, succession planning, or succession-related closure.

The dataset contains multiple NAICS versions across the historical period. Business counts are rounded to units of ten, and the private-sector total is not necessarily additive across industry categories.

Direct succession variables such as owner age, retirement intention, succession plan, successor, ownership transfer, planned exit date, reason for closure, and succession-related closure are not provided.

**Audit decision:** KEEP WITH LIMITATIONS

---

# 4. Business Dynamics by Firm Size — 33-10-0088-01

**Provider:** Statistics Canada  
**Table:** 33-10-0088-01  
**Official source link:** https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=3310008801  
**Original downloaded filename:** 33100088-eng.zip  
**Extracted raw data:** 33100088.csv  
**Metadata:** 33100088_MetaData.csv  
**File format:** CSV + metadata CSV  
**Reference period:** 2001–2023  
**Geographic coverage:** Canadian provinces and territories, including Ontario; Niagara is not separately identified  
**Date downloaded:** 2026-10-01  
**Downloaded by:** Project team  
**Licence:** Statistics Canada Open Licence  
**Repository location:** data/raw/statcan/business_dynamics/  
**Raw file modified:** No  
**Status:** Acquired and audited

### Notes / Limitations

The dataset contains 9,108 rows and 16 columns.

It provides annual business-dynamics measures by firm size and province/territory, including active employer businesses, entrants, incumbents and exits.

Business exits use an employee-based operational definition and must not automatically be interpreted as succession events.

The firm-size categories include overlapping/nested categories such as 50 employees or more, 50 to less than 100 employees, and 100 employees or more. These categories must not be treated as mutually exclusive in later analysis.

The dataset contains 4,179 missing VALUE observations associated with `STATUS = x`. According to the Statistics Canada metadata, `x` indicates values suppressed to meet confidentiality requirements. These suppressed observations must not be treated as zero.

Direct succession variables such as owner age, retirement intention, succession plan, successor, ownership transfer, planned exit date, reason for closure, and succession-related closure are not provided.

**Audit decision:** KEEP WITH LIMITATIONS

---
# 5. Census Age Data â€” 98-10-0022-01

**Provider:** Statistics Canada  
**Table:** 98-10-0022-01  
**Official source link:** To be recorded at download  
**Original filename:** To be recorded  
**File format:** CSV + metadata planned  
**Reference period:** To be recorded  
**Geographic coverage:** To be confirmed from downloaded selection/metadata  
**Date downloaded:** To be recorded  
**Downloaded by:** To be recorded  
**Licence:** Statistics Canada Open Licence  
**Repository location:** `data/raw/statcan/census/`  
**Raw file modified:** No  
**Status:** Planned for Week 3 acquisition

### Important Limitation

Population age must not automatically be treated as business-owner age.

---

# 6. Census Class of Worker / Self-Employment â€” 98-10-0592-01

**Provider:** Statistics Canada  
**Table:** 98-10-0592-01  
**Official source link:** To be recorded at download  
**Original filename:** To be recorded  
**File format:** CSV + metadata planned  
**Reference period:** To be recorded  
**Geographic coverage:** To be confirmed from downloaded selection/metadata  
**Date downloaded:** To be recorded  
**Downloaded by:** To be recorded  
**Licence:** Statistics Canada Open Licence  
**Repository location:** `data/raw/statcan/census/`  
**Raw file modified:** No  
**Status:** Planned for Week 3 acquisition

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

**Original Source â†’ Raw File â†’ Interim/Cleaned Data â†’ Processed/Aggregated Data â†’ Analysis/Model**

This ensures that another person can understand where our data came from and reproduce the major stages of our work.

