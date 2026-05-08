"""Rung 5: Apply.

Use the refactored format_user_label on a small directory of "users".

Try it: uv run python apply.py
"""
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path

_spec = spec_from_file_location("_solo", Path(__file__).parent / "solo.py")
_solo = module_from_spec(_spec)
_spec.loader.exec_module(_solo)


USERS = [
    {"name": "Ada Lovelace", "title": "Dr."},
    {"name": "Linus Torvalds"},
    {"email": "anon@example.com"},
    {"name": "", "email": "fallback@example.com"},
    {},
    None,
]


def main() -> None:
    for u in USERS:
        print(_solo.format_user_label(u))


if __name__ == "__main__":
    main()
