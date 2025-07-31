# Tsuna Excel Sorting App

This repository contains a small command line utility to load an Excel file and sort its contents by a chosen column. The first column is kept exactly as it originally appeared and does not move with the sorted rows. Sorting by the first column itself is not allowed.

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

The script sorts data by `COLUMN_NAME`. Only columns after the first one are reordered; the first column stays in its original order. When saving to an output file, cells that have changed position are highlighted in yellow‑green. If `--output` is omitted, the sorted data will be printed to the console.
