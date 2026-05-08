"""M11 reorder: trees + recursion interleave.

Spec §7.2 — recursion was Module 20 (Days 99-102), AFTER trees in
Module 18 (Days 87-90). Tree traversals lean on recursion the
student hasn't formally been taught. Flip it: pull recursion-formal
into the trees arc.

New ordering (Days 87-102):
    87  binary-tree-basics                    (Module 18, unchanged)
    88  tree-traversals                       (Module 18, unchanged)
    89  base-and-recursive-cases              ← was 099 (recursion FORMAL)
    90  bst-insert-search                     ← was 089
    91  bst-delete-and-balance                ← was 090 (recursion w/ state)
    92  heap-invariant-and-heapq              ← was 091 (Module 19)
    93  build-your-own-heap-and-top-k         ← was 092
    94  hash-table-chaining                   ← was 093
    95  hash-table-open-addressing            ← was 094
    96  hash-function-design-and-word-counter ← was 095
    97  tracing-recursion                     ← was 100 (Module 20 tail)
    98  recursion-vs-iteration                ← was 101
    99  stack-depth-and-python-limits         ← was 102
   100  project-day-1-design-and-scaffold     ← was 096 (project)
   101  project-day-2-build-core              ← was 097
   102  project-day-3-test-and-ship           ← was 098

Module assignment after rotation:
  Module 18 (Days 87-91): "trees, recursion, BST"
  Module 19 (Days 92-96): heaps + hash (unchanged content, +1 each)
  Module 20 (Days 97-99): recursion tail (3 days, was 4)
  phase-4 project (100-102): unchanged content, +4 each

Idempotent. Mirrors the rotation across curriculum/ and solutions/.
"""
from __future__ import annotations

import shutil
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from bytelings import info_toml  # noqa: E402
from bytelings.scaffolding import SKELETON  # noqa: E402


# old_slug → new_slug
ROTATION = {
    "099-base-and-recursive-cases":             "089-base-and-recursive-cases",
    "089-bst-insert-search":                    "090-bst-insert-search",
    "090-bst-delete-and-balance":               "091-bst-delete-and-balance",
    "091-heap-invariant-and-heapq":             "092-heap-invariant-and-heapq",
    "092-build-your-own-heap-and-top-k":        "093-build-your-own-heap-and-top-k",
    "093-hash-table-chaining":                  "094-hash-table-chaining",
    "094-hash-table-open-addressing":           "095-hash-table-open-addressing",
    "095-hash-function-design-and-word-counter":"096-hash-function-design-and-word-counter",
    "100-tracing-recursion":                    "097-tracing-recursion",
    "101-recursion-vs-iteration":               "098-recursion-vs-iteration",
    "102-stack-depth-and-python-limits":        "099-stack-depth-and-python-limits",
    "096-project-day-1-design-and-scaffold":    "100-project-day-1-design-and-scaffold",
    "097-project-day-2-build-core":             "101-project-day-2-build-core",
    "098-project-day-3-test-and-ship":          "102-project-day-3-test-and-ship",
}

# new_slug → v1 slug for old_slug back-compat in info.toml.
def _old_slug_for(new_slug: str) -> str:
    """The v1 ('day-NNN-name') slug a learner's progress.json may carry."""
    # Find the inverse of ROTATION: which OLD slug maps to this NEW slug?
    for old, new in ROTATION.items():
        if new == new_slug:
            # The old slug under M6 was just "day-" + the pre-rotation name.
            # Pre-rotation, the slug might already have been moved by M6 etc.;
            # for M11 we treat its v1 slug as day-<old name from this rotation>.
            return f"day-{old}"
    return f"day-{new_slug}"


def _rotate_tree(base: Path) -> bool:
    """Apply the 14-way rotation in `base`. Return True if changed."""
    if not base.is_dir():
        return False
    # Idempotency: if the destination of the FIRST mapping already exists,
    # we've rotated.
    sentinel_new = next(iter(ROTATION.values()))
    sentinel_old = next(iter(ROTATION.keys()))
    if (base / sentinel_new).is_dir() and not (base / sentinel_old).is_dir():
        return False
    if not (base / sentinel_old).is_dir():
        # Nothing to rotate — old layout missing.
        return False

    # Stage every old slug to a TEMP location, then rename to new slugs.
    # This avoids collisions when old → new positions overlap.
    temp_root = base / "_m11_temp"
    if temp_root.exists():
        raise RuntimeError(f"stale rotation temp dir: {temp_root}")
    temp_root.mkdir()
    try:
        for old in ROTATION:
            src = base / old
            if not src.is_dir():
                raise RuntimeError(f"expected {src} to exist for rotation")
            (src).rename(temp_root / old)
        for old, new in ROTATION.items():
            (temp_root / old).rename(base / new)
    finally:
        if temp_root.exists():
            shutil.rmtree(temp_root)
    return True


def run(root: Path) -> None:
    curriculum = root / "curriculum"
    solutions = root / "solutions"
    rc = _rotate_tree(curriculum)
    rs = _rotate_tree(solutions)
    if not (rc or rs):
        print("Already rotated — nothing to do.")
        return
    info_toml.regenerate_from_skeleton(curriculum, SKELETON, _old_slug_for)
    print("M11 rotation complete. info.toml regenerated.")


def main() -> None:
    root = Path(sys.argv[1]) if len(sys.argv) > 1 else Path.cwd()
    run(root)


if __name__ == "__main__":
    main()
