"""
Audit script for Statistics Canada Table 33-10-1176-01
(Canadian Business Counts).

Read-only: the raw CSV is never modified.
No cleaning, filtering or merging is done.

Usage (from the repository root):

    python audit_script.py

Optional file-path override:

    python audit_script.py path/to/file.csv

To save the audit output:

    python audit_script.py > docs/data_audits/audit_script_output.txt
"""

import collections
import csv
import glob
import hashlib
import os
import re
import sys


# ---------------------------------------------------------
# FILE PATH
# ---------------------------------------------------------

DEFAULT_PATH = "data/raw/33101176.csv"

file_path = (
    sys.argv[1]
    if len(sys.argv) > 1
    else DEFAULT_PATH
)


# ---------------------------------------------------------
# NIAGARA GEOGRAPHY
# ---------------------------------------------------------

NIAGARA_MUNICIPALITIES = [
    "Fort Erie",
    "Grimsby",
    "Lincoln",
    "Niagara Falls",
    "Niagara-on-the-Lake",
    "Pelham",
    "Port Colborne",
    "St. Catharines",
    "Thorold",
    "Wainfleet",
    "Welland",
    "West Lincoln",
]

# Niagara census division code used inside the Niagara
# census-subdivision DGUIDs.
NIAGARA_CD_CODE = "3526"


# ---------------------------------------------------------
# DATASET DIMENSIONS
# ---------------------------------------------------------

# These columns contain measures, flags, units or
# Statistics Canada series identifiers rather than the
# main identifying dimensions.

NON_DIMENSION_COLS = {
    "VALUE",
    "STATUS",
    "SYMBOL",
    "TERMINATED",
    "DECIMALS",
    "UOM",
    "UOM_ID",
    "SCALAR_FACTOR",
    "SCALAR_ID",
    "VECTOR",
    "COORDINATE",
}


# ---------------------------------------------------------
# HELPER FUNCTIONS
# ---------------------------------------------------------

def find_col(headers, startswith):
    """Find a column whose name starts with the supplied text."""

    for header in headers:
        if header.strip().lower().startswith(
            startswith.lower()
        ):
            return header

    return None


def key_hash(values):
    """
    Create a compact fingerprint for duplicate checks.

    This avoids storing very large full-text keys for
    more than one million rows.
    """

    joined = "\x1f".join(
        (value or "")
        for value in values
    )

    return hashlib.blake2b(
        joined.encode("utf-8"),
        digest_size=16,
    ).digest()


def is_blank(value):
    """Return True when a value is missing or blank."""

    return (
        value is None
        or value.strip() == ""
    )


# ---------------------------------------------------------
# MAIN AUDIT
# ---------------------------------------------------------

def main():

    # -----------------------------------------------------
    # CHECK FILE
    # -----------------------------------------------------

    if not os.path.isfile(file_path):

        print(
            f"ERROR: raw data file not found: "
            f"'{file_path}'"
        )

        print(
            f"Current working directory: "
            f"{os.getcwd()}"
        )

        print(
            "Run this script from the repository root, "
            "or pass the CSV path as an argument."
        )

        print(
            "If the file is stored with Git LFS, "
            "run 'git lfs pull' first."
        )

        sys.exit(1)


    # -----------------------------------------------------
    # READ RAW DATA
    # -----------------------------------------------------

    with open(
        file_path,
        newline="",
        encoding="utf-8-sig",
    ) as file:

        reader = csv.DictReader(file)

        headers = reader.fieldnames

        if not headers:
            print("ERROR: No CSV headers found.")
            sys.exit(1)

        col_ref = find_col(
            headers,
            "REF_DATE",
        )

        col_geo = find_col(
            headers,
            "GEO",
        )

        col_dguid = find_col(
            headers,
            "DGUID",
        )

        col_naics = find_col(
            headers,
            "North American Industry",
        )

        col_size = find_col(
            headers,
            "Employment size",
        )

        dim_cols = [
            header
            for header in headers
            if header not in NON_DIMENSION_COLS
        ]


        # -------------------------------------------------
        # STORAGE
        # -------------------------------------------------

        row_count = 0

        missing = collections.Counter()

        uniques = {
            header: collections.Counter()
            for header in headers
            if header in {
                col_ref,
                col_size,
                "STATUS",
                "SYMBOL",
                "UOM",
                "SCALAR_FACTOR",
                "TERMINATED",
            }
        }

        # GEO -> DGUID set
        geo_dguid = {}

        naics_vals = set()

        full_row_hashes = set()
        exact_dupes = 0

        dim_keys = set()
        dim_dupes = 0

        core_keys = set()
        core_dupes = 0

        core5_keys = set()
        core5_dupes = 0

        vector_coord_keys = set()
        vector_coord_dupes = 0

        non_numeric_value = 0
        negative_value = 0
        zero_value = 0

        vmin = None
        vmax = None


        # -------------------------------------------------
        # PROCESS ROWS
        # -------------------------------------------------

        for row in reader:

            row_count += 1


            # ---------------------------------------------
            # MISSING VALUES
            # ---------------------------------------------

            for header in headers:

                if is_blank(
                    row.get(header)
                ):
                    missing[header] += 1


            # ---------------------------------------------
            # UNIQUE VALUES
            # ---------------------------------------------

            for header, counter in uniques.items():

                counter[
                    row.get(header, "")
                ] += 1


            # ---------------------------------------------
            # GEOGRAPHY
            # ---------------------------------------------

            if col_geo:

                geo = row.get(
                    col_geo,
                    "",
                )

                dguid = (
                    row.get(
                        col_dguid,
                        "",
                    )
                    if col_dguid
                    else ""
                )

                geo_dguid.setdefault(
                    geo,
                    set(),
                ).add(dguid)


            # ---------------------------------------------
            # NAICS
            # ---------------------------------------------

            if col_naics:

                naics_vals.add(
                    row.get(
                        col_naics,
                        "",
                    )
                )


            # ---------------------------------------------
            # EXACT DUPLICATE ROW
            # ---------------------------------------------

            digest = hashlib.blake2b(
                "\x1f".join(
                    row.get(header, "") or ""
                    for header in headers
                ).encode("utf-8"),
                digest_size=16,
            ).digest()

            if digest in full_row_hashes:
                exact_dupes += 1

            else:
                full_row_hashes.add(
                    digest
                )


            # ---------------------------------------------
            # DUPLICATES ON ALL DIMENSIONS
            # ---------------------------------------------

            dimension_key = key_hash(
                row.get(header)
                for header in dim_cols
            )

            if dimension_key in dim_keys:
                dim_dupes += 1

            else:
                dim_keys.add(
                    dimension_key
                )


            # ---------------------------------------------
            # FOUR CORE DIMENSIONS
            # ---------------------------------------------

            core_key = key_hash(
                (
                    row.get(col_ref),
                    row.get(col_geo),
                    row.get(col_naics),
                    row.get(col_size),
                )
            )

            if core_key in core_keys:
                core_dupes += 1

            else:
                core_keys.add(
                    core_key
                )


            # ---------------------------------------------
            # CORE DIMENSIONS + DGUID
            # ---------------------------------------------

            core5_key = key_hash(
                (
                    row.get(col_ref),
                    row.get(col_geo),
                    row.get(col_dguid),
                    row.get(col_naics),
                    row.get(col_size),
                )
            )

            if core5_key in core5_keys:
                core5_dupes += 1

            else:
                core5_keys.add(
                    core5_key
                )


            # ---------------------------------------------
            # VECTOR + COORDINATE
            # ---------------------------------------------

            if (
                "VECTOR" in headers
                and "COORDINATE" in headers
            ):

                vector_key = key_hash(
                    (
                        row.get("VECTOR"),
                        row.get("COORDINATE"),
                    )
                )

                if vector_key in vector_coord_keys:
                    vector_coord_dupes += 1

                else:
                    vector_coord_keys.add(
                        vector_key
                    )


            # ---------------------------------------------
            # VALUE CHECKS
            # ---------------------------------------------

            value = row.get(
                "VALUE"
            )

            if not is_blank(value):

                try:

                    number = float(
                        value
                    )

                    if vmin is None:
                        vmin = number
                    else:
                        vmin = min(
                            vmin,
                            number,
                        )

                    if vmax is None:
                        vmax = number
                    else:
                        vmax = max(
                            vmax,
                            number,
                        )

                    if number < 0:
                        negative_value += 1

                    if number == 0:
                        zero_value += 1

                except ValueError:
                    non_numeric_value += 1


    # -----------------------------------------------------
    # OUTPUT — STRUCTURE
    # -----------------------------------------------------

    print("=" * 70)

    print(
        f"FILE: {file_path}"
    )

    print("\n1. STRUCTURE")

    print(
        f"Rows (excluding header): "
        f"{row_count:,}"
    )

    print(
        f"Columns: "
        f"{len(headers)}"
    )

    print(
        f"Column names: "
        f"{headers}"
    )

    print(
        "Identifying dimension columns "
        f"used for uniqueness: {dim_cols}"
    )


    # -----------------------------------------------------
    # OUTPUT — GEOGRAPHY
    # -----------------------------------------------------

    print("\n2. GEOGRAPHY")

    print(
        f"Unique GEO values: "
        f"{len(geo_dguid):,}"
    )

    all_dguids = {
        dguid
        for dguids in geo_dguid.values()
        for dguid in dguids
    }

    print(
        f"Unique DGUID values: "
        f"{len(all_dguids):,}"
    )

    prefix_counts = collections.Counter(
        dguid[:9]
        for dguid in all_dguids
        if dguid
    )

    print(
        "Geographic levels: unique DGUIDs "
        "by first 9 characters:"
    )

    for prefix, count in sorted(
        prefix_counts.items()
    ):

        print(
            f"  - {prefix}: "
            f"{count:,}"
        )


    # ---------------------------------------------
    # DUPLICATED GEO NAMES
    # ---------------------------------------------

    shared_geo_names = sum(
        1
        for dguids in geo_dguid.values()
        if len(dguids) > 1
    )

    print(
        "GEO names that map to more "
        f"than one DGUID: {shared_geo_names:,}"
    )


    # ---------------------------------------------
    # NIAGARA MUNICIPALITY CHECK
    # ---------------------------------------------

    print(
        "\nNiagara Region municipality check "
        "using exact GEO names and Niagara DGUIDs:"
    )

    niagara_found = 0

    for municipality in NIAGARA_MUNICIPALITIES:

        matches = []

        for geo, dguids in geo_dguid.items():

            if (
                geo.strip().lower()
                == municipality.lower()
            ):

                niagara_dguids = [
                    dguid
                    for dguid in dguids
                    if NIAGARA_CD_CODE
                    in dguid
                ]

                if niagara_dguids:

                    matches.append(
                        (
                            geo,
                            sorted(
                                niagara_dguids
                            ),
                        )
                    )


        if not matches:

            print(
                f"  - {municipality}: "
                "NOT FOUND as a Niagara municipality"
            )

        else:

            niagara_found += 1

            for geo, dguids in matches:

                print(
                    f"  - {municipality}: "
                    f"GEO='{geo}' | "
                    f"DGUID={dguids}"
                )


    print(
        "\nNiagara municipalities found: "
        f"{niagara_found}/"
        f"{len(NIAGARA_MUNICIPALITIES)}"
    )


    # ---------------------------------------------
    # NIAGARA / ST CATHARINES GEO LABELS
    # ---------------------------------------------

    niagara_any = sorted(
        geo
        for geo in geo_dguid
        if (
            "niagara" in geo.lower()
            or "st. catharines"
            in geo.lower()
        )
    )

    print(
        "\nOther GEO values containing "
        "'Niagara' or 'St. Catharines':"
    )

    for geo in niagara_any:

        print(
            f"  - '{geo}' | "
            f"DGUID="
            f"{sorted(geo_dguid[geo])}"
        )


    # -----------------------------------------------------
    # OUTPUT — BUSINESS INFORMATION
    # -----------------------------------------------------

    print(
        "\n3. BUSINESS INFORMATION"
    )

    if col_size:

        print(
            f"Employment size categories "
            f"in '{col_size}' "
            f"({len(uniques[col_size])}):"
        )

        for category, count in sorted(
            uniques[col_size].items()
        ):

            print(
                f"  - '{category}': "
                f"{count:,} rows"
            )


        lowered = [
            category.lower()
            for category
            in uniques[col_size]
        ]

        print(
            "Contains 'without employees'?",
            any(
                "without" in category
                for category in lowered
            ),
        )

        print(
            "Contains 'indeterminate'?",
            any(
                "indeterminate" in category
                for category in lowered
            ),
        )

    else:

        print(
            "No 'Employment size' "
            "column found."
        )


    # -----------------------------------------------------
    # NAICS
    # -----------------------------------------------------

    if col_naics:

        print(
            f"Unique NAICS values: "
            f"{len(naics_vals):,}"
        )

        len_counts = (
            collections.Counter()
        )

        no_code = []

        names_to_codes = (
            collections.defaultdict(
                set
            )
        )

        for naics in naics_vals:

            match = re.search(
                r"\[([^\]]+)\]\s*$",
                naics,
            )

            if match:

                code = match.group(1)

                first_code = (
                    code.split("-")[0]
                )

                digits = re.sub(
                    r"\D",
                    "",
                    first_code,
                )

                len_counts[
                    len(digits)
                ] += 1

                industry_name = (
                    naics[
                        :match.start()
                    ].strip()
                )

                names_to_codes[
                    industry_name
                ].add(code)

            else:

                no_code.append(
                    naics
                )


        print(
            "NAICS code depth "
            "(digits in bracketed code) "
            "-> number of unique values:"
        )

        for depth, count in sorted(
            len_counts.items()
        ):

            print(
                f"  - {depth}-digit: "
                f"{count:,}"
            )


        print(
            "NAICS values with NO "
            "bracketed code:",
            no_code
            if no_code
            else "none",
        )


        repeated = {
            name: sorted(codes)
            for name, codes
            in names_to_codes.items()
            if len(codes) > 1
        }

        print(
            "Industry names that appear "
            "under more than one code: "
            f"{len(repeated)}"
        )

        for name, codes in sorted(
            repeated.items()
        ):

            print(
                f"  - {name}: "
                f"{codes}"
            )


        print(
            "All NAICS values:"
        )

        for naics in sorted(
            naics_vals
        ):

            print(
                f"  - {naics}"
            )

    else:

        print(
            "No NAICS column found."
        )


    # -----------------------------------------------------
    # OUTPUT — DATA QUALITY
    # -----------------------------------------------------

    print(
        "\n4. DATA QUALITY"
    )

    print(
        "Missing (blank) cells "
        "per column:"
    )

    for header in headers:

        print(
            f"  - {header}: "
            f"{missing[header]:,}"
        )


    for header in (
        "STATUS",
        "SYMBOL",
        "TERMINATED",
    ):

        if header in uniques:

            print(
                f"Distinct values in "
                f"{header}: "
                f"{dict(uniques[header])}"
            )


    print(
        "Exact duplicate rows "
        "(entire row identical): "
        f"{exact_dupes:,}"
    )

    print(
        "Duplicates on all identifying "
        "dimension columns: "
        f"{dim_dupes:,}"
    )

    print(
        "Duplicates on "
        "REF_DATE+GEO+NAICS+"
        "Employment size only: "
        f"{core_dupes:,}"
    )

    print(
        "Duplicates on "
        "REF_DATE+GEO+DGUID+NAICS+"
        "Employment size: "
        f"{core5_dupes:,}"
    )


    if (
        "VECTOR" in headers
        and "COORDINATE" in headers
    ):

        print(
            "Duplicates on "
            "VECTOR+COORDINATE: "
            f"{vector_coord_dupes:,}"
        )


    print(
        "VALUE: "
        f"non-numeric={non_numeric_value:,}, "
        f"negative={negative_value:,}, "
        f"zero={zero_value:,}, "
        f"min={vmin}, "
        f"max={vmax}"
    )


    for header in (
        "UOM",
        "SCALAR_FACTOR",
    ):

        if header in uniques:

            print(
                f"Distinct values in "
                f"{header}: "
                f"{dict(uniques[header])}"
            )


    # -----------------------------------------------------
    # OUTPUT — TIME COVERAGE
    # -----------------------------------------------------

    print(
        "\n5. TIME COVERAGE"
    )

    if col_ref:

        print(
            "Unique REF_DATE values: "
            f"{sorted(uniques[col_ref])}"
        )

        for ref_date, count in sorted(
            uniques[col_ref].items()
        ):

            print(
                f"  - {ref_date}: "
                f"{count:,} rows"
            )


    # -----------------------------------------------------
    # METADATA
    # -----------------------------------------------------

    print(
        "\n6. METADATA "
        "(frequency / reference-period "
        "information)"
    )

    meta_files = [
        path
        for path in glob.glob(
            os.path.join(
                os.path.dirname(file_path)
                or ".",
                "*",
            )
        )
        if (
            "meta"
            in os.path.basename(
                path
            ).lower()
            and path.lower().endswith(
                ".csv"
            )
        )
    ]


    if not meta_files:

        print(
            "  No metadata CSV found "
            "next to the raw file."
        )


    for metadata_file in meta_files:

        print(
            f"  Metadata file: "
            f"{metadata_file}"
        )

        with open(
            metadata_file,
            newline="",
            encoding="utf-8-sig",
            errors="replace",
        ) as metadata:

            for line in metadata:

                line_lower = (
                    line.lower()
                )

                if any(
                    term in line_lower
                    for term in (
                        "frequency",
                        "release",
                        "reference period",
                        "time series",
                        "fluctuations",
                    )
                ):

                    print(
                        "   ",
                        line.strip(),
                    )


    # -----------------------------------------------------
    # SUCCESSION VARIABLES
    # -----------------------------------------------------

    print(
        "\n7. SUCCESSION VARIABLES"
    )

    succession_terms = [
        "owner age",
        "retirement",
        "planned exit",
        "succession",
        "successor",
        "ownership transfer",
        "closure reason",
        "reason for closure",
    ]

    hits = [
        header
        for header in headers
        if any(
            term in header.lower()
            for term
            in succession_terms
        )
    ]


    print(
        "Columns whose names suggest "
        "succession information: "
        f"{hits if hits else 'NONE'}"
    )


if __name__ == "__main__":
    main()
