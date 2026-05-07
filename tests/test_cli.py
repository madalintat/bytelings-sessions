"""Tests for the `swe` CLI — uses Click's CliRunner so no real fs ops."""
import json
from pathlib import Path

from click.testing import CliRunner

from bytelings.cli import cli


def test_welcome_runs_clean():
    result = CliRunner().invoke(cli, ["welcome"])
    assert result.exit_code == 0
    assert (
        "bytelings" in result.output.lower()
        or "rustlings" in result.output.lower()
        or "rung" in result.output.lower()
    )


def test_init_copies_curriculum(tmp_path: Path, monkeypatch):
    """`init` should produce a curriculum/ directory in cwd."""
    monkeypatch.chdir(tmp_path)
    result = CliRunner().invoke(cli, ["init"])
    assert result.exit_code == 0, result.output
    assert (tmp_path / "curriculum").is_dir()
    # Should contain at least phase-1
    assert (tmp_path / "curriculum" / "phase-1-python-core").is_dir()


def test_init_refuses_to_overwrite(tmp_path: Path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    (tmp_path / "curriculum").mkdir()
    result = CliRunner().invoke(cli, ["init"])
    assert result.exit_code != 0
    assert "already exists" in result.output.lower()


def test_init_force_overwrites(tmp_path: Path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    (tmp_path / "curriculum").mkdir()
    (tmp_path / "curriculum" / "stale.txt").write_text("old")
    result = CliRunner().invoke(cli, ["init", "--force"])
    assert result.exit_code == 0, result.output
    assert not (tmp_path / "curriculum" / "stale.txt").exists()
    assert (tmp_path / "curriculum" / "phase-1-python-core").is_dir()


def test_list_shows_days(cli_runner: CliRunner, fake_curriculum: Path):
    result = cli_runner.invoke(cli, ["list"])
    assert result.exit_code == 0
    assert "day-001" in result.output


def test_hint_shows_concept(cli_runner: CliRunner, fake_curriculum: Path):
    result = cli_runner.invoke(cli, ["hint"])
    assert result.exit_code == 0
    assert "Day 1" in result.output or "concept" in result.output.lower()


def test_today_with_no_curriculum_says_so(cli_runner: CliRunner):
    result = cli_runner.invoke(cli, ["today"])
    assert result.exit_code == 0
    assert (
        "complete" in result.output.lower()
        or "no days" in result.output.lower()
        or "scaffold" in result.output.lower()
    )


def test_today_shows_day_when_curriculum_present(
    cli_runner: CliRunner, fake_curriculum: Path
):
    result = cli_runner.invoke(cli, ["today"])
    assert result.exit_code == 0
    assert "day-001" in result.output


def test_progress_command_runs_clean(
    cli_runner: CliRunner, fake_curriculum: Path
):
    result = cli_runner.invoke(cli, ["progress"])
    assert result.exit_code == 0


def test_done_marks_current_rung(
    cli_runner: CliRunner, fake_curriculum: Path, tmp_path: Path
):
    result = cli_runner.invoke(cli, ["done"])
    assert result.exit_code == 0
    pj = tmp_path / "progress" / "progress.json"
    assert pj.exists()
    data = json.loads(pj.read_text())
    assert data["current_rung"] >= 2 or 1 in data["completed_rungs_today"]


def test_next_advances_rung(
    cli_runner: CliRunner, fake_curriculum: Path
):
    cli_runner.invoke(cli, ["today"])
    result = cli_runner.invoke(cli, ["next"])
    assert result.exit_code == 0


def test_reset_day(
    cli_runner: CliRunner, fake_curriculum: Path, tmp_path: Path
):
    cli_runner.invoke(cli, ["done"])
    result = cli_runner.invoke(cli, ["reset", "day-001-uv-setup"])
    assert result.exit_code == 0
    data = json.loads((tmp_path / "progress" / "progress.json").read_text())
    assert "day-001-uv-setup" not in data["completed_days"]
