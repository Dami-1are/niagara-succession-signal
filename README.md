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

The project will investigate and document relevant data sources including:

- Canadian Business Counts
- Statistics Canada business-dynamics data
- Niagara Employment Inventory (NEI)
- Statistics Canada Census and demographic data
- CFIB succession-related research
- Niagara Region open-data and economic-development sources
- Other relevant and properly licensed public datasets

Datasets used in the final analysis should be documented with information such as:

- Source
- Dataset name
- Year or version
- Geographic coverage
- Important variables
- Data limitations
- Cleaning performed
- Transformations performed

---

# Project Methodology

The project follows the general workflow below:

**Research Question**

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

---

# Repository Structure

> **Note:** The structure below represents the target repository layout for the project. Folders and files are created and populated gradually as the relevant project phases begin.

```text
niagara-succession-signal/
│
├── data/
│   ├── raw/
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
│   └── MEETING_NOTES/
│
├── README.md
├── CONTRIBUTING.md
├── RISK_REGISTER.md
├── DECISIONS.md
├── ASSUMPTIONS.md
├── DATA_DICTIONARY.md
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

After cloning it once, you will use `git pull` to get new changes.

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

If the project is not already open, go to the project folder:

```bash
cd niagara-succession-signal
```

---

## Step 2 — Go to the Main Branch

Run:

```bash
git switch main
```

---

## Step 3 — Get the Latest Version

Before starting any new task, always update your local copy.

Run:

```bash
git pull origin main
```

This brings the latest approved changes from GitHub to your computer.

---

## Step 4 — Create a Branch for Your Task

### Do not work directly on `main`.

Create a separate branch for your assigned task.

Use:

```bash
git switch -c your-branch-name
```

For example:

```bash
git switch -c data-source-research
```

Another example:

```bash
git switch -c update-assumptions
```

Your branch name should be short and related to the task you are working on.

---

## Step 5 — Check Your Current Branch

Run:

```bash
git branch
```

You may see something similar to:

```text
* data-source-research
  main
```

The branch with the `*` beside it is the branch you are currently using.

Before changing project files, make sure you are working on your task branch and not `main`.

---

## Step 6 — Do Your Assigned Work

Complete your assigned task in the correct project folder.

While working:

- Do not delete another person's work.
- Do not rename shared folders without team agreement.
- Do not move project folders without team agreement.
- Do not work directly on `main`.
- Do not upload unrelated files.
- Keep your work inside the correct project folder.
- Ask for help early if you are blocked.

---

## Step 7 — Check Your Changes

When you finish your work, run:

```bash
git status
```

This shows files that have been:

- Added
- Changed
- Deleted

Check the list before continuing.

---

## Step 8 — Add Your Changes

If everything is correct, run:

```bash
git add .
```

Then check again:

```bash
git status
```

Make sure you are only adding files that belong to your task.

---

## Step 9 — Commit Your Work

Commit your work with a short message explaining what you completed.

For example:

```bash
git commit -m "Add data source research"
```

Another example:

```bash
git commit -m "Update project assumptions"
```

Another example:

```bash
git commit -m "Add Week 1 meeting notes"
```

### Good Commit Messages

A good commit message explains what changed.

Examples:

```text
Add data source research
Update project assumptions
Add business counts dataset
Document data limitations
Fix data dictionary definitions
```

Avoid unclear messages such as:

```text
update
work
done
changes
my work
```

---

## Step 10 — Push Your Branch to GitHub

For the first push of your branch, run:

```bash
git push -u origin your-branch-name
```

For example:

```bash
git push -u origin data-source-research
```

After the first push, later changes from the same branch can normally be pushed using:

```bash
git push
```

---

## Step 11 — Open a Pull Request

After pushing your branch:

1. Open the Niagara Succession Signal repository on GitHub.
2. GitHub may show a **Compare & pull request** button.
3. Click it.
4. Make sure your branch is being compared with `main`.
5. Give the Pull Request a clear title.
6. Briefly explain what you changed.
7. Submit the Pull Request for review.

### Example Pull Request Title

```text
Add Week 2 data source research
```

### Example Pull Request Description

```text
## What I Did

- Researched possible project data sources.
- Added relevant dataset links.
- Documented the available years.
- Added notes about possible data limitations.

## Files Changed

- REFERENCES.md
- data source documentation

## Status

Ready for review.
```

---

# If Corrections Are Requested

If someone reviews your Pull Request and asks you to make corrections, you do **not** need to create another branch.

Stay on the same branch.

Make the requested corrections.

Then run:

```bash
git status
```

Add the corrected files:

```bash
git add .
```

Commit the corrections:

```bash
git commit -m "Address review feedback"
```

Then push:

```bash
git push
```

Your existing Pull Request will automatically update with the new changes.

---

# After Your Pull Request Is Merged

After your work has been reviewed, approved, and merged into `main`, update your computer.

First go back to `main`:

```bash
git switch main
```

Then run:

```bash
git pull origin main
```

Your local `main` branch will now contain the latest approved work.

---

# Starting Your Next Task

Before starting another task:

```bash
git switch main
```

Then:

```bash
git pull origin main
```

Then create a **new branch** for the new task:

```bash
git switch -c new-branch-name
```

Do not continue using an old branch for an unrelated new task.

---

# Important Git Rules

## Rule 1 — Do Not Work Directly on Main

The `main` branch should contain reviewed and approved project work.

Always create a branch for your task.

---

## Rule 2 — Pull Before Starting New Work

Always run:

```bash
git switch main
```

followed by:

```bash
git pull origin main
```

before creating a new task branch.

This helps you start from the latest version of the project.

---

## Rule 3 — Do Not Delete or Overwrite Other People's Work

If you notice a conflict or something you do not understand, ask before deleting or replacing files.

---

## Rule 4 — Use Clear Commit Messages

Your commit message should explain what you changed.

---

## Rule 5 — Raise Problems Early

If you cannot complete a task because of:

- Missing data
- Git problems
- Access problems
- Technical problems
- Unclear instructions
- Conflicting files

inform the team early.

Do not wait until the deadline.

---

# Git Quick Reference

### Clone the project for the first time

```bash
git clone https://github.com/joyce-ai4health/niagara-succession-signal.git
```

### Enter the project

```bash
cd niagara-succession-signal
```

### Open it in VS Code

```bash
code .
```

### Check the project

```bash
git status
```

### Go to main

```bash
git switch main
```

### Get the latest changes

```bash
git pull origin main
```

### Create a task branch

```bash
git switch -c your-branch-name
```

### Check your branch

```bash
git branch
```

### Check your changes

```bash
git status
```

### Add your changes

```bash
git add .
```

### Commit your changes

```bash
git commit -m "Describe what you changed"
```

### Push your branch for the first time

```bash
git push -u origin your-branch-name
```

### Push later changes

```bash
git push
```

---

# Required Deliverables

| No. | Deliverable | Repository Location |
|---|---|---|
| **4.1** | Aggregated Data Layer | `data/processed/` |
| **4.2** | Research Report | `reports/research_report/` |
| **4.3** | Infographics & Visual Assets | `visuals/` |
| **4.4** | Graphs & Exploratory Visuals | `notebooks/03_eda/`, `visuals/` |
| **4.5** | Predictive / Forecasting Model | `notebooks/04_feature_engineering/`, `notebooks/05_modelling/`, `notebooks/06_evaluation/`, `models/` |
| **4.6** | Business Acquisition / Succession Playbook | `reports/succession_playbook/` |
| **4.7** | Local-Economy Impact Analysis | `notebooks/07_local_economy_impact/` |
| **4.8** | Government & Private-Sector Remediation Report | `reports/remediation_report/` |
| **4.9** | Innovation Extensions | `innovation/`, `dashboard/` |

---

# Project Roadmap

The project is organised into seven phases from September 2026 to January 2027.

| Phase | Period | Focus |
|---|---|---|
| **Phase 1** | Sep 14 – Oct 4 | Understand & Plan |
| **Phase 2** | Oct 5 – Oct 25 | Build the Data Foundation |
| **Phase 3** | Oct 26 – Nov 15 | Explore & Discover |
| **Phase 4** | Nov 16 – Dec 6 | Forecasting & Modelling |
| **Phase 5** | Dec 7 – Dec 27 | From Prediction to Action |
| **Phase 6** | Dec 28 – Jan 17 | Tell the Story |
| **Phase 7** | Jan 18 – Jan 31 | Quality Control & Final Package |

## Current Phase

### Phase 1 — Understand & Plan

The current focus is:

- Understanding the challenge
- Defining the research problem
- Agreeing on research questions
- Defining objectives
- Defining project scope
- Documenting assumptions
- Understanding required deliverables
- Preparing for data-source research

---

# Team

The Niagara Succession Signal team consists of:

- Theophilus
- OHONBA
- Damilare
- Precious
- Mano
- Lucky
- Oluwatosin
- Emmanuella
- Ruth
- Stephen
- Joyce

Team members collaborate across the different phases of the project, with weekly tasks assigned according to the project roadmap and the work required for each phase.

---

# Collaboration Workflow

The team uses GitHub for project management, version control, review, and documentation.

Our standard workflow is:

**Issue → Branch → Work → Commit → Push → Pull Request → Review → Merge**

# Definition of Done

## Finished ≠ Done

Completing the work on your computer does not automatically mean the task is done.

A task is considered **DONE** only when it has been:

**Completed → Documented → Pushed to GitHub → Reviewed → Corrections Resolved → Approved**

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

---

# Reproducibility

The project should be understandable and reproducible by another analyst.

Where applicable, we will document:

- Data sources
- Dataset versions and years
- Data transformations
- Cleaning decisions
- Missing-value handling
- Assumptions
- Feature engineering
- Model configurations
- Validation procedures
- Random seeds
- Software dependencies
- Analytical limitations
- Output-generation procedures

The goal is for another analyst to understand:

> **What we did, why we did it, what data we used, and how our results were produced.**

---

# Project Documentation

Additional project documentation is maintained throughout the repository:

- `CONTRIBUTING.md` — collaboration and contribution guidelines.
- `RISK_REGISTER.md` — identified project risks and mitigation actions.
- `DECISIONS.md` — important project and analytical decisions.
- `ASSUMPTIONS.md` — assumptions requiring documentation and validation.
- `DATA_DICTIONARY.md` — definitions and descriptions of analytical variables.
- `REFERENCES.md` — datasets, research papers, reports, and supporting sources.
- `docs/MEETING_NOTES/` — records of project meetings, decisions, and agreed actions.

---

# Project Status

**Current Phase:** Phase 1 — Understand & Plan

**Current Status:** In Progress

**Project Start:** September 2026

**Internal Completion Target:** January 2027

---

# Acknowledgement

This project is being developed as part of the **DataraFlow Internship — Cohort 2**.

---

# Niagara Succession Signal

**Data → Evidence → Insight → Action**
