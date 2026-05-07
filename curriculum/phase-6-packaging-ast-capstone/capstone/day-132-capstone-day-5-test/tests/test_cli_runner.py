"""CLI tests using click.testing.CliRunner.

We have to load `cli.py` carefully because it does relative imports.
"""
import importlib.util
import sys
from datetime import date
from pathlib import Path

from click.testing import CliRunner

_HERE = Path(__file__).parent.parent
_PKG = _HERE / "src" / "habit"


def _load_cli():
    """Load core, storage, then cli, fixing up relative imports each time."""
    core_src = (_PKG / "core.py").read_text(encoding="utf-8")
    storage_src = (_PKG / "storage.py").read_text(encoding="utf-8").replace(
        "from .core import", "from _d132cli_core import"
    )
    cli_src = (_PKG / "cli.py").read_text(encoding="utf-8")
    cli_src = cli_src.replace("from . import storage",
                              "import _d132cli_storage as storage")
    cli_src = cli_src.replace("from .core import",
                              "from _d132cli_core import")

    core_mod = type(sys)("_d132cli_core")
    sys.modules["_d132cli_core"] = core_mod
    exec(compile(core_src, str(_PKG / "core.py"), "exec"), core_mod.__dict__)

    storage_mod = type(sys)("_d132cli_storage")
    sys.modules["_d132cli_storage"] = storage_mod
    exec(compile(storage_src, str(_PKG / "storage.py"), "exec"),
         storage_mod.__dict__)

    cli_mod = type(sys)("_d132cli_cli")
    sys.modules["_d132cli_cli"] = cli_mod
    exec(compile(cli_src, str(_PKG / "cli.py"), "exec"), cli_mod.__dict__)
    return cli_mod


cli = _load_cli()


def test_help_runs():
    result = CliRunner().invoke(cli.main, ["--help"])
    assert result.exit_code == 0
    assert "habit" in result.output.lower() or "tiny" in result.output.lower()


def test_done_then_list(tmp_path, monkeypatch):
    monkeypatch.setenv("HABIT_DATA", str(tmp_path / "data.json"))
    runner = CliRunner()
    r1 = runner.invoke(cli.main, ["done", "meditate"])
    assert r1.exit_code == 0
    r2 = runner.invoke(cli.main, ["list"])
    assert r2.exit_code == 0
    assert "meditate" in r2.output


def test_reset_unknown_fails(tmp_path, monkeypatch):
    monkeypatch.setenv("HABIT_DATA", str(tmp_path / "data.json"))
    result = CliRunner().invoke(cli.main, ["reset", "nope", "--yes"])
    assert result.exit_code == 1
    assert "nope" in (result.output + (result.stderr if hasattr(result, "stderr") else ""))


def test_done_idempotent_same_day(tmp_path, monkeypatch):
    monkeypatch.setenv("HABIT_DATA", str(tmp_path / "data.json"))
    runner = CliRunner()
    runner.invoke(cli.main, ["done", "meditate"])
    runner.invoke(cli.main, ["done", "meditate"])
    # The data file should record meditate exactly once.
    import json
    data = json.loads((tmp_path / "data.json").read_text())
    assert len(data["habits"]["meditate"]["log"]) == 1
