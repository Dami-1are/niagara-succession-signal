# CFIB Succession Evidence Notes

## 1. Source

**Source:** Canadian Federation of Independent Business (CFIB), *Succession Tsunami*  
**Source year:** 2022  
**Raw source file:** data/raw/cfib/succession/CFIB_Succession_Tsunami.pdf

The CFIB report presents national survey evidence on business-owner exit intentions, intended exit approaches, succession planning, and succession barriers.

## 2. Survey Context

The survey was conducted online between **June 27 and August 17, 2022**.

The survey included **2,479 small-business owners in Canada**.

The evidence extracted into the structured dataset represents survey-level findings and should not be interpreted as measurements of individual businesses.

## 3. Extracted Succession Evidence

The structured dataset contains the following required evidence:

### Exit intention

- **76%** of Canada's business owners planned to exit their business within the next 10 years.
- Source: Figure 1, page 4.

### Intended exit methods

- **49%** planned to sell to buyer(s) unrelated to family.
- **24%** planned to sell to family member(s).
- **23%** planned to sell to employee(s).
- **21%** planned to transfer to family member(s), such as through inheritance.
- Source: Figure 5, page 8.

These percentages are retained as separate observations. They are **not assumed to be mutually exclusive** and must not be interpreted as categories that sum to 100%.

### Succession planning

- **9%** had a formal written succession plan.
- **45%** had an informal or unwritten succession plan.
- **46%** had no succession plan.
- Source: Figure 8, page 11.

### Succession planning by exit timeline

For owners intending to exit within **12 months**:

- **16%** had a formal written plan.
- **54%** had an informal or unwritten plan.

For owners intending to exit in **6–10 years**:

- **6%** had a formal written plan.
- **44%** had an informal or unwritten plan.

- Source: Figure 9, page 12.

The exit-timeline population is retained in the population field so these percentages are not interpreted as applying to all survey respondents.

### Succession barriers

- **54%** identified finding a buyer or suitable successor as the top obstacle.
- Source: Figure 12, page 14.

This figure represents a reported succession obstacle. It must **not** be interpreted as a 54% probability of succession failure, business closure, or inability to transfer a business.

## 4. Geographic Scope

The CFIB evidence is **national Canadian evidence**.

The geography is recorded as **Canada** in the structured dataset.

These percentages must not be presented as direct measurements of Niagara businesses, Ontario businesses, or individual businesses in Niagara.

The CFIB findings may provide contextual evidence for understanding succession dynamics, but they do not establish Niagara-specific succession rates or outcomes.

## 5. Margin of Error Qualification

The report states that a probability sample with the same number of respondents would have an approximate **±2.0 percentage-point margin of error**.

This qualification is preserved as a methodological statement.

The dataset does **not** state that the CFIB survey itself has a ±2.0% margin of error.

## 6. Conceptual Separation

The following concepts are kept separate in the structured dataset:

1. Exit intention
2. Intended exit method
3. Succession planning
4. Succession planning by exit timeline
5. Succession barriers

These measures should not be combined into a single succession probability or business-closure indicator.

## 7. Validation

The structured dataset was checked for:

- Required evidence categories.
- Correct percentage values.
- Source-page traceability.
- National Canadian geographic scope.
- Survey population context.
- Timeline-specific population context.
- Separation of exit intention, exit methods, succession planning, and succession barriers.
- Non-additive treatment of exit-method percentages.
- Appropriate interpretation of the 54% succession-barrier figure.

The final structured dataset contains **13 evidence records** and **11 columns**.

## 8. Traceability

| Evidence | Figure | Source Page |
|---|---:|---:|
| 76% plan to exit within next 10 years | Figure 1 | 4 |
| 49%, 24%, 23%, 21% intended exit methods | Figure 5 | 8 |
| 9%, 45%, 46% succession planning status | Figure 8 | 11 |
| 16%, 54%, 6%, 44% planning by exit timeline | Figure 9 | 12 |
| 54% finding a buyer or suitable successor | Figure 12 | 14 |

## 9. Related Files

Structured evidence:

data/processed/cfib/cfib_succession_evidence_structured.csv

Raw source:

data/raw/cfib/succession/CFIB_Succession_Tsunami.pdf

Week 3 source audit:

docs/data_audits/SUCCESSION_DATA_AUDIT.md

## 10. Data Handling Decision

The raw CFIB PDF is preserved unchanged.

The structured CSV contains extracted evidence only. No business-level records are created from the CFIB survey, and no CFIB percentage is merged with Statistics Canada, Census, NEI, Business Dynamics, Canadian Business Counts, or individual Niagara-business data.

The CFIB evidence is therefore treated as **contextual succession evidence**, not direct Niagara business-level succession evidence.

