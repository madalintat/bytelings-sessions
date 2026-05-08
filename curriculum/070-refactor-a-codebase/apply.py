"""Rung 5: Apply.

Run analyze_orders against a small fixture and pretty-print.

Try it: uv run python 05_apply.py
"""
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path

_spec = spec_from_file_location("_solo", Path(__file__).parent / "04_solo.py")
_solo = module_from_spec(_spec)
_spec.loader.exec_module(_solo)


ORDERS = [
    {"id": 1, "total": 120},
    {"id": 2, "total": 45, "refunded": True},
    {"id": 3, "total": 80},
    {"id": 4, "total": 200},
    {"id": 5, "total": 30, "refunded": True},
]


def main() -> None:
    summary = _solo.analyze_orders(ORDERS)
    for k, v in summary.items():
        print(f"{k:>16}: {v}")


if __name__ == "__main__":
    main()
