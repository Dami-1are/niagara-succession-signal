# Niagara Succession Signal — Risk Register

This risk register records the main risks, limitations and data gaps identified during the Niagara Succession Signal project.

The register will be updated as the project progresses and new information becomes available.

---

## Risk Status

- 🔴 High — could seriously affect our ability to answer the research question
- 🟡 Medium — important limitation that needs to be managed
- 🟢 Low — manageable with normal project controls

---

## Current Risk Register

| ID | Risk / Data Gap | Level | Why It Matters | How We Will Manage It | Review |
|---|---|---|---|---|---|
| R01 | Public access to the 2026 NEI succession responses has not been confirmed | 🔴 High | These responses may contain some of the most direct Niagara-specific succession information available to the project | Investigate whether the succession-specific responses can be accessed through Niagara Region/Economic Development or another official release. Do not assume the data is available until confirmed | Week 3 |
| R02 | Public NEI data does not currently give us confirmed owner age, retirement intention, successor or succession-plan fields | 🔴 High | Without direct succession variables, we cannot simply label individual businesses as succession risks | Build the methodology around clearly justified indicators/proxies where necessary and document their limitations. Continue searching for direct succession evidence | Weeks 3–7 |
| R03 | Business closure/exit does not tell us why the business closed | 🔴 High | A business may close because of failure, sale, merger, retirement or other reasons | Never label every closure as succession-related. Use closure/exit data as supporting evidence only unless the reason can be established | Throughout project |
| R04 | CFIB succession research is national, not Niagara-specific | 🟡 Medium | Canadian succession percentages may not represent Niagara businesses | Use CFIB as national context/benchmark evidence. Do not directly apply national percentages to Niagara without a justified method | Throughout project |
| R05 | Statistics Canada Business Dynamics annual data is mainly national/provincial rather than Niagara-specific | 🟡 Medium | Ontario trends cannot automatically be presented as Niagara trends | Use it as historical/benchmark context and combine it carefully with stronger local sources | Weeks 3–6 |
| R06 | CMA geography may not represent the whole Niagara Region | 🟡 Medium | Treating CMA figures as Niagara Region figures could produce misleading results | Check geographic definitions before using CMA data and clearly label the geography used | Week 3 |
| R07 | Census self-employment is only a proxy for business ownership | 🟡 Medium | Not every self-employed person represents the type of business owner relevant to this project | Describe it as self-employment data, not direct business-owner data, and use it only as demographic context | Throughout project |
| R08 | Census data is mainly from 2021 and may reflect pandemic-period conditions | 🟡 Medium | Labour and business behaviour during the pandemic may differ from normal periods | Clearly record the reference period and avoid treating 2021 conditions as automatically representative of 2026 | Throughout project |
| R09 | Sources cover different years | 🟡 Medium | Comparing figures from different periods without checking them may create false patterns | Record the reference period of every dataset and align years where possible before comparison | Weeks 3–5 |
| R10 | Sources use different geographic levels | 🟡 Medium | Canada, Ontario, CMA, Census Division, Census Subdivision and Niagara Region figures are not interchangeable | Record geography for every dataset and only combine geographic levels when the method is justified | Weeks 3–5 |
| R11 | NAICS classifications or categories may differ between sources or years | 🟡 Medium | Industry comparisons may be incorrect if classifications do not match | Inspect NAICS versions and levels during the data audit and create a documented mapping if required | Weeks 3–5 |
| R12 | Business-size definitions may differ between sources | 🟡 Medium | Terms such as micro, small, medium and large may use different employee thresholds | Record each source's definition before comparing or combining size categories | Week 3 |
| R13 | Experimental Statistics Canada opening/closure data may be revised or less stable than established series | 🟡 Medium | Results based on experimental estimates require additional caution | Clearly label the series as experimental, preserve metadata and compare with established sources where possible | Throughout project |
| R14 | Missing values or incomplete records may exist in downloaded datasets | 🟡 Medium | Missing information can affect analysis and later modelling | Measure missingness during Week 3 audit before making any cleaning or imputation decision | Weeks 3–4 |
| R15 | Duplicate or inconsistent business records may exist | 🟡 Medium | Duplicate records could inflate counts or distort analysis | Check identifiers, business names, addresses and other relevant fields during the audit before removing anything | Weeks 3–4 |
| R16 | Joining datasets from different sources may not be straightforward | 🔴 High | Sources may not share a reliable business-level identifier | Do not force business-level joins. First identify valid common keys such as geography, NAICS, year or size category and document the level at which sources can legitimately be combined | Weeks 3–6 |
| R17 | Proxy variables could be mistaken for direct evidence of succession risk | 🔴 High | This could lead us to claim more than the evidence supports | Clearly distinguish direct variables, proxy indicators and contextual variables in the methodology | Throughout project |
| R18 | Raw data could accidentally be changed during cleaning | 🟡 Medium | We need the original data for reproducibility and auditing | Preserve original downloads unchanged in `data/raw/`. Perform cleaning in later stages and save resulting files separately | Weeks 3–4 |

---

# Main Week 2 Data Gap

The most important issue identified during Week 2 is that we currently have strong information about Niagara businesses but limited direct Niagara-specific information about business succession.

We can observe information such as:

- municipality;
- industry and NAICS;
- employment size;
- business opening year;
- business counts;
- business entries and exits;
- demographic patterns; and
- regional economic conditions.

However, we have not yet confirmed public Niagara business-level data containing:

- owner age;
- retirement intention;
- intended exit timeline;
- identified successor; or
- succession-plan status.

This gap will influence how we design the Succession Signal.

---

# Important Project Rule

Our final Succession Signal must distinguish between:

**direct evidence**, **proxy indicators**, and **contextual information**.

We will not assume that:

- business closure = succession failure;
- business exit = succession failure;
- older population = older business owners;
- self-employed person = business owner;
- small business = high succession risk; or
- Canadian succession statistics = Niagara succession statistics.

Any proxy used later in the project must have a clear reason, supporting evidence and documented limitation.

---

# Risk Review

This register is a living project document.

Risks will be reviewed as we move through:

**Data Collection → Data Audit → Cleaning → EDA → Problem Framing → Feature Engineering → Modelling → Evaluation → Recommendations**

New risks will be added when discovered, and existing risks will be updated when they are resolved or better evidence becomes available.

## Business Dynamics Audit Risks

- **Business exit is not a direct succession indicator.** The Business Dynamics datasets define exits based on the presence of employees across consecutive years. An exit does not establish owner retirement, ownership transfer, succession planning, or succession-related closure. Any later use of exit measures as a succession proxy must document this limitation and supporting evidence.

- **Geography is not Niagara-specific.** The Business Dynamics datasets provide provincial and territorial geography, including Ontario, but do not directly identify Niagara. These data therefore cannot by themselves establish Niagara-specific business succession patterns.

- **NAICS classifications vary across the time series.** The industry classification system changes across reference periods. Any later longitudinal industry comparison must account for the applicable NAICS version.

- **Firm-size categories include nested groups.** Dataset 33-10-0088-01 contains overlapping firm-size categories such as "50 employees or more" alongside "50 to less than 100 employees" and "100 employees or more." These categories must not be summed as if they were mutually exclusive.

- **Dataset 33-10-0088-01 contains suppressed observations.** There are 4,179 missing `VALUE` observations associated with `STATUS = x`. According to the Statistics Canada metadata, `x` means the values were suppressed to meet the confidentiality requirements of the Statistics Act. These suppressed observations must not be treated as zero and must be handled appropriately during later cleaning and analysis.
