# NEI Cleaning Report (Week 4)

Dataset: Niagara Employment Inventory (NEI)
Raw file (unchanged): data/raw/OpenData_Consolidated_NEI_Opendata_-482263215789080610.csv
Notebook: notebooks/02_data_cleaning/02_nei_cleaning.ipynb
Output: data/interim/nei_cleaned.csv
Geography: Niagara business records, with municipality. Survey years in the file; 2020 and 2021 are not present and were NOT interpolated or created.

## Dimensions
- Raw: 98,065 rows, 20 columns.
- Cleaned: 98,065 rows, 22 columns. 0 rows removed.
- The two added columns are quality flags (below). All 20 original columns are kept.

## Missing values (raw)
- business_po_box 94,275; business_unit 74,541; business_website 34,573; secondary_naics 19,404; business_postal_code 127; x 3; y 3.
- opening_year: 199 missing plus 31,306 rows holding the placeholder 0.
- floor_size_sqft: 2,695 missing plus more than 53,000 rows holding the placeholder 0.
- Placeholder zeros in opening_year and floor_size_sqft were converted to missing. Records with missing secondary_naics were kept without inventing codes.
- 3 records have missing coordinates (nei_id 4760, 7972, 7984, survey year 2016). They were kept as missing and not imputed or deleted.

## Duplicates
- 0 exact duplicate rows.
- 82,219 repeated nei_id occurrences are longitudinal observations of the same business across survey years, not duplicates.
- (nei_id, year) pairs were also checked.

## Flags added (flags only; no rows removed or changed)
- postal_code_status: 127 Missing, 153 Invalid - Review; all other rows are valid. The exact validation rule is in the notebook.
- nei_id_conflict: True (278 rows) when the same nei_id in the same year appears under more than one distinct business_name; every row in such a group is flagged. Missing names count as their own value.

## Reproducibility
- The notebook reads the raw file from data/raw/ using repo-relative paths and writes only data/interim/nei_cleaned.csv.
- QA re-run on 2026-10-12 regenerated the file with identical content (only line endings differed).
- The notebook is committed without saved outputs; re-run it to see them.

## Limitations
- No succession, exit, owner-age, retirement or successor variable exists or was created.
- NEI records describe businesses present in a survey year. Absence from a later year is not evidence of closure, and closure is not evidence of succession.
- Optional fields (floor size, opening year, website) are largely unrecorded.
