# Tsuna Excel Sorting App

This repository contains a command line tool to load an Excel file and sort its
contents by a chosen column while keeping the first column in its original order.

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

The script sorts data by `COLUMN_NAME` while leaving the first column unchanged.
Sorting by the first column is not supported. If `--output` is omitted, the
sorted data will be printed to the console.

