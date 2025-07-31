import argparse
import sys

try:
    from openpyxl import load_workbook
    from openpyxl.styles import PatternFill
except ImportError:
    pass  # openpyxl is optional unless writing to Excel

try:
    import pandas as pd
except ImportError as e:
    sys.exit("pandas library is required. Please install pandas and openpyxl before running this script.")

def main():
    parser = argparse.ArgumentParser(description="Read an Excel file and sort it by a specific column")
    parser.add_argument("input", help="Path to the Excel file to read")
    parser.add_argument("--column", required=True, help="Column name to sort by")
    parser.add_argument("--output", help="Output Excel file path. If omitted, sorted data is printed")
    args = parser.parse_args()


    df = pd.read_excel(args.input)
    if args.column not in df.columns:
        sys.exit(f"Column '{args.column}' not found in the spreadsheet")
    if args.column == df.columns[0]:
        sys.exit("Sorting by the first column is not allowed because the first column must remain unchanged")

    first_col = df.columns[0]
    first_data = df[first_col]

    other_cols = df.columns[1:]
    df_other = df[other_cols].sort_values(by=args.column).reset_index(drop=True)
    df_sorted = pd.concat([first_data, df_other], axis=1)

    if args.output:
        df_sorted.to_excel(args.output, index=False)
        print(f"Sorted data saved to {args.output}")
    else:
        print(df_sorted)

if __name__ == "__main__":
    main()
