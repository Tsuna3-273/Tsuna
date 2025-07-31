# Tsuna Excel Sorting App

This repository contains a small command line utility to load an Excel file and sort its contents by a chosen column.

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

If `--output` is omitted, the sorted data will be printed to the console.
