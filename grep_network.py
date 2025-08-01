import os
import re


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


def main() -> None:
    directory = input("検索するディレクトリを入力してください: ").strip()
    pattern = input("検索する文字列(正規表現)を入力してください: ").strip()

    if not os.path.isdir(directory):
        print(f"Directory not found: {directory}")
        return

    results = search_directory(directory, pattern)

    if not results:
        print("該当する行は見つかりませんでした。")
        return

    print("\n=== 検索結果 ===")
    for path, lineno, text in results:
        print(f"{path}:{lineno}: {text}")


if __name__ == "__main__":
    main()
