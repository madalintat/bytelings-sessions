"""Rung 5: Apply.

Sort a small list of student records by GPA (descending) and break
ties by enrolled-date (oldest first). Print the result.

Try it: uv run python 05_apply.py
"""
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path

_spec = spec_from_file_location(
    "_solo", Path(__file__).parent / "04_solo.py"
)
_solo = module_from_spec(_spec)
_spec.loader.exec_module(_solo)


STUDENTS = [
    {"name": "alice", "gpa": 3.7, "enrolled": "2022-09"},
    {"name": "Bob",   "gpa": 3.9, "enrolled": "2021-09"},
    {"name": "carol", "gpa": 3.7, "enrolled": "2020-09"},
    {"name": "Dave",  "gpa": 3.9, "enrolled": "2022-09"},
]


def main() -> None:
    ordered = sorted(STUDENTS, key=lambda s: (-s["gpa"], s["enrolled"]))
    print("By GPA desc, enrolled asc:")
    for s in ordered:
        print(f"  {s['gpa']:.1f}  {s['enrolled']}  {s['name']}")

    print("\nNice sort of names:")
    print(_solo.nice_sort([s["name"] for s in STUDENTS]))


if __name__ == "__main__":
    main()
