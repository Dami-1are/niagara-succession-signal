# Niagara Succession Signal — Data Dictionary

## Purpose

This document will describe the variables used in the Niagara Succession Signal project.

The data dictionary will be completed and updated as datasets are collected, audited, cleaned and combined.

Only variables that are confirmed in the actual downloaded datasets will be documented as available.

We will not add a variable simply because we expect or want it to exist.

---

# 1. Data Dictionary Status

**Current Stage:** Week 2 — Data Source Research completed

**Next Stage:** Week 3 — Data Collection and Audit

At this stage, the final variable list is not yet complete because the Priority A datasets have not all been collected and audited.

During Week 3, the actual column names and definitions will be taken directly from the downloaded datasets and their official metadata.

---

# 2. Variable Documentation Template

For every variable that enters our analysis, we will record:

| Field | Description |
|---|---|
| Dataset | Dataset where the variable comes from |
| Original Column Name | Exact name used in the source file |
| Standardised Name | Name used in our processed dataset, if changed |
| Description | What the variable represents |
| Data Type | Text, integer, decimal, date, category, etc. |
| Unit | Unit of measurement where applicable |
| Example | Example value |
| Geographic Level | Canada, Ontario, CMA, CD, CSD, Niagara Region, municipality, etc. |
| Reference Period | Year/date represented |
| Missing Values | Number or percentage missing |
| Source | Original organisation/dataset |
| Direct / Proxy / Context | How the variable relates to succession risk |
| Transformation | Any cleaning or transformation applied |
| Notes / Limitations | Important cautions about interpretation |

---

# 3. Consolidated Niagara Employment Inventory

**Provider:** Niagara Region

**Status:** Awaiting Week 3 audit

The actual variables from the downloaded NEI dataset will be entered here after acquisition.

| Original Column | Standardised Name | Description | Type | Missing | Role | Notes |
|---|---|---|---|---|---|---|
| To be confirmed | To be confirmed | To be confirmed from actual dataset | TBD | TBD | TBD | Week 3 audit |

### Variables We Will Specifically Look For

During the audit, we will check whether the dataset contains fields relating to:

- municipality;
- business name or identifier;
- NAICS;
- sector/industry;
- business opening year;
- employee size;
- business status; and
- other relevant business characteristics.

We will also check whether the public dataset actually contains:

- owner age;
- retirement intention;
- intended exit timeline;
- successor availability;
- succession-plan status; or
- reason for closure.

These succession variables will **not** be recorded as available unless they are confirmed in the actual data.

---

# 4. Canadian Business Counts

**Provider:** Statistics Canada

**Priority table:** 33-10-1176-01

**Status:** Awaiting Week 3 audit

| Original Column | Standardised Name | Description | Type | Missing | Role | Notes |
|---|---|---|---|---|---|---|
| To be confirmed | To be confirmed | To be confirmed from downloaded table and metadata | TBD | TBD | Context | Week 3 audit |

We expect this source to support information relating to business counts, geography, industry/NAICS and employment-size ranges.

The exact downloaded columns and categories will be documented from the source file and metadata.

---

# 5. Business Dynamics

**Provider:** Statistics Canada

**Priority tables:**

- 33-10-0087-01 — Business Dynamics by Industry
- 33-10-0088-01 — Business Dynamics by Firm Size

**Status:** Awaiting Week 3 audit

| Original Column | Standardised Name | Description | Type | Missing | Role | Notes |
|---|---|---|---|---|---|---|
| To be confirmed | To be confirmed | To be confirmed from downloaded tables and metadata | TBD | TBD | Context / Proxy | Week 3 audit |

Business exits will **not** automatically be classified as succession-related closures.

---

# 6. Census Age Data

**Provider:** Statistics Canada

**Table:** 98-10-0022-01

**Status:** Awaiting Week 3 audit

| Original Column | Standardised Name | Description | Type | Missing | Role | Notes |
|---|---|---|---|---|---|---|
| To be confirmed | To be confirmed | To be confirmed from downloaded table and metadata | TBD | TBD | Context | Week 3 audit |

Age information describes the population represented by the Census geography.

It must not automatically be interpreted as the age of business owners.

---

# 7. Census Class of Worker / Self-Employment

**Provider:** Statistics Canada

**Table:** 98-10-0592-01

**Status:** Awaiting Week 3 audit

| Original Column | Standardised Name | Description | Type | Missing | Role | Notes |
|---|---|---|---|---|---|---|
| To be confirmed | To be confirmed | To be confirmed from downloaded table and metadata | TBD | TBD | Proxy / Context | Week 3 audit |

Self-employment will not automatically be treated as direct evidence of business ownership.

---

# 8. Variable Classification

Every important variable used in the project will be classified into one of three groups.

### Direct Variable

A variable that directly measures the succession issue we are studying.

Examples could include owner retirement intention or succession-plan status **if such variables are actually obtained**.

### Proxy Variable

A variable that does not directly measure succession but may help us estimate or understand succession risk when properly justified.

The use of every proxy must be explained in the methodology.

### Context Variable

A variable that helps describe Niagara's businesses, population or economy but does not itself measure succession risk.

---

# 9. Standardisation Rules

When datasets are cleaned later in the project:

1. Original column names will first be recorded.
2. Any renamed column will have both its original and standardised name documented.
3. Data types will be recorded.
4. Units will be recorded where applicable.
5. Missing values will be measured before treatment.
6. Category mappings will be documented.
7. NAICS mappings or changes will be documented.
8. Business-size definitions will be documented.
9. Geographic transformations will be documented.
10. Derived variables will include an explanation of how they were calculated.

---

# 10. Derived Variables

Any variable created by our team will be documented separately.

| Derived Variable | Created From | Formula / Rule | Purpose | Limitation |
|---|---|---|---|---|
| To be determined | TBD | TBD | TBD | TBD |

A derived succession-risk feature will not be presented as an observed variable.

---

# 11. Data Dictionary Completion Rule

This data dictionary will be considered complete when:

- [ ] Every dataset used in the aggregated data layer is documented.
- [ ] Every retained variable is documented.
- [ ] Original column names are recorded.
- [ ] Standardised names are recorded where applicable.
- [ ] Variable definitions are recorded.
- [ ] Data types are recorded.
- [ ] Units are recorded where applicable.
- [ ] Geographic levels are recorded.
- [ ] Reference periods are recorded.
- [ ] Missingness is documented.
- [ ] Transformations are documented.
- [ ] Derived variables are documented.
- [ ] Direct, proxy and contextual variables are distinguished.
- [ ] Important limitations are documented.
- [ ] Definitions are checked against official source metadata.

---

# Relationship to Required Deliverable 4.1

The challenge requires an **Aggregated Data Layer**: a cleaned, documented, aggregated dataset joining relevant open sources at appropriate sector and municipal levels.

This data dictionary will provide part of the documentation supporting that aggregated data layer.

The final data dictionary will describe the actual datasets and variables used in the project so that another person can understand and reproduce our analytical dataset.
