"""Tests for rung 2 — uses caplog to capture logger output."""
import importlib.util
import inspect
import logging
from pathlib import Path

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_2"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "fluency.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


def test_logs_info_on_start_and_done(caplog):
    with caplog.at_level(logging.INFO, logger=ex.log.name):
        ex.process("u1", {"x": 1})
    levels = [r.levelno for r in caplog.records]
    assert levels.count(logging.INFO) >= 2
    assert all(r.levelno >= logging.INFO for r in caplog.records)


def test_warning_for_empty_payload(caplog):
    with caplog.at_level(logging.WARNING, logger=ex.log.name):
        ex.process("u1", {})
    assert any(r.levelno == logging.WARNING for r in caplog.records)


def test_error_for_fatal(caplog):
    with caplog.at_level(logging.ERROR, logger=ex.log.name):
        ex.process("u1", {"fatal": True})
    assert any(r.levelno == logging.ERROR for r in caplog.records)


def test_no_print_calls():
    src = inspect.getsource(ex.process)
    assert "print(" not in src, "replace prints with log.* calls"


def test_uses_percent_format():
    """log calls should use %s, not f-strings, for the message template."""
    src = inspect.getsource(ex.process)
    # Look for any log call with an f-string opening.
    assert 'log.info(f"' not in src, "use %s formatting in log calls"
    assert 'log.warning(f"' not in src, "use %s formatting in log calls"
    assert 'log.error(f"' not in src, "use %s formatting in log calls"
