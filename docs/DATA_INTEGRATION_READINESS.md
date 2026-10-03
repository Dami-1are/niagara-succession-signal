# Week 3 — Cross-Source Data Compatibility & Integration Readiness Audit
## Purpose

This document assesses whether the Week 3 datasets can be safely combined or compared in later stages of the project.

The focus is on compatibility across geography, time coverage, industry classification, business-size definitions and possible joining keys.

No datasets will be merged at this stage.

## Datasets to Assess

The integration-readiness review will consider the following Week 3 data sources:

1. Niagara Employment Inventory (NEI)
2. Statistics Canada — Canadian Business Counts
3. Statistics Canada — Business Dynamics / Business Entries and Exits
4. Statistics Canada — Census and Demographics
5. Succession-specific datasets or supporting sources identified during Week 3

## Compatibility Checks

Each dataset will be reviewed across the following areas:

- Geography
- Time coverage
- Industry / NAICS classification
- Business-size definitions
- Possible joining keys
- Level of aggregation
- Direct succession variables
- Important limitations

## Integration Readiness Matrix

| Dataset | Geography | Time Coverage | Industry / NAICS | Business Size | Possible Join Keys | Aggregation Level | Succession Variables | Limitations | Integration Status |
|---|---|---|---|---|---|---|---|---|---|

| Niagara Employment Inventory (NEI) | Niagara Region / municipality | Multiple available inventory periods | NAICS and industry fields available | Employee-size categories | Geography, NAICS, time, size; business identifiers within NEI | Business-level | No direct succession variables | Closure status does not identify succession reason | Ready with transformation |
| Canadian Business Counts | Aggregate geographic business counts | Single audited reference period; documented title/reference-period discrepancy | Industry/NAICS available | Business-size information available | Geography, NAICS, reference period, size | Aggregate | No direct succession label | Not business-level; time discrepancy documented | Ready with transformation |
| Business Dynamics | Aggregate | Multiple periods documented in audit | Industry information available | Firm-size source available | Geography, industry, time, size where compatible | Aggregate | No direct succession label | Exit reason is not succession reason | Not directly compatible |
| Census and Demographics | Niagara Region; geography varies by table | Census reference periods | Industry structure available in self-employment table | Not equivalent to NEI employee-size categories | Geography and industry where compatible | Population / labour-force aggregate | No direct succession variables | Population age is not owner age; self-employment is not automatically business ownership | Not directly compatible |
| Succession-specific sources | Canada and provincial/territorial, including Ontario; not Niagara-specific | Varies by source | Industry dimensions available in relevant sources | Varies by source | Ontario/Canada, industry, size and time where compatible | Aggregate | Succession intentions and related measures available | No individual Niagara succession-closure label | Not directly compatible |

### Integration Status Definitions

- Ready — The dataset is sufficiently compatible with another project dataset for planned integration.
- Ready with transformation — The dataset can be integrated, but fields such as geography, time period, NAICS codes or business-size categories must first be standardized.
- Not directly compatible — The dataset cannot be directly joined at its current level of detail, but it may still be useful for comparison, benchmarking or context.
- Pending review — The dataset has not yet been fully assessed.
## Cross-Source Assessment

The completed Week 3 audits show that the project datasets are useful together, but they are not all directly joinable at their current levels of detail.

### 1. Niagara Employment Inventory (NEI)

The NEI is the main Niagara-specific business dataset. It contains local business information including municipality, NAICS/industry information, business opening information, employee-size categories, business identifiers and closed/vacant status.

The NEI does not contain direct succession variables such as owner age, retirement intention, succession-plan status or an identified successor.

**Integration status:** Ready with transformation.

### 2. Canadian Business Counts

Canadian Business Counts has been reviewed and approved with documented limitations. It provides aggregate business-count information that can support comparison with the Niagara business landscape.

The audit identified a reference-period issue: the downloaded data supports a `2026-01` reference period while the cube title refers to June 2026. It must therefore be treated as a single-period aggregate source and not used by itself to establish trends.

**Integration status:** Ready with transformation for aggregate comparison.

### 3. Business Dynamics

The Business Dynamics datasets provide contextual information on business entries, exits and business activity over time.

These datasets remain supporting sources. Any later analytical use must respect the geography, aggregation, time and other limitations documented in the Week 3 audit.

They should not be treated as direct evidence that an individual Niagara business closed because of succession.

**Integration status:** Not directly compatible for business-level joining; suitable for contextual or aggregate comparison.

### 4. Census and Demographics

Both Census datasets will be retained as supporting datasets.

Table 98-10-0022-01 provides detailed Niagara demographic and population-age context, including all 12 municipalities. Population age must not be interpreted as business-owner age.

Table 98-10-0592-01 provides self-employment, class-of-worker and industry context for Niagara. However, self-employment must not automatically be interpreted as business ownership or direct evidence of succession risk. The downloaded Niagara table does not provide municipality-level records.

Neither Census dataset contains direct evidence of owner retirement intention, succession-plan status, an identified successor, intended transfer timeline or succession-related closure.

**Integration status:** Not directly compatible for business-level joining; retain for demographic and labour-force context.

### 5. Succession-Specific Sources

The succession audit concluded that all five reviewed sources should be kept with documented limitations.

The Statistics Canada succession sources provide Canada and provincial/territorial evidence, including Ontario, but do not provide Niagara Region as a separate geography.

Table 33-10-1196-01 provides the strongest direct evidence because it measures intentions and timelines to sell or transfer ownership. The other succession sources provide supporting evidence on transfer expectations, considerations, planning readiness, exit methods and succession barriers.

These sources do not provide a direct label identifying succession-related closure for individual Niagara businesses.

**Integration status:** Not directly compatible for business-level joining; suitable for Ontario/Canada benchmarking and succession context.

### Overall Integration Finding

No source should be forced into a business-level join simply because similar fields exist.

Potential common dimensions across the sources include:

- geography;
- NAICS/industry;
- time or reference period; and
- business-size categories.

These fields must be standardized and their aggregation levels checked before any later integration.

The project must clearly distinguish:

- business-level observations;
- aggregate statistics;
- direct succession variables;
- proxy indicators; and
- contextual variables.

No Week 3 dataset provides a confirmed business-level label showing that a Niagara business closure occurred because of succession.

## Integration Decision Log

### Decision 1 — Use NEI as the main Niagara business-level source

**Datasets involved:** Niagara Employment Inventory and supporting datasets.

**Decision:** Retain NEI as the main local business dataset.

**Reason:** NEI provides Niagara-specific business information, including municipality, industry/NAICS, business opening information, employee-size categories and business identifiers.

**Required transformation:** Standardize relevant geography, NAICS, time and business-size fields before comparison with other sources.

**Risk/limitation:** NEI does not directly identify succession-related closure.

**Next action:** Prepare NEI for cleaning and later feature engineering without modifying the raw file.

### Decision 2 — Use aggregate sources only at valid aggregation levels

**Datasets involved:** Canadian Business Counts, Business Dynamics, Census/Demographics and succession-specific sources.

**Decision:** Do not force business-level joins with NEI.

**Reason:** These sources differ in geography, aggregation level, reference period and unit of observation.

**Required transformation:** Harmonize compatible geography, NAICS, time and business-size categories where valid.

**Risk/limitation:** Invalid joins could create unsupported business-level conclusions from aggregate evidence.

**Next action:** Define the valid analytical level for each source before integration.

### Decision 3 — Treat Census age and self-employment as contextual variables

**Datasets involved:** Census/Demographics and NEI.

**Decision:** Retain Census variables for contextual analysis only.

**Reason:** Population age is not business-owner age, and self-employment is not automatically equivalent to business ownership.

**Required transformation:** Aggregate or align Census measures only at compatible geographic and industry levels.

**Risk/limitation:** These variables could be misinterpreted as direct succession indicators.

**Next action:** Clearly label them as contextual or proxy variables in later methodology and feature documentation.

### Decision 4 — Use succession datasets for benchmark and conceptual evidence

**Datasets involved:** Statistics Canada succession tables, CFIB succession research and NEI.

**Decision:** Keep all five succession sources with documented limitations, but do not use them as individual Niagara business labels.

**Reason:** They provide evidence on succession intentions, transfer expectations, considerations and planning, but not confirmed succession-related closures for individual Niagara businesses.

**Required transformation:** Align Ontario/Canada-level measures with compatible industry, size or time dimensions only where analytically valid.

**Risk/limitation:** Aggregate succession patterns could be incorrectly attributed to individual Niagara businesses.

**Next action:** Use these sources to support proxy design, interpretation and benchmarking rather than direct labelling.

### Decision 5 — Preserve time-period differences

**Datasets involved:** All Week 3 sources.

**Decision:** Do not assume that similarly named or recently downloaded datasets represent the same time period.

**Reason:** The audits identified differences in reference periods, including the Canadian Business Counts reference-period/title discrepancy.

**Required transformation:** Create standardized reference-period fields and document any unresolved discrepancies.

**Risk/limitation:** Incorrect time alignment could produce misleading comparisons.

**Next action:** Confirm time compatibility before any cross-source analysis.

## Week 3 Integration Readiness Conclusion

The Week 3 datasets are suitable for continued use, but they are not one directly mergeable dataset.

The safest integration strategy is to use the Niagara Employment Inventory as the main local business source and use Canadian Business Counts, Business Dynamics, Census/Demographics and succession-specific sources at compatible aggregate levels for context, benchmarking and carefully defined proxy development.

Any later integration must preserve the distinction between direct observations, proxy indicators and contextual evidence.

No cleaning, merging, feature engineering, succession scoring or modelling is performed as part of this Week 3 integration-readiness audit.
