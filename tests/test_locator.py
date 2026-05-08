"""Tests for locator.py — curriculum scanning and rung discovery."""
from pathlib import Path

from bytelings import locator
from bytelings.progress import Progress


def test_all_days_returns_in_order(fake_curriculum: Path):
    days = locator.all_days(fake_curriculum)
    assert [d.slug for d in days] == [
        "001-uv-setup",
        "002-numbers",
        "003-booleans",
    ]


def test_day_number_property(fake_curriculum: Path):
    days = locator.all_days(fake_curriculum)
    assert days[0].number == 1
    assert days[2].number == 3


def test_find_day_by_slug(fake_curriculum: Path):
    d = locator.find_day("002-numbers", fake_curriculum)
    assert d is not None
    assert d.number == 2
    assert d.path.name == "002-numbers"


def test_find_day_returns_none_for_missing(fake_curriculum: Path):
    assert locator.find_day("999-nope", fake_curriculum) is None


def test_rungs_of_day(fake_curriculum: Path):
    d = locator.find_day("001-uv-setup", fake_curriculum)
    assert d is not None
    rungs = locator.rungs_of(d)
    assert len(rungs) == 5
    assert rungs[0].number == 1
    assert rungs[0].file.name == "README.md"
    assert rungs[0].test_file is None
    assert rungs[1].number == 2
    assert rungs[1].file.name == "fluency.py"
    assert rungs[1].test_file is not None
    assert rungs[1].test_file.name == "fluency_test.py"
    assert rungs[4].file.name == "apply.py"
    # Apply rung now declares apply_test.py as its (optional) test
    # file. The Rung.test_file path is always set; the watcher checks
    # .exists() before invoking pytest, so days without an
    # apply_test.py still behave as "no automated tests" at runtime.
    assert rungs[4].test_file is not None
    assert rungs[4].test_file.name == "apply_test.py"


def test_first_unfinished_day_skips_completed(fake_curriculum: Path):
    p = Progress(completed_days=["001-uv-setup"])
    d = locator.first_unfinished_day(p, fake_curriculum)
    assert d is not None
    assert d.slug == "002-numbers"


def test_first_unfinished_day_returns_none_when_all_done(fake_curriculum: Path):
    p = Progress(completed_days=[
        "001-uv-setup", "002-numbers", "003-booleans"
    ])
    assert locator.first_unfinished_day(p, fake_curriculum) is None


# v1 backwards-compat tests
def test_find_day_by_old_slug(fake_curriculum: Path):
    """find_day must accept the old v1 slug (day-NNN-name) too."""
    d = locator.find_day("day-002-numbers", fake_curriculum)
    assert d is not None
    assert d.slug == "002-numbers"
    assert d.old_slug == "day-002-numbers"


def test_first_unfinished_day_honors_v1_slugs_in_progress(fake_curriculum: Path):
    """If progress.completed_days contains v1 slugs, those days are skipped."""
    p = Progress(completed_days=["day-001-uv-setup"])
    d = locator.first_unfinished_day(p, fake_curriculum)
    assert d is not None
    assert d.slug == "002-numbers"


def test_current_or_next_day_honors_v1_current_day(fake_curriculum: Path):
    """current_or_next_day resolves v1 slug in p.current_day."""
    p = Progress(current_day="day-002-numbers")
    d = locator.current_or_next_day(p, fake_curriculum)
    assert d is not None
    assert d.slug == "002-numbers"


def test_current_or_next_day_honors_v1_completed_days(fake_curriculum: Path):
    """current_or_next_day skips days listed with v1 slugs in completed_days."""
    p = Progress(completed_days=["day-001-uv-setup", "day-002-numbers"])
    d = locator.current_or_next_day(p, fake_curriculum)
    assert d is not None
    assert d.slug == "003-booleans"
