"""M6 reorder: hashing-first.

Three-way folder rotation:
    old 017-bigo-notation-intro      → new 022-bigo-notation-intro
    old 021-what-is-hashing          → new 017-what-is-hashing
    old 022-dict-vs-list-decision    → new 021-dict-vs-list-decision

Applied to both curriculum/ and solutions/. info.toml is regenerated
from bytelings.scaffolding.SKELETON (which carries the post-M6
ordering). Per-day old_slug fields are set so a learner mid-curriculum
on a v1 progress.json keeps resolving (locator.find_day matches both).

Idempotent: detects whether the rotation already happened and exits.
"""
from __future__ import annotations

import shutil
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from bytelings import info_toml  # noqa: E402
from bytelings.scaffolding import SKELETON  # noqa: E402


# old_path → new_path within each top-level tree.
ROTATION = {
    "017-bigo-notation-intro":   "022-bigo-notation-intro",
    "021-what-is-hashing":       "017-what-is-hashing",
    "022-dict-vs-list-decision": "021-dict-vs-list-decision",
}

# new_slug → v1 slug (with day- prefix), to preserve back-compat in
# info.toml's old_slug field.
NEW_TO_V1_OLD_SLUG = {
    "017-what-is-hashing":       "day-021-what-is-hashing",
    "021-dict-vs-list-decision": "day-022-dict-vs-list-decision",
    "022-bigo-notation-intro":   "day-017-bigo-notation-intro",
}


def _rotate_tree(base: Path) -> bool:
    """Rotate the three folder pairs in `base`. Return True if changed."""
    if not base.is_dir():
        return False
    # Idempotency: if 017-what-is-hashing already exists, we've rotated.
    if (base / "017-what-is-hashing").is_dir():
        return False
    # Stage in TEMP first to avoid name collisions during the rotation.
    temp = base / "_m6_temp_017"
    if temp.exists():
        raise RuntimeError(f"stale rotation temp dir: {temp}")
    (base / "017-bigo-notation-intro").rename(temp)
    (base / "021-what-is-hashing").rename(base / "017-what-is-hashing")
    (base / "022-dict-vs-list-decision").rename(base / "021-dict-vs-list-decision")
    temp.rename(base / "022-bigo-notation-intro")
    return True


def _write_info_toml(curriculum: Path) -> None:
    """Regenerate info.toml from SKELETON, preserving old_slug for moved days."""
    entries: list[info_toml.DayEntry] = []
    for phase, module, day_slugs in SKELETON:
        for slug in day_slugs:
            day_number = int(slug.split("-")[0])
            old_slug = NEW_TO_V1_OLD_SLUG.get(slug, f"day-{slug}")
            entries.append(info_toml.DayEntry(
                slug=slug,
                path=f"curriculum/{slug}",
                day_number=day_number,
                phase=phase,
                module=module,
                old_slug=old_slug,
                patterns=[],
            ))
    # Preserve any patterns already tagged in the existing info.toml.
    existing = {e.slug: e for e in info_toml.load(curriculum / "info.toml")}
    enriched = [
        info_toml.DayEntry(
            slug=e.slug, path=e.path, day_number=e.day_number,
            phase=e.phase, module=e.module, old_slug=e.old_slug,
            patterns=existing[e.slug].patterns if e.slug in existing else e.patterns,
        )
        for e in entries
    ]
    info_toml.dump(enriched, curriculum / "info.toml")


def run(root: Path) -> None:
    curriculum = root / "curriculum"
    solutions = root / "solutions"
    rotated_c = _rotate_tree(curriculum)
    rotated_s = _rotate_tree(solutions)
    if not (rotated_c or rotated_s):
        print("Already rotated — nothing to do.")
        return
    _write_info_toml(curriculum)
    print(f"M6 rotation complete. info.toml regenerated.")


def main() -> None:
    root = Path(sys.argv[1]) if len(sys.argv) > 1 else Path.cwd()
    run(root)


if __name__ == "__main__":
    main()
