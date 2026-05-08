"""Rung 5: Apply.

A revenue-dashboard simulation: load 365 days of fake data, then
answer 4 different range-sum queries instantly using RangeSum.

Try it: uv run python apply.py
"""
import random
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path

_spec = spec_from_file_location(
    "_solo", Path(__file__).parent / "solo.py"
)
_solo = module_from_spec(_spec)
_spec.loader.exec_module(_solo)


def main() -> None:
    random.seed(42)
    revenue = [random.randint(80, 500) for _ in range(365)]
    rs = _solo.RangeSum(revenue)

    print(f"Total year:        {rs.query(0, 365)}")
    print(f"Q1 (days 0-90):    {rs.query(0, 90)}")
    print(f"Q2 (days 90-181):  {rs.query(90, 181)}")
    print(f"Q3 (days 181-273): {rs.query(181, 273)}")
    print(f"Q4 (days 273-365): {rs.query(273, 365)}")
    print(f"July only:         {rs.query(181, 212)}")


if __name__ == "__main__":
    main()
