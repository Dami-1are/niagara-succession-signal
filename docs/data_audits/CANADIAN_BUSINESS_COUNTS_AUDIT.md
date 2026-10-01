Canadian Business Counts — Data Audit
Auditor: Theophilus / Ruth

Date: October 1, 2026

Dataset: Statistics Canada Table 33-10-1176-01 (Canadian Business Counts, with employees, census metropolitan areas and census subdivisions)

1. Dataset Structure
Number of rows: 1,047,957

Number of columns: 16

Actual column names: 'REF_DATE', 'GEO', 'DGUID', 'Employment size', 'North American Industry Classification System (NAICS)', 'UOM', 'UOM_ID', 'SCALAR_FACTOR', 'SCALAR_ID', 'VECTOR', 'COORDINATE', 'VALUE', 'STATUS', 'SYMBOL', 'TERMINATED', 'DECIMALS'

Important identifiers: GEO (Geographic name), DGUID (Geographic ID code), Employment size, North American Industry Classification System (NAICS)

Important measures: VALUE (This holds the actual count of businesses)

2. Geography
Geographic levels present: 3,163 unique geographic areas.

Can Niagara be identified? Yes, Niagara-specific subdivisions and the overarching CMA were positively identified in the GEO and DGUID columns. Actual values found include:

St. Catharines - Niagara (DGUID: 2021S0503539)

St. Catharines (DGUID: 2021A00053526053)

Niagara Falls (DGUID: 2021A00053526043)

Niagara-on-the-Lake (DGUID: 2021A00053526047)

3. Business Information
Business counts present: Yes, stored in the VALUE column.

NAICS / Industry categories: Yes, the dataset includes hierarchical industry classifications ranging from 2-digit broad sectors (e.g., Retail trade) down to detailed 6-digit NAICS codes.

Employee-size categories: Yes, provided in the Employment size column. The actual categories present in this dataset are strictly for businesses with employees:

Total, with employees

1 to 4 employees (Micro)

5 to 9 employees

10 to 19 employees

20 to 49 employees

50 to 99 employees

100 to 199 employees

200 to 499 employees

500 plus employees

Note: "Without employees" or "Indeterminate" categories were not found in this specific CSV extract.

4. Data Quality
Missing values: 0 missing values found in the VALUE column.

Suppressed values: 0 suppressed values found (checked for 'x', 'X', or 'F' in STATUS and SYMBOL columns).

Duplicate records: 0 exact row duplicates exist when factoring in the full Statistics Canada identifier columns (VECTOR or COORDINATE). However, when evaluating based only on our core business dimensions (REF_DATE, GEO, NAICS, Employment size), we found 83,212 duplicates. This confirms we must include the additional dimensions present in the file (such as UOM / Unit of Measure) to create a fully unique row identifier during the cleaning phase.

5. Time Coverage
Actual reference period(s): The only unique REF_DATE found in the dataset is 2026-01.

Update Frequency: As per the downloaded cube metadata, this data is updated semi-annually.

6. Possible Future Joining Keys
DGUID / GEO: To join with Census demographic data for the same municipalities.

NAICS: To join with industry-specific risk profiles or the Niagara Employment Inventory.

REF_DATE: To align with other datasets from 2026.

7. Confirmation of the Succession-Data Gap
Owner age: Absent

Retirement intention / Planned exit: Absent

Succession-plan status: Absent

Ownership transfer information: Absent

Reason for closure: Absent

8. New Findings or Limitations
The sheer size of the dataset (1,047,957 rows) is a finding in itself. We must strictly filter this data by Niagara's DGUID identifiers early in the data cleaning phase (Week 4/5) to make it manageable, rather than attempting to process the entire national file.

9. Final Dataset Decision
Decision: KEEP WITH LIMITATIONS

Reason: This dataset is critical for establishing the baseline number and size of businesses in Niagara, but it completely lacks the demographic and succession-planning variables required to directly measure succession risk, confirming we must model this gap using other sources.