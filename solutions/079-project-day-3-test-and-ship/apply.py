"""Rung 5: Apply — the shippable CLI.

Generates synthetic logs in a temp dir, runs the SERIAL and PARALLEL
analyzers, prints both timings + the speedup, then prints the summary.

Try it: uv run python apply.py
"""
import logging
import tempfile
import time
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)-7s %(name)s: %(message)s",
    datefmt="%H:%M:%S",
)

_solo_spec = spec_from_file_location("_solo", Path(__file__).parent / "solo.py")
_solo = module_from_spec(_solo_spec)
_solo_spec.loader.exec_module(_solo)


def time_it(label: str, fn, *args, **kw):
    start = time.perf_counter()
    out = fn(*args, **kw)
    elapsed = (time.perf_counter() - start) * 1000
    print(f"{label:>10}: {elapsed:7.1f} ms")
    return out, elapsed


def main() -> None:
    with tempfile.TemporaryDirectory() as td:
        td_path = Path(td)
        paths = _solo.make_files(td_path, n_files=4, n_lines=2000, seed=0)
        serial, t_serial = time_it("serial", _solo.analyze_paths, paths)
        parallel, t_par = time_it("parallel", _solo.analyze_paths_parallel, paths, max_workers=4)
        if t_par > 0:
            print(f"  speedup: {t_serial / t_par:.2f}x")
    print()
    print(f"parsed:  {parallel.parsed}")
    print(f"skipped: {parallel.skipped}")
    print("levels:")
    for level, count in sorted(parallel.levels.items()):
        print(f"  {level:<6}: {count}")
    print("top paths:")
    for path, count in parallel.top_paths.most_common(5):
        print(f"  {count:>4}  {path}")


if __name__ == "__main__":
    main()
