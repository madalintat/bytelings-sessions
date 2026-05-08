"""Rung 5: Apply.

Apply `clamp` to a real-world chunk: a stats summarizer that has to
keep numbers in a sane range (think: progress bars, percentages, brightness).

Try it: uv run python apply.py
"""
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path

_spec = spec_from_file_location("_solo", Path(__file__).parent / "solo.py")
_solo = module_from_spec(_spec)
_spec.loader.exec_module(_solo)


def normalize_progress(raw_percentages: list[float]) -> list[int]:
    """Clamp each value to [0, 100], round to int."""
    return [int(round(_solo.clamp(p, 0.0, 100.0))) for p in raw_percentages]


def main() -> None:
    raw = [-5.0, 0.0, 17.6, 50.5, 99.9, 105.0, 200.0]
    print(normalize_progress(raw))


if __name__ == "__main__":
    main()
