"""Tests for rung 2."""
import importlib.util
from pathlib import Path

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_2"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "fluency.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


def test_eq_mut():
    """Two Mut(1) instances ARE equal — dataclass synthesizes __eq__."""
    assert ex.EQ_MUT is True


def test_is_mut():
    """Two distinct constructor calls return distinct objects."""
    assert ex.IS_MUT is False


def test_hashable_imm():
    """Frozen dataclasses are hashable."""
    assert ex.HASHABLE_IMM is True


def test_hashable_mut():
    """Plain @dataclass with __eq__ becomes unhashable."""
    assert ex.HASHABLE_MUT is False
