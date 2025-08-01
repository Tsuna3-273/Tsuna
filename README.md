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
in a directory (for example, on a network share). Run the script and you will be
prompted for the directory to search and the text or regular expression to look
for. Subdirectories are included automatically. Each matching line is printed to
the console in the format `path:line_number: line text` so the results are easy
to read. Text files are opened in UTF‑8 with decoding errors ignored, allowing
files containing multi-byte characters to be processed.

```bash
python grep_network.py
```


