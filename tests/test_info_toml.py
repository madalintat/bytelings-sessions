"""Tests for bytelings.info_toml — load/dump round-trip."""
from pathlib import Path

from bytelings import info_toml


def test_load_one_entry(tmp_path: Path):
    f = tmp_path / "info.toml"
    f.write_text(
        '[[day]]\n'
        'slug = "001-uv-setup-and-pytest"\n'
        'path = "curriculum/001-uv-setup-and-pytest"\n'
        'day_number = 1\n'
        'phase = "phase-1-python-core"\n'
        'module = "module-01-setup-and-values"\n'
        'old_slug = "day-001-uv-setup-and-pytest"\n'
        'patterns = []\n'
    )
    entries = info_toml.load(f)
    assert len(entries) == 1
    assert entries[0].slug == "001-uv-setup-and-pytest"
    assert entries[0].day_number == 1
    assert entries[0].old_slug == "day-001-uv-setup-and-pytest"
    assert entries[0].patterns == []


def test_dump_round_trips(tmp_path: Path):
    entries = [
        info_toml.DayEntry(
            slug="001-foo",
            path="curriculum/001-foo",
            day_number=1,
            phase="phase-1-python-core",
            module="module-01-setup-and-values",
            old_slug="day-001-foo",
            patterns=[],
        ),
        info_toml.DayEntry(
            slug="002-bar",
            path="curriculum/002-bar",
            day_number=2,
            phase="phase-1-python-core",
            module="module-01-setup-and-values",
            old_slug="day-002-bar",
            patterns=["P-01", "P-07"],
        ),
    ]
    f = tmp_path / "info.toml"
    info_toml.dump(entries, f)
    loaded = info_toml.load(f)
    assert loaded == entries


def test_load_missing_file_returns_empty(tmp_path: Path):
    assert info_toml.load(tmp_path / "no.toml") == []
