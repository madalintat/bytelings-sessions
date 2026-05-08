"""Rung 5: Apply — workflow validator smoke test.

    uv run python apply.py

Runs the validator on a correct workflow (asserts []) and on a broken
one (asserts one complaint about id-token). Prints a final success line.
"""
from __future__ import annotations
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path

_HERE = Path(__file__).parent

_s = spec_from_file_location("_solo", _HERE / "solo.py")
_solo = module_from_spec(_s)
_s.loader.exec_module(_solo)

CORRECT_WORKFLOW = """\
name: Release
on:
  push:
    tags: ["v*"]
jobs:
  pypi-publish:
    runs-on: ubuntu-latest
    permissions:
      id-token: write
    environment:
      name: pypi
      url: https://pypi.org/project/my-linter/
    steps:
      - uses: actions/checkout@v4
      - uses: pypa/gh-action-pypi-publish@release/v1
"""

BROKEN_WORKFLOW = """\
name: Release
on:
  push:
    tags: ["v*"]
jobs:
  pypi-publish:
    runs-on: ubuntu-latest
    environment:
      name: pypi
      url: https://pypi.org/project/my-linter/
    steps:
      - uses: actions/checkout@v4
      - uses: pypa/gh-action-pypi-publish@release/v1
"""


def main() -> None:
    errors = _solo.validate_publish_workflow(CORRECT_WORKFLOW)
    assert errors == [], f"Correct workflow should pass, got: {errors}"
    print("Correct workflow: no complaints.")

    broken_errors = _solo.validate_publish_workflow(BROKEN_WORKFLOW)
    assert len(broken_errors) >= 1, (
        f"Broken workflow (no id-token) should have at least 1 complaint, "
        f"got: {broken_errors}"
    )
    assert any("id-token" in c for c in broken_errors), (
        f"Expected id-token complaint, got: {broken_errors}"
    )
    print(f"Broken workflow complaints ({len(broken_errors)}):")
    for c in broken_errors:
        print(f"  - {c}")

    print("\n✓ workflow validator works.")


if __name__ == "__main__":
    main()
