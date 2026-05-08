"""Tests for rung 2."""
import importlib.util
from pathlib import Path

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_2"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "02_fluency.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


def test_add_and_lines():
    w = ex.ListWriter()
    w.add("alpha")
    w.add("beta")
    assert w.lines == ["alpha", "beta"]


def test_does_not_inherit_from_list():
    """Refactored ListWriter should COMPOSE a list, not BE a list."""
    assert not issubclass(ex.ListWriter, list), (
        "ListWriter must not inherit from list — store one instead"
    )


def test_no_list_methods_leak():
    """Composition means: only the public API is on the object."""
    w = ex.ListWriter()
    # `append` was a list method — it should not exist on the wrapper.
    assert not hasattr(w, "append"), (
        "stop exposing list's full API — give the wrapper its own surface"
    )


def test_indexing_not_supported():
    """If composing, indexing the writer directly should not work."""
    w = ex.ListWriter()
    w.add("x")
    import pytest
    with pytest.raises((TypeError, AttributeError)):
        _ = w[0]
