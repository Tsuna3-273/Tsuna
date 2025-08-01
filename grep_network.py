import argparse
import os
import re
import sys


def grep_text_files(directory: str, pattern: str, output: str) -> None:
    """Write searched file names and matching lines to ``output``.

    Matched lines are prefixed with ``"=== matched ==="``. Files are read as
    UTF-8 and decoding errors are ignored so that text containing multi-byte
    characters does not stop the search.
    """
    regex = re.compile(pattern)
    try:
        with open(output, "w", encoding="utf-8") as out_fh:
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
                        try:
                            with open(path, "r", encoding="utf-8", errors="ignore") as fh:
                                for line in fh:
                                    if regex.search(line):
                                        out_fh.write("=== matched === " + line)
                        except FileNotFoundError:
                            print(f"File not found: {path}", file=sys.stderr)
                        except OSError as exc:
                            print(f"Error reading {path}: {exc}", file=sys.stderr)
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
    args = parser.parse_args()

    if not os.path.isdir(args.directory):
        sys.exit(f"Directory not found: {args.directory}")

    grep_text_files(args.directory, args.pattern, args.output)
    print(f"Wrote matching lines to {args.output}")


if __name__ == "__main__":
    main()
