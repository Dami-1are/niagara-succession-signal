# Niagara Succession Signal — Week 2 Team Contributions

## Week 2 Focus

Week 2 focused on **data-source research and evaluation**.

The goal was not simply to find as many datasets as possible. We needed to understand:

- what data is available;
- what each source contains;
- how it could support our research question;
- whether it is specific to Niagara;
- what important variables are missing; and
- which sources should move forward to Week 3.

The findings below summarise the contributions reported by the team during Week 2.

---

# 1. Stephen & Mano

## Area

**Niagara Employment Inventory (NEI) & Niagara Open Data**

### Contribution

Stephen and Mano investigated Niagara Region's local business data and identified the **Consolidated Niagara Employment Inventory (NEI) Open Data**.

They reported that the dataset contains approximately **98,065 records** and includes information such as:

- municipality;
- NAICS;
- sector;
- industry;
- business opening year; and
- employee-size range.

They also investigated:

- dataset accessibility;
- available download formats;
- update information; and
- licensing.

They identified employee-size categories including:

- Micro;
- Small;
- Medium;
- Large;
- Undetermined; and
- Permanently Closed/Vacant.

### Important Finding

The public attributes they inspected did not show direct succession variables such as:

- owner age;
- retirement intention;
- successor information; or
- succession-plan status.

The team also noted that **Permanently Closed/Vacant cannot automatically be interpreted as a succession-related closure**.

### Week 3 Decision

**KEEP — Priority A**

The Consolidated NEI will be one of our main local business datasets and will be downloaded and audited in Week 3.

---

# 2. Oluwatosin & Ohonba

## Area

**Business-owner retirement, succession planning, exit timelines and barriers to succession**

### Contribution

Oluwatosin and Ohonba researched information relating to:

- business-owner retirement;
- succession planning;
- intended exit timelines;
- barriers to succession; and
- Canadian/Ontario statistics and reports.

They identified Statistics Canada and CFIB materials and found downloadable resources in formats including CSV, ZIP and PDF.

They also identified information relating to:

- legacy planning for small and medium enterprises; and
- business intentions and timelines for selling or transferring ownership.

### Important Finding

A major limitation they identified was **geography**.

Much of the succession-related information they found was Canadian or Ontario-level information rather than Niagara-specific information.

When they narrowed the search to Niagara, the Consolidated NEI provided useful local business characteristics but did not solve the direct succession-data gap.

### Week 3 Decision

**KEEP SELECTIVELY**

Relevant Statistics Canada datasets will move forward where appropriate.

CFIB succession research will be retained mainly as **supporting research/context**, not treated as Niagara-specific business-level data.

The Niagara succession-data gap remains open.

---

# 3. Damilare & Lucky

## Area

**Statistics Canada — Business Dynamics / Entries & Exits**

### Contribution

Damilare and Lucky investigated Statistics Canada's Business Dynamics data.

They identified information relating to:

- business entrants;
- incumbent businesses;
- business exits;
- industry;
- firm size;
- job creation and destruction; and
- business survival.

They found that the data provides useful historical information that can help us understand broader business entry and exit patterns.

They also identified sub-annual business opening and closure series.

### Important Finding

They correctly identified a major methodological limitation:

**A business exit does not tell us why the business exited.**

An exit may relate to different circumstances and cannot automatically be classified as:

- business failure;
- owner retirement; or
- succession failure.

They also found that the strongest annual Business Dynamics series are geographically broader than our Niagara-specific research question.

### Week 3 Decision

**KEEP — Priority A for selected Business Dynamics tables**

The selected Business Dynamics datasets will be used primarily for historical patterns, benchmarks and context.

They will not independently determine whether a Niagara business is experiencing succession risk.

---

# 4. Precious & Ruth

## Area

**Statistics Canada — Census & Demographics**

### Contribution

Precious and Ruth investigated the **2021 Census of Population** to understand the demographic and labour information available for Niagara.

They identified information relating to:

- age;
- median and average age;
- labour-force characteristics;
- class of worker;
- self-employment;
- industry;
- occupation; and
- geography.

They found that Census information is available at useful geographic levels for studying Niagara and its municipalities.

They also identified Niagara Region's own Census highlights as a possible supporting cross-check.

### Important Finding

They correctly identified that:

**Self-employed does not automatically mean business owner.**

Therefore, self-employment can only be used as a **proxy or contextual variable** where properly justified.

They also identified important time limitations because the Census represents specific census periods rather than continuous current information.

### Week 3 Decision

**KEEP — Priority A for selected Census tables**

The selected Census datasets will support demographic and self-employment context.

They will not be presented as direct business-owner succession information.

---

# 5. Team Lead — Joyce

## Area

**Coordination, review and Week 2 documentation**

### Contribution

As Team Lead, I coordinated the Week 2 data-source research and brought the individual research areas together into one project-level view.

My Week 2 work included:

- coordinating the team's data-source investigation;
- reviewing team updates;
- comparing the usefulness of the identified sources;
- identifying overlaps between team findings;
- separating direct, proxy and contextual information;
- documenting important data gaps;
- organising sources into acquisition priorities;
- documenting licensing and usage considerations;
- preparing the Week 3 data acquisition plan;
- preparing the data dictionary structure;
- preparing the Week 3 data audit structure;
- documenting raw-data source tracking requirements; and
- mapping the identified sources to the challenge deliverables.

A major focus of the review was making sure we do not claim that the available data tells us more than it actually does.

---

# 6. Combined Week 2 Findings

When we combined the team's research, several important conclusions became clear.

### 1. We have useful Niagara-specific business data

The Consolidated NEI gives us an important local foundation for understanding Niagara businesses.

### 2. We have useful Statistics Canada data

Statistics Canada provides information that can help us understand:

- business counts;
- business entries and exits;
- business size;
- demographic patterns; and
- self-employment.

### 3. We have useful succession research

CFIB and other research can help us understand the wider Canadian succession problem, including retirement, exit intentions and succession barriers.

### 4. We still have a major data gap

The public sources identified so far do not give us a confirmed direct Niagara business-level dataset containing all the succession variables we would ideally want.

Examples include:

- owner age;
- retirement intention;
- identified successor;
- succession-plan status; and
- confirmed succession-related reason for closure.

### 5. We must use proxies carefully

Variables such as:

- population age;
- self-employment;
- business age;
- business exits; and
- employee size

may provide useful information, but they must not automatically be described as direct evidence of succession risk.

---

# 7. Week 2 Team Decision

Based on the combined research, our data sources have been grouped into:

### Priority A — Core acquisition

Sources selected for Week 3 download and audit.

### Priority B — Supporting / Conditional

Sources that may provide benchmarks, context or additional analysis where needed.

### Priority C — Access Pending

Potentially valuable information that still requires access investigation.

The detailed acquisition decisions are documented in:

`docs/DATA_ACQUISITION_PLAN.md`

---

# 8. What Moves Into Week 3

Week 3 will move from:

**Finding possible data**

to:

**Collecting and understanding the actual data.**

The team will:

1. download the approved Priority A datasets;
2. preserve the original raw files;
3. record every source in `data/raw/DATA_SOURCES.md`;
4. preserve relevant metadata;
5. audit the datasets using `docs/DATA_AUDIT_TEMPLATE.md`;
6. confirm the actual columns available;
7. identify missing values and duplicates;
8. examine geography, time coverage, NAICS and business-size definitions;
9. identify legitimate possible joining keys;
10. check again for direct succession variables; and
11. document any new risks or data gaps.

---

# Week 2 Conclusion

Week 2 showed us that finding a dataset is not the same as finding the **right** dataset.

Our research identified useful local, provincial and national sources, but it also showed us where the evidence is limited.

Instead of hiding those limitations, we have documented them so that our next decisions are based on what the data can genuinely support.

Week 3 will now test these sources using the actual downloaded data before we move into cleaning, aggregation or modelling.
