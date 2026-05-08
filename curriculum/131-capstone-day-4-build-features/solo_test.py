"""HIDDEN tests for rung 4 — do not peek before solving solo.py."""
from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_4"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "solo.py")
ex = importlib.util.module_from_spec(_spec)
sys.modules[_NAME] = ex
_spec.loader.exec_module(ex)

_CFG = {
    "function-too-long-max": 50,
    "nested-loop-depth-max": 3,
}


def test_function_too_long_fires():
    assert ex.apply_threshold("function-too-long", _CFG, 51) is True


def test_function_too_long_at_limit_does_not_fire():
    assert ex.apply_threshold("function-too-long", _CFG, 50) is False


def test_function_too_long_under_limit():
    assert ex.apply_threshold("function-too-long", _CFG, 10) is False


def test_nested_loop_fires():
    assert ex.apply_threshold("nested-loop-depth", _CFG, 4) is True


def test_nested_loop_at_limit_does_not_fire():
    assert ex.apply_threshold("nested-loop-depth", _CFG, 3) is False


def test_nested_loop_under_limit():
    assert ex.apply_threshold("nested-loop-depth", _CFG, 1) is False


def test_custom_threshold():
    cfg = {"function-too-long-max": 10, "nested-loop-depth-max": 1}
    assert ex.apply_threshold("function-too-long", cfg, 11) is True
    assert ex.apply_threshold("function-too-long", cfg, 10) is False


def test_unknown_rule_returns_false():
    assert ex.apply_threshold("no-such-rule", _CFG, 999) is False
