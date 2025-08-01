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

The repository also includes a small utility to search for matching lines in
text files under a directory (for example, on a network share). Each searched
file name is written to the output, and matching lines are prefixed with
`=== found ===`. The script ignores the output file when searching. Results
are written to a file, which defaults to `grep_out.txt` but can be changed with
`--output`. Text files are opened in UTF‑8 with decoding errors ignored so
multi-byte characters are supported. The output file is encoded as Shift‑JIS
so it can be viewed with tools expecting that encoding. Use `--html` to
generate an additional HTML report that opens in your default browser.

```bash
python grep_network.py DIRECTORY PATTERN --output results.txt --html results.html
```


