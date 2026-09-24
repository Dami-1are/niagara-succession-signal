# Niagara Succession Signal — Data Acquisition Plan

## Purpose

During Week 2, our team researched different data sources that could support the Niagara Succession Signal project.

This document records which sources we have decided to carry forward into Week 3, what we need from each source, and what should happen after the data is downloaded.

Week 3 will focus on **Data Collection and Audit**.

Downloading a dataset does not mean that it has been approved for modelling. Every dataset must first be inspected and audited.

---

# 1. Acquisition Priority

We divided the sources into three groups:

### Priority A — Must Download

These are the main datasets we currently expect to use in the project.

### Priority B — Supporting / Conditional

These sources may support our analysis but should only be downloaded or extracted where they provide information we actually need.

### Priority C — Access Pending

These are potentially valuable sources that we have not yet confirmed we can access.

---

# 2. Priority A — Must Download

| Dataset | Provider | Why We Need It | Format | Destination | Status |
|---|---|---|---|---|---|
| Consolidated Niagara Employment Inventory | Niagara Region | Main local source for Niagara businesses, municipality, industry/NAICS, employment size and other business characteristics | CSV preferred | `data/raw/nei/` | To download |
| Canadian Business Counts – 33-10-1176-01 | Statistics Canada | Local business counts by geography, industry and employment size | CSV + metadata | `data/raw/statcan/business_counts/` | To download |
| Business Dynamics by Industry – 33-10-0087-01 | Statistics Canada | Historical business entry and exit patterns by industry | CSV + metadata | `data/raw/statcan/business_dynamics/` | To download |
| Business Dynamics by Firm Size – 33-10-0088-01 | Statistics Canada | Historical entry/exit patterns by business size | CSV + metadata | `data/raw/statcan/business_dynamics/` | To download |
| Census Age Data – 98-10-0022-01 | Statistics Canada | Niagara demographic age structure | CSV + metadata | `data/raw/statcan/census/` | To download |
| Census Class of Worker / Self-Employment – 98-10-0592-01 | Statistics Canada | Self-employment patterns by age and industry | CSV + metadata | `data/raw/statcan/census/` | To download |

---

# 3. Priority B — Supporting / Conditional Sources

These sources are useful, but we do not need to download everything immediately.

| Source | Provider | Possible Use | Decision |
|---|---|---|---|
| Canadian Business Counts – 33-10-1174-01 | Statistics Canada | Ontario/Canada employer-business benchmark | Download only if needed for comparison |
| Canadian Business Counts – 33-10-1175-01 | Statistics Canada | Businesses without employees | Download if needed for business-structure analysis |
| Employment Dynamics – 33-10-0089-01 | Statistics Canada | Employment creation/destruction connected with business dynamics | Download if needed for jobs-exposure analysis |
| Experimental Business Openings/Closures – 33-10-0270-01 | Statistics Canada | More recent monthly opening/closure patterns | Use if geography and methodology are suitable |
| Experimental Openings/Closures by Employment Size – 33-10-0722-01 | Statistics Canada | Recent opening/closure patterns by business size | Use if needed after audit |
| CFIB Succession Tsunami | CFIB | National succession context, owner exit intentions and barriers | Keep as research/reference material |
| Niagara Regional Quick Facts | Niagara Economic Development | Local business/economic context | Extract only figures required |
| Niagara Economic Indicators | Niagara Economic Development | Regional economic impact context | Extract only relevant indicators |
| Niagara Labour Force | Niagara Economic Development | Employment and sector context | Extract only relevant indicators |
| Niagara Economic Development Reports | Niagara Economic Development | Sector and economic context | Keep only relevant reports |

---

# 4. Priority C — Access Pending

## 2026 Niagara Employment Inventory Succession Information

**Provider:** Niagara Region / Niagara Economic Development

**Priority:** HIGH if accessible

During Week 2, we confirmed that the 2026 Niagara Employment Inventory survey included succession-planning questions.

However, we have not yet confirmed public access to the responses.

This is important because the information may provide more direct evidence about succession planning among Niagara businesses.

### Week 3 Action

We will investigate whether the succession-specific information can be obtained through:

- an official public release;
- Niagara Open Data;
- Niagara Economic Development;
- another official Niagara Region publication or data product; or
- an appropriate official data request/contact route.

Until access is confirmed, this information will **not** be treated as an available dataset.

**Status:** ACCESS PENDING

---

# 5. What We Are NOT Doing During Acquisition

During Week 3 data collection, we will not immediately:

- clean the datasets;
- delete missing values;
- remove duplicates;
- rename columns;
- merge datasets;
- create succession-risk scores;
- engineer modelling features;
- train machine-learning models; or
- assume that an apparent data problem should be corrected.

The first task is to understand what we actually downloaded.

---

# 6. Raw Data Storage Structure

Where practical, raw datasets should follow this structure:

```text
data/
└── raw/
    ├── nei/
    └── statcan/
        ├── business_counts/
        ├── business_dynamics/
        └── census/
```

Research reports and reference documents should not be mixed with the main tabular datasets.

They should remain in the appropriate documentation/reference location.

---

# 7. Raw Data Rule

Files placed in `data/raw/` represent the original source data.

Once downloaded:

**DO NOT EDIT THE RAW FILE.**

If changes are needed later, a new version should be created in the appropriate downstream folder.

The raw file should remain available so that another team member can reproduce our work from the original source.

---

# 8. What Must Be Recorded for Every Download

For every dataset collected during Week 3, we will record:

1. Dataset name
2. Source organisation
3. Official source link
4. Table/dataset number where applicable
5. Date downloaded
6. File format
7. Reference period/year
8. Geographic coverage
9. Licence
10. Original filename
11. Repository location
12. Team member who collected it

This will create a clear record of where every dataset came from.

---

# 9. Week 3 Initial Data Audit

After acquisition, each dataset will be inspected before cleaning.

The initial audit should record:

- number of rows;
- number of columns;
- column names;
- data types;
- sample records;
- missing values;
- duplicate records;
- geographic fields;
- date/year fields;
- NAICS/industry fields;
- business-size fields;
- identifiers or possible joining keys;
- unusual values;
- metadata availability; and
- obvious limitations.

---

# 10. Joining Rule

We will not assume that datasets can be joined simply because they relate to businesses.

Before combining sources, we must identify a legitimate common level such as:

- geography;
- year;
- NAICS/industry;
- employment-size category; or
- another verified common identifier.

If no reliable business-level identifier exists, we will not force a business-level merge.

---

# 11. Succession Variable Rule

During the Week 3 audit, we will specifically check whether any acquired source actually contains variables related to:

- owner age;
- retirement intention;
- intended exit timeline;
- successor availability;
- succession-plan status; or
- reason for business closure.

If these variables are not present, we will record them as missing rather than create or assume them.

---

# 12. Week 3 Acquisition Completion Criteria

Data acquisition will be considered complete when:

- [ ] All Priority A datasets have been downloaded or a reason for non-access has been documented.
- [ ] Original files are preserved.
- [ ] Statistics Canada metadata is preserved with downloaded tables.
- [ ] Download dates are recorded.
- [ ] Official source links are recorded.
- [ ] Licences are recorded.
- [ ] Reference periods are recorded.
- [ ] Geographic levels are recorded.
- [ ] Raw files have not been cleaned or modified.
- [ ] Initial audit has been completed for every Priority A dataset.
- [ ] Access status of the 2026 NEI succession information has been investigated and documented.
- [ ] Any new data gaps discovered during acquisition have been added to `RISK_REGISTER.md`.

---

# Week 2 to Week 3 Handover

Week 2 answered:

**What data might help us answer the project question?**

Week 3 will answer:

**What data do we actually have, what is inside it, what is its quality, and what can it legitimately support?**

We will only move from data collection into cleaning after we understand the datasets we have acquired.
