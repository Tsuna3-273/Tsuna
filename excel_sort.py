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

    df_original = pd.read_excel(args.input)
    if args.column not in df_original.columns:
        sys.exit(f"Column '{args.column}' not found in the spreadsheet")
    first_col_name = df_original.columns[0]
    if args.column == first_col_name:
        sys.exit(
            "Sorting by the first column is not allowed because the first column must remain unchanged"
        )

    # Sort entire rows based on the chosen column. The first column moves with
    # its row but is not used as a sort key.
    df_sorted = df_original.sort_values(by=args.column).reset_index(drop=True)

    if args.output:
        df_sorted.to_excel(args.output, index=False)

        try:
            wb = load_workbook(args.output)
            ws = wb.active
            fill = PatternFill(start_color="CCFF99", end_color="CCFF99", fill_type="solid")
            diff = df_sorted.ne(df_original)
            for i, row in enumerate(diff.itertuples(index=False), start=2):
                for j, changed in enumerate(row, start=1):
                    if changed:
                        ws.cell(row=i, column=j).fill = fill
            wb.save(args.output)
        except Exception as e:
            print(f"Failed to apply cell highlighting: {e}")

        print(f"Sorted data saved to {args.output}")
    else:
        print(df_sorted)

if __name__ == "__main__":
    main()
