"""Shared pytest fixtures for swe runner tests."""
from pathlib import Path

import pytest
from click.testing import CliRunner


@pytest.fixture
def tmp_progress_path(tmp_path: Path) -> Path:
    """A throwaway path for progress.json in tests."""
    return tmp_path / "progress.json"


@pytest.fixture
def fake_curriculum(tmp_path: Path) -> Path:
    """Build a tiny fake curriculum tree under tmp_path/curriculum."""
    root = tmp_path / "curriculum"
    p1 = root / "phase-1-python-core" / "module-01-setup-and-values"
    p1.mkdir(parents=True)
    for n, slug in [(1, "uv-setup"), (2, "numbers"), (3, "booleans")]:
        d = p1 / f"day-{n:03d}-{slug}"
        d.mkdir()
        (d / "concept.md").write_text(f"# Day {n}\n")
        for r in (2, 3, 4):
            (d / f"0{r}_x.py").write_text("")
            (d / f"0{r}_x_test.py").write_text(
                "def test_ok():\n    assert True\n"
            )
        (d / "05_apply.py").write_text("")
    return root


@pytest.fixture
def cli_runner(tmp_path: Path, monkeypatch) -> CliRunner:
    """A CliRunner with cwd already chdir'd to a throwaway tmp_path.

    Use with `fake_curriculum` to also seed the curriculum tree.
    """
    monkeypatch.chdir(tmp_path)
    return CliRunner()
