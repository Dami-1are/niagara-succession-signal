# Niagara Succession Signal — Week 3 Data Audit Template

## Purpose

This template provides a standard method for auditing every dataset collected for the Niagara Succession Signal project.

Week 3 focuses on **Data Collection and Audit**.

The purpose of the audit is to understand the data **before cleaning, transforming, merging or modelling it**.

Each Priority A dataset must have a completed audit.

---

# 1. Dataset Identification

**Dataset name:**  
**Provider:**  
**Table/Dataset number:**  
**Official source link:**  
**Original filename:**  
**File format:**  
**Date downloaded:**  
**Downloaded/Audited by:**  
**Repository location:**  
**Licence:**  

---

# 2. Basic Dataset Information

Record what is actually present in the downloaded file.

| Check | Finding |
|---|---|
| Number of rows | |
| Number of columns | |
| Reference year/period | |
| Geographic coverage | |
| Smallest geographic level available | |
| Industry classification | |
| NAICS version, if stated | |
| Business-size classification, if available | |
| Metadata available? | Yes / No |
| Documentation available? | Yes / No |

---

# 3. Column Review

List the actual columns found in the dataset.

| Column Name | Meaning | Data Type | Example Value | Important for Project? |
|---|---|---|---|---|
| | | | | |
| | | | | |
| | | | | |

Add more rows as required.

Do not guess what a column means.

Where possible, confirm its meaning using the official metadata or documentation.

---

# 4. Missing Values

Check each important variable for missing information.

| Variable | Missing Count | Missing % | Possible Meaning / Note |
|---|---:|---:|---|
| | | | |
| | | | |

At this stage:

**Do not delete or fill missing values.**

Only document what you find.

---

# 5. Duplicate Check

**Total duplicate rows:**  

**Possible duplicate business records:**  

**Fields used to check duplicates:**  

**Notes:**

Describe anything unusual.

Do not remove duplicates during the audit.

---

# 6. Geographic Audit

Record the geographic information available.

Possible examples include:

- Canada
- Ontario
- Niagara Region
- Census Division (CD)
- Census Subdivision (CSD)
- Census Metropolitan Area (CMA)
- municipality

### Findings

**Geographic field(s):**  

**Geographic level(s):**  

**Does Niagara appear directly?** Yes / No

**Are Niagara municipalities available?** Yes / No / Not applicable

**Geographic limitations:**  

---

# 7. Time Coverage

**Earliest year/date:**  

**Latest year/date:**  

**Frequency:**  
Annual / Semi-annual / Quarterly / Monthly / Census year / Other

**Does the dataset cover multiple years?** Yes / No

**Important time-related limitations:**  

---

# 8. Industry / NAICS Review

**Does the dataset contain industry information?** Yes / No

**Does it contain NAICS?** Yes / No

**NAICS version:**  

**NAICS level/digits available:**  

**Important industry fields:**  

**Notes / limitations:**  

This information will help us determine whether datasets can later be compared or aggregated by industry.

---

# 9. Business Size / Employment Review

**Does the dataset contain employment information?** Yes / No

**Does it contain business-size categories?** Yes / No

**Size variable:**  

**Available categories:**  

**Definition of categories:**  

**Source of definition:**  

**Notes / limitations:**  

Do not assume that "small", "medium" or "large" has the same definition across different datasets.

---

# 10. Succession-Related Variable Check

Check specifically whether the dataset contains any of the following.

| Variable | Present? | Actual Column Name | Notes |
|---|---|---|---|
| Owner age | Yes / No | | |
| Retirement intention | Yes / No | | |
| Intended exit timeline | Yes / No | | |
| Successor identified | Yes / No | | |
| Succession plan | Yes / No | | |
| Reason for closure | Yes / No | | |
| Business status | Yes / No | | |
| Business opening year | Yes / No | | |

Do not mark a variable **Yes** simply because it was mentioned in a questionnaire or report.

It must exist in the actual acquired dataset.

---

# 11. Direct, Proxy and Context Variables

Classify potentially useful variables.

### Direct Variables

Variables that directly measure succession or a closely defined outcome.

**Found:**  

---

### Proxy Variables

Variables that may help estimate or understand succession risk but do not directly measure it.

**Found:**  

---

### Context Variables

Variables that describe the business, population or economy but do not directly measure succession risk.

**Found:**  

---

# 12. Possible Joining Keys

Check whether this dataset has variables that could potentially connect it to another dataset.

Possible examples:

- municipality;
- geographic code;
- year;
- NAICS;
- industry;
- employment-size category; or
- verified business identifier.

| Possible Key | Present? | Example | Notes |
|---|---|---|---|
| Geography | | | |
| Year | | | |
| NAICS | | | |
| Industry | | | |
| Business size | | | |
| Business identifier | | | |

### Important Rule

A possible common variable does **not** automatically mean two datasets can be joined.

The meaning, level and coding must first be checked.

---

# 13. Unusual Values / Quality Issues

Record anything that may affect later analysis.

Examples may include:

- unexpected categories;
- blank fields;
- inconsistent spelling;
- impossible values;
- unusual codes;
- mixed data types;
- duplicated records;
- suppressed values;
- outdated records; or
- unclear definitions.

### Findings

1.  
2.  
3.  

---

# 14. Dataset Strengths

What does this dataset do well for our project?

1.  
2.  
3.  

---

# 15. Dataset Limitations

What can this dataset **not** tell us?

1.  
2.  
3.  

Do not hide limitations. They are part of the methodology.

---

# 16. Relevance to the Challenge

Which deliverables could this dataset potentially support?

- [ ] 4.1 Aggregated data layer
- [ ] 4.2 Research report
- [ ] 4.3 Infographics & visual assets
- [ ] 4.4 Graphs & exploratory visuals
- [ ] 4.5 Predictive model for forecasting business closures
- [ ] 4.6 Business acquisition / succession playbook
- [ ] 4.7 Local-economy impact analysis
- [ ] 4.8 Government & private-sector remediation report
- [ ] 4.9 Nice-to-have extension(s)

### Explain briefly

**How could this dataset help?**

---

# 17. Dataset Decision

After completing the audit, select one:

- [ ] **KEEP — Core:** Important dataset for the main analysis
- [ ] **KEEP — Supporting:** Useful for context or validation
- [ ] **CONDITIONAL:** May be useful depending on later analysis
- [ ] **DO NOT USE:** Not suitable for the project

### Reason for decision

---

# 18. Actions Required Before Cleaning

List anything that must be resolved before this dataset moves into Week 4 cleaning.

1.  
2.  
3.  

Examples:

- confirm category definition;
- investigate missing values;
- confirm geographic codes;
- check NAICS version;
- clarify duplicate records;
- obtain missing metadata; or
- resolve licence/source issue.

---

# 19. New Risks or Data Gaps

Did this audit identify a new project risk?

**Yes / No**

If yes, describe it:

**Risk / gap:**  

**Why it matters:**  

**Action required:**  

If significant, add it to `RISK_REGISTER.md`.

---

# 20. Audit Sign-Off

**Dataset audited by:**  

**Date audit completed:**  

**Reviewed by:**  

**Review date:**  

**Audit status:**  
Draft / Needs Review / Approved

---

# Week 3 Audit Rule

A dataset should not move directly from:

**Download → Cleaning**

The required process is:

**Download → Preserve Raw File → Record Source → Audit → Review → Cleaning**

This helps us make cleaning decisions based on what is actually present in the data rather than assumptions.

---

# Week 3 Audit Completion Criteria

An audit is complete when:

- [ ] Dataset source has been recorded in `data/raw/DATA_SOURCES.md`
- [ ] Raw file has been preserved unchanged
- [ ] Rows and columns have been recorded
- [ ] Columns have been reviewed
- [ ] Missing values have been checked
- [ ] Duplicates have been checked
- [ ] Geography has been confirmed
- [ ] Time coverage has been confirmed
- [ ] Industry/NAICS information has been checked
- [ ] Business-size information has been checked
- [ ] Succession-related variables have been checked
- [ ] Possible joining keys have been identified
- [ ] Data-quality problems have been documented
- [ ] Strengths and limitations have been recorded
- [ ] Dataset relevance has been assessed
- [ ] Keep/conditional/do-not-use decision has been recorded
- [ ] New risks have been added to the risk register where necessary
- [ ] Audit has been reviewed
