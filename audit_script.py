import csv

file_path = "data/raw/statcan/business_counts/33101176-eng/33101176.csv"

print("Loading massive dataset, please wait...\n")

try:
    with open(file_path, 'r', encoding='utf-8-sig') as f:
        reader = csv.reader(f)
        headers = next(reader)
        
        row_count = 0
        geo_index = headers.index('GEO') if 'GEO' in headers else -1
        unique_geos = set()
        
        for row in reader:
            row_count += 1
            if geo_index != -1 and len(row) > geo_index:
                unique_geos.add(row[geo_index])
                
    print("--- 1. DATASET STRUCTURE ---")
    print(f"Total Rows (excluding header): {row_count:,}")
    print(f"Total Columns: {len(headers)}")
    print(f"Column Names: {headers}\n")

    print("--- 2. GEOGRAPHY ---")
    if geo_index != -1:
        print(f"Unique Geographic Areas: {len(unique_geos)}")
        print(f"Sample Geographies: {list(unique_geos)[:5]}\n")
    else:
        print("No 'GEO' column found.")
        
except FileNotFoundError:
    print("Error: Still can't find it. Let me know if you see this!")