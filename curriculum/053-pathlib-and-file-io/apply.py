"""Rung 5: Apply.

Tiny CLI: print the largest file in a directory tree, with its size.

Try it:
    uv run python apply.py /path/to/folder

Patterns: P-01 (sentinel-loop), P-03 (walrus-in-condition).
"""
import sys
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path

_spec = spec_from_file_location("_solo", Path(__file__).parent / "solo.py")
_solo = module_from_spec(_spec)
_spec.loader.exec_module(_solo)


def main() -> None:
    if len(sys.argv) < 2:
        print("usage: apply.py <folder>")
        return
    folder = Path(sys.argv[1])
    if not folder.is_dir():
        print(f"not a directory: {folder}")
        return
    biggest = _solo.largest_file(folder)
    if biggest is None:
        print(f"(no files under {folder})")
        return
    size_kb = biggest.stat().st_size / 1024
    print(f"{size_kb:>8.1f} KB  {biggest}")


if __name__ == "__main__":
    main()
