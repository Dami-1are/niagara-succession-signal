# Succession Data Audit

## 1. Purpose

This audit reviews the succession-related datasets collected for the Niagara Succession Signal project.

The purpose is to determine whether the sources can help distinguish ordinary business closure from closure or transition risk associated with business succession.

The audit covers four Statistics Canada datasets and one Canadian Federation of Independent Business (CFIB) report.

---

## 2. Sources Reviewed

### Statistics Canada

1. Table 33-10-1196-01 — Intentions for businesses to sell or transfer ownership within the next 10 years
2. Table 33-10-1197-01 — Expectations related to selling or transferring the business
3. Table 33-10-1198-01 — Considerations related to the sale or transfer of the business
4. Table 33-10-1199-01 — Scenarios if a business is unable to find a suitable buyer or successor

Raw files are stored in:

`data/raw/statcan/succession/`

### Canadian Federation of Independent Business (CFIB)

Report reviewed:

**Succession Tsunami: Preparing for a Decade of Small Business Transitions in Canada**

Stored in:

`data/raw/cfib/succession/CFIB_Succession_Tsunami.pdf`

---

# 3. Statistics Canada Table 33-10-1196-01

## Dataset Purpose

This table measures businesses' intentions to sell or transfer ownership within the next 10 years.

## Dataset Structure

- Rows: 6,664
- Reference period: 2026
- Unit of measure: Percent
- Geographic coverage: Canada and provinces/territories
- Ontario: Available
- Niagara-specific geography: Not available

## Succession Measures

The dataset contains the following categories:

- Yes, business intends to sell or transfer ownership within the next 10 years
- Timeline within 2 years
- Timeline within 3 to 5 years
- Timeline within 6 to 10 years
- Timeline unknown
- No intention to sell or transfer ownership within the next 10 years
- Intention unknown

## Business Characteristics

The table provides breakdowns including:

- NAICS industry
- employment size
- business or organization type
- age of business
- urban/rural geography
- majority ownership characteristics
- majority ownership by a person aged 65 or older

Employment-size categories include:

- 1 to 4 employees
- 5 to 19 employees
- 20 to 99 employees
- 100 or more employees

## Data Quality

Missing `VALUE`: 2,194

Status distribution:

- A: 1,288
- B: 796
- C: 886
- D: 619
- E: 881
- F: 1,009
- `..`: 1,185

The metadata states that the quality indicators are based on standard error:

- A = Excellent
- B = Very good
- C = Good
- D = Acceptable
- E = Use with caution
- F = Too unreliable to be published

`..` represents data not available for a specific reference period.

The `SYMBOL` field is empty throughout the dataset.

## Relevance

**KEEP — HIGH RELEVANCE**

This table provides direct evidence of succession intention and expected transition timing.

However, the data are not Niagara-specific and must not be interpreted as individual-business succession probabilities.

---

# 4. Statistics Canada Table 33-10-1197-01

## Dataset Purpose

This table measures expectations surrounding the sale or transfer of businesses.

## Dataset Structure

- Rows: 6,664
- Reference period: 2026
- Unit of measure: Percent
- Ontario: Available
- Niagara-specific geography: Not available

## Measures

The table includes expectations relating to:

- availability of qualified buyers
- receiving a fair market price
- having sufficient time and resources to pursue a sale or transfer
- consulting professional or advisory support
- using government programs or supports
- none
- unknown

## Business Characteristics

Breakdowns include:

- NAICS industry
- employment size
- business age
- business type
- urban/rural characteristics
- majority ownership characteristics
- majority ownership by a person aged 65 or older

## Data Quality

Missing `VALUE`: 3,129

Status distribution:

- A: 2,043
- B: 247
- C: 276
- D: 279
- E: 690
- F: 945
- `..`: 2,184

The `SYMBOL` field is empty throughout the dataset.

## Relevance

**KEEP — HIGH RELEVANCE**

The table provides useful evidence about conditions that may make successful succession easier or more difficult.

It is contextual evidence and does not directly identify Niagara businesses experiencing succession risk.

---

# 5. Statistics Canada Table 33-10-1198-01

## Dataset Purpose

This table measures factors businesses consider when selling or transferring ownership.

## Dataset Structure

- Rows: 19,040
- Reference period: 2026
- Unit of measure: Percent
- Ontario: Available
- Niagara-specific geography: Not available

## Considerations

The dataset includes:

- finding a buyer in Canada
- protecting employees
- maintaining a presence in the local community
- obtaining the highest price
- preserving the business's culture or values

Each consideration is classified as:

- Very important
- Somewhat important
- Not important
- Unknown

## Business Characteristics

The dataset contains:

- NAICS breakdowns
- employment-size breakdowns
- ownership characteristics
- majority ownership by a person aged 65 or older

## Data Quality

Missing `VALUE`: 8,488

Status distribution:

- A: 6,348
- B: 845
- C: 956
- D: 859
- E: 1,544
- F: 2,248
- `..`: 6,240

The `SYMBOL` field is empty throughout the dataset.

## Relevance

**KEEP — SUPPORTING CONTEXT**

This dataset helps explain what business owners value during succession and transfer.

It is less direct as a succession-risk indicator than Tables 33-10-1196-01 and 33-10-1199-01.

---

# 6. Statistics Canada Table 33-10-1199-01

## Dataset Purpose

This table examines what businesses may do if they are unable to find a suitable buyer or successor.

## Dataset Structure

- Rows: 14,280
- Reference period: 2026
- Unit of measure: Percent
- Ontario: Available
- Niagara-specific geography: Not available

## Scenarios

Three scenarios are measured:

1. Continue operating under current ownership
2. Sell at a reduced value or under less favourable terms, including to a less preferred buyer
3. Scale down or close operations

Likelihood is classified as:

- Very likely
- Somewhat likely
- Somewhat unlikely
- Very unlikely
- Unknown

## Business Characteristics

The dataset includes:

- NAICS
- employment size
- ownership characteristics
- majority ownership by a person aged 65 or older

## Data Quality

Missing `VALUE`: 6,493

Status distribution:

- A: 4,615
- B: 714
- C: 671
- D: 618
- E: 1,169
- F: 1,813
- `..`: 4,680

The `SYMBOL` field is empty throughout the dataset.

The number of missing `VALUE` records corresponds to the combined number of records with `F` and `..` status:

`1,813 + 4,680 = 6,493`

## Relevance

**KEEP — VERY HIGH RELEVANCE**

This is one of the most directly relevant succession datasets identified.

The scenario:

**“Scale down or close operations”**

is explicitly linked to a business being unable to find a suitable buyer or successor.

This provides evidence supporting the conceptual distinction between general business failure and succession-related closure.

However, these percentages must not be assigned directly to individual Niagara businesses.

---

# 7. CFIB Succession Tsunami Report

## Source

Canadian Federation of Independent Business (CFIB)

**Succession Tsunami: Preparing for a Decade of Small Business Transitions in Canada**

## Survey Basis

The CFIB Business Succession Planning Survey was:

- conducted online;
- conducted from June 27 to August 17, 2022;
- based on 2,479 small-business owners in Canada.

The report states that, for comparison purposes, a probability sample with the same number of respondents would have a margin of error of approximately ±2.0%.

This should not be interpreted as an actual probability-sample margin of error for the CFIB survey.

## Key Findings Relevant to the Project

### Exit intentions

The report states that:

**76% of Canada's business owners planned to exit their business within the next 10 years.**

### Method of exiting

Reported intended exit methods included:

- 49% — sell to buyer(s) unrelated to their family
- 24% — sell to family member(s)
- 23% — sell to employee(s)
- 21% — transfer to family member(s)

These percentages should not automatically be treated as mutually exclusive categories.

### Succession planning

The report found:

- 9% had a formal written succession plan
- 45% had an informal/unwritten succession plan
- 46% had no succession plan

Among owners intending to exit within 12 months:

- 16% had a formal plan
- 54% had an informal plan

Among owners intending to exit within 6 to 10 years:

- 6% had a formal plan
- 44% had an informal plan

### Succession barriers

The report identifies **finding a buyer or suitable successor** as the top obstacle encountered by business owners when developing a succession plan, reported by **54%** of owners.

## Relevance

**KEEP — CONTEXTUAL EVIDENCE**

The CFIB report provides strong national context on:

- succession intentions;
- succession preparedness;
- intended exit methods; and
- barriers to successful business transfer.

However, the findings are national survey evidence and should not be used as direct Niagara-level or individual-business measurements.

---

# 8. Geographic Limitation

A major limitation across the reviewed succession sources is geography.

The four Statistics Canada tables contain Canada and provincial/territorial data, including Ontario, but do not contain Niagara Region as a separate geography.

The CFIB report provides national evidence.

Therefore:

**No reviewed succession source directly measures succession intentions for individual Niagara businesses.**

Ontario and Canadian evidence should be treated as contextual or benchmark information rather than direct Niagara observations.

---

# 9. Business-Level Limitation

The reviewed sources provide aggregate statistics.

They do not identify:

- individual Niagara business owners planning retirement;
- individual businesses with a succession plan;
- individual businesses actively seeking buyers;
- whether a particular Niagara closure occurred because of succession;
- whether an individual business has a willing successor.

Therefore, succession risk cannot be directly observed at the individual-business level using these sources alone.

---

# 10. Potential Integration with Niagara Data

The Statistics Canada succession tables provide dimensions that can potentially be aligned conceptually with Niagara business data, including:

- NAICS industry
- employment size
- business age
- ownership age characteristics
- urban/rural characteristics

These variables may support the development of contextual succession-risk indicators.

Any integration must clearly distinguish:

**observed Niagara business characteristics**

from

**aggregate Ontario/Canada succession evidence.**

Aggregate succession percentages must not be presented as known probabilities for individual Niagara businesses.

---

# 11. Overall Assessment

The succession sources are useful and should be retained.

### Highest direct relevance

**33-10-1199-01**

because it explicitly links inability to find a buyer or successor with the possibility of scaling down or closing operations.

### Direct succession-intention evidence

**33-10-1196-01**

because it measures intentions and timelines to sell or transfer ownership.

### Supporting evidence

**33-10-1197-01** provides expectations surrounding successful transfer.

**33-10-1198-01** provides considerations affecting sale or transfer.

**CFIB Succession Tsunami** provides national context on exit intentions, planning readiness, exit methods and succession barriers.

---

# 12. Final Decision

**KEEP ALL FIVE SOURCES, WITH DOCUMENTED LIMITATIONS.**

The sources provide valuable evidence for understanding business succession and constructing the conceptual framework for the Niagara Succession Signal.

They do **not** provide a direct label identifying succession-related closure for individual Niagara businesses.

The project must therefore avoid treating these aggregate measures as direct observations of individual Niagara succession risk.