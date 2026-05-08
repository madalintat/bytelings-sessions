"""Rung 5: Apply.

Tiny CLI: pretty-print a tree, level by level.

Reads a tree literal in the same format as Day 87:
    "(value left right)"   where left/right are also trees, or "_"

Then prints each level on its own line.

Try it:
    echo "(4 (2 (1 _ _) (3 _ _)) (6 _ (7 _ _)))" | uv run python apply.py
    -> 4
       2 6
       1 3 7
"""
import sys
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path

_spec = spec_from_file_location(
    "_guided", Path(__file__).parent / "guided.py"
)
_guided = module_from_spec(_spec)
_spec.loader.exec_module(_guided)


def parse(s: str):
    s = s.strip()
    if s.startswith("_"):
        return None, s[1:]
    assert s.startswith("("), f"expected '(' at: {s!r}"
    s = s[1:]
    i = 0
    while i < len(s) and not s[i].isspace():
        i += 1
    value = int(s[:i])
    s = s[i:].lstrip()
    left, s = parse(s)
    s = s.lstrip()
    right, s = parse(s)
    s = s.lstrip()
    assert s.startswith(")"), f"expected ')' at: {s!r}"
    return _guided.TreeNode(value, left, right), s[1:]


def main() -> None:
    text = sys.stdin.read().strip()
    if not text:
        print("(no input)")
        return
    root, _ = parse(text)
    for level in _guided.levels(root):
        print(" ".join(str(v) for v in level))


if __name__ == "__main__":
    main()
