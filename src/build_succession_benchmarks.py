from pathlib import Path
import re
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]

STATCAN_FILES = {
    "1196": ROOT / "data/interim/statcan_33101196_ontario_cleaned.csv",
    "1197": ROOT / "data/interim/statcan_33101197_ontario_cleaned.csv",
    "1198": ROOT / "data/interim/statcan_33101198_ontario_cleaned.csv",
    "1199": ROOT / "data/interim/statcan_33101199_ontario_cleaned.csv",
}
CFIB_FILE = ROOT / "data/processed/cfib/cfib_succession_evidence_structured.csv"
SECTOR_CROSSWALK = ROOT / "data/processed/layer/crosswalk_naics_sector.csv"
OUTPUT_DIR = ROOT / "data/processed/layer"
NOTES_DIR = ROOT / "docs/layer_notes"

STANDARD_COLUMNS = [
    "geography_level", "geography", "year",
    "table_id", "business_characteristic", "characteristic_group",
    "naics_sector_code", "naics_sector_label", "size_band",
    "measure", "category", "value", "unit", "value_status",
    "quality_flag", "caution", "caution_flag",
    "evidence_type", "source",
]

CFIB_COLUMNS = [
    "geography_level", "geography", "year", "ref_period",
    "naics_sector_code", "naics_sector_label", "size_band",
    "measure", "value", "unit", "value_status",
    "quality_flag", "caution_flag", "evidence_type", "source",
    "population", "source_page", "notes",
]

PROXY_COLUMNS = [
    "proxy_name", "table", "what_it_measures",
    "why_relevant_to_succession", "what_it_is_not",
    "evidence_type", "source", "limitations",
]


def read_csv(path):
    if not path.exists():
        raise FileNotFoundError(f"Required input is missing: {path}")
    return pd.read_csv(path, dtype=str, keep_default_na=False)


def build_sector_map():
    df = read_csv(SECTOR_CROSSWALK)
    required = {"naics_sector_code", "naics_sector_label"}
    if not required.issubset(df.columns):
        raise ValueError(f"Sector crosswalk needs columns: {required}")

    mapping = {}
    for _, row in df.iterrows():
        code = str(row["naics_sector_code"]).strip()
        label = str(row["naics_sector_label"]).strip()
        if code and label:
            mapping[code] = label
    return mapping


def find_sector(text, sector_map):
    text = str(text)
    match = re.search(r"\[(\d{2})\]", text)
    if match and match.group(1) in sector_map:
        code = match.group(1)
        return code, sector_map[code]

    if "all industries" in text.lower():
        return "ALL", "All industries"

    return "UNCLASSIFIED", "Unclassified"


def build_ontario_benchmark(sector_map):
    expected_rows = {
        "1196": 476,
        "1197": 476,
        "1198": 1360,
        "1199": 1020,
    }
    frames = []

    measure_columns = {
        "1196": "Intentions for businesses to sell or transfer ownership within the next 10 years",
        "1197": "Expectations related to selling or transferring of the business",
        "1198": "Considerations related to the sale or transfer of the business",
        "1199": "Various scenarios if business is unable to find a suitable buyer or successor",
    }

    for table_id, path in STATCAN_FILES.items():
        df = read_csv(path)

        if len(df) != expected_rows[table_id]:
            raise ValueError(
                f"{path.name}: expected {expected_rows[table_id]} rows, "
                f"found {len(df)}"
            )

        measure_col = measure_columns[table_id]
        required = {
            "REF_DATE", "GEO", "Business characteristics",
            "VALUE", "STATUS", "UOM", measure_col,
        }
        missing = required - set(df.columns)
        if missing:
            raise ValueError(f"{path.name} is missing columns: {missing}")

        for _, row in df.iterrows():
            sector_code, sector_label = find_sector(
                row["Business characteristics"], sector_map
            )

            dimensions = [str(row[measure_col]).strip()]
            for col in ["Level of importance", "Likelihood"]:
                if col in df.columns and str(row[col]).strip():
                    dimensions.append(str(row[col]).strip())

            characteristics = str(row["Business characteristics"])
            size_match = re.search(
                r"(1 to 4 employees|5 to 19 employees|"
                r"20 to 99 employees|100 or more employees)",
                characteristics,
                flags=re.IGNORECASE,
            )
            if size_match:
                dimensions.append(f"Source size group: {size_match.group(1)}")

            measure = " | ".join(x for x in dimensions if x)
            raw_value = str(row["VALUE"]).strip()
            quality = str(row["STATUS"]).strip()

            if raw_value in {"", "..", "F"} or quality in {"F", ".."}:
                value = pd.NA
            else:
                try:
                    value = float(raw_value.replace(",", ""))
                except ValueError:
                    value = pd.NA

            if quality == "F":
                value_status = "suppressed"
            elif quality == ".." or pd.isna(value):
                value_status = "not_available"
            else:
                value_status = "ok"

            # E indicates a caution flag; D remains unflagged unless confirmed.
            caution = quality == "E"

            characteristic = str(row["Business characteristics"]).strip()

            lower_characteristic = characteristic.lower()
            if "all industries" in lower_characteristic:
                characteristic_group = "other"
            elif re.search(r"\[\d{2}\]", characteristic):
                characteristic_group = "sector"
            elif re.search(
                r"(1 to 4 employees|5 to 19 employees|"
                r"20 to 99 employees|100 or more employees)",
                characteristic,
                flags=re.IGNORECASE,
            ):
                characteristic_group = "size"
            elif "years" in lower_characteristic or "age" in lower_characteristic:
                characteristic_group = "business age"
            elif "ownership" in lower_characteristic or "owner" in lower_characteristic:
                characteristic_group = "ownership"
            else:
                characteristic_group = "other"

            # Preserve the source response label rather than guessing categories.
            category = str(row[measure_col]).strip()

            frames.append({
                "geography_level": "ontario",
                "geography": "Ontario",
                "year": int(float(row["REF_DATE"])),
                "table_id": f"33-10-{table_id}-01",
                "business_characteristic": characteristic,
                "characteristic_group": characteristic_group,
                "naics_sector_code": sector_code,
                "naics_sector_label": sector_label,
                "size_band": "no_size_band",
                "measure": measure_columns[table_id],
                "category": category,
                "value": value,
                "unit": "percent",
                "value_status": value_status,
                "quality_flag": quality,
                "caution": caution,
                "caution_flag": caution,
                "evidence_type": "benchmark_not_niagara",
                "source": f"Statistics Canada table 33-10-{table_id}-01",
            })

    result = pd.DataFrame(frames, columns=STANDARD_COLUMNS)

    if len(result) != 3332:
        raise AssertionError(f"Expected 3,332 rows, found {len(result)}")

    if (
        result.loc[result["quality_flag"].eq("F"), "value"].notna().any()
        or result.loc[result["quality_flag"].eq(".."), "value"].notna().any()
    ):
        raise AssertionError("F/.. values must remain missing")

    return result


def build_cfib_benchmark():
    df = read_csv(CFIB_FILE)
    required = {
        "source", "source_year", "topic", "measure", "category",
        "value", "unit", "population", "geography", "source_page", "notes",
    }
    missing = required - set(df.columns)
    if missing:
        raise ValueError(f"CFIB input is missing columns: {missing}")
    if len(df) != 13:
        raise ValueError(f"Expected 13 CFIB rows, found {len(df)}")

    records = []
    for _, row in df.iterrows():
        raw_value = str(row["value"]).strip()
        try:
            value = float(raw_value.replace(",", "")) if raw_value else pd.NA
        except ValueError:
            value = pd.NA

        measure_parts = [
            str(row["topic"]).strip(),
            str(row["measure"]).strip(),
            str(row["category"]).strip(),
        ]

        records.append({
            "geography_level": "canada",
            "geography": "Canada",
            "year": int(float(row["source_year"])),
            "ref_period": "",
            "naics_sector_code": "ALL",
            "naics_sector_label": "All sectors",
            "size_band": "no_size_band",
            "measure": " | ".join(x for x in measure_parts if x),
            "value": value,
            "unit": str(row["unit"]).strip().lower() or "percent",
            "value_status": "ok" if not pd.isna(value) else "not_available",
            "quality_flag": "",
            "caution_flag": False,
            "evidence_type": "benchmark_not_niagara",
            "source": f'{row["source"]} ({row["source_year"]})',
            "population": row["population"],
            "source_page": row["source_page"],
            "notes": row["notes"],
        })

    return pd.DataFrame(records, columns=CFIB_COLUMNS)


def build_proxy_register():
    rows = [
        {
            "proxy_name": "Business age (NEI opening_year)",
            "table": "NEI business inventory",
            "what_it_measures": "Years since a business opened, grouped into age bands.",
            "why_relevant_to_succession": "Business maturity may help identify businesses for further succession research.",
            "what_it_is_not": "The owner's age or proof that succession is planned.",
            "evidence_type": "proxy",
            "source": "NEI; opening_year",
            "limitations": "Opening year may be missing or inaccurate; age alone does not establish succession risk.",
        },
        {
            "proxy_name": "Micro-business share (CBC, 1-4 employees)",
            "table": "Canadian Business Counts",
            "what_it_measures": "Share of employer businesses with 1-4 employees.",
            "why_relevant_to_succession": "Small employer businesses may have different continuity and transfer constraints.",
            "what_it_is_not": "A measure of owner-operators or succession plans.",
            "evidence_type": "proxy",
            "source": "Canadian Business Counts; size-band crosswalk",
            "limitations": "Excludes non-employer businesses and does not identify owner age or transfer intentions.",
        },
        {
            "proxy_name": "Sector exposure",
            "table": "NEI / Canadian Business Counts / benchmark tables",
            "what_it_measures": "Business distribution by industry sector.",
            "why_relevant_to_succession": "Provides industry context for comparing business composition and possible succession pressures.",
            "what_it_is_not": "A direct measure of succession risk.",
            "evidence_type": "proxy",
            "source": "NAICS sector crosswalk and source datasets",
            "limitations": "Sector differences do not prove a business will close or transfer.",
        },
        {
            "proxy_name": "Population aged 65+ share",
            "table": "Census population by age",
            "what_it_measures": "Share of municipal residents aged 65 or older.",
            "why_relevant_to_succession": "Provides demographic context for communities where succession support may be relevant.",
            "what_it_is_not": "The share of business owners aged 65+.",
            "evidence_type": "context",
            "source": "Statistics Canada Census age data",
            "limitations": "Resident age is not business-owner age or a measure of retirement intentions.",
        },
        {
            "proxy_name": "Population aged 55-64 share",
            "table": "Census population by age",
            "what_it_measures": "Share of municipal residents aged 55-64.",
            "why_relevant_to_succession": "Provides context on the population approaching typical retirement ages.",
            "what_it_is_not": "Owners' retirement plans or business succession risk.",
            "evidence_type": "context",
            "source": "Statistics Canada Census age data",
            "limitations": "Population-level age structure cannot be assigned to business owners.",
        },
        {
            "proxy_name": "Self-employed by age and sector",
            "table": "Census self-employment",
            "what_it_measures": "Counts of self-employed people by age group and sector at Niagara-wide level.",
            "why_relevant_to_succession": "Shows age patterns among self-employed people that may inform further research.",
            "what_it_is_not": "A direct count of business owners or a municipal-level measure.",
            "evidence_type": "context",
            "source": "Statistics Canada Census self-employment data",
            "limitations": "Self-employment does not equal business ownership; geography and classification limits apply.",
        },
        {
            "proxy_name": "NEI inventory turnover",
            "table": "NEI year-over-year inventory comparison",
            "what_it_measures": "Businesses newly listed or marked closed/vacant between inventory snapshots.",
            "why_relevant_to_succession": "Provides an indirect local signal of changes in the business inventory.",
            "what_it_is_not": "A closure rate or proof that a succession occurred.",
            "evidence_type": "proxy",
            "source": "NEI inventory snapshots",
            "limitations": "Inventory changes can reflect data coverage, listing updates, relocation, or status changes.",
        },
        {
            "proxy_name": "Ontario sale/transfer intention by sector",
            "table": "benchmark_ontario_succession",
            "what_it_measures": "Ontario survey shares reporting an intention to sell or transfer a business within 10 years.",
            "why_relevant_to_succession": "Offers provincial context for succession intentions by business characteristics.",
            "what_it_is_not": "A Niagara rate or evidence that a sale/transfer occurred.",
            "evidence_type": "benchmark_not_niagara",
            "source": "Statistics Canada tables 33-10-1196 to 33-10-1199",
            "limitations": "Survey estimates are provincial, aggregated and subject to source quality flags.",
        },
        {
            "proxy_name": "Ontario exit rate by sector and size",
            "table": "benchmark_ontario_dynamics",
            "what_it_measures": "Ontario employer businesses that stopped being active, by sector and size group.",
            "why_relevant_to_succession": "Adds broader business-dynamics context for interpreting continuity challenges.",
            "what_it_is_not": "A succession-related closure rate.",
            "evidence_type": "benchmark_not_niagara",
            "source": "Statistics Canada Business Dynamics",
            "limitations": "Ontario-wide benchmark; exit does not establish the reason a business stopped operating.",
        },
        {
            "proxy_name": "CFIB succession planning gaps",
            "table": "benchmark_canada_cfib",
            "what_it_measures": "Canadian survey evidence on succession plans, exit methods and reported obstacles.",
            "why_relevant_to_succession": "Provides national context on planning gaps and transfer challenges.",
            "what_it_is_not": "A Niagara or Ontario estimate.",
            "evidence_type": "benchmark_not_niagara",
            "source": "CFIB, Succession Tsunami (2022)",
            "limitations": "National survey from 2022; response categories may allow multiple answers and must retain source notes.",
        },
    ]
    return pd.DataFrame(rows, columns=PROXY_COLUMNS)


def write_notes():
    notes = """# Week 6 - Succession Benchmark Table and Proxy Register

## Purpose and scope

This layer keeps Ontario Statistics Canada succession survey estimates and Canadian Federation of Independent Business (CFIB) national survey evidence separate from Niagara-specific observations. Ontario and Canada values are benchmarks, not measured Niagara rates.

## Reproducibility

Run `python src/build_succession_benchmarks.py`. The script reads the four cleaned Ontario StatCan tables, the structured 13-row CFIB table and the sector crosswalk. It does not edit `data/raw/`.

## Ontario StatCan benchmark

All 3,332 source rows are retained (476 + 476 + 1,360 + 1,020). Survey values remain percentages and reference year 2026 is preserved.

- `STATUS == F`: `value_status=suppressed`; value remains missing because the estimate is too unreliable to publish.
- `STATUS == ..`: `value_status=not_available`; value remains missing because it is unavailable for the reference period.
- Original status codes are retained in `quality_flag`.
- `E` rows are flagged with `caution_flag=True`; `D` rows are not flagged unless the project lead confirms otherwise.
- Suppressed or unavailable values are never imputed or replaced with zero.
- Source size bins are retained in the measure label and are not forced into incompatible standard size bands.

## CFIB benchmark

All 13 CFIB rows are retained, including population, source page and notes. The evidence is from Canada in 2022, not Niagara or Ontario. Where the source permits multiple responses, categories must not be treated as mutually exclusive.

## Proxy register

The register documents the ten proxies in the Week 6 specification. It distinguishes indirect proxies from demographic context and provincial/national benchmarks. Self-employment is not described as a direct business-owner count; population age is not owner age; business exits are not automatically succession-related closures.

## Limitations and decisions to confirm

1. There is no direct Niagara succession variable or Niagara business-owner age in this layer.
2. NEI inventory turnover is an indirect inventory-change signal, not a closure rate or succession measure.
3. Ontario survey results and national CFIB evidence must not be presented as Niagara rates.
4. The `D` and `E` caution treatment is provisional and requires confirmation.
5. NEI licensing and redistribution permission remain unresolved; do not redistribute NEI source records until licensing is confirmed.
6. Small-cell modelling rules remain open in the draft specification.

## Validation

The builder checks expected row counts for each StatCan input, the combined 3,332-row total, the 13-row CFIB total, and that F/.. values remain missing. Outputs are written under `data/processed/layer/`.
"""
    (NOTES_DIR / "succession_benchmark_notes.md").write_text(
        notes, encoding="utf-8"
    )


def main():
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    NOTES_DIR.mkdir(parents=True, exist_ok=True)

    sector_map = build_sector_map()
    ontario = build_ontario_benchmark(sector_map)
    cfib = build_cfib_benchmark()
    proxies = build_proxy_register()

    ontario_path = OUTPUT_DIR / "benchmark_ontario_succession.csv"
    cfib_path = OUTPUT_DIR / "benchmark_canada_cfib.csv"
    proxy_path = OUTPUT_DIR / "proxy_register.csv"

    ontario.to_csv(ontario_path, index=False)
    cfib.to_csv(cfib_path, index=False)
    proxies.to_csv(proxy_path, index=False)
    write_notes()

    print("Succession benchmark build complete.")
    print(f"Ontario StatCan rows: {len(ontario):,}")
    print(f"Canada CFIB rows: {len(cfib):,}")
    print(f"Proxy register rows: {len(proxies):,}")
    print(f"Methods note: {NOTES_DIR / 'succession_benchmark_notes.md'}")
    print("\nOntario value-status counts:")
    print(ontario["value_status"].value_counts(dropna=False).to_string())
    print("\nOntario quality-flag counts:")
    print(
        ontario["quality_flag"].replace("", "(blank)")
        .value_counts(dropna=False).to_string()
    )


if __name__ == "__main__":
    main()
