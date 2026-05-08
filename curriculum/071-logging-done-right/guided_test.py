"""Tests for rung 3."""
import importlib.util
import logging
from pathlib import Path

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_3"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "03_guided.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


def good():
    pass


def bad():
    raise RuntimeError("kaboom")


def test_returns_success_count():
    assert ex.run_jobs([good, good, bad, good]) == 3


def test_does_not_propagate(caplog):
    with caplog.at_level(logging.ERROR, logger=ex.log.name):
        ex.run_jobs([bad, bad, bad])
    # If it propagated, we wouldn't get here.


def test_logs_info_on_success(caplog):
    with caplog.at_level(logging.INFO, logger=ex.log.name):
        ex.run_jobs([good])
    info_records = [r for r in caplog.records if r.levelno == logging.INFO]
    assert info_records, "log at INFO on success"
    assert "good" in info_records[0].getMessage()


def test_logs_error_on_failure(caplog):
    with caplog.at_level(logging.ERROR, logger=ex.log.name):
        ex.run_jobs([bad])
    err_records = [r for r in caplog.records if r.levelno == logging.ERROR]
    assert err_records, "log at ERROR on failure"


def test_traceback_included(caplog):
    """log.exception(...) should attach exc_info to the record."""
    with caplog.at_level(logging.ERROR, logger=ex.log.name):
        ex.run_jobs([bad])
    err = next(r for r in caplog.records if r.levelno == logging.ERROR)
    assert err.exc_info is not None, (
        "use log.exception(...) inside the except block — exc_info should be attached"
    )
