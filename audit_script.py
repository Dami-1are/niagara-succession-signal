"""
Audit script for Statistics Canada Table 33-10-1176-01 (Canadian Business Counts).

Read-only: the raw CSV is never modified. No cleaning, filtering or merging is done.
Usage (from the repository root):
    python audit_script.py                      # uses data/raw/33101176.csv
    python audit_script.py path/to/file.csv     # optional override
Tip: save the output so the audit report can cite it:
    python audit_script.py > docs/data_audits/audit_script_output.txt
"""
import collections
import csv
import glob
import hashlib
import os
import re
import sys

DEFAULT_PATH = "data/raw/33101176.csv"
file_path = sys.argv[1] if len(sys.argv) > 1 else DEFAULT_PATH

# The 12 Niagara Region municipalities (names searched in the GEO column).
NIAGARA_MUNICIPALITIES = [
    "Fort Erie", "Grimsby", "Lincoln", "Niagara Falls", "Niagara-on-the-Lake",
    "Pelham", "Port Colborne", "St. Catharines", "Thorold", "Wainfleet",
    "Welland", "West Lincoln",
]

# Columns that hold measures, flags, units or StatCan series identifiers rather than
# the real dimensions (REF_DATE, GEO, DGUID, Employment size, NAICS).
NON_DIMENSION_COLS = {"VALUE", "STATUS", "SYMBOL", "TERMINATED", "DECIMALS",
                      "UOM", "UOM_ID", "SCALAR_FACTOR", "SCALAR_ID", "VECTOR", "COORDINATE"}


def find_col(headers, startswith):
    for h in headers:
        if h.strip().lower().startswith(startswith.lower()):
            return h
    return None


def key_hash(values):
    """Compact 16-byte fingerprint of a key, so 1M+ rows don't exhaust memory."""
    joined = "\x1f".join((v or "") for v in values)
    return hashlib.blake2b(joined.encode("utf-8"), digest_size=16).digest()


def is_blank(x):
    return x is None or x.strip() == ""


def main():
    if not os.path.isfile(file_path):
        print(f"ERROR: raw data file not found: '{file_path}'")
        print(f"       Current working directory: {os.getcwd()}")
        print("       Run this script from the repository root, or pass the CSV path as an argument.")
        print("       If the file is stored with Git LFS, run 'git lfs pull' first.")
        sys.exit(1)

    with open(file_path, newline="", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        headers = reader.fieldnames
        col_ref = find_col(headers, "REF_DATE")
        col_geo = find_col(headers, "GEO")
        col_dguid = find_col(headers, "DGUID")
        col_naics = find_col(headers, "North American Industry")
        col_size = find_col(headers, "Employment size")
        dim_cols = [h for h in headers if h not in NON_DIMENSION_COLS]

        row_count = 0
        missing = collections.Counter()          # blank cells per column
        uniques = {h: collections.Counter() for h in headers
                   if h in {col_ref, col_size, "STATUS", "SYMBOL", "UOM", "SCALAR_FACTOR", "TERMINATED"}}
        geo_dguid = {}                           # GEO -> set of DGUIDs
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
        vmin, vmax = None, None

        for row in reader:
            row_count += 1
            for h in headers:
                if is_blank(row.get(h)):
                    missing[h] += 1
            for h, counter in uniques.items():
                counter[row[h]] += 1
            if col_geo:
                geo_dguid.setdefault(row[col_geo], set()).add(row.get(col_dguid, "") if col_dguid else "")
            if col_naics:
                naics_vals.add(row[col_naics])

            # exact duplicate (entire row)
            digest = hashlib.blake2b("\x1f".join(row[h] or "" for h in headers).encode("utf-8"),
                                     digest_size=16).digest()
            if digest in full_row_hashes:
                exact_dupes += 1
            else:
                full_row_hashes.add(digest)

            # duplicate on all identifying dimension columns
            k = key_hash(row[h] for h in dim_cols)
            if k in dim_keys:
                dim_dupes += 1
            else:
                dim_keys.add(k)

            # duplicate on the 4 "core" business dimensions only
            ck = key_hash((row.get(col_ref), row.get(col_geo), row.get(col_naics), row.get(col_size)))
            if ck in core_keys:
                core_dupes += 1
            else:
                core_keys.add(ck)

            # same 4 fields PLUS DGUID (tests whether DGUID explains the 4-field duplicates)
            ck5 = key_hash((row.get(col_ref), row.get(col_geo), row.get(col_dguid), row.get(col_naics), row.get(col_size)))
            if ck5 in core5_keys:
                core5_dupes += 1
            else:
                core5_keys.add(ck5)

            # duplicate on VECTOR + COORDINATE (if present)
            if "VECTOR" in headers and "COORDINATE" in headers:
                vk = key_hash((row["VECTOR"], row["COORDINATE"]))
                if vk in vector_coord_keys:
                    vector_coord_dupes += 1
                else:
                    vector_coord_keys.add(vk)

            # unusual values in VALUE
            v = row.get("VALUE")
            if not is_blank(v):
                try:
                    num = float(v)
                    vmin = num if vmin is None else min(vmin, num)
                    vmax = num if vmax is None else max(vmax, num)
                    if num < 0:
                        negative_value += 1
                    if num == 0:
                        zero_value += 1
                except ValueError:
                    non_numeric_value += 1

    print("=" * 70)
    print(f"FILE: {file_path}")
    print("1. STRUCTURE")
    print(f"Rows (excluding header): {row_count:,}")
    print(f"Columns: {len(headers)}")
    print(f"Column names: {headers}")
    print(f"Identifying dimension columns used for uniqueness: {dim_cols}")

    print("\n2. GEOGRAPHY")
    print(f"Unique GEO values: {len(geo_dguid):,}")
    all_dguids = {d for ds in geo_dguid.values() for d in ds}
    prefix_counts = collections.Counter(d[:9] for d in all_dguids)
    print(f"Unique DGUID values: {len(all_dguids):,}")
    print("Geographic levels: unique DGUIDs by first 9 characters (vintage + type + schema).")
    print("  Confirm what each prefix means in StatCan's DGUID documentation, e.g. ...0005 = census")
    print("  subdivision, S0503 = CMA/CA:")
    for p, c in sorted(prefix_counts.items()):
        print(f"  - {p}: {c:,}")
    shared = sum(1 for ds in geo_dguid.values() if len(ds) > 1)
    print(f"GEO names that map to more than one DGUID: {shared:,}")
    print("Niagara Region municipality check (case-insensitive match on GEO; verify manually):")
    for name in NIAGARA_MUNICIPALITIES:
        matches = sorted(g for g in geo_dguid if name.lower() in g.lower())
        if not matches:
            print(f"  - {name}: NOT FOUND in this dataset")
        for g in matches:
            print(f"  - {name}: GEO='{g}' | DGUID={sorted(geo_dguid[g])}")
    print("  (Check each match is actually the Niagara one: Niagara census division code is 3526,")
    print("   so Niagara CSD DGUIDs should contain it. 'Lincoln' also matches non-Niagara places.)")
    niagara_any = sorted(g for g in geo_dguid if "niagara" in g.lower() or "st. catharines" in g.lower())
    print("All GEO values containing 'Niagara' or 'St. Catharines':")
    for g in niagara_any:
        print(f"  - '{g}' | DGUID={sorted(geo_dguid[g])}")

    print("\n3. BUSINESS INFORMATION")
    if col_size:
        print(f"Employment size categories in '{col_size}' ({len(uniques[col_size])}):")
        for k, c in sorted(uniques[col_size].items()):
            print(f"  - '{k}': {c:,} rows")
        lowered = [k.lower() for k in uniques[col_size]]
        print("Contains 'without employees'?", any("without" in k for k in lowered))
        print("Contains 'indeterminate'?", any("indeterminate" in k for k in lowered))
    else:
        print("No 'Employment size' column found.")
    if col_naics:
        print(f"Unique NAICS values: {len(naics_vals):,}")
        len_counts = collections.Counter()
        no_code = []
        names_to_codes = collections.defaultdict(set)
        for n in naics_vals:
            m = re.search(r"\[([^\]]+)\]\s*$", n)
            if m:
                digits = re.sub(r"\D", "", m.group(1).split("-")[0])
                len_counts[len(digits)] += 1
                names_to_codes[n[:m.start()].strip()].add(m.group(1))
            else:
                no_code.append(n)
        print("NAICS code depth (digits in the bracketed code) -> number of unique NAICS values:")
        for d, c in sorted(len_counts.items()):
            print(f"  - {d}-digit: {c:,}")
        print(f"NAICS values with NO bracketed code: {no_code if no_code else 'none'}")
        repeated = {k: sorted(v) for k, v in names_to_codes.items() if len(v) > 1}
        print(f"Industry names that appear under more than one code: {len(repeated)}")
        for k, v in sorted(repeated.items()):
            print(f"  - {k}: {v}")
        print("All NAICS values:")
        for n in sorted(naics_vals):
            print(f"  - {n}")
    else:
        print("No NAICS column found.")

    print("\n4. DATA QUALITY")
    print("Missing (blank) cells per column:")
    for h in headers:
        print(f"  - {h}: {missing[h]:,}")
    for h in ("STATUS", "SYMBOL", "TERMINATED"):
        if h in uniques:
            print(f"Distinct values in {h}: {dict(uniques[h])}")
    print(f"Exact duplicate rows (entire row identical): {exact_dupes:,}")
    print(f"Duplicates on all identifying dimension columns: {dim_dupes:,}")
    print(f"Duplicates on REF_DATE+GEO+NAICS+Employment size only: {core_dupes:,}")
    print(f"Duplicates on REF_DATE+GEO+DGUID+NAICS+Employment size: {core5_dupes:,}")
    if "VECTOR" in headers and "COORDINATE" in headers:
        print(f"Duplicates on VECTOR+COORDINATE: {vector_coord_dupes:,}")
    print(f"VALUE: non-numeric={non_numeric_value:,}, negative={negative_value:,}, "
          f"zero={zero_value:,}, min={vmin}, max={vmax}")
    for h in ("UOM", "SCALAR_FACTOR"):
        if h in uniques:
            print(f"Distinct values in {h}: {dict(uniques[h])}")

    print("\n5. TIME COVERAGE")
    if col_ref:
        print(f"Unique REF_DATE values: {sorted(uniques[col_ref])}")
        for k, c in sorted(uniques[col_ref].items()):
            print(f"  - {k}: {c:,} rows")

    print("\n6. METADATA (frequency / release info, if a metadata file is present in data/raw/)")
    meta_files = [p for p in glob.glob(os.path.join(os.path.dirname(file_path) or ".", "*"))
                  if "meta" in os.path.basename(p).lower() and p.lower().endswith(".csv")]
    if not meta_files:
        print("  No metadata CSV found next to the raw file.")
    for mf in meta_files:
        print(f"  Metadata file: {mf}")
        with open(mf, newline="", encoding="utf-8-sig", errors="replace") as m:
            for line in m:
                if any(w in line.lower() for w in ("frequency", "release", "reference period")):
                    print("   ", line.strip())

    print("\n7. SUCCESSION VARIABLES")
    wanted = ["owner age", "age", "retire", "exit", "succession", "successor", "transfer", "closure"]
    hits = [h for h in headers if any(w in h.lower() for w in wanted)]
    print(f"Columns whose names suggest succession information: {hits if hits else 'NONE'}")


if __name__ == "__main__":
    main()
