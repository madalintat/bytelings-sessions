"""Tests for rung 2."""
import importlib.util
from datetime import datetime
from pathlib import Path

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_2"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "02_fluency.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


def test_construct_with_fields():
    r = ex.LogRecord(
        ts=datetime(2026, 5, 8, 10), level="INFO", fields={"path": "/x"}
    )
    assert r.level == "INFO"
    assert r.fields == {"path": "/x"}


def test_default_fields_is_empty_dict():
    r = ex.LogRecord(ts=datetime(2026, 5, 8, 10), level="INFO")
    assert r.fields == {}


def test_default_fields_independent_per_instance():
    """If you used `fields: dict = {}` instead of default_factory=dict,
    all instances share the same dict — a classic mutable-default bug."""
    a = ex.LogRecord(ts=datetime(2026, 5, 8, 10), level="INFO")
    b = ex.LogRecord(ts=datetime(2026, 5, 8, 10), level="INFO")
    a.fields["mutated"] = "yes"
    assert "mutated" not in b.fields, (
        "use field(default_factory=dict), not `fields={}`"
    )
