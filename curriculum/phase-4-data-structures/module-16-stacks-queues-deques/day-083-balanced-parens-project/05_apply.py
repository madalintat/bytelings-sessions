"""Rung 5: Apply.

Tiny CLI: a bracket linter for files.

Usage:
    uv run python 05_apply.py <path>

Reads the file, runs check_brackets, and prints either OK or a
one-line diagnostic with the (line, column) and a caret pointing at
the bad character.
"""
import sys
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path

_spec = spec_from_file_location(
    "_guided", Path(__file__).parent / "03_guided.py"
)
_guided = module_from_spec(_spec)
_spec.loader.exec_module(_guided)


def index_to_line_col(text: str, idx: int) -> tuple[int, int]:
    line = text.count("\n", 0, idx) + 1
    last_nl = text.rfind("\n", 0, idx)
    col = idx - (last_nl + 1) + 1
    return line, col


def main() -> None:
    if len(sys.argv) != 2:
        print("usage: 05_apply.py <path>", file=sys.stderr)
        sys.exit(2)
    text = Path(sys.argv[1]).read_text()
    problem = _guided.check_brackets(text)
    if problem is None:
        print("OK")
        return
    line, col = index_to_line_col(text, problem.index)
    print(f"{problem.kind} at line {line}, col {col}: {problem.char!r}")


if __name__ == "__main__":
    main()
