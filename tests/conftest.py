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
    """Build a tiny fake v2 curriculum tree under tmp_path."""
    from bytelings import info_toml

    curriculum = tmp_path / "curriculum"
    curriculum.mkdir()
    entries = []
    for n, slug_part in [(1, "uv-setup"), (2, "numbers"), (3, "booleans")]:
        slug = f"{n:03d}-{slug_part}"
        d = curriculum / slug
        d.mkdir()
        (d / "README.md").write_text(f"# Day {n}\n")
        (d / "apply.py").write_text("")
        for kind in ("fluency", "guided", "solo"):
            (d / f"{kind}.py").write_text("")
            (d / f"{kind}_test.py").write_text(
                "def test_ok():\n    assert True\n"
            )
        entries.append(info_toml.DayEntry(
            slug=slug,
            path=f"curriculum/{slug}",
            day_number=n,
            phase="phase-1-python-core",
            module="module-01-setup-and-values",
            old_slug=f"day-{slug}",
            patterns=[],
        ))
    info_toml.dump(entries, curriculum / "info.toml")
    return curriculum


@pytest.fixture
def cli_runner(tmp_path: Path, monkeypatch) -> CliRunner:
    """A CliRunner with cwd already chdir'd to a throwaway tmp_path.

    Use with `fake_curriculum` to also seed the curriculum tree.
    """
    monkeypatch.chdir(tmp_path)
    return CliRunner()
