# Tsuna Excel Sorting App

This repository contains a small command line utility to load an Excel file and sort its contents by a chosen column. Entire rows are reordered based on the selected column, but the first column cannot be used as the sort key. The first column stays paired with its original row values.

## Requirements

- Python 3.12 or higher
- `pandas` and `openpyxl` packages

Install the required packages with:

```bash
pip install pandas openpyxl
```

## Usage

```bash
python excel_sort.py path/to/file.xlsx --column COLUMN_NAME --output sorted.xlsx
```

The script sorts data by `COLUMN_NAME` while moving the entire row so the first column travels with its row. When saving to an output file, cells that have changed position are highlighted in yellow‑green. If `--output` is omitted, the sorted data will be printed to the console.
