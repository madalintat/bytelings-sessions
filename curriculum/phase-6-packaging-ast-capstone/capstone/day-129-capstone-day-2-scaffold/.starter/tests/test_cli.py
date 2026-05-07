"""Day 2 — confirm the scaffold runs.

We load src/habit/cli.py via importlib so this test works whether or
not you've run `uv sync` to install the package. Tomorrow's tests will
assume an install and use plain `from habit import ...`.
"""
import importlib.util
import sys
from pathlib import Path

from click.testing import CliRunner

_HERE = Path(__file__).parent.parent
_CLI_PATH = _HERE / "src" / "habit" / "cli.py"
_NAME = "_capstone_day129_cli"
_spec = importlib.util.spec_from_file_location(_NAME, _CLI_PATH)
cli = importlib.util.module_from_spec(_spec)
sys.modules[_NAME] = cli
_spec.loader.exec_module(cli)


def test_help_runs():
    runner = CliRunner()
    result = runner.invoke(cli.main, ["--help"])
    assert result.exit_code == 0
    assert "habit" in result.output.lower() or "tiny daily habits" in result.output.lower()


def test_list_runs():
    runner = CliRunner()
    result = runner.invoke(cli.main, ["list"])
    assert result.exit_code == 0


def test_done_placeholder():
    runner = CliRunner()
    result = runner.invoke(cli.main, ["done", "meditate"])
    assert result.exit_code == 0
    assert "meditate" in result.output


def test_version_option():
    runner = CliRunner()
    result = runner.invoke(cli.main, ["--version"])
    assert result.exit_code == 0
