"""Rung 5: Apply.

A small "import graph" sanity-check: report whether your modules have
any circular imports.

Try it: uv run python apply.py
"""
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path

_spec = spec_from_file_location(
    "_solo", Path(__file__).parent / "solo.py"
)
_solo = module_from_spec(_spec)
_spec.loader.exec_module(_solo)


def main() -> None:
    clean_imports = {
        "app.cli":      ["app.config", "app.runner"],
        "app.config":   [],
        "app.runner":   ["app.config", "app.io"],
        "app.io":       [],
    }
    bad_imports = {
        "app.cli":      ["app.runner"],
        "app.runner":   ["app.io"],
        "app.io":       ["app.cli"],   # creates a cycle cli -> runner -> io -> cli
    }

    for label, graph in [("clean", clean_imports), ("bad  ", bad_imports)]:
        print(f"{label}: cycle = {_solo.has_cycle(graph)}")


if __name__ == "__main__":
    main()
