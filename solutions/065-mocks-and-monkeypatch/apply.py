"""Rung 5: Apply.

A tiny CLI that prints the greeting from rung 4. In real life, the
`USER_NAME` would come from a deployment config or session.

Try it:
  USER_NAME=alice uv run python 05_apply.py
  uv run python 05_apply.py
"""
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path

_spec = spec_from_file_location("_solo", Path(__file__).parent / "04_solo.py")
_solo = module_from_spec(_spec)
_spec.loader.exec_module(_solo)


def main() -> None:
    print(_solo.current_user_greeting())


if __name__ == "__main__":
    main()
