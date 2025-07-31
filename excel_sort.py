import argparse
import sys

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
    df_sorted = df.sort_values(by=args.column)

    if args.output:
        df_sorted.to_excel(args.output, index=False)
        print(f"Sorted data saved to {args.output}")
    else:
        print(df_sorted)

if __name__ == "__main__":
    main()
