import argparse
import os
import re
import sys
import html
import webbrowser


def grep_text_files(
    directory: str, pattern: str, output: str, html_output: str | None = None
) -> None:
    """Write searched file names and matching lines to ``output``.

    If ``html_output`` is provided, a simple HTML report is also generated so the
    results can be viewed in a browser. Matched lines are prefixed with
    ``"=== found ==="``. Files are read as UTF-8 and decoding errors are
    ignored so that text containing multi-byte characters does not stop the
    search.
    """
    regex = re.compile(pattern)
    try:
        # Write the results in Shift-JIS encoding. Characters that cannot be
        # represented are replaced so the script never fails when encountering
        # unexpected text.
        with open(output, "w", encoding="shift_jis", errors="replace") as out_fh:
            html_lines = [] if html_output else None
            for root, _, files in os.walk(directory):
                for filename in files:
                    if filename.lower().endswith(".txt"):
                        path = os.path.join(root, filename)
                        # Skip the output file if it appears in the walk
                        if (
                            os.path.abspath(path) == os.path.abspath(output)
                            or filename.lower() == "grep_out.txt"
                        ):
                            continue
                        out_fh.write(f"{path}\n")
                        if html_lines is not None:
                            html_lines.append(path)
                        try:
                            with open(path, "r", encoding="utf-8", errors="ignore") as fh:
                                for line in fh:
                                    if regex.search(line):
                                        out_fh.write("=== found === " + line)
                                        if html_lines is not None:
                                            html_lines.append("=== found === " + line.rstrip("\n"))
                        except FileNotFoundError:
                            print(f"File not found: {path}", file=sys.stderr)
                        except OSError as exc:
                            print(f"Error reading {path}: {exc}", file=sys.stderr)
        if html_lines is not None:
            with open(html_output, "w", encoding="utf-8") as html_fh:
                html_fh.write("<html><body><pre>\n")
                for line in html_lines:
                    html_fh.write(html.escape(line) + "\n")
                html_fh.write("</pre></body></html>\n")
            webbrowser.open(f"file://{os.path.abspath(html_output)}")
    except OSError as exc:
        sys.exit(f"Cannot write to {output}: {exc}")


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Search for lines matching PATTERN in text files under a network directory"
    )
    parser.add_argument("directory", help="Path to the directory on the network")
    parser.add_argument("pattern", help="Regex pattern to search for")
    parser.add_argument(
        "--output",
        "-o",
        default="grep_out.txt",
        help="File to write matching lines (default: grep_out.txt)",
    )
    parser.add_argument(
        "--html",
        help="Optional HTML file to also write results for viewing in a browser",
    )
    args = parser.parse_args()

    if not os.path.isdir(args.directory):
        sys.exit(f"Directory not found: {args.directory}")

    grep_text_files(args.directory, args.pattern, args.output, args.html)
    print(f"Wrote matching lines to {args.output}")
    if args.html:
        print(f"HTML results saved to {args.html}")


if __name__ == "__main__":
    main()
