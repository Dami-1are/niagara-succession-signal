# Canadian Business Counts — Data Audit

**Auditor:** Theophilus / Ruth
**Date:** October 1, 2026
**Dataset:** Statistics Canada Table 33-10-1176-01 (Canadian Business Counts, with employees, census metropolitan areas and census subdivisions)

---

## 1. Dataset Structure
* **Number of rows:** 1,047,957
* **Number of columns:** 16
* **Actual column names:** 'REF_DATE', 'GEO', 'DGUID', 'Employment size', 'North American Industry Classification System (NAICS)', 'UOM', 'UOM_ID', 'SCALAR_FACTOR', 'SCALAR_ID', 'VECTOR', 'COORDINATE', 'VALUE', 'STATUS', 'SYMBOL', 'TERMINATED', 'DECIMALS'
* **Important identifiers:** GEO (Geographic name), DGUID (Geographic ID code), Employment size, North American Industry Classification System (NAICS)
* **Important measures:** VALUE (This holds the actual count of businesses)

## 2. Geography
* **Geographic levels present:** 3,163 unique geographic areas (Census Metropolitan Areas and Census Subdivisions).
* **Can Niagara be identified?** Yes, by filtering the `GEO` column for Niagara-specific subdivisions (e.g., St. Catharines, Niagara Falls, Welland) or the overarching CMA.
* **Available geographic names/codes:** Uses both plain text names (`GEO`) and standardized alphanumeric geographic IDs (`DGUID`).
* **Geographic limitations:** The dataset is extremely large nationwide. We will need to carefully filter by Niagara's specific `DGUID` codes to isolate our region and avoid processing 1 million rows unnecessarily.

## 3. Business Information
* **Business counts present:** Yes, stored in the `VALUE` column.
* **Employee-size categories:** Yes, provided in the `Employment size` column.
* **Micro/small-business info:** Yes, the employment size brackets allow us to isolate micro and small businesses.
* **Indeterminate businesses:** Yes, typical for this Statistics Canada table (businesses without employees).
* **NAICS / Industry sector info:** Yes, included in the `North American Industry Classification System (NAICS)` column.

## 4. Data Quality
* **Missing values:** Handled via standard Statistics Canada formatting.
* **Suppressed values:** Yes, the `STATUS` and `SYMBOL` columns are included specifically to indicate suppressed data (often marked with 'x' for confidentiality in smaller geographic areas).
* **Duplicate records:** None expected in raw StatCan extracts, but each row represents a unique combination of Geography + NAICS + Size.
* **Unusual values / unclear categories:** Nothing unusual, standard Statistics Canada schema.
* **Other quality concerns:** None at the raw stage.

## 5. Time Coverage
* **Actual reference period(s):** Contains `REF_DATE` data for June 2026.
* **Frequency:** Snapshot (usually updated semi-annually by StatCan).
* **Time limitations:** Represents a specific point in time rather than longitudinal changes.

## 6. Possible Future Joining Keys
* **DGUID / GEO:** To join with Census demographic data for the same municipalities.
* **NAICS:** To join with industry-specific risk profiles or the Niagara Employment Inventory.
* **REF_DATE:** To align with other datasets from 2026.

## 7. Confirmation of the Succession-Data Gap
* **Owner age:** Absent
* **Retirement intention / Planned exit:** Absent
* **Succession-plan status:** Absent
* **Ownership transfer information:** Absent
* **Reason for closure:** Absent

## 8. New Findings or Limitations
The sheer size of the dataset (1,047,957 rows) is a finding in itself. We must strictly filter this data by Niagara's `DGUID` identifiers early in the data cleaning phase (Week 4/5) to make it manageable, rather than attempting to process the entire national file.

## 9. Final Dataset Decision
**Decision:** KEEP WITH LIMITATIONS
**Reason:** This dataset is critical for establishing the baseline number and size of businesses in Niagara, but it completely lacks the demographic and succession-planning variables required to directly measure succession risk, confirming we must model this gap using other sources.