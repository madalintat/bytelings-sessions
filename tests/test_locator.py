"""Tests for locator.py — curriculum scanning and rung discovery."""
from pathlib import Path

from bytelings import locator
from bytelings.progress import Progress


def test_all_days_returns_in_order(fake_curriculum: Path):
    days = locator.all_days(fake_curriculum)
    assert [d.slug for d in days] == [
        "day-001-uv-setup",
        "day-002-numbers",
        "day-003-booleans",
    ]


def test_day_number_property(fake_curriculum: Path):
    days = locator.all_days(fake_curriculum)
    assert days[0].number == 1
    assert days[2].number == 3


def test_find_day_by_slug(fake_curriculum: Path):
    d = locator.find_day("day-002-numbers", fake_curriculum)
    assert d is not None
    assert d.number == 2
    assert d.path.name == "day-002-numbers"


def test_find_day_returns_none_for_missing(fake_curriculum: Path):
    assert locator.find_day("day-999-nope", fake_curriculum) is None


def test_rungs_of_day(fake_curriculum: Path):
    d = locator.find_day("day-001-uv-setup", fake_curriculum)
    assert d is not None
    rungs = locator.rungs_of(d)
    assert len(rungs) == 5
    assert rungs[0].number == 1
    assert rungs[0].file.name == "concept.md"
    assert rungs[0].test_file is None
    assert rungs[1].number == 2
    assert rungs[1].file.name == "02_fluency.py"
    assert rungs[1].test_file is not None
    assert rungs[1].test_file.name == "02_fluency_test.py"
    assert rungs[4].file.name == "05_apply.py"
    assert rungs[4].test_file is None


def test_first_unfinished_day_skips_completed(fake_curriculum: Path):
    p = Progress(completed_days=["day-001-uv-setup"])
    d = locator.first_unfinished_day(p, fake_curriculum)
    assert d is not None
    assert d.slug == "day-002-numbers"


def test_first_unfinished_day_returns_none_when_all_done(fake_curriculum: Path):
    p = Progress(completed_days=[
        "day-001-uv-setup", "day-002-numbers", "day-003-booleans"
    ])
    assert locator.first_unfinished_day(p, fake_curriculum) is None
