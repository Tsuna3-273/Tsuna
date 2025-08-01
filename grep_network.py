import os
import re
import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext


def search_directory(directory: str, pattern: str) -> list[tuple[str, int, str]]:
    """Return a list of tuples ``(file_path, line_number, line_text)`` for lines
    matching ``pattern`` in ``directory`` and all subdirectories."""

    regex = re.compile(pattern)
    matches: list[tuple[str, int, str]] = []

    for root, _, files in os.walk(directory):
        for filename in files:
            if filename.lower().endswith(".txt"):
                path = os.path.join(root, filename)
                try:
                    with open(path, "r", encoding="utf-8", errors="ignore") as fh:
                        for lineno, line in enumerate(fh, start=1):
                            if regex.search(line):
                                matches.append((path, lineno, line.rstrip("\n")))
                except OSError as exc:
                    print(f"Error reading {path}: {exc}")

    return matches


def browse_directory(var: tk.StringVar) -> None:
    """Open a directory chooser and set ``var`` to the selected path."""

    path = filedialog.askdirectory()
    if path:
        var.set(path)


def perform_search(
    dir_var: tk.StringVar,
    pattern_var: tk.StringVar,
    output: scrolledtext.ScrolledText,
) -> None:
    """Run the search and append results to ``output``."""

    directory = dir_var.get()
    pattern = pattern_var.get()

    if not directory:
        messagebox.showerror("エラー", "検索するディレクトリを指定してください")
        return
    if not os.path.isdir(directory):
        messagebox.showerror("エラー", f"Directory not found: {directory}")
        return

    results = search_directory(directory, pattern)

    if not results:
        output.insert(tk.END, "該当する行は見つかりませんでした。\n")
        return

    for path, lineno, text in results:
        output.insert(tk.END, f"{path}:{lineno}: {text}\n")


def clear_results(output: scrolledtext.ScrolledText) -> None:
    """Remove all text from ``output``."""

    output.delete("1.0", tk.END)


def main() -> None:
    root = tk.Tk()
    root.title("Network Grep")

    dir_var = tk.StringVar()
    pattern_var = tk.StringVar()

    frame = tk.Frame(root, padx=10, pady=10)
    frame.pack(fill=tk.BOTH, expand=True)

    # Make widgets expand when the window is resized
    frame.columnconfigure(1, weight=1)
    frame.rowconfigure(2, weight=1)

    tk.Label(frame, text="検索するディレクトリ:").grid(row=0, column=0, sticky=tk.W)
    dir_entry = tk.Entry(frame, textvariable=dir_var)
    dir_entry.grid(row=0, column=1, sticky="ew")
    tk.Button(frame, text="参照", command=lambda: browse_directory(dir_var)).grid(row=0, column=2, padx=5)

    tk.Label(frame, text="検索文字列:").grid(row=1, column=0, pady=5, sticky=tk.W)
    pattern_entry = tk.Entry(frame, textvariable=pattern_var)
    pattern_entry.grid(row=1, column=1, sticky="ew")

    search_btn = tk.Button(
        frame,
        text="検索",
        command=lambda: perform_search(dir_var, pattern_var, results_box),
    )
    search_btn.grid(row=1, column=2, padx=5)

    results_box = scrolledtext.ScrolledText(frame)
    results_box.grid(row=2, column=0, columnspan=3, pady=10, sticky="nsew")

    clear_btn = tk.Button(frame, text="クリアー", command=lambda: clear_results(results_box))
    clear_btn.grid(row=3, column=1, sticky=tk.W)

    exit_btn = tk.Button(frame, text="終了", command=root.destroy)
    exit_btn.grid(row=3, column=2, sticky=tk.E)

    root.mainloop()


if __name__ == "__main__":
    main()
