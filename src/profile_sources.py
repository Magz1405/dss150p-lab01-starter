import os
import pandas as pd
from pathlib import Path

# Set the base directory to the current folder (where your files are located)
BASE_DIR = Path(".")

# 1. Load the data using format-appropriate readers
customers = pd.read_csv(BASE_DIR / "customers.csv")
orders = pd.read_json(BASE_DIR / "orders.json")
products = pd.read_parquet(BASE_DIR / "products.parquet")

# Dictionary to loop through each dataset
datasets = {
    "customers.csv": (BASE_DIR / "customers.csv", customers),
    "orders.json": (BASE_DIR / "orders.json", orders),
    "products.parquet": (BASE_DIR / "products.parquet", products),
}

# 2. Loop through and print the required profile items
for name, (path, df) in datasets.items():
    print(f"\n{'='*50}")
    print(f"PROFILING: {name}")
    print(f"{'='*50}")
    
    # File name and file size in KB
    size_kb = os.path.getsize(path) / 1024
    print(f"File Name: {name}")
    print(f"File Size: {size_kb:.2f} KB\n")
    
    # Number of rows and columns
    print(f"Shape (Rows, Columns): {df.shape}")
    
    # Column names in original order
    print(f"Columns: {list(df.columns)}\n")
    
    # Inferred data type of every column
    print("--- Data Types ---")
    print(df.dtypes)
    
    # Number of missing/null values per column
    print("\n--- Missing/Null Values ---")
    print(df.isna().sum())
    
   # Number of fully duplicated rows (convert to string to handle nested JSON/dicts)
    print(f"\nFully Duplicated Rows: {df.astype(str).duplicated().sum()}")
    
    # Number of distinct values per column
    print("\n--- Distinct Values per Column ---")
    print(df.astype(str).nunique())
    
    # For numeric columns: minimum and maximum values
    numeric_cols = df.select_dtypes(include='number')
    if not numeric_cols.empty:
        print("\n--- Numeric Columns (Min/Max) ---")
        print(numeric_cols.agg(['min', 'max']))
    
    # For date/time-like columns: earliest and latest values
    datetime_cols = df.select_dtypes(include='datetime')
    if not datetime_cols.empty:
        print("\n--- Datetime Columns (Min/Max) ---")
        print(datetime_cols.agg(['min', 'max']))
        
    # First five records
    print("\n--- First 5 Records ---")
    print(df.head())
    print("\n")