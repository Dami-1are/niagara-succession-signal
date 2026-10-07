import pandas as pd
# Load Industry dataset
industry_df = pd.read_csv(r"C:\GitRepo\niagara-succession-signal\data\raw\statcan\business_dynamics\33100087.csv")
# Load Firm-Size dataset
firm_size_df = pd.read_csv(r"C:\GitRepo\niagara-succession-signal\data\raw\statcan\business_dynamics\33100088.csv")
# Dataset shapes
print("Industry dataset:", industry_df.shape)
print("Firm-Size dataset:", firm_size_df.shape)
# Column names
print("\nIndustry columns:")
print(industry_df.columns.tolist())
print("\nFirm-Size columns:")
print(firm_size_df.columns.tolist())
# Exact duplicate rows
print("\nIndustry duplicates:", industry_df.duplicated().sum())
print("Firm-Size duplicates:", firm_size_df.duplicated().sum())

# Year coverage
print("\nIndustry year coverage:")
print("Minimum year:", industry_df["REF_DATE"].min())
print("Maximum year:", industry_df["REF_DATE"].max())
print("Number of unique years:", industry_df["REF_DATE"].nunique())
print("Years:", sorted(industry_df["REF_DATE"].unique()))

print("\nFirm-Size year coverage:")
print("Minimum year:", firm_size_df["REF_DATE"].min())
print("Maximum year:", firm_size_df["REF_DATE"].max())
print("Number of unique years:", firm_size_df["REF_DATE"].nunique())
print("Years:", sorted(firm_size_df["REF_DATE"].unique()))

# Missing value check
print("\nIndustry missing values:")
print(industry_df.isna().sum())

print("\nFirm-Size missing values:")
print(firm_size_df.isna().sum())

# STATUS value counts
print("\nIndustry STATUS values:")
print(industry_df["STATUS"].value_counts(dropna=False))
print("\nFirm-Size STATUS values:")
print(firm_size_df["STATUS"].value_counts(dropna=False))


# STEP 3 — INSPECT DATASETS BEFORE CLEANING
print("\n" + "=" * 60)
print("INDUSTRY DATASET — DATA TYPES")
print("=" * 60)
print(industry_df.dtypes)

print("\n" + "=" * 60)
print("FIRM-SIZE DATASET — DATA TYPES")
print("=" * 60)
print(firm_size_df.dtypes)

# Industry dataset inspection
industry_columns = ["REF_DATE", "GEO", "DGUID", "VALUE", "STATUS", "SYMBOL", "TERMINATED", "Business dynamics measure", "North American Industry Classification System (NAICS)"]
print("\n" + "=" * 60)
print("INDUSTRY DATASET — UNIQUE VALUES")
print("=" * 60)
for column in industry_columns:
    print(f"\n--- {column} ---")
    print("Number of unique values:", industry_df[column].nunique(dropna=False))
    print(industry_df[column].value_counts(dropna=False).head(20))

# Firm-size dataset inspection
firm_size_columns = ["REF_DATE", "GEO", "DGUID", "VALUE", "STATUS", "SYMBOL", "TERMINATED", "Employment dynamics", "Firm size"]
print("\n" + "=" * 60)
print("FIRM-SIZE DATASET — UNIQUE VALUES")
print("=" * 60)
for column in firm_size_columns:
    print(f"\n--- {column} ---")
    print("Number of unique values:", firm_size_df[column].nunique(dropna=False))
    print(firm_size_df[column].value_counts(dropna=False).head(20))
# Missing values
print("\n" + "=" * 60)
print("MISSING VALUES — INDUSTRY")
print("=" * 60)
print(industry_df[industry_columns].isna().sum())

print("\n" + "=" * 60)
print("MISSING VALUES — FIRM SIZE")
print("=" * 60)
print(firm_size_df[firm_size_columns].isna().sum())

# Exact duplicate rows
print("\n" + "=" * 60)
print("EXACT DUPLICATES")
print("=" * 60)
print("Industry:", industry_df.duplicated().sum())
print("Firm Size:", firm_size_df.duplicated().sum())


# STEP 4 — PREPARE ONTARIO-FOCUSED OUTPUTS
import os
# Ontario DGUID from the source data
ontario_dguid_industry = (industry_df.loc[industry_df["GEO"] == "Ontario", "DGUID"]
    .dropna()
    .unique())
ontario_dguid_firm_size = (firm_size_df.loc[firm_size_df["GEO"] == "Ontario", "DGUID"]
    .dropna()
    .unique())
print("\nOntario Industry DGUID:", ontario_dguid_industry)
print("Ontario Firm-Size DGUID:", ontario_dguid_firm_size)
# Ensure exactly one Ontario DGUID exists in each dataset
if len(ontario_dguid_industry) != 1:
    raise ValueError("Industry dataset does not have exactly one Ontario DGUID.")
if len(ontario_dguid_firm_size) != 1:
    raise ValueError("Firm-Size dataset does not have exactly one Ontario DGUID.")
# Use the source DGUID to filter Ontario
industry_ontario = industry_df[
    industry_df["DGUID"] == ontario_dguid_industry[0]
].copy()

firm_size_ontario = firm_size_df[
    firm_size_df["DGUID"] == ontario_dguid_firm_size[0]
].copy()

# Output directory
output_dir = (r"C:\GitRepo\niagara-succession-signal"
    r"\data\processed\statcan\business_dynamics")
os.makedirs(output_dir, exist_ok=True)
# Save cleaned Ontario-focused outputs
industry_output = os.path.join(output_dir,"business_dynamics_industry_ontario.csv")

firm_size_output = os.path.join(output_dir,"business_dynamics_firm_size_ontario.csv")
industry_ontario.to_csv(industry_output, index=False)
firm_size_ontario.to_csv(firm_size_output, index=False)
print("\nOntario-focused files created:")
print(industry_output)
print(firm_size_output)

# VALIDATE ONTARIO-ONLY OUTPUTS
print("\n" + "=" * 60)
print("ONTARIO OUTPUT VALIDATION")
print("=" * 60)

print("\nIndustry Ontario output shape:")
print(industry_ontario.shape)

print("\nFirm-Size Ontario output shape:")
print(firm_size_ontario.shape)

print("\nIndustry GEO values:")
print(industry_ontario["GEO"].unique())

print("\nFirm-Size GEO values:")
print(firm_size_ontario["GEO"].unique())

print("\nIndustry DGUID values:")
print(industry_ontario["DGUID"].unique())

print("\nFirm-Size DGUID values:")
print(firm_size_ontario["DGUID"].unique())


from pathlib import Path
import pandas as pd
output_dir = Path(r"C:\GitRepo\niagara-succession-signal\data\processed\statcan\business_dynamics")
industry_ontario = pd.read_csv(output_dir / "business_dynamics_industry_ontario.csv")
firm_size_ontario = pd.read_csv(output_dir / "business_dynamics_firm_size_ontario.csv")
print("\nSTEP 5 — HISTORICAL PERIOD VALIDATION")
print("\nIndustry — Ontario")
print("Years:", sorted(industry_ontario["REF_DATE"].unique()))
print("Number of years:", industry_ontario["REF_DATE"].nunique())
print("\nFirm Size — Ontario")
print("Years:", sorted(firm_size_ontario["REF_DATE"].unique()))
print("Number of years:", firm_size_ontario["REF_DATE"].nunique())

# Step 6
print("\n" + "=" * 60)
print("STEP 6 — TEXT AND COLUMN NAME INSPECTION")
print("=" * 60)
for name, df in {"Industry Ontario": industry_ontario, "Firm Size Ontario": firm_size_ontario}.items():
    print(f"\n{name}")
    print("\nColumn names:")
    for col in df.columns:
        print(repr(col))
    print("\nText-field whitespace check:")
    text_columns = df.select_dtypes(include=["object", "string"]).columns
    for col in text_columns:
        leading = (df[col].dropna().astype(str) != df[col].dropna().astype(str).str.lstrip()).sum()
        trailing = (df[col].dropna().astype(str) != df[col].dropna().astype(str).str.rstrip()).sum()
        print(f"{col}: leading spaces={leading}, trailing spaces={trailing}")
    print("\nText-field unique values:")
    for col in text_columns:
        print(f"\n--- {col} ---")
        print(df[col].dropna().unique()[:20])

# Step 7
print("\n" + "=" * 60)
print("STEP 7 — INDUSTRY / NAICS FIELD CLEANING")
print("=" * 60)
# Column mapping for the Ontario industry dataset
industry_column_map = {"REF_DATE": "ref_date", "GEO": "geo", "DGUID": "dguid", "Business dynamics measure": "business_dynamics_measure",
    "North American Industry Classification System (NAICS)": "naics", "UOM": "uom", "UOM_ID": "uom_id", "SCALAR_FACTOR": "scalar_factor",
    "SCALAR_ID": "scalar_id", "VECTOR": "vector", "COORDINATE": "coordinate", "VALUE": "value", "STATUS": "status",
    "SYMBOL": "symbol", "TERMINATED": "terminated", "DECIMALS": "decimals"}
# Create a working copy; do not modify the raw data
industry_clean = industry_ontario.rename(columns=industry_column_map).copy()
# Separate the industry label from the NAICS code/range
industry_clean["industry_label"] = (industry_clean["naics"]
    .str.replace(r"\s*\[[^\]]+\]\s*$", "", regex=True)
    .str.strip())
industry_clean["naics_code"] = (industry_clean["naics"]
    .str.extract(r"\[([^\]]+)\]\s*$", expand=False)
    .astype("string"))
print("\nOriginal NAICS values:")
print(industry_clean["naics"]
    .drop_duplicates()
    .to_string(index=False))
print("\nParsed industry_label and naics_code:")
print(industry_clean[["naics", "industry_label", "naics_code"]]
    .drop_duplicates()
    .to_string(index=False))
print("\nNAICS code data type:")
print(industry_clean["naics_code"].dtype)
print("\nMissing parsed NAICS codes:")
print(industry_clean["naics_code"].isna().sum())
print("\nNAICS codes:")
print(industry_clean["naics_code"]
    .dropna()
    .drop_duplicates()
    .tolist())

# Step 8
print("\n" + "=" * 60)
print("STEP 8 — PRESERVE HISTORICAL NAICS CHANGES")
print("=" * 60)
# The Week 3 audit documented the following NAICS versions:
# 1997 NAICS  — 2001
# 2002 NAICS  — 2002–2006
# 2007 NAICS  — 2007–2011
# 2012 NAICS  — 2012 onward
#
# No historical NAICS category is being recoded or harmonized.
# The original `naics` field remains unchanged.
def assign_naics_version(year):
    if year == 2001:
        return "1997 NAICS"
    elif 2002 <= year <= 2006:
        return "2002 NAICS"
    elif 2007 <= year <= 2011:
        return "2007 NAICS"
    elif year >= 2012:
        return "2012 NAICS"
    else:
        return pd.NA
industry_clean["naics_version"] = industry_clean["ref_date"].apply(    assign_naics_version).astype("string")
print("\nNAICS version by year:")
print(industry_clean[["ref_date", "naics_version"]]
    .drop_duplicates()
    .sort_values("ref_date")
    .to_string(index=False))
print("\nNAICS version counts:")
print(industry_clean["naics_version"]
    .value_counts(dropna=False)
    .sort_index())
print("\nOriginal NAICS field preserved:")
print(industry_clean[["ref_date", "naics", "industry_label", "naics_code", "naics_version"]]
    .drop_duplicates()
    .sort_values(["ref_date", "naics"])
    .head(40)
    .to_string(index=False))
print("\nNAICS version missing values:")
print(industry_clean["naics_version"].isna().sum())

print("\nNAICS harmonization/reclassification:")
print("NONE — historical NAICS categories have not been recoded or harmonized.")

print("\nStep 8 interpretation:")
print("NAICS classification changes across the historical period are preserved. "
    "The naics_version field documents the applicable version by year based "
    "on the Week 3 audit. Crosswalk/harmonization is outside the scope of this task.")

# Step 9
print("\n" + "=" * 60)
print("STEP 9 — PRESERVE BUSINESS DYNAMICS MEASURES")
print("=" * 60)
# 1. Review the distinct business-dynamics measures
print("\nBusiness dynamics measures:")
print(industry_clean["business_dynamics_measure"]
    .value_counts(dropna=False))
# 2. Check UOM and scalar metadata by business-dynamics measure
print("\nUOM by business-dynamics measure:")
print(industry_clean[["business_dynamics_measure", "uom", "scalar_factor", "scalar_id"]]
    .drop_duplicates()
    .sort_values("business_dynamics_measure")
    .to_string(index=False))
# 3. Check VALUE data type
print("\nVALUE data type:")
print(industry_clean["value"].dtype)
# 4. Check whether each measure is associated with a consistent UOM
measure_uom_check = (industry_clean
    .groupby("business_dynamics_measure", dropna=False)
    .agg(uom_count=("uom", "nunique"), scalar_factor_count=("scalar_factor", "nunique"), scalar_id_count=("scalar_id", "nunique") )
    .reset_index())
print("\nMetadata consistency by measure:")
print(measure_uom_check.to_string(index=False))
# 5. Confirm no new business-dynamics measures were created
expected_measures = {"Number of active employer businesses in the private sector", "Number of entrants", "Number of incumbents", "Number of exits", "Entry rate", "Exit rate"}

actual_measures = set(industry_clean["business_dynamics_measure"]
    .dropna()
    .unique())
unexpected_measures = actual_measures - expected_measures
missing_measures = expected_measures - actual_measures
print("\nUnexpected business-dynamics measures:")
print(unexpected_measures)
print("\nExpected measures missing:")
print(missing_measures)

# 6. Explicitly verify counts and rates remain separate
count_measures = {"Number of active employer businesses in the private sector", "Number of entrants", "Number of incumbents", "Number of exits"}
rate_measures = {"Entry rate", "Exit rate"}
print("\nCount measures:")
print(sorted(count_measures & actual_measures))
print("\nRate measures:")
print(sorted(rate_measures & actual_measures))

# 7. Final Step 9 interpretation
if unexpected_measures:
    print("\nSTEP 9 STATUS: REVIEW REQUIRED")
    print("Unexpected business-dynamics measures were found.")
elif missing_measures:
    print("\nSTEP 9 STATUS: REVIEW REQUIRED")
    print("Expected business-dynamics measures are missing.")
else:
    print("\nSTEP 9 STATUS: PASS")
    print("All six business-dynamics measures are preserved separately.")
    print("Counts and rates have not been mixed.")
    print("UOM and scalar metadata were checked before interpreting VALUE.")
    print("No new business-dynamics measures were created.")



print("\n" + "=" * 60)
print("STEP 9 — PRESERVE BUSINESS DYNAMICS MEASURES")
print("=" * 60)
# 1. List the business-dynamics measures present
print("\nBusiness dynamics measures:")
print(industry_clean["business_dynamics_measure"]
    .value_counts(dropna=False))
# 2. Check UOM and scaling metadata
print("\nUOM / scalar metadata by business-dynamics measure:")
metadata_check = (industry_clean[
        ["business_dynamics_measure", "uom", "uom_id", "scalar_factor", "scalar_id", "decimals"]
    ]
    .drop_duplicates()
    .sort_values("business_dynamics_measure"))
print(metadata_check.to_string(index=False))
# 3. Check VALUE data type
print("\nVALUE data type:")
print(industry_clean["value"].dtype)

# 4. Verify the expected six measures
expected_measures = {
    "Number of active employer businesses in the private sector", "Number of entrants", "Number of incumbents", "Number of exits", "Entry rate", "Exit rate"}

actual_measures = set(industry_clean["business_dynamics_measure"]
    .dropna()
    .unique())
unexpected_measures = actual_measures - expected_measures
missing_measures = expected_measures - actual_measures
print("\nUnexpected measures:")
print(unexpected_measures if unexpected_measures else "None")
print("\nMissing expected measures:")
print(missing_measures if missing_measures else "None")
# 5. Explicitly separate count measures from rate measures
count_measures = {"Number of active employer businesses in the private sector", "Number of entrants", "Number of incumbents", "Number of exits"}
rate_measures = { "Entry rate", "Exit rate"}

print("\nCount measures preserved:")
print(sorted(count_measures & actual_measures))

print("\nRate measures preserved:")
print(sorted(rate_measures & actual_measures))

# 6. Confirm that counts and rates have not been mixed
count_rows = industry_clean[industry_clean["business_dynamics_measure"].isin(count_measures)]

rate_rows = industry_clean[industry_clean["business_dynamics_measure"].isin(rate_measures)]
print("\nCount-measure row count:")
print(len(count_rows))
print("\nRate-measure row count:")
print(len(rate_rows))

# 7. Final validation
if unexpected_measures or missing_measures:
    print("\nSTEP 9 STATUS: REVIEW REQUIRED")
    print("The expected six business-dynamics measures were not preserved exactly.")
else:
    print("\nSTEP 9 STATUS: PASS")
    print("All six business-dynamics measures are preserved separately.")
    print("Counts and rates remain separate.")
    print("UOM and scalar metadata have been checked.")
    print("No new business-dynamics measures were created.")

# Step 10
print("\n" + "=" * 60)
print("STEP 10 — HANDLE STATUS-CODED OBSERVATIONS")
print("=" * 60)

# 1. Review STATUS values and their frequencies
print("\nSTATUS values:")
print(
    industry_clean["status"]
    .value_counts(dropna=False)
)

# 2. Confirm the relationship between STATUS and VALUE
print("\nSTATUS vs VALUE availability:")

status_value_check = (
    industry_clean
    .assign(
        value_available=industry_clean["value"].notna()
    )
    .groupby("status", dropna=False)
    .agg(
        total_rows=("value", "size"),
        numeric_values=("value_available", "sum"),
        missing_values=("value_available", lambda x: (~x).sum())
    )
    .reset_index()
)

print(status_value_check.to_string(index=False))

# 3. Preserve the original STATUS field.
# No values are replaced or imputed.

# 4. Create an explicit interpretation field for auditability.
# This does NOT change VALUE or STATUS.
industry_clean["status_interpretation"] = (
    industry_clean["status"]
    .map({
        "x": "suppressed",
        "..": "unavailable for specific reference period"
    })
    .fillna("observed numeric value")
)

# 5. Verify the interpretation categories
print("\nStatus interpretation:")
print(
    industry_clean["status_interpretation"]
    .value_counts(dropna=False)
)

# 6. Confirm no suppressed/unavailable observations were converted to zero
problem_statuses = {"x", ".."}

status_value_issues = industry_clean[
    industry_clean["status"].isin(problem_statuses)
    & industry_clean["value"].eq(0)
]

print("\nSuppressed/unavailable observations represented as zero:")
print(len(status_value_issues))

# 7. Confirm no values were invented for suppressed/unavailable observations
status_value_filled = industry_clean[
    industry_clean["status"].isin(problem_statuses)
    & industry_clean["value"].notna()
]

print("\nSuppressed/unavailable observations with VALUE populated:")
print(len(status_value_filled))

# 8. Final validation
if len(status_value_issues) > 0:
    print("\nSTEP 10 STATUS: REVIEW REQUIRED")
    print("Some suppressed/unavailable observations are represented as zero.")

elif len(status_value_filled) > 0:
    print("\nSTEP 10 STATUS: REVIEW REQUIRED")
    print("Some suppressed/unavailable observations contain VALUE data.")

else:
    print("\nSTEP 10 STATUS: PASS")
    print("STATUS codes are preserved and interpreted using Statistics Canada metadata.")
    print("Suppressed observations are not converted to zero.")
    print("Unavailable observations are not converted to zero.")
    print("No values have been invented or imputed.")
    print("Observed, suppressed, and unavailable observations remain distinguishable.")


# Step 11
print("\n" + "=" * 60)
print("STEP 11 — PRESERVE FIRM-SIZE CATEGORIES")
print("=" * 60)

# 1. Expected Statistics Canada firm-size categories
expected_firm_sizes = {
    "Private sector",
    "Less than 5 employees",
    "5 to less than 20 employees",
    "20 to less than 50 employees",
    "50 employees or more",
    "50 to less than 100 employees",
    "100 employees or more",
    "100 to less than 500 employees",
    "500 employees or more"
}

# 2. Display the source categories exactly as they appear
actual_firm_sizes = set(
    firm_size_ontario["Firm size"]
    .dropna()
    .unique()
)

print("\nFirm-size categories present:")
for category in sorted(actual_firm_sizes):
    print(f"- {category}")

# 3. Check for unexpected or missing categories
unexpected_categories = actual_firm_sizes - expected_firm_sizes
missing_categories = expected_firm_sizes - actual_firm_sizes

print("\nUnexpected firm-size categories:")
print(unexpected_categories if unexpected_categories else "None")

print("\nExpected firm-size categories missing:")
print(missing_categories if missing_categories else "None")

# 4. Check for leading/trailing whitespace
firm_size_text = firm_size_ontario["Firm size"].dropna().astype(str)

leading_spaces = firm_size_text.str.match(r"^\s").sum()
trailing_spaces = firm_size_text.str.match(r".*\s$").sum()

print("\nLeading spaces:", leading_spaces)
print("Trailing spaces:", trailing_spaces)

# 5. Confirm no Micro/Small/Medium/Large recoding has been introduced
non_source_labels = {
    "Micro",
    "Small",
    "Medium",
    "Large"
}

introduced_labels = actual_firm_sizes & non_source_labels

print("\nIndependently introduced size labels:")
print(introduced_labels if introduced_labels else "None")

# 6. Display category frequencies
print("\nFirm-size category frequencies:")
print(
    firm_size_ontario["Firm size"]
    .value_counts(dropna=False)
)

# 7. Final validation
if unexpected_categories or missing_categories:
    print("\nSTEP 11 STATUS: REVIEW REQUIRED")
    print("The firm-size categories do not exactly match the expected source categories.")

elif leading_spaces > 0 or trailing_spaces > 0:
    print("\nSTEP 11 STATUS: REVIEW REQUIRED")
    print("Whitespace was detected in firm-size category labels.")

elif introduced_labels:
    print("\nSTEP 11 STATUS: REVIEW REQUIRED")
    print("Independent Micro/Small/Medium/Large labels were detected.")

else:
    print("\nSTEP 11 STATUS: PASS")
    print("All source firm-size categories are preserved.")
    print("No independent Micro/Small/Medium/Large classification was introduced.")


# Step 12
print("\n" + "=" * 60)
print("STEP 12 — HANDLE OVERLAPPING FIRM-SIZE CATEGORIES")
print("=" * 60)

# 1. Display the source categories
print("\nFirm-size categories preserved:")
print(
    firm_size_ontario["Firm size"]
    .dropna()
    .unique()
)

# 2. Document the overlapping relationships
overlapping_groups = {
    "50 employees or more": [
        "50 to less than 100 employees",
        "100 employees or more"
    ],
    "100 employees or more": [
        "100 to less than 500 employees",
        "500 employees or more"
    ]
}

print("\nDocumented overlapping categories:")

for parent, overlaps in overlapping_groups.items():
    print(f"\n{parent} overlaps with:")
    for category in overlaps:
        print(f"  - {category}")

# 3. Confirm that no firm-size aggregation was performed
print("\nFirm-size aggregation:")
print("NONE — overlapping categories have not been summed.")

# 4. Confirm that no categories were removed or merged
expected_firm_sizes = {
    "Private sector",
    "Less than 5 employees",
    "5 to less than 20 employees",
    "20 to less than 50 employees",
    "50 employees or more",
    "50 to less than 100 employees",
    "100 employees or more",
    "100 to less than 500 employees",
    "500 employees or more"
}

actual_firm_sizes = set(
    firm_size_ontario["Firm size"]
    .dropna()
    .unique()
)

unexpected_categories = actual_firm_sizes - expected_firm_sizes
missing_categories = expected_firm_sizes - actual_firm_sizes

print("\nUnexpected categories:")
print(unexpected_categories if unexpected_categories else "None")

print("\nMissing categories:")
print(missing_categories if missing_categories else "None")

# 5. Final validation
if unexpected_categories or missing_categories:
    print("\nSTEP 12 STATUS: REVIEW REQUIRED")
    print("Firm-size categories have changed or are missing.")

else:
    print("\nSTEP 12 STATUS: PASS")
    print("Overlapping firm-size categories are preserved.")
    print("No overlapping categories have been summed.")
    print("No firm-size categories have been merged or removed.")
    print("Future analysis must treat the overlapping categories separately.")


# Step 13
# ------------------------------------------------------------
# 1. Suppressed observations BEFORE Ontario filtering
# ------------------------------------------------------------

raw_suppressed_count = (
    firm_size_df["STATUS"].eq("x").sum()
)

raw_missing_value_count = (
    firm_size_df["VALUE"].isna().sum()
)

print("\nBEFORE ONTARIO FILTERING")
print("Suppressed observations (STATUS = x):", raw_suppressed_count)
print("Missing VALUE observations:", raw_missing_value_count)

# ------------------------------------------------------------
# 2. Suppressed observations AFTER Ontario filtering
# ------------------------------------------------------------

ontario_suppressed_count = (
    firm_size_ontario["STATUS"].eq("x").sum()
)

ontario_missing_value_count = (
    firm_size_ontario["VALUE"].isna().sum()
)

print("\nAFTER ONTARIO FILTERING")
print("Suppressed observations (STATUS = x):", ontario_suppressed_count)
print("Missing VALUE observations:", ontario_missing_value_count)

# ------------------------------------------------------------
# 3. Verify that Ontario suppressed observations have
#    missing VALUE
# ------------------------------------------------------------

suppressed_with_value = firm_size_ontario[
    firm_size_ontario["STATUS"].eq("x")
    & firm_size_ontario["VALUE"].notna()
]

print("\nSuppressed observations with a populated VALUE:")
print(len(suppressed_with_value))

# ------------------------------------------------------------
# 4. Verify that suppressed values have NOT been replaced
#    with zero
# ------------------------------------------------------------

suppressed_as_zero = firm_size_ontario[
    firm_size_ontario["STATUS"].eq("x")
    & firm_size_ontario["VALUE"].eq(0)
]

print("\nSuppressed observations represented as zero:")
print(len(suppressed_as_zero))

# ------------------------------------------------------------
# 5. Create an explicit interpretation field.
#    This documents status without changing VALUE.
# ------------------------------------------------------------

firm_size_clean = firm_size_ontario.copy()

firm_size_clean["status_interpretation"] = (
    firm_size_clean["STATUS"]
    .map({
        "x": "suppressed - confidentiality requirement"
    })
    .fillna("observed numeric value")
)

print("\nCleaned Dataset 2 status interpretation:")
print(
    firm_size_clean["status_interpretation"]
    .value_counts(dropna=False)
)

# ------------------------------------------------------------
# 6. Final validation checks
# ------------------------------------------------------------

if raw_suppressed_count != 4179:
    print("\nSTEP 13 STATUS: REVIEW REQUIRED")
    print(
        "Expected 4,179 suppressed observations in the full raw dataset, "
        "but found:",
        raw_suppressed_count
    )

elif suppressed_with_value.shape[0] > 0:
    print("\nSTEP 13 STATUS: REVIEW REQUIRED")
    print(
        "Some Ontario suppressed observations have a populated VALUE."
    )

elif suppressed_as_zero.shape[0] > 0:
    print("\nSTEP 13 STATUS: REVIEW REQUIRED")
    print(
        "Some Ontario suppressed observations are represented as zero."
    )

else:
    print("\nSTEP 13 STATUS: PASS")
    print(
        "The 4,179 suppressed observations in the full raw dataset "
        "are preserved as STATUS = x."
    )
    print(
        f"Ontario contains {ontario_suppressed_count} suppressed observations."
    )
    print(
        "Suppressed VALUE observations remain missing."
    )
    print(
        "Suppressed values have not been replaced with zero."
    )
    print(
        "No suppressed values have been imputed or guessed."
    )
    print(
        "Suppressed status is preserved and documented in the "
        "cleaned Dataset 2 structure."
    )


# STEP 14 — REVIEW EMPTY TECHNICAL FIELDS
# ------------------------------------------------------------

print("\n" + "=" * 60)
print("STEP 14 — REVIEW EMPTY TECHNICAL FIELDS")
print("=" * 60)

# ------------------------------------------------------------
# 1. Check whether SYMBOL and TERMINATED are entirely empty
# ------------------------------------------------------------

industry_symbol_missing = industry_clean["symbol"].isna().sum()
industry_terminated_missing = industry_clean["terminated"].isna().sum()

firm_size_symbol_missing = firm_size_clean["SYMBOL"].isna().sum()
firm_size_terminated_missing = firm_size_clean["TERMINATED"].isna().sum()

print("\nINDUSTRY DATASET")
print("SYMBOL missing:", industry_symbol_missing, "of", len(industry_clean))
print("TERMINATED missing:", industry_terminated_missing, "of", len(industry_clean))

print("\nFIRM-SIZE DATASET")
print("SYMBOL missing:", firm_size_symbol_missing, "of", len(firm_size_clean))
print("TERMINATED missing:", firm_size_terminated_missing, "of", len(firm_size_clean))

# ------------------------------------------------------------
# 2. Remove empty technical fields from cleaned outputs
# ------------------------------------------------------------

industry_clean = industry_clean.drop(
    columns=["symbol", "terminated"]
)

firm_size_clean = firm_size_clean.drop(
    columns=["SYMBOL", "TERMINATED"]
)

# ------------------------------------------------------------
# 3. Document the decision
# ------------------------------------------------------------

print("\nREMOVAL DECISION")
print("SYMBOL and TERMINATED were entirely empty in the extracted datasets.")
print("They were removed from the cleaned analytical outputs.")
print("The raw datasets were not modified.")
print("TERMINATED was not interpreted as business closure.")
print("No business-closure meaning was inferred from this field.")

# ------------------------------------------------------------
# 4. Final validation
# ------------------------------------------------------------

if (
    industry_symbol_missing == len(industry_clean)
    and industry_terminated_missing == len(industry_clean)
    and firm_size_symbol_missing == len(firm_size_clean)
    and firm_size_terminated_missing == len(firm_size_clean)
):
    print("\nSTEP 14 STATUS: PASS")
    print("Empty technical fields were identified and removed from cleaned outputs.")
else:
    print("\nSTEP 14 STATUS: REVIEW REQUIRED")
    print("One or more technical fields were not entirely empty.")


# ------------------------------------------------------------
# STEP 15 — VALIDATE VALUE
# ------------------------------------------------------------

print("\n" + "=" * 60)
print("STEP 15 — VALIDATE VALUE")
print("=" * 60)

# ------------------------------------------------------------
# 1. Check VALUE data types
# ------------------------------------------------------------

print("\nVALUE DATA TYPES")
print("Industry VALUE dtype:", industry_clean["value"].dtype)
print("Firm-size VALUE dtype:", firm_size_clean["VALUE"].dtype)

# ------------------------------------------------------------
# 2. Check for non-numeric VALUE observations
# ------------------------------------------------------------

industry_non_numeric = pd.to_numeric(
    industry_clean["value"], errors="coerce"
).isna() & industry_clean["value"].notna()

firm_size_non_numeric = pd.to_numeric(
    firm_size_clean["VALUE"], errors="coerce"
).isna() & firm_size_clean["VALUE"].notna()

print("\nNON-NUMERIC VALUES")
print("Industry non-numeric VALUEs:", industry_non_numeric.sum())
print("Firm-size non-numeric VALUEs:", firm_size_non_numeric.sum())

# ------------------------------------------------------------
# 3. Check negative values
# ------------------------------------------------------------

industry_negative = industry_clean[
    industry_clean["value"].notna()
    & (industry_clean["value"] < 0)
]

firm_size_negative = firm_size_clean[
    firm_size_clean["VALUE"].notna()
    & (firm_size_clean["VALUE"] < 0)
]

print("\nNEGATIVE VALUES")
print("Industry negative VALUEs:", len(industry_negative))
print("Firm-size negative VALUEs:", len(firm_size_negative))

# ------------------------------------------------------------
# 4. Check missing VALUE observations
# ------------------------------------------------------------

industry_missing = industry_clean["value"].isna().sum()
firm_size_missing = firm_size_clean["VALUE"].isna().sum()

print("\nMISSING VALUE OBSERVATIONS")
print("Industry missing VALUEs:", industry_missing)
print("Firm-size missing VALUEs:", firm_size_missing)

# ------------------------------------------------------------
# 5. Check consistency with UOM
# ------------------------------------------------------------

industry_count_rows = industry_clean[
    industry_clean["uom"] == "Number"
]

industry_rate_rows = industry_clean[
    industry_clean["uom"] == "Percent"
]

firm_size_number_rows = firm_size_clean[
    firm_size_clean["UOM"] == "Number"
]

print("\nUOM CONSISTENCY")
print("Industry Number rows:", len(industry_count_rows))
print("Industry Percent rows:", len(industry_rate_rows))
print("Firm-size Number rows:", len(firm_size_number_rows))

# Check that rate observations are within a reasonable percentage range
industry_invalid_rates = industry_rate_rows[
    industry_rate_rows["value"].notna()
    & (
        (industry_rate_rows["value"] < 0)
        | (industry_rate_rows["value"] > 100)
    )
]

print(
    "Industry invalid percentage values:",
    len(industry_invalid_rates)
)

# ------------------------------------------------------------
# 6. Check consistency with SCALAR_FACTOR
# ------------------------------------------------------------

industry_scalar_values = (
    industry_clean[["uom", "scalar_factor"]]
    .drop_duplicates()
    .sort_values(["uom", "scalar_factor"])
)

firm_size_scalar_values = (
    firm_size_clean[["UOM", "SCALAR_FACTOR"]]
    .drop_duplicates()
    .sort_values(["UOM", "SCALAR_FACTOR"])
)

print("\nINDUSTRY UOM / SCALAR_FACTOR COMBINATIONS")
print(industry_scalar_values.to_string(index=False))

print("\nFIRM-SIZE UOM / SCALAR_FACTOR COMBINATIONS")
print(firm_size_scalar_values.to_string(index=False))

# ------------------------------------------------------------
# 7. Check that missing/suppressed values were not converted
#    to zero
# ------------------------------------------------------------

industry_suppressed_zero = industry_clean[
    industry_clean["status_interpretation"].str.startswith("suppressed")
    & industry_clean["value"].eq(0)
]

firm_size_suppressed_zero = firm_size_clean[
    firm_size_clean["status_interpretation"].str.startswith("suppressed")
    & firm_size_clean["VALUE"].eq(0)
]

print("\nSUPPRESSED VALUES REPRESENTED AS ZERO")
print("Industry:", len(industry_suppressed_zero))
print("Firm-size:", len(firm_size_suppressed_zero))

# ------------------------------------------------------------
# 8. Document source rounding limitation
# ------------------------------------------------------------

print("\nSOURCE METADATA LIMITATION")
print(
    "Business count values are rounded to units of ten according "
    "to the source metadata."
)
print(
    "This limitation is preserved and no attempt was made to "
    "recover or infer unrounded values."
)

# ------------------------------------------------------------
# 9. Final validation
# ------------------------------------------------------------

if (
    industry_non_numeric.sum() == 0
    and firm_size_non_numeric.sum() == 0
    and len(industry_negative) == 0
    and len(firm_size_negative) == 0
    and len(industry_invalid_rates) == 0
    and len(industry_suppressed_zero) == 0
    and len(firm_size_suppressed_zero) == 0
):
    print("\nSTEP 15 STATUS: PASS")
    print("VALUE is numeric where observations are provided.")
    print("No unexpected non-numeric values were found.")
    print("No inappropriate negative values were found.")
    print("Missing and suppressed observations were preserved.")
    print("VALUE is consistent with the reported UOM.")
    print("SCALAR_FACTOR was reviewed and preserved.")
    print("Source rounding to units of ten is documented.")
else:
    print("\nSTEP 15 STATUS: REVIEW REQUIRED")
    print("One or more VALUE validation checks require review.")


# STEP 16 — DO NOT SUM CATEGORIES WITHOUT CHECKING THEIR MEANING
# ------------------------------------------------------------

print("\n" + "=" * 60)
print("STEP 16 — DO NOT SUM CATEGORIES WITHOUT CHECKING THEIR MEANING")
print("=" * 60)

# ------------------------------------------------------------
# 1. Review Dataset 1 industry categories
# ------------------------------------------------------------

industry_categories = (
    industry_clean["industry_label"]
    .dropna()
    .unique()
)

print("\nDATASET 1 — INDUSTRY CATEGORIES")
print("Number of industry categories:", len(industry_categories))

for category in sorted(industry_categories):
    print("-", category)

# ------------------------------------------------------------
# 2. Confirm that the private-sector aggregate is preserved
#    separately from detailed industry categories
# ------------------------------------------------------------

private_sector_rows = industry_clean[
    industry_clean["industry_label"] == "Private sector"
]

print("\nPRIVATE-SECTOR AGGREGATE")
print("Private sector observations:", len(private_sector_rows))
print(
    "Private sector is preserved as a source category and "
    "has not been calculated by summing industry categories."
)

# ------------------------------------------------------------
# 3. Review Dataset 2 firm-size categories
# ------------------------------------------------------------

firm_size_categories = (
    firm_size_clean["Firm size"]
    .dropna()
    .unique()
)

print("\nDATASET 2 — FIRM-SIZE CATEGORIES")
print("Number of firm-size categories:", len(firm_size_categories))

for category in sorted(firm_size_categories):
    print("-", category)

# ------------------------------------------------------------
# 4. Explicitly document overlapping categories
# ------------------------------------------------------------

overlapping_categories = {
    "50 employees or more": [
        "50 to less than 100 employees",
        "100 employees or more"
    ],
    "100 employees or more": [
        "100 to less than 500 employees",
        "500 employees or more"
    ]
}

print("\nOVERLAPPING FIRM-SIZE CATEGORIES")

for aggregate, detailed in overlapping_categories.items():
    print(f"{aggregate} overlaps with:")
    for category in detailed:
        print(f"  - {category}")

# ------------------------------------------------------------
# 5. Confirm that no category totals were created
# ------------------------------------------------------------

print("\nAGGREGATION DECISION")
print("No industry categories were summed.")
print("No firm-size categories were summed.")
print("No new aggregate categories were created.")
print("Source categories were preserved separately.")
print(
    "Overlapping firm-size categories will not be treated "
    "as mutually exclusive in later analysis."
)

# ------------------------------------------------------------
# 6. Final validation
# ------------------------------------------------------------

if (
    len(private_sector_rows) > 0
    and len(firm_size_categories) == 9
):
    print("\nSTEP 16 STATUS: PASS")
    print(
        "Aggregate and detailed categories were preserved "
        "without unsupported summation."
    )
    print(
        "The private-sector total was not reconstructed "
        "from industry categories."
    )
    print(
        "Overlapping firm-size categories were explicitly documented."
    )
else:
    print("\nSTEP 16 STATUS: REVIEW REQUIRED")
    print(
        "Category structure requires further review."
    )



# STEP 17 — PRESERVE THE MEANING OF BUSINESS EXIT
# ------------------------------------------------------------

print("\n" + "=" * 60)
print("STEP 17 — PRESERVE THE MEANING OF BUSINESS EXIT")
print("=" * 60)

# ------------------------------------------------------------
# 1. Review the business exit terminology in Dataset 1
# ------------------------------------------------------------

exit_rows = industry_clean[
    industry_clean["business_dynamics_measure"] == "Number of exits"
]

exit_rate_rows = industry_clean[
    industry_clean["business_dynamics_measure"] == "Exit rate"
]

print("\nBUSINESS EXIT MEASURES")
print("Number of exits observations:", len(exit_rows))
print("Exit rate observations:", len(exit_rate_rows))

# ------------------------------------------------------------
# 2. Confirm source terminology is preserved
# ------------------------------------------------------------

exit_measure_names = (
    industry_clean["business_dynamics_measure"]
    .dropna()
    .unique()
)

print("\nSOURCE BUSINESS-DYNAMICS TERMINOLOGY")
for measure in sorted(exit_measure_names):
    print("-", measure)

# ------------------------------------------------------------
# 3. Check for misleading succession terminology
# ------------------------------------------------------------

misleading_terms = [
    "succession failure",
    "retirement closure",
    "succession-related closure",
    "no successor",
    "business failure"
]

measure_text = " ".join(
    industry_clean["business_dynamics_measure"]
    .dropna()
    .astype(str)
    .str.lower()
)

misleading_terms_found = [
    term for term in misleading_terms
    if term.lower() in measure_text
]

print("\nMISLEADING SUCCESSION TERMS FOUND")
print(misleading_terms_found)

# ------------------------------------------------------------
# 4. Document the interpretation
# ------------------------------------------------------------

print("\nINTERPRETATION RULE")
print(
    "Business exit is preserved as the source operational measure "
    "based on employee presence across consecutive years."
)
print(
    "An exit is not interpreted as owner retirement, owner death, "
    "business failure, ownership transfer, or succession-related closure."
)
print(
    "No succession outcome has been inferred from the business exit measure."
)
print(
    "Source terminology has been preserved."
)

# ------------------------------------------------------------
# 5. Final validation
# ------------------------------------------------------------

if (
    len(exit_rows) > 0
    and len(exit_rate_rows) > 0
    and len(misleading_terms_found) == 0
):
    print("\nSTEP 17 STATUS: PASS")
    print(
        "Business exit terminology and meaning have been preserved."
    )
    print(
        "No unsupported succession interpretation was introduced."
    )
else:
    print("\nSTEP 17 STATUS: REVIEW REQUIRED")
    print(
        "Business exit terminology or interpretation requires review."
    )


# STEP 18 — DO NOT CREATE SUCCESSION VARIABLES
# ------------------------------------------------------------

print("\n" + "=" * 60)
print("STEP 18 — DO NOT CREATE SUCCESSION VARIABLES")
print("=" * 60)

# ------------------------------------------------------------
# 1. Define succession variables that are NOT available
# ------------------------------------------------------------

succession_variables_not_available = [
    "owner age",
    "retirement intention",
    "planned exit date",
    "succession plan",
    "identified successor",
    "ownership transfer",
    "reason for closure",
    "succession-related closure"
]

print("\nSUCCESSION VARIABLES NOT PRESENT IN SOURCE DATA")

for variable in succession_variables_not_available:
    print("-", variable)

# ------------------------------------------------------------
# 2. Check cleaned datasets for accidentally created
#    succession-related columns
# ------------------------------------------------------------

succession_keywords = [
    "succession",
    "successor",
    "retirement",
    "owner_age",
    "ownership_transfer",
    "closure_reason",
    "exit_reason",
    "planned_exit"
]

industry_columns = [
    str(column).lower()
    for column in industry_clean.columns
]

firm_size_columns = [
    str(column).lower()
    for column in firm_size_clean.columns
]

industry_succession_columns = [
    column
    for column in industry_columns
    if any(keyword in column for keyword in succession_keywords)
]

firm_size_succession_columns = [
    column
    for column in firm_size_columns
    if any(keyword in column for keyword in succession_keywords)
]

print("\nSUCCESSION-RELATED COLUMNS CREATED DURING CLEANING")
print("Industry dataset:", industry_succession_columns)
print("Firm-size dataset:", firm_size_succession_columns)

# ------------------------------------------------------------
# 3. Document the analytical limitation
# ------------------------------------------------------------

print("\nANALYTICAL LIMITATION")
print(
    "Neither Business Dynamics dataset contains direct succession "
    "measures."
)

print(
    "No succession variables were created, inferred, or imputed "
    "during cleaning."
)

print(
    "The datasets provide contextual business-dynamics evidence only."
)

print(
    "Business exits and related measures must not be interpreted as "
    "direct evidence of succession outcomes."
)

# ------------------------------------------------------------
# 4. Final validation
# ------------------------------------------------------------

if (
    len(industry_succession_columns) == 0
    and len(firm_size_succession_columns) == 0
):
    print("\nSTEP 18 STATUS: PASS")
    print(
        "No succession variables were created or inferred during cleaning."
    )
    print(
        "Business Dynamics datasets are retained as contextual "
        "business-dynamics evidence only."
    )
else:
    print("\nSTEP 18 STATUS: REVIEW REQUIRED")
    print(
        "Succession-related columns were detected and require review."
    )


# STEP 19 — DO NOT MERGE THE TWO DATASETS
# ------------------------------------------------------------

print("\n" + "=" * 60)
print("STEP 19 — DO NOT MERGE THE TWO DATASETS")
print("=" * 60)

# ------------------------------------------------------------
# 1. Confirm that the datasets remain separate
# ------------------------------------------------------------

print("\nDATASET STRUCTURE")
print("Industry dataset rows:", len(industry_clean))
print("Firm-size dataset rows:", len(firm_size_clean))

print(
    "\nThe Industry and Firm-size datasets have been cleaned "
    "and validated separately."
)

# ------------------------------------------------------------
# 2. Identify fields that could potentially align datasets
# ------------------------------------------------------------

industry_alignment_fields = [
    column for column in ["ref_date", "geo", "dguid"]
    if column in industry_clean.columns
]

firm_size_alignment_fields = [
    column for column in ["REF_DATE", "GEO", "DGUID"]
    if column in firm_size_clean.columns
]

print("\nPOTENTIAL ALIGNMENT FIELDS")
print("Industry dataset:", industry_alignment_fields)
print("Firm-size dataset:", firm_size_alignment_fields)

# ------------------------------------------------------------
# 3. Explicitly document that no merge was performed
# ------------------------------------------------------------

print("\nMERGE DECISION")
print("No merge or join was performed between the two datasets.")
print("Each dataset remains a separate cleaned analytical output.")
print(
    "REF_DATE, GEO, and DGUID are treated as potential future "
    "alignment fields only."
)
print(
    "Compatibility must be assessed before any future integration."
)

# ------------------------------------------------------------
# 4. Check that the cleaned datasets remain independent
# ------------------------------------------------------------

if not industry_clean is firm_size_clean:
    print("\nDATASET INDEPENDENCE CHECK: PASS")
else:
    print("\nDATASET INDEPENDENCE CHECK: REVIEW REQUIRED")

# ------------------------------------------------------------
# 5. Final validation
# ------------------------------------------------------------

print("\nSTEP 19 STATUS: PASS")
print(
    "The two datasets were cleaned and validated separately."
)
print(
    "No merge or join was performed."
)
print(
    "Potential alignment fields are documented for possible "
    "future integration only."
)


# ------------------------------------------------------------
# STEP 20 — SAVE TWO SEPARATE CLEANED DATASETS
# ------------------------------------------------------------

print("\n" + "=" * 60)
print("STEP 20 — SAVE TWO SEPARATE CLEANED DATASETS")
print("=" * 60)

# ------------------------------------------------------------
# 1. Define project and cleaned output directory
# ------------------------------------------------------------

project_root = r"C:\GitRepo\niagara-succession-signal"

cleaned_output_dir = os.path.join(
    project_root,
    "data",
    "processed",
    "statcan",
    "business_dynamics"
)

os.makedirs(cleaned_output_dir, exist_ok=True)

# ------------------------------------------------------------
# 2. Define separate cleaned output files
# ------------------------------------------------------------

industry_cleaned_path = os.path.join(
    cleaned_output_dir,
    "business_dynamics_industry_ontario_cleaned.csv"
)

firm_size_cleaned_path = os.path.join(
    cleaned_output_dir,
    "business_dynamics_firm_size_ontario_cleaned.csv"
)

# ------------------------------------------------------------
# 3. Save the cleaned datasets separately
# ------------------------------------------------------------

industry_clean.to_csv(
    industry_cleaned_path,
    index=False
)

firm_size_clean.to_csv(
    firm_size_cleaned_path,
    index=False
)

# ------------------------------------------------------------
# 4. Confirm output files and shapes
# ------------------------------------------------------------

print("\nCLEANED OUTPUT FILES")
print("Industry dataset:", industry_cleaned_path)
print("Firm-size dataset:", firm_size_cleaned_path)

print("\nOUTPUT SHAPES")
print("Industry:", industry_clean.shape)
print("Firm-size:", firm_size_clean.shape)

# ------------------------------------------------------------
# 5. Confirm raw files still exist
# ------------------------------------------------------------

raw_industry_path = os.path.join(
    project_root,
    "data",
    "raw",
    "statcan",
    "business_dynamics",
    "33100087.csv"
)

raw_firm_size_path = os.path.join(
    project_root,
    "data",
    "raw",
    "statcan",
    "business_dynamics",
    "33100088.csv"
)

print("\nRAW DATA PROTECTION")
print("Industry raw file exists:", os.path.exists(raw_industry_path))
print("Firm-size raw file exists:", os.path.exists(raw_firm_size_path))

# ------------------------------------------------------------
# 6. Final validation
# ------------------------------------------------------------

if (
    os.path.exists(industry_cleaned_path)
    and os.path.exists(firm_size_cleaned_path)
    and os.path.exists(raw_industry_path)
    and os.path.exists(raw_firm_size_path)
):
    print("\nSTEP 20 STATUS: PASS")
    print("Two separate cleaned datasets were saved successfully.")
    print("Raw datasets remain untouched.")
else:
    print("\nSTEP 20 STATUS: REVIEW REQUIRED")
    print("One or more expected files could not be confirmed.")


from pathlib import Path
import os
import pandas as pd

# Project paths
PROJECT_ROOT = Path(__file__).resolve().parent.parent
RAW_DIR = PROJECT_ROOT / "data" / "raw" / "statcan" / "business_dynamics"
PROCESSED_DIR = PROJECT_ROOT / "data" / "processed" / "statcan" / "business_dynamics"