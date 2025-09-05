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
view the results in a list below. Each time you press **検索**, new results are
appended to the list so previous searches remain visible until you clear them.
Use the **クリアー** button to remove all output. The input boxes and results
area grow or shrink when the window is resized. Subdirectories are searched
automatically and matching results are grouped by file. The searched directory
is shown once at the top, then each file name appears on a line beginning with
`検索ファイル:` and the matching lines are indented underneath. Special
characters like `[` are automatically escaped so they can be searched without
using a backslash. Text files are opened in UTF‑8 with decoding errors ignored,
allowing files containing multi-byte characters to be processed.

```bash
python grep_network.py
```



## Web App: Automation & Search Assistant

This repository now includes a simple Streamlit web application that combines the Excel/CSV automation assistant with an optional document search and summarization tool.

### Installation

Install the web app dependencies:

```bash
pip install -r requirements.txt
```

### Running

Launch the app with:

```bash
streamlit run app.py
```

Set the `OPENAI_API_KEY` environment variable before running. The Excel/CSV tab accepts a file upload and a natural language instruction, generates Python code with the OpenAI API, executes it, and displays the result. The Document Search tab lets you upload plain text files, search them using embeddings, and view an AI-generated summary of the best match.
