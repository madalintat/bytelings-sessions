"""Tests for rung 3 — behavior + structural."""
import importlib.util
import inspect
from pathlib import Path

import pytest

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_3"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "03_guided.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


@pytest.mark.parametrize(
    "country, expected",
    [
        ("US", 5),
        ("CA", 7),
        ("MX", 10),
        ("UK", 12),
        ("DE", 15),
        ("FR", 15),
        ("IT", 15),
        ("ES", 15),
        ("JP", 25),
        ("XX", 25),
    ],
)
def test_costs(country, expected):
    assert ex.shipping_cost(country) == expected


def test_table_populated():
    """COSTS must have entries — proves you actually built the table."""
    assert len(ex.COSTS) >= 8, "fill out COSTS"


def test_shipping_uses_table_not_long_if():
    """The function body should be short — if/elif chain is a smell."""
    src = inspect.getsource(ex.shipping_cost)
    # Heuristic: refactored body has few/no `elif` branches.
    assert src.count("elif") == 0, "replace the elif chain with COSTS.get(...)"
