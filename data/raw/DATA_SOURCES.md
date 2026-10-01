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
**Official source link:** To be recorded at download  
**Original filename:** To be recorded  
**File format:** CSV planned  
**Reference period:** To be confirmed from downloaded data/metadata  
**Geographic coverage:** Niagara Region  
**Date downloaded:** To be recorded  
**Downloaded by:** To be recorded  
**Licence:** Open Government Licence 2.0 — Niagara Region, subject to confirmation on the dataset page at download  
**Repository location:** `data/raw/nei/`  
**Raw file modified:** No  
**Status:** Planned for Week 3 acquisition

### Notes

The NEI is expected to provide important local business information such as municipality, industry/NAICS and employment size.

The actual fields will be confirmed during the Week 3 audit.

---

# 2. Canadian Business Counts — 33-10-1176-01

**Provider:** Statistics Canada  
**Table:** 33-10-1176-01  
**Official source link:** https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=3310117601
**Original filename:** 33101176-eng.csv  
**File format:** CSV + metadata included
**Reference period:** January 2026  
**Geographic coverage:** Census metropolitan areas and census subdivisions  
**Date downloaded:** October 1, 2026  
**Downloaded by:** Theophilus and Feranmi  
**Licence:** Statistics Canada Open Licence  
**Repository location:** `data/raw/statcan/business_counts/`  
**Raw file modified:** No  
**Status:** Downloaded and Audited (Week 3)

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

# 6. Census Class of Worker / Self-Employment — 98-10-0592-01

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

**Original Source → Raw File → Interim/Cleaned Data → Processed/Aggregated Data → Analysis/Model**

This ensures that another person can understand where our data came from and reproduce the major stages of our work.
