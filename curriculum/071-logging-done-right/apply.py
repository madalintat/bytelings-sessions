"""Rung 5: Apply.

Set up a real logger and run audit() a few times. Output goes to stderr
with timestamps and levels — exactly what you'd see in production.

Try it: uv run python apply.py

Patterns: P-01 (sentinel-loop), P-03 (walrus-in-condition).
"""
import logging
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)-8s %(name)s: %(message)s",
    datefmt="%H:%M:%S",
)

_spec = spec_from_file_location("_solo", Path(__file__).parent / "solo.py")
_solo = module_from_spec(_spec)
_spec.loader.exec_module(_solo)


def main() -> None:
    _solo.audit("startup")
    _solo.audit("login", user="ada", method="password")
    _solo.audit("checkout", user="ada", amount=4200, currency="USD")
    _solo.audit("logout", user="ada")


if __name__ == "__main__":
    main()
