"""Walk the v2 curriculum (info.toml-driven) and identify days, rungs."""
from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

from .info_toml import DayEntry, load as load_info_toml
from .progress import Progress

CURRICULUM_ROOT = Path("curriculum")


@dataclass(frozen=True)
class Day:
    slug: str
    path: Path
    phase: str
    module: str
    old_slug: str = ""

    @property
    def number(self) -> int:
        return int(self.slug.split("-")[0])


@dataclass(frozen=True)
class Rung:
    number: int
    file: Path
    test_file: Path | None
    name: str


_RUNG_SPECS = [
    (1, "README.md", None, "Read the concept"),
    (2, "fluency.py", "fluency_test.py", "Fluency drill"),
    (3, "guided.py", "guided_test.py", "Guided implement"),
    (4, "solo.py", "solo_test.py", "Solo implement"),
    (5, "apply.py", None, "Apply"),
]


def _entries(root: Path) -> list[DayEntry]:
    return load_info_toml(root / "info.toml")


def all_days(root: Path = CURRICULUM_ROOT) -> list[Day]:
    """Return every day from info.toml in chronological (day-number) order."""
    days = [
        Day(
            slug=e.slug,
            path=root / e.slug,
            phase=e.phase,
            module=e.module,
            old_slug=e.old_slug,
        )
        for e in _entries(root)
    ]
    days.sort(key=lambda d: d.number)
    return days


def find_day(slug: str, root: Path = CURRICULUM_ROOT) -> Day | None:
    """Find a day by new slug OR old slug (v1 backwards-compat)."""
    for day in all_days(root):
        if day.slug == slug or day.old_slug == slug:
            return day
    return None


def rungs_of(day: Day) -> list[Rung]:
    return [
        Rung(
            number=n,
            file=day.path / fname,
            test_file=(day.path / tname) if tname else None,
            name=label,
        )
        for n, fname, tname, label in _RUNG_SPECS
    ]


def first_unfinished_day(
    p: Progress, root: Path = CURRICULUM_ROOT
) -> Day | None:
    for day in all_days(root):
        if day.slug not in p.completed_days and day.old_slug not in p.completed_days:
            return day
    return None


def current_or_next_day(
    p: Progress, root: Path = CURRICULUM_ROOT
) -> Day | None:
    """Locate the day to work on. Honors v1 slugs in progress.json."""
    days = all_days(root)
    if p.current_day:
        for d in days:
            if d.slug == p.current_day or d.old_slug == p.current_day:
                return d
    for d in days:
        if d.slug not in p.completed_days and d.old_slug not in p.completed_days:
            return d
    return None


def rung_for(p: Progress, rungs: list[Rung]) -> Rung:
    """Return the Rung matching p.current_rung; falls back to first unfinished."""
    for r in rungs:
        if r.number == p.current_rung:
            return r
    return rungs[0]
