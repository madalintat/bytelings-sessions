"""Rung 5: Apply — solved version.

Load the inline CSV, run select_activities, verify the count, print results.
The greedy picks 4 talks: Keynote(0-60), Type Systems(60-120),
Lightning Talks(150-180), Panel Discussion(180-240).
"""
import csv
import io
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path

_spec = spec_from_file_location(
    "_guided", Path(__file__).parent / "guided.py"
)
_guided = module_from_spec(_spec)
_spec.loader.exec_module(_guided)

_CSV = """\
start,end,title
0,60,Keynote
30,90,Python Internals
60,120,Type Systems Deep Dive
90,150,Async Patterns
120,180,Testing at Scale
150,180,Lightning Talks
180,240,Panel Discussion
"""


def _load() -> list[tuple[int, int]]:
    reader = csv.DictReader(io.StringIO(_CSV))
    return [(int(r["start"]), int(r["end"])) for r in reader]


def main() -> None:
    talks = _load()
    chosen = _guided.select_activities(talks)

    print("All talks:")
    for s, e in talks:
        print(f"  [{s:3d}-{e:3d}]")

    print(f"\nMaximum non-overlapping subset ({len(chosen)} talks):")
    for s, e in chosen:
        print(f"  [{s:3d}-{e:3d}]")

    # Sorted by finish: (0,60),(30,90),(60,120),(90,150),(150,180),(120,180),(180,240)
    # Greedy: take (0,60), skip (30,90), take (60,120), skip (90,150),
    #         take (150,180), take (180,240) → 4 talks.
    assert len(chosen) == 4, f"Expected 4 talks, got {len(chosen)}: {chosen}"
    assert all(
        chosen[i][0] >= chosen[i - 1][1] for i in range(1, len(chosen))
    ), "Result contains overlapping activities!"
    print("\nAll assertions passed.")


if __name__ == "__main__":
    main()
