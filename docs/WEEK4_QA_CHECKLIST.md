# Week 4 QA Checklist (in progress)

Reviewer: Joyce (Team Lead) | Branch: `week4-final-qa` | Started: 2026-10-12
Status values: Approved / Approved after correction / Needs correction / Pending.
"Approved after correction" means data checks passed and only the listed corrections remain.

## Summary

| Assignee | Dataset | Issue # | PR # | Raw protected | Reproducible | Status |
|---|---|---|---|---|---|---|
| Stephen | NEI cleaning | #15 | #24, #40 | Yes | Verified (re-run gives identical content) | Approved after correction |
| Lucky | Canadian Business Counts | not yet recorded | #29 | Yes | Verified (both CSVs identical on re-run) | Approved after correction |
| Damilare | Business Dynamics | not yet recorded | #26 | Yes | Verified (both CSVs identical on re-run) | Approved after correction |
| Precious | Census Age | not yet recorded | #28 | Yes (no modification found) | Verified (raw file restored, notebook re-run gives identical CSV) | Approved after correction |
| Ruth | Self-Employment | not yet recorded | #30 | Yes | Not re-run; raw file is excluded only locally | Approved after correction |
| Oluwatosin | StatCan succession (1196-1199) | #20 | #27 | Yes | Not re-run | Approved (data checks) |
| Emmanuella | CFIB evidence | not yet recorded | #25 | Yes | n/a (manual extraction, pages recorded) | Approved after correction |
| Theophilus | Documentation | not yet recorded | #39 | n/a | n/a | Approved after correction |

## Step 2: Workflow
PASS. Only 4 non-merge commits on `main` since 2026-09-25, all by Joyce (README, RISK_REGISTER, WEEK_2_CONTRIBUTIONS, raw data via Git LFS). No contributor cleaning work was done on `main`. PR #26 was merged while "Changes requested" still showed (fixes are on `main`). PR #40 and PR #30 were authored by the QA reviewer.

## Step 3: Raw data protection
- Git history shows no raw data file modified. Only `data/raw/DATA_SOURCES.md` and `data/raw/README.md` were edited, in Week 3.
- `data/raw/statcan/census/98100022.csv` was untracked in commit `373db9e` (2026-10-03, large file). `DATA_SOURCES.md` line 179 still lists the old location.

## Findings by assignee

### Stephen: NEI
- 98,065 rows x 22 columns; 0 rows removed; no succession-related columns. Added flags: `postal_code_status`, `nei_id_conflict` (278 True).
- Corrections: no standalone cleaning report; define `nei_id_conflict` in plain language; notebook saved with no outputs; PR #40 changed the cleaned file after PR #24 approval with no independent review.

### Lucky: Canadian Business Counts
- 10,462 x 14; 12 municipalities by DGUID; CMA in a separate file; size bands sum to the total in 2,933 of 2,933 pairs; no zeros or blanks; `ref_date` 2026-01 discrepancy documented.
- Corrections: notebook template writes the wrong notebook path into the report; notebook in `scripts/` and report in `reports/` (non-standard folders).

### Damilare: Business Dynamics
- Industry 2,484 x 18; firm size 828 x 15; Ontario only; 2001-2023; 36 `..` and 196 `x` kept missing; report matches output; all four PR #26 review requests resolved.
- Corrections: outputs are in `data/processed/` while others are in `data/interim/`. Not yet text-checked: NAICS version note, overlapping firm-size note, exits not renamed as succession.

### Precious: Census Age
- 3,328 rows = 13 geographies x 128 age labels x 2 census years. `Census year (2)` kept; 0 whitespace issues; 0 duplicates; no succession columns. Zeros look like genuine rounded zeros; Men+ plus Women+ differs from Total in 1,565 rows (random rounding preserved). Checked on the cleaned file only.
- Corrections: files at repo root; notebook reads `data/raw/98100022.csv`, which does not exist; raw path inconsistent across documents; re-run needed once the raw file is restored; confirm report covers overlapping ages and rounding.

### Ruth: Self-Employment
- 125,714 rows before and after; one Niagara CD DGUID; 2021; 25% sample documented; two self-employed measures separated; report states self-employment is not business ownership. Raw STATUS and SYMBOL are empty, so dropping them lost nothing.
- Corrections: raw file `9810059201_databaseLoadingData.csv` is excluded only locally; document the download source; notebook not re-run.

### Oluwatosin: StatCan succession
- Four separate Ontario-only files; percentages preserved; every missing VALUE has status F or `..`; table 1199 nulls (344) match status codes; zeros are real values; quality ratings kept. Not re-run.

### Emmanuella: CFIB
- 13 rows; Canada only; source pages recorded; all four evidence types present; limitations in notes; PDF unchanged.
- Corrections: spot-check 2 or 3 values against the PDF; output is in `data/processed/` (folder decision).

### Theophilus: Documentation
- Statistics Canada, Business Dynamics and CFIB outputs are documented; Census raw-file problems are recorded.
- Corrections: add `nei_id_conflict` and `postal_code_status` to the dictionary and Week 4 document; add the two Census raw files to the dictionary.

## Still open
- Issue numbers and PRs #31-#38 to record from GitHub.
- `data/processed/README.md` calls the folder "analysis-ready" (Step 4).
- Steps 13-19 cross-checks are summarised in the handover.
- Project status update only after the corrections above are resolved.
---

## Corrections update (2026-10-13, branch week4-corrections)

Done:
- Precious: Census Age notebook, report and CSV moved to notebooks/02_data_cleaning/, docs/data_audits/CENSUS_AGE_CLEANING_REPORT.md and data/interim/. Notebook paths fixed. Raw file restored locally and added to .gitignore. Re-run produced an identical CSV. Report documents overlapping ages, random rounding and suppression handling.
- Stephen: docs/data_audits/NEI_CLEANING_REPORT.md added; nei_id_conflict and postal_code_status defined in the data dictionary.
- Lucky: report path text fixed in the notebook template. Notebook and report stay in scripts/ and reports/ (moving the notebook would break its repo-root detection).
- Damilare: report contains the NAICS-version and overlapping firm-size notes. Outputs stay in data/processed/ (moving them would break the script).
- Emmanuella: 1 value spot-checked against the PDF (Figure 8, formal written plan 9%, matches). Output stays in data/processed/; data/processed/README.md rewritten to say these are not final analytical datasets.
- Ruth: download source and local-only exclusion documented in data/raw/DATA_SOURCES.md.
- Theophilus: NEI flags and the two Census raw files added to docs/DATA_DICTIONARY.md (by Joyce).

Still open (non-critical, record only):
- Issue numbers and PRs #31-#38 not yet recorded.
- Ruth and Oluwatosin notebooks not re-run by QA.
- Only 1 of 13 CFIB values checked against the PDF.
- Lucky notebook and report remain in non-standard folders.
