"""Rung 5: Apply — solved version.

Runs the full pyproject mini-pipeline and verifies the results inline.
"""
from __future__ import annotations
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path

_HERE = Path(__file__).parent

_f = spec_from_file_location("_fluency", _HERE / "fluency.py")
_fluency = module_from_spec(_f)
_f.loader.exec_module(_fluency)

_g = spec_from_file_location("_guided", _HERE / "guided.py")
_guided = module_from_spec(_g)
_g.loader.exec_module(_guided)

_s = spec_from_file_location("_solo", _HERE / "solo.py")
_solo = module_from_spec(_s)
_s.loader.exec_module(_solo)

GOOD_PYPROJECT = """
[project]
name = "my-linter"
version = "0.1.0"
requires-python = ">=3.12"
dependencies = [
    "click>=8.1",
    "rich",
    "httpx>=0.27.0,<1",
]

[project.scripts]
my-linter = "my_linter.cli:main"

[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"
"""


def main() -> None:
    print("=== Validation ===")
    errors = _fluency.validate_pyproject(GOOD_PYPROJECT)
    assert errors == []
    print("  Good pyproject: no errors ✓")

    broken_errors = _fluency.validate_pyproject(_fluency.SAMPLE_PYPROJECT)
    assert "missing required table: build-system" in broken_errors
    print(f"  Broken pyproject errors: {broken_errors}")

    print("\n=== Console-script target ===")
    target = _guided.console_script_target(GOOD_PYPROJECT, "my-linter")
    assert target == "my_linter.cli:main"
    print(f"  my-linter → {target}")
    assert _guided.console_script_target(GOOD_PYPROJECT, "no-such-cmd") is None
    print("  no-such-cmd → None")

    print("\n=== Dependencies ===")
    deps = _solo.parse_dependencies(GOOD_PYPROJECT)
    assert ("click", ">=8.1") in deps
    assert ("rich", "") in deps
    assert ("httpx", ">=0.27.0,<1") in deps
    for pkg, spec in deps:
        print(f"  {pkg!r:20s} {spec!r}")

    print("\n✓ pyproject pipeline works.")


if __name__ == "__main__":
    main()
