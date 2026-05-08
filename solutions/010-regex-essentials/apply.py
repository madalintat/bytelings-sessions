"""Rung 5: Apply.

Tiny CLI: read text from stdin, print every email found, one per line.

Reuses find_emails from rung 4.

Try it: echo "Contact alice@example.com or bob@acme.io" | uv run python apply.py
"""
import sys
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path

_spec = spec_from_file_location(
    "_solo", Path(__file__).parent / "solo.py"
)
_solo = module_from_spec(_spec)
_spec.loader.exec_module(_solo)


def main() -> None:
    text = sys.stdin.read()
    for email in _solo.find_emails(text):
        print(email)


if __name__ == "__main__":
    main()
