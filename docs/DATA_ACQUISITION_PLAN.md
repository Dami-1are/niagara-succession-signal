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


---

# 13. Week 2 Data Source Decision Matrix

This matrix summarises our final Week 2 decisions about the data sources researched by the team.

It shows which sources we are carrying forward, why we need them, their main limitations, and what will happen to them in Week 3.

| Data Source | Decision | Role in Project | Priority | Main Limitation | Week 3 Action |
|---|---|---|---|---|---|
| Consolidated Niagara Employment Inventory (NEI) | Keep | Main local business-level source for municipality, industry/NAICS, employment size and other business characteristics | A — Must Download | Public data inspected so far does not provide confirmed direct succession variables | Download CSV, preserve raw copy and audit all fields |
| Canadian Business Counts — 33-10-1176-01 | Keep | Local business counts by geography, industry and employment size | A — Must Download | Business counts do not directly measure succession risk | Download CSV + metadata and audit |
| Business Dynamics by Industry — 33-10-0087-01 | Keep | Historical business entry and exit patterns by industry | A — Must Download | Business exit does not tell us why the business exited | Download CSV + metadata and audit |
| Business Dynamics by Firm Size — 33-10-0088-01 | Keep | Historical business entry/exit patterns by business size | A — Must Download | Mainly useful as broader benchmark/context rather than direct Niagara succession evidence | Download CSV + metadata and audit |
| Census Age Data — 98-10-0022-01 | Keep | Niagara demographic age structure | A — Must Download | Population age is not the same as business-owner age | Download CSV + metadata and audit |
| Census Class of Worker / Self-Employment — 98-10-0592-01 | Keep | Self-employment patterns by age and industry | A — Must Download | Self-employment is only a proxy and does not directly identify business owners | Download CSV + metadata and audit |
| Canadian Business Counts — 33-10-1174-01 | Conditional | Ontario/Canada employer-business benchmark | B — Supporting | Broader geography than our main Niagara focus | Download only if required for comparison |
| Canadian Business Counts — 33-10-1175-01 | Conditional | Businesses without employees | B — Supporting | Does not directly measure succession | Use if required for business-structure analysis |
| Employment Dynamics — 33-10-0089-01 | Conditional | Jobs created/destroyed in business dynamics | B — Supporting | Does not directly identify succession-related employment loss | Use if required for local-economy/jobs-exposure analysis |
| Experimental Business Openings/Closures — 33-10-0270-01 | Conditional | More recent opening and closure patterns | B — Supporting | Experimental series and closure reason is unknown | Use only if geography and methodology are suitable |
| Experimental Openings/Closures by Employment Size — 33-10-0722-01 | Conditional | Recent opening/closure patterns by business size | B — Supporting | Experimental data and closure does not equal succession failure | Use if required after audit |
| CFIB Succession Research | Keep as reference | Canadian succession-planning context, owner exit intentions and barriers | B — Reference | National findings cannot automatically be treated as Niagara findings | Preserve as reference material and cite appropriately |
| Niagara Regional Quick Facts | Keep as reference | Local economic and business context | B — Reference | Contextual information rather than direct succession data | Extract only relevant figures with their reference year |
| Niagara Economic Indicators | Keep as reference | Regional economic context | B — Reference | Does not directly measure business succession | Extract only relevant indicators |
| Niagara Labour Force | Keep as reference | Employment and labour-market context | B — Reference | Labour-force statistics do not identify succession risk | Extract only relevant indicators |
| Niagara Economic Development Reports | Keep selectively | Sector and regional economic context | B — Reference | Relevance varies by report | Keep only reports directly useful to the project |
| 2026 NEI Succession Information | Investigate | Potential direct evidence of succession planning in Niagara | C — Access Pending / High Value | Public access to the succession-specific responses has not been confirmed | Investigate official access during Week 3 |

---

## Final Week 2 Data Decision

Our Week 2 research shows that no single identified public source can answer the full succession-risk question by itself.

We will therefore use the sources for different purposes:

- **NEI** will provide the main local business structure.
- **Statistics Canada Business Counts** will provide business-count benchmarks.
- **Statistics Canada Business Dynamics** will provide entry and exit patterns.
- **Census data** will provide demographic and self-employment context.
- **CFIB research** will provide Canadian succession-planning context.
- **Niagara economic sources** will provide local economic context.
- **2026 NEI succession information** remains an important access gap that we will continue investigating.

The team will not treat proxy or contextual information as direct evidence of succession risk.

The final choice of variables and datasets used in the aggregated data layer will be made only after Week 3 data collection and audit.
