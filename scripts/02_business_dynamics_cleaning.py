from pathlib import Path

import pandas as pd


# ============================================================
# BUSINESS DYNAMICS CLEANING
# Statistics Canada tables 33-10-0087-01 and 33-10-0088-01
# ============================================================

PROJECT_ROOT = Path(__file__).resolve().parents[1]

RAW_DIR = (
    PROJECT_ROOT
    / "data"
    / "raw"
    / "statcan"
    / "business_dynamics"
)

PROCESSED_DIR = (
    PROJECT_ROOT
    / "data"
    / "processed"
    / "statcan"
    / "business_dynamics"
)

PROCESSED_DIR.mkdir(parents=True, exist_ok=True)

RAW_INDUSTRY = RAW_DIR / "33100087.csv"
RAW_FIRM_SIZE = RAW_DIR / "33100088.csv"

INDUSTRY_OUTPUT = (
    PROCESSED_DIR
    / "business_dynamics_industry_ontario_cleaned.csv"
)

FIRM_SIZE_OUTPUT = (
    PROCESSED_DIR
    / "business_dynamics_firm_size_ontario_cleaned.csv"
)

ONTARIO_DGUID = "2016A000235"


def assign_naics_version(year):
    if year == 2001:
        return "1997 NAICS"
    if 2002 <= year <= 2006:
        return "2002 NAICS"
    if 2007 <= year <= 2011:
        return "2007 NAICS"
    if year >= 2012:
        return "2012 NAICS"
    return pd.NA


def validate(condition, message):
    if not condition:
        raise ValueError(f"VALIDATION FAILED: {message}")


print("=" * 70)
print("BUSINESS DYNAMICS CLEANING")
print("=" * 70)

# ============================================================
# 1. CHECK RAW FILES
# ============================================================

validate(RAW_INDUSTRY.exists(), f"Missing raw file: {RAW_INDUSTRY}")
validate(RAW_FIRM_SIZE.exists(), f"Missing raw file: {RAW_FIRM_SIZE}")

# ============================================================
# 2. LOAD RAW DATA
# ============================================================

industry_raw = pd.read_csv(RAW_INDUSTRY)
firm_size_raw = pd.read_csv(RAW_FIRM_SIZE)

print("\nRAW DATASET SHAPES")
print("Industry:", industry_raw.shape)
print("Firm-size:", firm_size_raw.shape)

validate(
    industry_raw.shape == (27324, 16),
    f"Unexpected industry raw shape: {industry_raw.shape}",
)

validate(
    firm_size_raw.shape == (9108, 16),
    f"Unexpected firm-size raw shape: {firm_size_raw.shape}",
)

# ============================================================
# 3. FILTER ONTARIO
# ============================================================

industry_ontario = industry_raw[
    industry_raw["DGUID"].eq(ONTARIO_DGUID)
].copy()

firm_size_ontario = firm_size_raw[
    firm_size_raw["DGUID"].eq(ONTARIO_DGUID)
].copy()

print("\nONTARIO DATASET SHAPES")
print("Industry:", industry_ontario.shape)
print("Firm-size:", firm_size_ontario.shape)

validate(
    industry_ontario.shape == (2484, 16),
    f"Unexpected Ontario industry shape: {industry_ontario.shape}",
)

validate(
    firm_size_ontario.shape == (828, 16),
    f"Unexpected Ontario firm-size shape: {firm_size_ontario.shape}",
)

validate(
    industry_ontario["GEO"].eq("Ontario").all(),
    "Industry dataset contains non-Ontario GEO values.",
)

validate(
    firm_size_ontario["GEO"].eq("Ontario").all(),
    "Firm-size dataset contains non-Ontario GEO values.",
)

# ============================================================
# 4. CLEAN INDUSTRY DATASET
# ============================================================

industry_column_map = {
    "REF_DATE": "ref_date",
    "GEO": "geo",
    "DGUID": "dguid",
    "Business dynamics measure": "business_dynamics_measure",
    "North American Industry Classification System (NAICS)": "naics",
    "UOM": "uom",
    "UOM_ID": "uom_id",
    "SCALAR_FACTOR": "scalar_factor",
    "SCALAR_ID": "scalar_id",
    "VECTOR": "vector",
    "COORDINATE": "coordinate",
    "VALUE": "value",
    "STATUS": "status",
    "SYMBOL": "symbol",
    "TERMINATED": "terminated",
    "DECIMALS": "decimals",
}

industry_clean = industry_ontario.rename(
    columns=industry_column_map
).copy()

industry_clean["industry_label"] = (
    industry_clean["naics"]
    .str.replace(r"\s*\[[^\]]+\]\s*$", "", regex=True)
    .str.strip()
)

industry_clean["naics_code"] = (
    industry_clean["naics"]
    .str.extract(r"\[([^\]]+)\]\s*$", expand=False)
    .astype("string")
)

industry_clean["naics_version"] = (
    industry_clean["ref_date"]
    .apply(assign_naics_version)
    .astype("string")
)

industry_clean["status_interpretation"] = (
    industry_clean["status"]
    .map(
        {
            "x": "suppressed",
            "..": "unavailable for specific reference period",
        }
    )
    .fillna("observed numeric value")
)

industry_clean = industry_clean.drop(
    columns=["symbol", "terminated"]
)

# ============================================================
# 5. CLEAN FIRM-SIZE DATASET
# ============================================================

firm_size_clean = firm_size_ontario.copy()

firm_size_clean["status_interpretation"] = (
    firm_size_clean["STATUS"]
    .map(
        {
            "x": "suppressed - confidentiality requirement"
        }
    )
    .fillna("observed numeric value")
)

firm_size_clean = firm_size_clean.drop(
    columns=["SYMBOL", "TERMINATED"]
)

# ============================================================
# 6. VALIDATE BUSINESS-DYNAMICS MEASURES
# ============================================================

expected_industry_measures = {
    "Number of active employer businesses in the private sector",
    "Number of entrants",
    "Number of incumbents",
    "Number of exits",
    "Entry rate",
    "Exit rate",
}

actual_industry_measures = set(
    industry_clean["business_dynamics_measure"].dropna().unique()
)

validate(
    actual_industry_measures == expected_industry_measures,
    f"Unexpected industry measures: {actual_industry_measures}",
)

validate(
    industry_clean["business_dynamics_measure"].value_counts().eq(414).all(),
    "Industry measure counts are not all 414.",
)

# ============================================================
# 7. VALIDATE YEARS
# ============================================================

expected_years = set(range(2001, 2024))

industry_years = set(industry_clean["ref_date"].dropna().unique())
firm_size_years = set(firm_size_clean["REF_DATE"].dropna().unique())

validate(
    industry_years == expected_years,
    "Industry year coverage is not 2001–2023.",
)

validate(
    firm_size_years == expected_years,
    "Firm-size year coverage is not 2001–2023.",
)

# ============================================================
# 8. VALIDATE DUPLICATES
# ============================================================

validate(
    industry_raw.duplicated().sum() == 0,
    "Duplicate rows found in raw industry dataset.",
)

validate(
    firm_size_raw.duplicated().sum() == 0,
    "Duplicate rows found in raw firm-size dataset.",
)

validate(
    industry_clean.duplicated().sum() == 0,
    "Duplicate rows found in cleaned industry dataset.",
)

validate(
    firm_size_clean.duplicated().sum() == 0,
    "Duplicate rows found in cleaned firm-size dataset.",
)

# ============================================================
# 9. VALIDATE INDUSTRY STATUS / MISSING VALUES
# ============================================================

industry_unavailable = industry_clean["status"].eq("..")
industry_suppressed = industry_clean["status"].eq("x")

validate(
    industry_suppressed.sum() == 0,
    "Ontario industry dataset contains unexpected STATUS = x.",
)

validate(
    industry_unavailable.sum() == 36,
    "Expected 36 unavailable industry observations.",
)

validate(
    industry_clean.loc[industry_unavailable, "value"].isna().all(),
    "Unavailable industry observations should have missing VALUE.",
)

validate(
    industry_clean["value"].isna().sum() == 36,
    "Expected 36 missing industry VALUE observations.",
)

validate(
    (
        industry_clean["status_interpretation"].str.startswith("suppressed")
        & industry_clean["value"].eq(0)
    ).sum()
    == 0,
    "Suppressed industry observations were represented as zero.",
)

# ============================================================
# 10. VALIDATE FIRM-SIZE SUPPRESSION
# ============================================================

firm_suppressed = firm_size_clean["STATUS"].eq("x")

validate(
    firm_suppressed.sum() == 196,
    "Expected 196 suppressed Ontario firm-size observations.",
)

validate(
    firm_size_clean.loc[firm_suppressed, "VALUE"].isna().all(),
    "Suppressed firm-size observations should have missing VALUE.",
)

validate(
    firm_size_clean["VALUE"].isna().sum() == 196,
    "Expected 196 missing firm-size VALUE observations.",
)

validate(
    (
        firm_size_clean["status_interpretation"].str.startswith("suppressed")
        & firm_size_clean["VALUE"].eq(0)
    ).sum()
    == 0,
    "Suppressed firm-size observations were represented as zero.",
)

validate(
    firm_size_raw["STATUS"].eq("x").sum() == 4179,
    "Expected 4,179 suppressed observations in raw firm-size data.",
)

# ============================================================
# 11. VALIDATE VALUE FIELDS
# ============================================================

industry_non_numeric = (
    pd.to_numeric(industry_clean["value"], errors="coerce").isna()
    & industry_clean["value"].notna()
)

firm_size_non_numeric = (
    pd.to_numeric(firm_size_clean["VALUE"], errors="coerce").isna()
    & firm_size_clean["VALUE"].notna()
)

validate(
    industry_non_numeric.sum() == 0,
    "Non-numeric industry VALUE observations found.",
)

validate(
    firm_size_non_numeric.sum() == 0,
    "Non-numeric firm-size VALUE observations found.",
)

validate(
    (
        industry_clean["value"].notna()
        & industry_clean["value"].lt(0)
    ).sum()
    == 0,
    "Negative industry VALUE observations found.",
)

validate(
    (
        firm_size_clean["VALUE"].notna()
        & firm_size_clean["VALUE"].lt(0)
    ).sum()
    == 0,
    "Negative firm-size VALUE observations found.",
)

# ============================================================
# 12. VALIDATE INDUSTRY UOM
# ============================================================

validate(
    (industry_clean["uom"] == "Number").sum() == 1656,
    "Expected 1,656 industry Number observations.",
)

validate(
    (industry_clean["uom"] == "Percent").sum() == 828,
    "Expected 828 industry Percent observations.",
)

industry_rates = industry_clean[
    industry_clean["uom"].eq("Percent")
]

validate(
    (
        industry_rates["value"].notna()
        & (
            industry_rates["value"].lt(0)
            | industry_rates["value"].gt(100)
        )
    ).sum()
    == 0,
    "Invalid industry percentage values found.",
)

validate(
    firm_size_clean["UOM"].eq("Number").all(),
    "Unexpected firm-size UOM value found.",
)

# ============================================================
# 13. VALIDATE NAICS STRUCTURE
# ============================================================

validate(
    industry_clean["industry_label"].nunique() == 18,
    "Expected 18 industry categories.",
)

validate(
    industry_clean["naics_code"].notna().sum() == 2208,
    "Unexpected number of parsed NAICS codes.",
)

validate(
    industry_clean["naics_code"].isna().sum() == 276,
    "Expected 276 missing NAICS codes.",
)

expected_naics_versions = {
    "1997 NAICS": 108,
    "2002 NAICS": 540,
    "2007 NAICS": 540,
    "2012 NAICS": 1296,
}

validate(
    industry_clean["naics_version"].value_counts().to_dict()
    == expected_naics_versions,
    "Unexpected historical NAICS version counts.",
)

# ============================================================
# 14. VALIDATE FIRM-SIZE STRUCTURE
# ============================================================

validate(
    firm_size_clean["Firm size"].nunique() == 9,
    "Expected 9 firm-size categories.",
)

validate(
    firm_size_clean["Firm size"].value_counts().eq(92).all(),
    "Each firm-size category should contain 92 observations.",
)

# The source contains overlapping aggregate categories.
# They are retained separately and are not summed.

# ============================================================
# 15. VALIDATE SUCCESSION LIMITATIONS
# ============================================================

succession_keywords = [
    "succession",
    "successor",
    "retirement",
    "owner_age",
    "ownership_transfer",
    "closure_reason",
    "exit_reason",
    "planned_exit",
]

cleaned_columns = [
    str(column).lower()
    for column in industry_clean.columns
] + [
    str(column).lower()
    for column in firm_size_clean.columns
]

succession_columns = [
    column
    for column in cleaned_columns
    if any(keyword in column for keyword in succession_keywords)
]

validate(
    len(succession_columns) == 0,
    f"Unexpected succession-related columns found: {succession_columns}",
)

# Business exits remain source operational measures.
# No succession variables are inferred or created.

# ============================================================
# 16. SAVE ONLY FINAL CLEANED DATASETS
# ============================================================

industry_clean.to_csv(
    INDUSTRY_OUTPUT,
    index=False,
)

firm_size_clean.to_csv(
    FIRM_SIZE_OUTPUT,
    index=False,
)

print("\nCLEANED OUTPUTS SAVED")
print(INDUSTRY_OUTPUT)
print(FIRM_SIZE_OUTPUT)

# ============================================================
# 17. RELOAD AND VALIDATE ACTUAL OUTPUT FILES
# ============================================================

industry_output_check = pd.read_csv(INDUSTRY_OUTPUT)
firm_size_output_check = pd.read_csv(FIRM_SIZE_OUTPUT)

validate(
    industry_output_check.shape == (2484, 18),
    f"Final industry output shape is {industry_output_check.shape}, "
    "expected (2484, 18).",
)

validate(
    firm_size_output_check.shape == (828, 15),
    f"Final firm-size output shape is {firm_size_output_check.shape}, "
    "expected (828, 15).",
)

validate(
    set(industry_output_check["ref_date"].dropna().unique())
    == expected_years,
    "Final industry output does not cover 2001–2023.",
)

validate(
    set(firm_size_output_check["REF_DATE"].dropna().unique())
    == expected_years,
    "Final firm-size output does not cover 2001–2023.",
)

validate(
    industry_output_check["geo"].eq("Ontario").all(),
    "Final industry output contains non-Ontario records.",
)

validate(
    firm_size_output_check["GEO"].eq("Ontario").all(),
    "Final firm-size output contains non-Ontario records.",
)

validate(
    industry_output_check.duplicated().sum() == 0,
    "Duplicate rows found in final industry output.",
)

validate(
    firm_size_output_check.duplicated().sum() == 0,
    "Duplicate rows found in final firm-size output.",
)

validate(
    industry_output_check["status"].eq("..").sum() == 36,
    "Final industry output has unexpected unavailable count.",
)

validate(
    industry_output_check["value"].isna().sum() == 36,
    "Final industry output has unexpected missing VALUE count.",
)

validate(
    firm_size_output_check["STATUS"].eq("x").sum() == 196,
    "Final firm-size output has unexpected suppressed count.",
)

validate(
    firm_size_output_check["VALUE"].isna().sum() == 196,
    "Final firm-size output has unexpected missing VALUE count.",
)

# ============================================================
# 18. FINAL RESULT
# ============================================================

print("\n" + "=" * 70)
print("FINAL VALIDATION: PASS")
print("=" * 70)
print("Industry output:", industry_output_check.shape)
print("Firm-size output:", firm_size_output_check.shape)
print("Industry years: 2001–2023")
print("Firm-size years: 2001–2023")
print("Industry geography: Ontario")
print("Firm-size geography: Ontario")
print("Industry unavailable observations: 36")
print("Firm-size suppressed observations: 196")
print("No intermediate CSV exports were created.")
print("The two datasets remain separate.")
print("Raw source files were read only and were not modified.")
print("Cleaning completed successfully from beginning to end.")
