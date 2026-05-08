"""Rung 5: Apply — solved version.

Reads a Python source file and prints:

    funcs: <count>
    imports: <count>
    longest fn: <name> (<lines>)

Reuses list_imports (guided.py) and function_summary (solo.py) via
the dynamic-import pattern from the starter.

    uv run python apply.py solo.py
"""
from __future__ import annotations

import ast
import sys
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path

_HERE = Path(__file__).parent

_g = spec_from_file_location("_guided", _HERE / "guided.py")
_guided = module_from_spec(_g)
_g.loader.exec_module(_guided)

_s = spec_from_file_location("_solo", _HERE / "solo.py")
_solo = module_from_spec(_s)
_s.loader.exec_module(_solo)


def main() -> None:
    if len(sys.argv) != 2:
        print("usage: python apply.py <python-file>")
        sys.exit(1)
    path = Path(sys.argv[1])
    src = path.read_text(encoding="utf-8")
    imports = _guided.list_imports(src)
    funcs = _solo.function_summary(src)
    print(f"funcs: {len(funcs)}")
    print(f"imports: {len(imports)}")
    if funcs:
        tree = ast.parse(src)
        lengths: dict[str, int] = {}
        for node in ast.walk(tree):
            if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
                end = getattr(node, "end_lineno", node.lineno) or node.lineno
                lengths[node.name] = end - node.lineno + 1
        name, length = max(lengths.items(), key=lambda kv: kv[1])
        print(f"longest fn: {name} ({length} lines)")


if __name__ == "__main__":
    main()
