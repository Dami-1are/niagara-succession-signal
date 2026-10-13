# Week 4 Handover: Data Cleaning & Validation

Prepared by Joyce (Team Lead). Detailed results: `docs/WEEK4_QA_CHECKLIST.md`.

## What Week 4 Accomplished
Nine cleaning or documentation tasks were submitted and merged (PRs #24 to #30, #39, #40). Raw data was not modified (git history shows only documentation edits under `data/raw/`). Cleaning was re-run and reproduced exactly for NEI, Canadian Business Counts and Business Dynamics. A re-run is still outstanding for Census Age, Self-Employment and the four StatCan succession tables.

## Cleaned Data Available
| Dataset | File | Level | Period |
|---|---|---|---|
| NEI | `data/interim/nei_cleaned.csv` (98,065 x 22) | Niagara business | survey years |
| Canadian Business Counts | `data/interim/canadian_business_counts_niagara_cleaned.csv` (10,462 x 14); CMA in separate `..._cma_reference.csv` | 12 municipalities | 2026-01 only |
| Business Dynamics | `data/processed/statcan/business_dynamics/` industry (2,484 x 18), firm size (828 x 15) | Ontario | 2001-2023 |
| Census Age | `census_age_niagara_cleaned.csv` (repo root, to be moved) (3,328 x 12) | Niagara CD + 12 municipalities | 2016, 2021 |
| Self-Employment | `data/interim/census_self_employment_niagara_cleaned.csv` (125,714 x 21) | Niagara CD only | 2021 (25% sample) |
| StatCan succession | `data/interim/statcan_33101196/7/8/9_ontario_cleaned.csv` (four files) | Ontario | see reports |
| CFIB | `data/processed/cfib/cfib_succession_evidence_structured.csv` (13 rows) | Canada | 2022 survey |

## Important Cleaning Decisions (Week 5 must respect)
- Missing and suppressed values stay missing, never zero: Business Dynamics (`..` 36, `x` 196), StatCan tables (status `F` and `..`), Canadian Business Counts (no absent combination filled).
- NEI: `postal_code_status` (153 Invalid - Review, 127 Missing) and `nei_id_conflict` (278 rows where one NEI_ID and year carries more than one business name) are flags only; no rows were removed. Repeated `nei_id` across years are longitudinal observations, not duplicates.
- Canadian Business Counts: sum size bands OR use "Total, with employees", never both. Use `naics_level_name` to avoid summing a sector with its subsectors. Never add the CMA to municipality totals.
- Census Age: use `Census year (2)`, not `REF_DATE`. Age categories overlap (single years, bands, broad groups). Men+ plus Women+ need not equal Total because of random rounding.
- Self-Employment: two "Self-employed" measures differ on unpaid family workers; use `class_worker_label`. Niagara Census Division only.
- StatCan succession tables stay separate; values are percentages with A to F quality ratings.

## Remaining Limitations (must stay explicit in EDA)
There is still no observed label saying whether any Niagara business closure was caused by succession. No dataset gives owner age, retirement intention, successor status or individual closure probability for Niagara businesses. Population age is not owner age. Self-employment is not business ownership. Business exits are not succession closures. Ontario and Canada evidence is contextual only.

## Evidence Types
- Direct (Niagara): NEI business records; Canadian Business Counts (municipality, single 2026-01 snapshot).
- Proxy (Niagara): Census Age (population age), Self-Employment (labour-force counts).
- Contextual: Business Dynamics (Ontario), StatCan succession tables (Ontario), CFIB (Canada).

## Integration Readiness
Possible later alignment: Canadian Business Counts, Census Age (DGUID), Self-Employment (Niagara CD DGUID); NEI to Canadian Business Counts via municipality, NAICS and employment-size, with care. Known incompatibilities: municipality vs Census Division vs Ontario vs Canada levels; reference periods (2026-01 vs 2016/2021 vs 2001-2023); NAICS versions and hierarchy (Self-Employment uses NAICS 2017; versions for the others to be confirmed); size-band definitions; survey populations. A shared column name does not prove a valid join. No datasets were merged.

## Outstanding Issues
1. Precious (Census Age): move notebook, report and CSV out of the repo root; fix the raw path (`data/raw/98100022.csv` does not exist; `DATA_SOURCES.md` points elsewhere); raw file untracked since 2026-10-03; re-run once the raw file is restored; confirm report covers overlapping ages and rounding.
2. Ruth: raw `9810059201_databaseLoadingData.csv` is excluded only locally; document the download source.
3. Stephen: add a cleaning report and define `nei_id_conflict`; PR #40 changed the cleaned file after PR #24 approval and had no independent review.
4. Lucky: fix the notebook path written into the report template; move files to standard folders.
5. Damilare, Emmanuella: decide `data/processed/` vs `data/interim/` and fix the "analysis-ready" wording in `data/processed/README.md`. Damilare: check the NAICS-version and overlapping firm-size notes. Emmanuella: spot-check values against the PDF.
6. Theophilus: add the NEI flags and the two Census raw files to the dictionary.
7. Record issue numbers and PRs #31 to #38.

## Week 5 Entry Conditions
Week 5 may start for a dataset when: its corrections above are resolved or recorded as non-critical; raw data is available or its download source is documented; the data dictionary and inventory match the approved outputs; the final `git status` is clean. Census Age and Self-Employment analysis should wait for their raw-file documentation. Status: not yet met. Week 4 should not be marked complete until the items above are closed.