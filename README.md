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
Sorting by the first column is not supported. If an output file is provided,
cells in columns other than the first that change position after sorting are
highlighted in yellow–green. If `--output` is omitted, the sorted data will be
printed to the console.

## Grep network directory

The repository also includes a small utility to search through all `.txt` files
in a directory (for example, on a network share). Running `python
grep_network.py` launches a simple GUI where you can select the directory to
search via a folder selection dialog, enter the search string in an edit box and
view the results in a list below. The input boxes and results area grow or
shrink when the window is resized. Subdirectories are searched automatically and
any matching lines are displayed with their file path and line number. Text
files are opened in UTF‑8 with decoding errors ignored, allowing files
containing multi-byte characters to be processed.

```bash
python grep_network.py
```


