import csv
import collections

# Corrected syntax: separate statements
file_path = "data/raw/statcan/business_counts/33101176-eng/33101176.csv"

def run_audit():
    try:
        with open(file_path, mode='r', encoding='utf-8-sig') as f:
            reader = csv.DictReader(f)
            
            row_count = 0
            missing_values_count = 0
            suppressed_values_count = 0
            
            # Data collection sets/lists
            ref_dates = set()
            niagara_geos = set()
            employment_sizes = set()
            
            # For duplicate checking (Update keys based on actual CSV columns)
            # Example composite key: REF_DATE, GEO, DGUID, North American Industry Classification System (NAICS), Employment size
            seen_records = set()
            duplicate_count = 0
            
            for row in reader:
                row_count += 1
                
                # 1. Track unique Reference Dates
                if 'REF_DATE' in row:
                    ref_dates.add(row['REF_DATE'])
                
                # 2. Identify Niagara GEOs/DGUIDs
                geo_val = row.get('GEO', '')
                if 'niagara' in geo_val.lower() or 'st. catharines' in geo_val.lower():
                    dguid_val = row.get('DGUID', 'Unknown DGUID')
                    niagara_geos.add(f"{geo_val} (DGUID: {dguid_val})")
                    
                # 3. Track Employment Size categories
                if 'Employment size' in row:
                    employment_sizes.add(row['Employment size'])
                
                # 4. Check for missing/suppressed values
                if not row.get('VALUE'):
                    missing_values_count += 1
                if row.get('STATUS') in ['x', 'X', 'F'] or row.get('SYMBOL') in ['x', 'X']:
                    suppressed_values_count += 1
                
                # 5. Duplicate Check
                # Adjust these column names if they differ in your CSV header
                composite_key = (
                    row.get('REF_DATE'),
                    row.get('GEO'),
                    row.get('North American Industry Classification System (NAICS)'),
                    row.get('Employment size')
                )
                
                if composite_key in seen_records:
                    duplicate_count += 1
                else:
                    seen_records.add(composite_key)

            # Print Findings to use in CANADIAN_BUSINESS_COUNTS_AUDIT.md
            print(f"--- AUDIT RESULTS ---")
            print(f"Total Rows: {row_count}")
            print(f"Unique REF_DATEs: {ref_dates}")
            print(f"Niagara Geographies found:\n  - " + "\n  - ".join(niagara_geos))
            print(f"Employment Size Categories:\n  - " + "\n  - ".join(employment_sizes))
            print(f"Missing 'VALUE' count: {missing_values_count}")
            print(f"Suppressed Records count: {suppressed_values_count}")
            print(f"Exact Duplicates found (based on composite key): {duplicate_count}")

    # Corrected Exception Handling with a clear, descriptive message
    except FileNotFoundError:
        print(f"Error: The dataset could not be found at '{file_path}'. "
              f"Please ensure the file has been extracted and resides in the correct directory.")

if __name__ == "__main__":
    run_audit()