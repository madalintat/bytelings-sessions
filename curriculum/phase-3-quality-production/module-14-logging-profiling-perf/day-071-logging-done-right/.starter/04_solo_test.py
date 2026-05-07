"""HIDDEN tests for rung 4 — do not peek before solving 04_solo.py."""
import importlib.util
import logging
from pathlib import Path

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_4"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "04_solo.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


def test_logs_info_to_audit_logger(caplog):
    with caplog.at_level(logging.INFO, logger="audit"):
        ex.audit("login", user="ada")
    assert any(r.name == "audit" and r.levelno == logging.INFO for r in caplog.records)


def test_message_template_uses_percent(caplog):
    """The record's `msg` attribute (template) should be the literal
    template, not the pre-formatted result. That's the whole point
    of structured logging."""
    with caplog.at_level(logging.INFO, logger="audit"):
        ex.audit("login", user="ada")
    rec = caplog.records[-1]
    assert rec.msg == "audit %s context=%s", (
        "use the literal template 'audit %s context=%s' — not an f-string"
    )


def test_args_carry_context(caplog):
    with caplog.at_level(logging.INFO, logger="audit"):
        ex.audit("checkout", user="ada", amount=42)
    rec = caplog.records[-1]
    assert rec.args[0] == "checkout"
    assert rec.args[1] == {"user": "ada", "amount": 42}


def test_no_kwargs_works(caplog):
    with caplog.at_level(logging.INFO, logger="audit"):
        ex.audit("ping")
    rec = caplog.records[-1]
    assert rec.args == ("ping", {})
