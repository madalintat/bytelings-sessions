"""One-shot v1 → v2 curriculum tree migration.

Usage:
    uv run python scripts/migrate_v1_to_v2.py [ROOT]

ROOT defaults to current working directory. Operates on ROOT/curriculum/.

What it does:
1. Walks the v1 tree (phase-N/module-NN/day-NNN-name/).
2. For each day:
   - Creates curriculum/NNN-name/ (drops `day-` prefix and phase/module dirs).
   - Renames 02_fluency.py → fluency.py (and likewise for guided/solo).
   - Renames 02_fluency_test.py → fluency_test.py (etc).
   - Renames concept.md → README.md.
   - Renames 05_apply.py → apply.py.
   - Copies .starter/* into solutions/NNN-name/ with the same renames.
3. Writes curriculum/info.toml with one entry per day.
4. Deletes phase-N-*/ trees (now empty) and any leftover .starter/ dirs.

Idempotent: if the new layout already exists, exits clean without re-doing work.
"""
from __future__ import annotations

import shutil
import sys
from dataclasses import dataclass
from pathlib import Path

# Append source root so we can import bytelings.info_toml when run as a script.
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from bytelings import info_toml  # noqa: E402

RUNG_RENAMES = {
    "concept.md": "README.md",
    "02_fluency.py": "fluency.py",
    "02_fluency_test.py": "fluency_test.py",
    "03_guided.py": "guided.py",
    "03_guided_test.py": "guided_test.py",
    "04_solo.py": "solo.py",
    "04_solo_test.py": "solo_test.py",
    "05_apply.py": "apply.py",
}


@dataclass(frozen=True)
class V1Day:
    """A v1 day folder, located before migration."""
    path: Path             # absolute path to the day folder
    old_slug: str          # "day-001-uv-setup-and-pytest"
    new_slug: str          # "001-uv-setup-and-pytest"
    day_number: int
    phase: str             # "phase-1-python-core"
    module: str            # "module-01-setup-and-values" or "phase-1-project-..."


def _discover_v1_days(curriculum_root: Path) -> list[V1Day]:
    """Walk phase-*/module-*/day-NNN-*/ and return ordered V1Day entries."""
    days: list[V1Day] = []
    for phase_dir in sorted(curriculum_root.glob("phase-*")):
        if not phase_dir.is_dir():
            continue
        for module_dir in sorted(phase_dir.iterdir()):
            if not module_dir.is_dir() or module_dir.name.startswith((".", "__")):
                continue
            for day_dir in sorted(module_dir.glob("day-*")):
                if not day_dir.is_dir():
                    continue
                old_slug = day_dir.name
                # day-001-foo → 001-foo
                new_slug = old_slug[len("day-"):] if old_slug.startswith("day-") else old_slug
                day_number = int(new_slug.split("-")[0])
                days.append(V1Day(
                    path=day_dir,
                    old_slug=old_slug,
                    new_slug=new_slug,
                    day_number=day_number,
                    phase=phase_dir.name,
                    module=module_dir.name,
                ))
    days.sort(key=lambda d: d.day_number)
    return days


def _migrate_day_files(day: V1Day, new_dir: Path) -> None:
    """Copy day files into new_dir with renames."""
    new_dir.mkdir(parents=True, exist_ok=True)
    for old_name, new_name in RUNG_RENAMES.items():
        src = day.path / old_name
        if src.is_file():
            shutil.copy2(src, new_dir / new_name)


def _migrate_starter(day: V1Day, sol_dir: Path) -> None:
    """Copy the day's .starter/* into solutions/<slug>/ with renames."""
    starter = day.path / ".starter"
    if not starter.is_dir():
        return
    sol_dir.mkdir(parents=True, exist_ok=True)
    for old_name, new_name in RUNG_RENAMES.items():
        src = starter / old_name
        if src.is_file():
            shutil.copy2(src, sol_dir / new_name)


def _new_entry(day: V1Day) -> info_toml.DayEntry:
    return info_toml.DayEntry(
        slug=day.new_slug,
        path=f"curriculum/{day.new_slug}",
        day_number=day.day_number,
        phase=day.phase,
        module=day.module,
        old_slug=day.old_slug,
        patterns=[],
    )


def run(root: Path) -> None:
    """Migrate ROOT/curriculum from v1 to v2. Idempotent."""
    curriculum = root / "curriculum"
    solutions = root / "solutions"

    # Idempotency: if info.toml already exists and we have NNN-name dirs,
    # we're already migrated. Nothing to do.
    if (curriculum / "info.toml").is_file() and any(
        (curriculum / d).is_dir()
        for d in ("001-uv-setup-and-pytest",)
    ):
        return

    v1_days = _discover_v1_days(curriculum)
    if not v1_days:
        # Nothing to migrate (e.g., already migrated and old dirs were removed
        # but info.toml was lost). Caller can decide what to do.
        return

    entries: list[info_toml.DayEntry] = []
    for day in v1_days:
        new_dir = curriculum / day.new_slug
        sol_dir = solutions / day.new_slug
        _migrate_day_files(day, new_dir)
        _migrate_starter(day, sol_dir)
        entries.append(_new_entry(day))

    info_toml.dump(entries, curriculum / "info.toml")

    # Now safe to delete old structure: remove every phase-*/ and any
    # leftover .starter/ dirs.
    for phase_dir in curriculum.glob("phase-*"):
        if phase_dir.is_dir():
            shutil.rmtree(phase_dir)
    for starter in curriculum.rglob(".starter"):
        if starter.is_dir():
            shutil.rmtree(starter)


def main() -> None:
    root = Path(sys.argv[1]) if len(sys.argv) > 1 else Path.cwd()
    run(root)
    print(f"Migrated {root}/curriculum → v2.")


if __name__ == "__main__":
    main()
