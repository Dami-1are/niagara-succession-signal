# Niagara Succession Signal — Week 2 Completion & Handover

## Week 2 Focus

**Data Source Research, Evaluation and Selection**

The purpose of Week 2 was to understand what data is available for the Niagara Succession Signal project before beginning data collection, cleaning or modelling.

Our main question for the week was:

> **What data is available, what can it help us answer, and what are its limitations?**

---

# 1. Week 2 Work Completed

## 1.1 Data Sources Researched

The team investigated several sources, including:

- Niagara Employment Inventory (NEI);
- Niagara Open Data;
- Statistics Canada Business Counts;
- Statistics Canada Business Dynamics;
- Statistics Canada Census and demographic data;
- CFIB succession research;
- Niagara economic and labour-market information; and
- other supporting Canadian/Ontario succession materials.

**Status: COMPLETE**

---

## 1.2 Niagara-Specific Business Data Identified

The Consolidated Niagara Employment Inventory was identified as an important local source.

It provides useful information about Niagara businesses, including fields relating to:

- municipality;
- industry/NAICS;
- business opening year;
- employee size; and
- other business characteristics.

The actual downloaded fields will be confirmed during Week 3.

**Status: COMPLETE FOR WEEK 2**

---

## 1.3 Statistics Canada Sources Identified

Selected Statistics Canada tables were identified for:

- business counts;
- business entries and exits;
- business size;
- demographic age structure; and
- self-employment/class-of-worker information.

The selected Priority A tables have been documented in the Data Acquisition Plan.

**Status: COMPLETE**

---

## 1.4 Succession Research Identified

The team identified supporting research relating to:

- business-owner retirement;
- intended business exits;
- succession planning;
- barriers to succession; and
- business transfer.

Much of this information is national or provincial rather than Niagara-specific.

It will therefore be used carefully as supporting context rather than automatically treated as local evidence.

**Status: COMPLETE**

---

# 2. Major Week 2 Data Gap

The most important limitation identified during Week 2 is the lack of confirmed public Niagara business-level data containing direct succession variables.

We have not yet confirmed public access to variables such as:

- owner age;
- retirement intention;
- intended exit timeline;
- identified successor;
- succession-plan status; or
- confirmed succession-related reason for closure.

This limitation has been recorded in the project Risk Register.

---

# 3. 2026 NEI Succession Information

We identified that succession-planning information associated with the 2026 Niagara Employment Inventory may be particularly valuable.

However, public access to the succession-specific responses has not yet been confirmed.

This source remains:

**ACCESS PENDING**

Further investigation will continue during Week 3.

---

# 4. Source Evaluation Completed

The team did not automatically accept every source discovered during Week 2.

Sources were evaluated based on:

- relevance to the research question;
- geographic coverage;
- available variables;
- reference period;
- accessibility;
- limitations;
- licence/usage conditions; and
- potential role in the project.

Sources were then classified as:

### Priority A — Must Download

Core datasets selected for Week 3 acquisition and audit.

### Priority B — Supporting / Conditional

Sources retained for context, benchmarking or later use if required.

### Priority C — Access Pending

Potentially important sources that still require access investigation.

**Status: COMPLETE**

---

# 5. Data Licensing Review

Usage and licensing requirements for the main data and research sources have been documented.

The project distinguishes between:

- open datasets that can be reused under their applicable licences; and
- copyrighted/supporting research materials that should primarily be cited rather than redistributed.

Details are recorded in:

`references/DATA_LICENSES.md`

**Status: COMPLETE**

---

# 6. Risks and Limitations Documented

The project Risk Register now records major issues identified during Week 2, including:

- lack of direct succession variables;
- uncertainty around access to 2026 NEI succession information;
- business exit not being equivalent to succession failure;
- geographic differences between sources;
- different reference periods;
- different business-size definitions;
- possible NAICS differences;
- proxy-variable limitations;
- possible dataset joining problems; and
- future missing-value/duplicate issues requiring audit.

Details are recorded in:

`RISK_REGISTER.md`

**Status: COMPLETE**

---

# 7. Data Acquisition Plan Prepared

A structured Week 3 Data Acquisition Plan has been prepared.

It identifies:

- Priority A datasets;
- supporting/conditional sources;
- access-pending sources;
- preferred file formats;
- planned raw-data locations;
- acquisition rules; and
- Week 3 completion criteria.

Details are recorded in:

`docs/DATA_ACQUISITION_PLAN.md`

**Status: COMPLETE**

---

# 8. Data Dictionary Structure Prepared

A Data Dictionary template has been prepared.

The dictionary has intentionally **not** been filled with assumed columns.

Actual variables will be documented after the datasets are downloaded and audited.

Details are recorded in:

`docs/DATA_DICTIONARY.md`

**Status: TEMPLATE COMPLETE**

---

# 9. Raw Data Tracking Prepared

A source-tracking log has been created so that every raw dataset can be traced back to its original source.

During Week 3, the team will record:

- source;
- official link;
- filename;
- download date;
- reference period;
- geography;
- licence;
- repository location; and
- person responsible for the download.

Details are recorded in:

`data/raw/DATA_SOURCES.md`

**Status: TEMPLATE COMPLETE**

---

# 10. Week 3 Data Audit Prepared

A standard audit template has been created so that all Priority A datasets will be reviewed consistently.

The audit will examine:

- rows and columns;
- data types;
- missing values;
- duplicates;
- geography;
- time coverage;
- NAICS/industry information;
- business size;
- succession-related variables;
- possible joining keys;
- data-quality issues;
- strengths;
- limitations; and
- dataset suitability.

Details are recorded in:

`docs/DATA_AUDIT_TEMPLATE.md`

**Status: TEMPLATE COMPLETE**

---

# 11. Team Contributions Documented

The research contributions shared by team members during Week 2 have been documented.

The contribution record includes:

- Stephen & Mano;
- Oluwatosin & Ohonba;
- Damilare & Lucky;
- Precious & Ruth; and
- Team Lead coordination and consolidation.

Details are recorded in:

`docs/WEEK_2_CONTRIBUTIONS.md`

**Status: COMPLETE**

---

# 12. Challenge Deliverables Considered

The identified data sources have been mapped to the official challenge deliverables:

- **4.1** Aggregated data layer
- **4.2** Research report
- **4.3** Infographics & visual assets
- **4.4** Graphs & exploratory visuals
- **4.5** Predictive model for forecasting business closures
- **4.6** Business acquisition / succession playbook
- **4.7** Local-economy impact analysis
- **4.8** Government & private-sector remediation report
- **4.9** Nice-to-have extensions

The mapping is currently a **planned mapping**.

Final use of each dataset will depend on what is confirmed during collection and audit.

**Status: COMPLETE FOR WEEK 2**

---

# 13. Predictive Model — Important Open Question

The challenge requires a predictive model for forecasting business closures.

However, at the end of Week 2 we have not yet confirmed the final:

- modelling unit;
- target variable;
- forecast horizon;
- modelling features; or
- method for connecting closure forecasting to succession risk.

We will not choose an algorithm simply because it is familiar.

The modelling approach must be based on the data that is actually available and the problem we can validly define.

**Status: TO BE RESOLVED IN LATER PROJECT PHASES**

This is not considered an incomplete Week 2 task.

---

# 14. What We Are NOT Doing Yet

The following activities were intentionally not part of Week 2:

- downloading all Priority A datasets;
- cleaning data;
- deleting missing values;
- removing duplicates;
- merging datasets;
- performing EDA;
- engineering features;
- creating a succession-risk score;
- selecting a machine-learning algorithm;
- training a predictive model; or
- producing final recommendations.

These activities belong to later phases of the roadmap.

---

# 15. Week 3 Handover

## Week 3 Focus

**Data Collection & Audit**

Week 3 will answer:

> **What data do we actually have, what is inside it, what is its quality, and what can it legitimately support?**

### Week 3 Initial Actions

The team will:

1. Download the approved Priority A datasets.
2. Preserve the original raw files.
3. Record every dataset in `data/raw/DATA_SOURCES.md`.
4. Preserve official metadata.
5. Complete an audit for each Priority A dataset.
6. Confirm actual variables and definitions.
7. Measure missing values.
8. Check duplicates.
9. Confirm geographic coverage.
10. Confirm reference periods.
11. Check NAICS and business-size definitions.
12. Identify possible joining keys.
13. Check for direct succession-related variables.
14. Investigate access to the 2026 NEI succession information.
15. Update the Risk Register with any new findings.

---

# 16. Week 2 Completion Checklist

- [x] Major data-source areas researched
- [x] Niagara local business source identified
- [x] Statistics Canada sources identified
- [x] Succession research identified
- [x] Major data gaps documented
- [x] Source limitations documented
- [x] Data licences documented
- [x] Data acquisition priorities established
- [x] Week 3 acquisition plan prepared
- [x] Data dictionary template prepared
- [x] Raw-data source tracking prepared
- [x] Data audit template prepared
- [x] Team contributions documented
- [x] Sources mapped to challenge deliverables
- [x] Risks recorded
- [x] Week 3 handover actions defined

---

# Week 2 Conclusion

Week 2 is complete from a **data-source research and planning perspective**.

The most important thing we learned is that having many data sources does not automatically mean we have direct evidence of succession risk.

We have useful information about Niagara businesses, business dynamics, demographics and the wider Canadian succession problem, but important succession-specific information remains limited.

Rather than hiding this gap or making assumptions, we have documented it.

We are therefore moving into Week 3 with a clear acquisition plan, clear data limitations, a standard audit process and a record of what each source may legitimately contribute to the project.

**Week 2 Status: READY FOR FINAL QA**
