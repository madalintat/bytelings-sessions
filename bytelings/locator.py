"""Walk the curriculum tree and identify days, rungs, and current location."""
from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

from .progress import Progress

CURRICULUM_ROOT = Path("curriculum")


@dataclass(frozen=True)
class Day:
    slug: str
    path: Path
    phase: str
    module: str

    @property
    def number(self) -> int:
        return int(self.slug.split("-")[1])


@dataclass(frozen=True)
class Rung:
    number: int
    file: Path
    test_file: Path | None
    name: str


_RUNG_SPECS = [
    (1, "concept.md", None, "Read the concept"),
    (2, "02_fluency.py", "02_fluency_test.py", "Fluency drill"),
    (3, "03_guided.py", "03_guided_test.py", "Guided implement"),
    (4, "04_solo.py", "04_solo_test.py", "Solo implement"),
    (5, "05_apply.py", None, "Apply"),
]


def _phase_dirs(root: Path):
    for d in sorted(root.glob("phase-*")):
        if d.is_dir():
            yield d


def _container_dirs(phase_dir: Path):
    """Yield module/, phase-project/, and capstone/ container dirs in a phase."""
    for sub in sorted(phase_dir.iterdir()):
        if sub.is_dir() and not sub.name.startswith(("__", ".")):
            yield sub


def all_days(root: Path = CURRICULUM_ROOT) -> list[Day]:
    """Return every day folder in chronological (day-number) order."""
    days: list[Day] = []
    for phase_dir in _phase_dirs(root):
        for container in _container_dirs(phase_dir):
            for day_dir in sorted(container.glob("day-*")):
                if not day_dir.is_dir():
                    continue
                days.append(Day(
                    slug=day_dir.name,
                    path=day_dir,
                    phase=phase_dir.name,
                    module=container.name,
                ))
    days.sort(key=lambda d: d.number)
    return days


def find_day(slug: str, root: Path = CURRICULUM_ROOT) -> Day | None:
    for day in all_days(root):
        if day.slug == slug:
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
        if day.slug not in p.completed_days:
            return day
    return None


def current_or_next_day(
    p: Progress, root: Path = CURRICULUM_ROOT
) -> Day | None:
    """Locate the day to work on: current_day if set & exists, else first unfinished.

    Single source of `all_days()` so both lookups share one tree walk.
    """
    days = all_days(root)
    if p.current_day:
        for d in days:
            if d.slug == p.current_day:
                return d
    for d in days:
        if d.slug not in p.completed_days:
            return d
    return None


def rung_for(p: Progress, rungs: list[Rung]) -> Rung:
    """Return the Rung matching p.current_rung; falls back to first unfinished."""
    for r in rungs:
        if r.number == p.current_rung:
            return r
    return rungs[0]
