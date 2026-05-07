"""HIDDEN tests for rung 4 — pin down behavior and check the refactor."""
import importlib.util
from pathlib import Path

import pytest

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_4"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "04_solo.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


@pytest.mark.parametrize(
    "user, expected",
    [
        (None, "anonymous"),
        ({}, "anonymous"),
        ({"email": "x@y.z"}, "x@y.z"),
        ({"name": "Ada"}, "Ada"),
        ({"name": "Ada", "title": "Dr."}, "Dr. Ada"),
        ({"name": "Ada", "suffix": "PhD"}, "Ada PhD"),
        ({"name": "Ada", "title": "Dr.", "suffix": "PhD"}, "Dr. Ada PhD"),
        ({"name": "", "email": "a@b"}, "a@b"),
        ({"name": "Ada", "email": "ignored@x"}, "Ada"),
    ],
)
def test_behavior_preserved(user, expected):
    assert ex.format_user_label(user) == expected


def test_max_nesting_depth():
    """Heuristic: refactor should have removed the 3-deep nesting."""
    import inspect

    src = inspect.getsource(ex.format_user_label)
    # Each leading-tab level is +4 spaces (after the 4 for body).
    # 3-deep nesting = lines starting with 16 spaces or more.
    deep_lines = [
        ln for ln in src.splitlines() if ln.startswith(" " * 16) and ln.strip()
    ]
    assert len(deep_lines) == 0, (
        f"still has lines at 4+ levels of indent: {deep_lines[:2]}"
    )
