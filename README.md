# Niagara Succession Signal

## Forecasting Small-Business Succession Risk in Niagara Region, Ontario

The **Niagara Succession Signal** is a data science and economic-development project focused on understanding the risk that otherwise viable small businesses may close because their owners retire or exit without suitable successors or buyers.

The project uses business, employment, demographic, and business-dynamics data to identify where succession risk may be concentrated across Niagara Region, estimate the businesses and jobs potentially exposed over the next 5–10 years, forecast future risk, and translate the findings into practical recommendations for government and private-sector stakeholders.

---

## Table of Contents

- [Project Overview](#project-overview)
- [The Problem](#the-problem)
- [Core Research Question](#core-research-question)
- [Research Questions](#research-questions)
- [Project Objectives](#project-objectives)
- [Project Scope](#project-scope)
- [Data Sources](#data-sources)
- [Project Methodology](#project-methodology)
- [Repository Structure](#repository-structure)
- [Getting Started](#getting-started)
- [Working on an Assigned Task](#working-on-an-assigned-task)
- [Required Deliverables](#required-deliverables)
- [Project Roadmap](#project-roadmap)
- [Team](#team)
- [Collaboration Workflow](#collaboration-workflow)
- [Definition of Done](#definition-of-done)
- [Ethics and Responsible Data Use](#ethics-and-responsible-data-use)
- [Reproducibility](#reproducibility)
- [Project Documentation](#project-documentation)
- [Project Status](#project-status)
- [Acknowledgement](#acknowledgement)

---

# Project Overview

Small businesses are an important part of local economies. They support employment, community services, entrepreneurship, and economic activity.

However, a business does not always close because it is failing.

An otherwise viable business may close when its owner retires or exits and there is no suitable successor or buyer to take over the business.

The **Niagara Succession Signal** project investigates this problem using data.

The project aims to understand where succession-related risk may be concentrated across Niagara Region and what the possible effects could be on businesses, employment, sectors, municipalities, and the wider local economy.

---

# The Problem

There is an important difference between ordinary business failure and succession-related closure.

### Business Failure

**Poor Performance → Financial Difficulty → Business Closure**

### Succession-Related Closure

**Viable Business → Owner Retires/Exits → No Successor or Buyer → Business Closure**

In the second situation, an otherwise viable business may disappear simply because ownership cannot successfully transfer to another person.

This project therefore seeks to understand succession-related closure risk separately from ordinary business-failure risk, as far as the available data allows.

---

# Core Research Question

> **Which parts of Niagara's small-business economy are most exposed to owner-succession risk over the next 5–10 years, how many businesses and jobs could potentially be affected, where is the risk concentrated by sector and municipality, and what can government and private-sector stakeholders do about it?**

### Project Decision Rule

Whenever a dataset, analysis, feature, chart, model, or new idea is proposed, we should ask:

> **How does this help us answer our research question?**

If we cannot clearly answer this question, we should reconsider whether the work belongs in the project.

---

# Research Questions

The main research question is broken into smaller questions that will guide the project:

1. How is Niagara's small-business population distributed across sectors and municipalities?
2. What historical patterns exist in business entries and exits?
3. What available indicators or proxies can help measure succession exposure?
4. Which sectors appear most exposed to succession risk?
5. Which municipalities appear most exposed to succession risk?
6. How many businesses could potentially be affected over the next 5–10 years?
7. How many jobs could potentially be exposed?
8. To what extent can the available data distinguish succession-related risk from ordinary business-failure risk?
9. What could estimated succession risk mean for Niagara's local economy?
10. What evidence-based actions could government and private-sector stakeholders consider?

These questions may be refined as the team learns more about the available data.

---

# Project Objectives

## Overall Objective

To assess and forecast small-business succession risk across Niagara Region and translate the findings into actionable economic-development insights.

## Specific Objectives

The project aims to:

- Quantify and map succession exposure across Niagara Region.
- Identify sectors with elevated succession risk.
- Identify municipalities with elevated succession risk.
- Estimate the number of businesses potentially exposed.
- Estimate the number of jobs potentially exposed.
- Examine succession-related risk separately from ordinary business failure where the available data permits.
- Develop a transparent and properly validated forecasting model.
- Assess the potential local-economic impact.
- Develop a generic business acquisition and succession playbook.
- Produce evidence-based recommendations for government and economic-development organisations.
- Produce evidence-based recommendations for private-sector stakeholders.
- Communicate findings through reports, graphs, infographics, and interactive visualisations.
- Maintain a reproducible and well-documented analytical workflow.

---

# Project Scope

## Geographic Scope

The project focuses on **Niagara Region, Ontario, Canada**.

Where supported by available data, the analysis will examine differences across Niagara's municipalities.

## Analytical Scope

The project focuses mainly on aggregate small-business succession risk.

Possible areas of analysis include:

- Business counts
- Business entries and exits
- Employment
- Industry and sector
- Municipality
- Business dynamics
- Demographic information
- Succession-related indicators or proxies where available

## Forecast Horizon

The primary analytical horizon is the next:

**5–10 years**

## Out of Scope

The project does not aim to:

- Profile individual business owners.
- Identify specific owners who may retire.
- Predict that a particular named business will close.
- Provide individual business-sale advice.
- Broker business sales or acquisitions.
- Make conclusions that are not supported by available evidence.

---

# Data Sources

Week 2 data-source research identified the following main source areas:

- Niagara Employment Inventory (NEI)
- Niagara Region Open Data
- Statistics Canada Canadian Business Counts
- Statistics Canada Business Dynamics
- Statistics Canada Census and demographic data
- CFIB succession-related research
- Niagara Region economic and labour-market sources
- Other relevant and properly licensed public datasets

The sources have been classified into:

### Priority A — Core Acquisition

Datasets selected for Week 3 download and audit.

### Priority B — Supporting / Conditional

Sources retained for context, benchmarking or additional analysis where required.

### Priority C — Access Pending

Potentially valuable sources where access or suitability still needs further investigation.

One important Week 2 finding is that the public sources identified so far do **not** provide a confirmed Niagara business-level dataset containing all the direct succession variables we would ideally want.

Examples include:

- owner age;
- retirement intention;
- intended exit timeline;
- identified successor;
- succession-plan status; and
- confirmed succession-related reason for closure.

This data gap is documented and will not be hidden by treating proxy variables as direct evidence.

Datasets used in the final analysis will be documented with information such as:

- source;
- dataset name;
- year or version;
- geographic coverage;
- important variables;
- licence;
- data limitations;
- cleaning performed; and
- transformations performed.

---

# Project Methodology

The project follows the general workflow below:

**Research Question**

↓

**Data Source Research & Evaluation**

↓

**Data Collection & Audit**

↓

**Data Cleaning**

↓

**Data Integration**

↓

**Aggregated Analytical Data Layer**

↓

**Exploratory Data Analysis**

↓

**Feature Engineering**

↓

**Forecasting / Predictive Modelling**

↓

**Model Evaluation & Uncertainty Assessment**

↓

**Succession-Risk Forecast**

↓

**Businesses & Jobs Exposure Analysis**

↓

**Local-Economy Impact Analysis**

↓

**Government & Private-Sector Recommendations**

↓

**Succession Playbook**

↓

**Infographics & Interactive Visualisation**

↓

**Research Report**

↓

**Reproducibility & Final Quality Assurance**

### Current Methodological Position

Week 2 completed the **Data Source Research & Evaluation** stage.

Week 3 moves into **Data Collection & Audit**.

The team will inspect the actual data before cleaning, integrating, engineering features, or selecting a final modelling approach.

---

# Repository Structure

> **Note:** The structure below represents the target repository layout for the project. Folders and files are created and populated gradually as the relevant project phases begin.

```text
niagara-succession-signal/
│
├── data/
│   ├── raw/
│   │   └── DATA_SOURCES.md
│   ├── interim/
│   └── processed/
│
├── notebooks/
│   ├── 01_data_collection/
│   ├── 02_data_cleaning/
│   ├── 03_eda/
│   ├── 04_feature_engineering/
│   ├── 05_modelling/
│   ├── 06_evaluation/
│   └── 07_local_economy_impact/
│
├── src/
│
├── scripts/
│
├── models/
│
├── dashboard/
│
├── visuals/
│
├── reports/
│   ├── research_report/
│   ├── succession_playbook/
│   ├── remediation_report/
│   ├── figures/
│   ├── tables/
│   └── presentations/
│
├── innovation/
│   └── policy_brief/
│
├── docs/
│   ├── DATA_ACQUISITION_PLAN.md
│   ├── DATA_AUDIT_TEMPLATE.md
│   ├── DATA_DICTIONARY.md
│   ├── WEEK_2_CONTRIBUTIONS.md
│   ├── WEEK_2_HANDOVER.md
│   └── MEETING_NOTES/
│
├── references/
│   └── DATA_LICENSES.md
│
├── README.md
├── CONTRIBUTING.md
├── RISK_REGISTER.md
├── DECISIONS.md
├── ASSUMPTIONS.md
├── REFERENCES.md
└── requirements.txt
```

---

# Getting Started

This section explains how team members can download a complete copy of the Niagara Succession Signal repository to their computers.

## Step 1 — Install Git

You need **Git** on your computer before you can clone the project.

Open your terminal and run:

```bash
git --version
```

If Git is installed, you should see a Git version number.

---

## Step 2 — Open VS Code

Open **Visual Studio Code**.

Then open the terminal by selecting:

**Terminal → New Terminal**

---

## Step 3 — Go to Where You Want to Save the Project

For example, if you want to save the project inside your Documents folder, run:

```bash
cd Documents
```

---

## Step 4 — Clone the Repository

Run:

```bash
git clone https://github.com/joyce-ai4health/niagara-succession-signal.git
```

This downloads a complete copy of the repository from GitHub to your computer.

### Important

You only need to clone the repository **once**.

Do not clone the repository every time you want to work on the project.

After cloning it once, use `git pull` to get new changes.

---

## Step 5 — Enter the Project Folder

Run:

```bash
cd niagara-succession-signal
```

---

## Step 6 — Open the Project in VS Code

Run:

```bash
code .
```

The `.` means:

> Open the current folder in VS Code.

You should now see the Niagara Succession Signal folders and files inside VS Code.

---

## Step 7 — Check That Git Is Connected

Run:

```bash
git status
```

Git should show information about the repository and your current branch.

---

# Working on an Assigned Task

After cloning the repository, follow these steps whenever you are assigned a new task.

## Step 1 — Go to the Project Folder

```bash
cd niagara-succession-signal
```

## Step 2 — Go to the Main Branch

```bash
git switch main
```

## Step 3 — Get the Latest Version

Before starting any new task:

```bash
git pull origin main
```

## Step 4 — Create a Branch for Your Task

### Do not work directly on `main`.

Use:

```bash
git switch -c your-branch-name
```

Example:

```bash
git switch -c data-source-research
```

Your branch name should be short and related to your assigned task.

## Step 5 — Check Your Current Branch

```bash
git branch
```

The branch with `*` beside it is your current branch.

Make sure you are not on `main` before changing project files.

## Step 6 — Do Your Assigned Work

While working:

- Do not delete another person's work.
- Do not rename shared folders without team agreement.
- Do not move shared project folders without team agreement.
- Do not work directly on `main`.
- Do not upload unrelated files.
- Keep your work inside the correct project folder.
- Ask for help early if you are blocked.

## Step 7 — Check Your Changes

```bash
git status
```

Review the files you have added, changed or deleted.

## Step 8 — Add Your Changes

```bash
git add .
```

Then check:

```bash
git status
```

Make sure you are only adding files related to your task.

## Step 9 — Commit Your Work

Example:

```bash
git commit -m "Add data source research"
```

Use a short message that clearly explains what changed.

## Step 10 — Push Your Branch

For the first push:

```bash
git push -u origin your-branch-name
```

Later pushes from the same branch can normally use:

```bash
git push
```

## Step 11 — Open a Pull Request

After pushing:

1. Open the repository on GitHub.
2. Click **Compare & pull request** if shown.
3. Confirm that your branch is being compared with `main`.
4. Give the Pull Request a clear title.
5. Briefly explain what you changed.
6. Submit it for review.

### Example Pull Request

**Title:**

```text
Add Week 2 data source research
```

**Description:**

```text
## What I Did

- Researched assigned project data sources.
- Added relevant dataset information.
- Documented important limitations.

## Status

Ready for review.
```

---

# If Corrections Are Requested

Stay on the same branch.

Make the requested corrections, then:

```bash
git status
git add .
git commit -m "Address review feedback"
git push
```

The existing Pull Request will update automatically.

---

# After Your Pull Request Is Merged

Return to `main`:

```bash
git switch main
```

Then update it:

```bash
git pull origin main
```

---

# Starting Your Next Task

Before starting another task:

```bash
git switch main
git pull origin main
git switch -c new-branch-name
```

Do not continue using an old branch for an unrelated new task.

---

# Important Git Rules

1. **Do not work directly on `main`.**
2. **Pull the latest `main` before creating a new task branch.**
3. **Do not delete or overwrite another person's work.**
4. **Use clear commit messages.**
5. **Raise missing-data, access, Git or technical problems early.**

---

# Git Quick Reference

```bash
# Clone once
git clone https://github.com/joyce-ai4health/niagara-succession-signal.git

# Enter project
cd niagara-succession-signal

# Open in VS Code
code .

# Check repository
git status

# Update main
git switch main
git pull origin main

# Create task branch
git switch -c your-branch-name

# Check branch
git branch

# Add changes
git add .

# Commit
git commit -m "Describe what you changed"

# First push
git push -u origin your-branch-name

# Later pushes
git push
```

---

# Required Deliverables

The project is organised around the official Founder Challenge deliverables.

| No. | Deliverable | Planned Repository Location |
|---|---|---|
| **4.1** | Aggregated Data Layer | `data/processed/` |
| **4.2** | Research Report | `reports/research_report/` |
| **4.3** | Infographics & Visual Assets | `visuals/` |
| **4.4** | Graphs & Exploratory Visuals | `notebooks/03_eda/`, `visuals/` |
| **4.5** | Predictive Model for Forecasting Business Closures | `notebooks/04_feature_engineering/`, `notebooks/05_modelling/`, `notebooks/06_evaluation/`, `models/` |
| **4.6** | Business Acquisition / Succession Playbook | `reports/succession_playbook/` |
| **4.7** | Local-Economy Impact Analysis | `notebooks/07_local_economy_impact/`, `reports/` |
| **4.8** | Government & Private-Sector Remediation Report | `reports/remediation_report/` |
| **4.9** | Nice-to-Have Extensions | `innovation/`, `dashboard/` |

## 4.1 — Aggregated Data Layer

The project will create a cleaned, documented and appropriately aggregated analytical data layer from the validated project sources.

The final structure will depend on:

- available geography;
- industry/NAICS compatibility;
- business-size definitions;
- reference periods;
- available joining keys; and
- findings from the data audit.

Datasets will only be combined where the relationship between them is methodologically valid.

---

## 4.2 — Research Report

The final research report will bring together:

- research problem;
- data sources;
- methodology;
- assumptions;
- limitations;
- exploratory analysis;
- model development and evaluation;
- findings;
- local-economy implications;
- recommendations; and
- conclusions.

Important claims should be traceable to either our analysis or a clearly identified source.

---

## 4.3 — Infographics & Visual Assets

The project will produce visual materials that communicate important findings to a non-technical audience.

Final topics will depend on the analysis but may include:

- sector exposure;
- municipal differences;
- business-size patterns;
- business and jobs exposure;
- succession-risk patterns; and
- major project findings.

---

## 4.4 — Graphs & Exploratory Visuals

Exploratory analysis will examine the structure, quality and patterns within the collected data.

Possible visual analysis may include:

- distributions;
- trends;
- sector comparisons;
- municipality comparisons;
- business-size patterns;
- business-entry and exit patterns;
- relationships between variables; and
- model diagnostics.

Final visuals will be based on what the audited data can legitimately support.

---

## 4.5 — Predictive Model for Forecasting Business Closures

The challenge requires a predictive model for forecasting business closures.

### Current Modelling Position

At the end of Week 2, the final:

- modelling unit;
- target variable;
- forecast horizon;
- feature set;
- modelling method; and
- connection between general business closure and succession-related closure

have **not yet been finalised**.

This is intentional.

The modelling approach will be selected after the team has collected and audited the relevant datasets.

### Important Rule

A business exit or closure will **not automatically be classified as a succession-related closure**.

The final model documentation should clearly explain:

- target definition;
- modelling unit;
- forecast horizon;
- features;
- assumptions;
- baseline;
- validation method;
- evaluation metrics;
- uncertainty;
- limitations; and
- interpretation of predictions.

---

## 4.6 — Business Acquisition / Succession Playbook

The project will develop a general playbook that translates the research findings into practical succession and acquisition considerations.

The playbook may draw on:

- analytical findings;
- sector patterns;
- municipality patterns;
- business-size patterns;
- succession research; and
- relevant supporting literature.

The playbook will provide a general framework and will not provide individual advice about identifiable business owners.

---

## 4.7 — Local-Economy Impact Analysis

The project will examine what succession-related business exposure could mean for Niagara's local economy.

Possible areas include:

- businesses potentially exposed;
- jobs potentially exposed;
- sector concentration;
- municipal vulnerability;
- wider economic effects; and
- areas where early intervention may be useful.

Final impact measures will depend on the available data and analytical results.

---

## 4.8 — Government & Private-Sector Remediation Report

The project will translate its findings into evidence-based recommendations.

Recommendations will distinguish between relevant stakeholder groups, including:

### Government / Economic-Development Stakeholders

Possible areas may include:

- succession awareness;
- business-owner support;
- local economic-development planning;
- succession preparedness;
- data collection; and
- targeted intervention.

### Private-Sector Stakeholders

Possible stakeholders may include:

- prospective buyers;
- lenders;
- brokers;
- chambers;
- business associations; and
- other organisations involved in business transfer and continuity.

Final recommendations must be connected to findings from the project.

---

## 4.9 — Nice-to-Have Extensions

The challenge identifies optional innovation extensions.

Possible extensions include:

- interactive dashboard or web tool;
- succession-readiness index or scoring method;
- buyer-business matching approach using aggregate or synthetic data;
- comparative case study applying the method to a Nigerian or other African regional economy;
- policy-brief version of the remediation report; and
- reproducibility / replication package.

### Current Decision

The team will not attempt every extension simply because it is available.

Extensions will be selected based on:

- usefulness;
- data availability;
- technical feasibility;
- available time;
- quality of the core project; and
- potential innovation value.

Completion of the core challenge work remains the priority.

---

# Deliverable Dependency

The deliverables are connected.

A simplified project flow is:

**Data Sources**

↓

**4.1 Aggregated Data Layer**

↓

**4.4 Graphs & Exploratory Visuals**

↓

**4.5 Predictive Model**

↓

**4.7 Local-Economy Impact Analysis**

↓

**4.6 Succession Playbook + 4.8 Remediation Report**

↓

**4.2 Research Report + 4.3 Infographics & Visual Assets**

↓

**4.9 Selected Innovation Extensions**

The quality of the later deliverables therefore depends heavily on the quality, documentation and validity of the data foundation.

---

# Project Roadmap

The project runs from September 2026 to January 2027, with the internal goal of completing the project before the final challenge submission period.

The roadmap moves from understanding the problem to building the data foundation, analysing the evidence, modelling, translating findings into action, communicating results and completing final quality assurance.

## Phase 1 — Understand & Plan

### Weeks 1–2

Focus:

- Understand the challenge.
- Understand the required deliverables.
- Define the research problem.
- Define research questions.
- Define objectives and scope.
- Research potential data sources.
- Evaluate source usefulness and limitations.
- Identify important data gaps.
- Establish data-acquisition priorities.
- Prepare for data collection and audit.

### Week 2 Status

**COMPLETE**

Week 2 data-source research and planning have been completed.

---

## Phase 2 — Build the Data Foundation

Focus:

- Data collection
- Data audit
- Data cleaning
- Data integration
- Data documentation
- Aggregated analytical data layer

### Week 3 — Data Collection & Audit

Week 3 will begin by collecting and auditing the approved Priority A datasets.

The team will:

1. Download approved Priority A datasets.
2. Preserve original raw files.
3. Record each source in `data/raw/DATA_SOURCES.md`.
4. Preserve official metadata.
5. Audit every Priority A dataset.
6. Confirm actual variables and definitions.
7. Check missing values.
8. Check duplicate records.
9. Confirm geographic coverage.
10. Confirm reference periods.
11. Check NAICS and industry definitions.
12. Check business-size definitions.
13. Identify possible joining keys.
14. Check for direct succession-related variables.
15. Investigate access to succession-specific NEI information.
16. Update the Risk Register where necessary.

### Important

Week 3 is an **audit stage**, not a cleaning stage.

The process is:

**Download → Preserve Raw File → Record Source → Audit → Review → Cleaning**

We will first understand what is actually in the data before deciding how to clean or transform it.

---

## Later Phases

Later project phases will cover:

- data cleaning;
- exploratory data analysis;
- problem refinement and KPI development;
- modelling planning;
- predictive modelling;
- model evaluation;
- feature engineering;
- final modelling;
- local-economy impact analysis;
- recommendations;
- succession playbook;
- research report;
- visual communication;
- innovation extensions where appropriate; and
- final quality assurance and submission preparation.

Detailed weekly assignments will continue to be documented as the project progresses.

---

# Team

The Niagara Succession Signal team consists of:

- Theophilus
- Damilare
- Precious
- Lucky
- Oluwatosin
- Emmanuella
- Ruth
- Stephen
- Joyce

Team members collaborate across the different phases of the project, with weekly tasks assigned according to the project roadmap and the work required for each phase.

---

# Collaboration Workflow

The team uses GitHub for project management, version control, review and documentation.

Our standard workflow is:

**Issue → Branch → Work → Commit → Push → Pull Request → Review → Merge**

Team members should work from assigned tasks and use separate branches rather than making unrelated changes directly on `main`.

---

# Definition of Done

## Finished ≠ Done

Completing work on a local computer does not automatically mean the task is done.

A task is considered **DONE** only when it has been:

**Completed → Documented → Pushed to GitHub → Reviewed → Corrections Resolved → Approved**

Where applicable, the work should also be reproducible by another team member.

---

# Ethics and Responsible Data Use

The team is committed to responsible data use.

We will:

- Use properly licensed or authorised data.
- Clearly identify data and research sources.
- Never fabricate missing information.
- Document missing values.
- Document important assumptions.
- Document cleaning and transformation decisions.
- Protect privacy.
- Avoid identifying individual business owners unnecessarily.
- Avoid unsupported claims.
- Report uncertainty honestly.
- Avoid overstating model performance.
- Clearly explain important data limitations.
- Clearly distinguish evidence from assumptions.
- Clearly distinguish direct variables from proxies and contextual variables.
- Avoid treating business closure as succession failure without supporting evidence.

---

# Reproducibility

The project should be understandable and reproducible by another analyst.

Where applicable, we will document:

- data sources;
- source links;
- dataset versions and years;
- geographic coverage;
- licences;
- raw filenames;
- data transformations;
- cleaning decisions;
- missing-value handling;
- assumptions;
- feature engineering;
- model configurations;
- validation procedures;
- random seeds;
- software dependencies;
- analytical limitations; and
- output-generation procedures.

The goal is for another analyst to understand:

> **What we did, why we did it, what data we used, where that data came from, and how our results were produced.**

## Data Traceability

Where applicable, analytical data should be traceable through:

**Original Source → Raw File → Interim/Cleaned Data → Processed/Aggregated Data → Analysis/Model → Final Output**

---

# Project Documentation

Project documentation is maintained throughout the repository.

## Core Governance Documents

- `CONTRIBUTING.md` — collaboration and contribution guidelines.
- `RISK_REGISTER.md` — identified project risks and mitigation actions.
- `DECISIONS.md` — important project and analytical decisions.
- `ASSUMPTIONS.md` — assumptions requiring documentation and validation.
- `REFERENCES.md` — datasets, research papers, reports and supporting sources.

## Data Documentation

- `docs/DATA_ACQUISITION_PLAN.md` — approved data-source priorities, acquisition plan and source-to-deliverable mapping.
- `docs/DATA_DICTIONARY.md` — structure for documenting the actual variables used in the project.
- `docs/DATA_AUDIT_TEMPLATE.md` — standard template for auditing datasets during Week 3.
- `data/raw/DATA_SOURCES.md` — provenance log for raw datasets collected by the team.
- `references/DATA_LICENSES.md` — data licensing and usage information.

## Week 2 Documentation

- `docs/WEEK_2_CONTRIBUTIONS.md` — record of the team's Week 2 research contributions and findings.
- `docs/WEEK_2_HANDOVER.md` — Week 2 completion record and handover into Week 3.

## Meeting Documentation

- `docs/MEETING_NOTES/` — records of project meetings, decisions and agreed actions.

These documents will continue to be updated as the project progresses.

---

# Week 2 Key Findings

Week 2 data-source research produced several important findings.

### 1. Niagara-specific business data is available

The Consolidated Niagara Employment Inventory provides an important local source for understanding Niagara's business structure.

### 2. Statistics Canada provides useful supporting data

Selected Statistics Canada sources can support analysis of:

- business counts;
- business entries and exits;
- business size;
- demographic patterns; and
- self-employment.

### 3. Succession research provides useful wider context

CFIB and other supporting research can help explain the broader Canadian succession problem.

However, national or provincial findings will not automatically be presented as Niagara-specific findings.

### 4. Direct Niagara succession information remains limited

The public sources identified so far do not provide a confirmed business-level dataset containing all the direct succession variables we would ideally want.

This is an important project limitation.

### 5. Proxy variables must be used carefully

Variables such as:

- population age;
- self-employment;
- business age;
- business exits; and
- employee size

may be useful indicators or contextual information, but they will not automatically be described as direct evidence of succession risk.

---

# Current Project Status

**Current Phase:** Phase 2 — Build the Data Foundation

**Week 1:** Complete

**Week 2:** Complete — Data Source Research, Evaluation & Planning

**Week 3:** Complete — Data Collection, Audit & Integration Readiness

**Next:** Week 4 — Data Cleaning

**Current Status:** In Progress

**Project Start:** September 2026

**Internal Completion Target:** January 31, 2027

### Week 3 Completion

Week 3 focused on acquiring, preserving, documenting, auditing and assessing the integration readiness of the project's priority data sources.

The completed Week 3 work includes:

- [x] Niagara Employment Inventory (NEI) acquired, preserved and audited
- [x] Canadian Business Counts audited
- [x] Business Dynamics / Business Entries and Exits audited
- [x] Census and demographic datasets audited
- [x] Succession-specific and supporting sources audited
- [x] Dataset structures, dimensions and relevant variables reviewed
- [x] Missing values and duplicate records assessed
- [x] Geographic and time coverage documented
- [x] Industry / NAICS compatibility assessed
- [x] Business-size information reviewed
- [x] Potential joining keys identified
- [x] Direct succession-variable availability assessed
- [x] Dataset strengths and limitations documented
- [x] Keep / conditional-use decisions recorded
- [x] Cross-source compatibility assessed
- [x] Integration readiness matrix completed
- [x] Integration decisions documented
- [x] Relevant risks recorded
- [x] Week 3 audits reviewed

### Week 3 Integration Position

The Week 3 audit confirmed that the project does not have a direct business-level label identifying succession-related closure in Niagara.

The datasets therefore have different analytical roles:

- **NEI** provides the core Niagara business-level foundation but requires transformation before later integration.
- **Canadian Business Counts** provides aggregate business-count and size context and can be used with appropriate standardization.
- **Business Dynamics** provides aggregate evidence on business entry and exit patterns but does not identify why a business exited.
- **Census and demographic data** provide supporting demographic, self-employment and industry context but must not be treated as direct business-owner succession evidence.
- **Succession-specific sources** provide direct evidence on succession intentions and related measures at broader geographic levels, but they do not provide an individual Niagara succession-closure label.

Cross-source integration must therefore respect differences in geography, time coverage, NAICS classification, business-size definitions and level of aggregation.

No datasets were merged during Week 3.

### Week 4 Readiness

With Week 3 complete, the project is ready to proceed to **Week 4 — Data Cleaning**.

Week 4 will focus on preparing the approved datasets for later analysis while preserving the original raw files and maintaining clear data traceability.


---

# Acknowledgement

This project is being developed as part of the **DataraFlow Internship — Cohort 2 Founder Challenge 2026**.

---

# Niagara Succession Signal

**Data → Evidence → Insight → Action**
