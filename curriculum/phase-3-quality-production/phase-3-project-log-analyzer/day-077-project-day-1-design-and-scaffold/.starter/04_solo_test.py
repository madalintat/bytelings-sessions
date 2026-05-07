"""HIDDEN tests for rung 4 — do not peek before solving 04_solo.py."""
import importlib.util
from pathlib import Path

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_4"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "04_solo.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


def test_line_count():
    text = ex.make_log_text(10, seed=1)
    lines = text.splitlines()
    assert len(lines) == 10


def test_trailing_newline():
    text = ex.make_log_text(3, seed=0)
    assert text.endswith("\n")


def test_zero_lines_returns_empty_string():
    assert ex.make_log_text(0) == ""


def test_deterministic_with_seed():
    a = ex.make_log_text(20, seed=42)
    b = ex.make_log_text(20, seed=42)
    assert a == b


def test_format_per_line():
    text = ex.make_log_text(5, seed=0)
    for line in text.splitlines():
        parts = line.split()
        assert len(parts) == 4, f"bad shape: {line!r}"
        # parts[0]: iso ts; parts[1]: LEVEL; parts[2]: path=...; parts[3]: status=...
        assert parts[1] in ("INFO", "ERROR")
        assert parts[2].startswith("path=/api/")
        assert parts[3].startswith("status=")


def test_error_rate_high_yields_errors():
    text = ex.make_log_text(100, error_rate=1.0, seed=0)
    levels = [ln.split()[1] for ln in text.splitlines()]
    assert all(lvl == "ERROR" for lvl in levels)


def test_error_rate_zero_yields_no_errors():
    text = ex.make_log_text(100, error_rate=0.0, seed=0)
    levels = [ln.split()[1] for ln in text.splitlines()]
    assert all(lvl == "INFO" for lvl in levels)


def test_status_matches_level():
    text = ex.make_log_text(50, seed=1)
    for line in text.splitlines():
        parts = line.split()
        level = parts[1]
        status = parts[3].split("=")[1]
        if level == "ERROR":
            assert status == "500"
        else:
            assert status == "200"
