"""Rung 5: Apply.

Tiny CLI: print a quick "tree report" given a tree literal on stdin.

Input format (one line, parens-style):
    "(value left right)"   where left and right are also trees, or "_"
Examples:
    "(1 _ _)"                   -> single leaf
    "(1 (2 _ _) (3 _ _))"       -> two children
    "(1 (2 (4 _ _) _) (3 _ _))"

Output: size, height, leaves, balanced?

This is mostly an excuse to traverse the tree we built; parsing is
intentionally tiny.

Try it:
    echo "(1 (2 _ _) (3 _ _))" | uv run python apply.py
"""
import sys
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path

_spec = spec_from_file_location(
    "_guided", Path(__file__).parent / "guided.py"
)
_guided = module_from_spec(_spec)
_spec.loader.exec_module(_guided)

_spec_f = spec_from_file_location(
    "_fluency", Path(__file__).parent / "fluency.py"
)
_fluency = module_from_spec(_spec_f)
_spec_f.loader.exec_module(_fluency)


def parse(s: str):
    s = s.strip()
    if s == "_":
        return None, ""
    assert s.startswith("("), f"expected '(' at: {s!r}"
    s = s[1:]
    # value is the first token
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
    # bridge node types between modules (they are structurally identical)
    print(f"size={_fluency.size(root)}")
    print(f"height={_fluency.height(root)}")
    print(f"leaves={_guided.count_leaves(root)}")
    print(f"max={_guided.max_value(root)}")
    print(f"balanced={_guided.is_balanced(root)}")


if __name__ == "__main__":
    main()
