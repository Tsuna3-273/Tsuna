import argparse
import os
import re
import sys


def grep_text_files(directory: str, pattern: str) -> None:
    """Print lines matching a pattern from all .txt files under directory."""
    regex = re.compile(pattern)
    for root, _, files in os.walk(directory):
        for filename in files:
            if filename.lower().endswith(".txt"):
                path = os.path.join(root, filename)
                try:
                    with open(path, "r", encoding="utf-8") as fh:
                        for line in fh:
                            if regex.search(line):
                                print(line.rstrip())
                except FileNotFoundError:
                    print(f"File not found: {path}", file=sys.stderr)
                except OSError as exc:
                    print(f"Error reading {path}: {exc}", file=sys.stderr)


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Search for lines matching PATTERN in text files under a network directory"
    )
    parser.add_argument("directory", help="Path to the directory on the network")
    parser.add_argument("pattern", help="Regex pattern to search for")
    args = parser.parse_args()

    if not os.path.isdir(args.directory):
        sys.exit(f"Directory not found: {args.directory}")

    grep_text_files(args.directory, args.pattern)


if __name__ == "__main__":
    main()
