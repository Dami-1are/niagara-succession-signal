import csv
import os
import re
from collections import Counter, defaultdict

# ---------------------------------------------------------
# FILE PATHS
# ---------------------------------------------------------

DATA_FILE = "data/raw/33101176.csv"
METADATA_FILE = "data/raw/33101176_MetaData.csv"

NAICS_COLUMN = "North American Industry Classification System (NAICS)"

# These are the 12 Niagara Region municipalities.
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

# Niagara census division code = 3526.
NIAGARA_CSD_PREFIX = "2021A00053526"

# St. Catharines - Niagara CMA DGUID.
NIAGARA_CMA_DGUID = "2021S0503539"


# ---------------------------------------------------------
# STORAGE
# ---------------------------------------------------------

row_count = 0
columns = []

geo_values = set()
dguids = set()
geo_to_dguid = defaultdict(set)

employment_sizes = Counter()
naics_values = set()
ref_dates = Counter()

missing = Counter()

status_values = Counter()
symbol_values = Counter()
terminated_values = Counter()

uom_values = Counter()
scalar_factor_values = Counter()

exact_rows = set()
exact_duplicates = 0

dimension_keys = set()
dimension_duplicates = 0

keys_without_dguid = set()
duplicates_without_dguid = 0

vector_coordinate_keys = set()
vector_coordinate_duplicates = 0

value_non_numeric = 0
value_negative = 0
value_zero = 0
value_min = None
value_max = None


# ---------------------------------------------------------
# READ RAW CSV
# ---------------------------------------------------------

with open(DATA_FILE, "r", encoding="utf-8-sig", newline="") as file:
    reader = csv.DictReader(file)

    columns = reader.fieldnames

    for row in reader:
        row_count += 1

        # Missing values
        for column in columns:
            if row[column] is None or row[column].strip() == "":
                missing[column] += 1

        ref_date = row["REF_DATE"].strip()
        geo = row["GEO"].strip()
        dguid = row["DGUID"].strip()
        employment_size = row["Employment size"].strip()
        naics = row[NAICS_COLUMN].strip()

        geo_values.add(geo)
        dguids.add(dguid)
        geo_to_dguid[geo].add(dguid)

        employment_sizes[employment_size] += 1
        naics_values.add(naics)
        ref_dates[ref_date] += 1

        status_values[row["STATUS"].strip()] += 1
        symbol_values[row["SYMBOL"].strip()] += 1
        terminated_values[row["TERMINATED"].strip()] += 1

        uom_values[row["UOM"].strip()] += 1
        scalar_factor_values[row["SCALAR_FACTOR"].strip()] += 1

        # Exact duplicate rows
        exact_key = tuple(row[column] for column in columns)

        if exact_key in exact_rows:
            exact_duplicates += 1
        else:
            exact_rows.add(exact_key)

        # Main identifying dimensions
        dimension_key = (
            ref_date,
            geo,
            dguid,
            employment_size,
            naics,
        )

        if dimension_key in dimension_keys:
            dimension_duplicates += 1
        else:
            dimension_keys.add(dimension_key)

        # Test what happens when DGUID is omitted
        no_dguid_key = (
            ref_date,
            geo,
            naics,
            employment_size,
        )

        if no_dguid_key in keys_without_dguid:
            duplicates_without_dguid += 1
        else:
            keys_without_dguid.add(no_dguid_key)

        # VECTOR + COORDINATE uniqueness
        vector_coordinate = (
            row["VECTOR"].strip(),
            row["COORDINATE"].strip(),
        )

        if vector_coordinate in vector_coordinate_keys:
            vector_coordinate_duplicates += 1
        else:
            vector_coordinate_keys.add(vector_coordinate)

        # VALUE checks
        value_text = row["VALUE"].strip()

        try:
            value = float(value_text)

            if value < 0:
                value_negative += 1

            if value == 0:
                value_zero += 1

            if value_min is None or value < value_min:
                value_min = value

            if value_max is None or value > value_max:
                value_max = value

        except ValueError:
            value_non_numeric += 1


# ---------------------------------------------------------
# GEOGRAPHY CHECKS
# ---------------------------------------------------------

geo_name_duplicates = {
    geo: values
    for geo, values in geo_to_dguid.items()
    if len(values) > 1
}

dguid_prefix_counts = Counter()

for dguid in dguids:
    dguid_prefix_counts[dguid[:9]] += 1


# Only accept Niagara CSD records whose DGUID contains
# Niagara census division code 3526.
niagara_municipality_results = {}

for municipality in NIAGARA_MUNICIPALITIES:
    matches = []

    for geo, geo_dguids in geo_to_dguid.items():
        if geo.lower() == municipality.lower():

            for dguid in geo_dguids:
                if dguid.startswith(NIAGARA_CSD_PREFIX):
                    matches.append((geo, dguid))

    niagara_municipality_results[municipality] = matches


# Niagara CMA check
niagara_cma_present = NIAGARA_CMA_DGUID in dguids


# ---------------------------------------------------------
# NAICS CHECKS
# ---------------------------------------------------------

naics_depth = Counter()
naics_without_code = []

industry_name_to_codes = defaultdict(set)

for label in naics_values:

    match = re.search(r"\[([0-9-]+)\]\s*$", label)

    if match:
        code = match.group(1)

        # Count digits only, so 31-33 is handled separately.
        digits = re.sub(r"\D", "", code)

        if "-" not in code:
            naics_depth[len(digits)] += 1

        industry_name = re.sub(r"\s*\[[^\]]+\]\s*$", "", label)

        industry_name_to_codes[industry_name].add(code)

    else:
        naics_without_code.append(label)


repeated_industry_names = {
    name: codes
    for name, codes in industry_name_to_codes.items()
    if len(codes) > 1
}


# ---------------------------------------------------------
# SUCCESSION COLUMN CHECK
# ---------------------------------------------------------

succession_terms = [
    "owner age",
    "retirement",
    "succession",
    "successor",
    "ownership transfer",
    "planned exit",
    "closure reason",
    "reason for closure",
]

succession_columns = []

for column in columns:
    column_lower = column.lower()

    if any(term in column_lower for term in succession_terms):
        succession_columns.append(column)


# ---------------------------------------------------------
# OUTPUT
# ---------------------------------------------------------

print("=" * 70)
print(f"FILE: {DATA_FILE}")

print("\n1. STRUCTURE")
print(f"Rows (excluding header): {row_count:,}")
print(f"Columns: {len(columns)}")
print(f"Column names: {columns}")

print("\n2. GEOGRAPHY")
print(f"Unique GEO values: {len(geo_values):,}")
print(f"Unique DGUID values: {len(dguids):,}")

print("DGUID prefixes:")
for prefix, count in sorted(dguid_prefix_counts.items()):
    print(f"  - {prefix}: {count:,}")

print(
    f"GEO names that map to more than one DGUID: "
    f"{len(geo_name_duplicates):,}"
)

print("\nNiagara Region municipality verification:")

for municipality in NIAGARA_MUNICIPALITIES:
    matches = niagara_municipality_results[municipality]

    if matches:
        print(f"  - {municipality}: {matches}")
    else:
        print(f"  - {municipality}: NOT FOUND")

print(
    f"\nSt. Catharines - Niagara CMA present: "
    f"{niagara_cma_present}"
)

print("\n3. BUSINESS INFORMATION")

print(
    f"Employment size categories "
    f"({len(employment_sizes)}):"
)

for category, count in sorted(employment_sizes.items()):
    print(f"  - {category}: {count:,} rows")

print(
    "Contains 'without employees'?",
    any(
        "without employees" in category.lower()
        for category in employment_sizes
    ),
)

print(
    "Contains 'indeterminate'?",
    any(
        "indeterminate" in category.lower()
        for category in employment_sizes
    ),
)

print(f"Unique NAICS values: {len(naics_values):,}")

print("NAICS code depth:")
for depth, count in sorted(naics_depth.items()):
    print(f"  - {depth}-digit: {count:,}")

print(
    "NAICS values with no bracketed code:",
    len(naics_without_code),
)

print(
    "Industry names appearing under more than one code:",
    len(repeated_industry_names),
)

print("\n4. DATA QUALITY")

print("Missing cells per column:")
for column in columns:
    print(f"  - {column}: {missing[column]:,}")

print(
    f"Exact duplicate rows: "
    f"{exact_duplicates:,}"
)

print(
    f"Duplicates on identifying dimensions: "
    f"{dimension_duplicates:,}"
)

print(
    "Duplicates without DGUID: "
    f"{duplicates_without_dguid:,}"
)

print(
    "Duplicates on VECTOR + COORDINATE: "
    f"{vector_coordinate_duplicates:,}"
)

print(
    "VALUE:",
    f"non-numeric={value_non_numeric:,},",
    f"negative={value_negative:,},",
    f"zero={value_zero:,},",
    f"min={value_min},",
    f"max={value_max}",
)

print(f"STATUS values: {dict(status_values)}")
print(f"SYMBOL values: {dict(symbol_values)}")
print(f"TERMINATED values: {dict(terminated_values)}")

print(f"UOM values: {dict(uom_values)}")
print(
    f"SCALAR_FACTOR values: "
    f"{dict(scalar_factor_values)}"
)

print("\n5. TIME COVERAGE")

for date, count in sorted(ref_dates.items()):
    print(f"  - {date}: {count:,} rows")


# ---------------------------------------------------------
# METADATA
# ---------------------------------------------------------

print("\n6. METADATA")

if os.path.exists(METADATA_FILE):

    print(f"Metadata file: {METADATA_FILE}")

    with open(
        METADATA_FILE,
        "r",
        encoding="utf-8-sig",
        errors="replace",
    ) as metadata:

        for line in metadata:

            if (
                "Cube Title" in line
                or "Business Counts" in line
                or "Frequency" in line
                or "Start Reference Period" in line
                or "End Reference Period" in line
                or "time series" in line.lower()
                or "Fluctuations in these figures" in line
            ):
                print(line.strip())

else:
    print("Metadata file not found.")


print("\n7. SUCCESSION VARIABLES")

if succession_columns:
    print(
        "Columns whose names suggest succession information:",
        succession_columns,
    )
else:
    print(
        "Columns whose names suggest succession information: NONE"
    )
