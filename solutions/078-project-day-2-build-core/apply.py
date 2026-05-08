"""Rung 5: Apply — a CLI front for today's analyzer.

Generate synthetic log files, run analyze_paths over them, print a
human-readable summary. The logging is configured here in the CLI;
the library code only does `log = getLogger(__name__)`.

Try it: uv run python 05_apply.py
"""
import logging
import tempfile
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path

_solo_spec = spec_from_file_location(
    "_solo", Path(__file__).parent / "04_solo.py"
)
_solo = module_from_spec(_solo_spec)
_solo_spec.loader.exec_module(_solo)


def make_synthetic_files(dir_path: Path, n_files: int = 3, n_lines: int = 200) -> list[Path]:
    """Drop a few synthetic log files in `dir_path`."""
    import random
    paths: list[Path] = []
    rng = random.Random(0)
    base_ts = "2026-05-08T10:%02d:%02d"
    for f in range(n_files):
        p = dir_path / f"service-{f}.log"
        lines = []
        for i in range(n_lines):
            ts = base_ts % (i // 60 % 60, i % 60)
            level = "ERROR" if rng.random() < 0.1 else "INFO"
            status = 500 if level == "ERROR" else 200
            path = f"/api/{rng.randint(0, 5)}"
            lines.append(f"{ts} {level} path={path} status={status}")
        p.write_text("\n".join(lines) + "\n")
        paths.append(p)
    return paths


def main() -> None:
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s %(levelname)-7s %(name)s: %(message)s",
        datefmt="%H:%M:%S",
    )
    with tempfile.TemporaryDirectory() as td:
        paths = make_synthetic_files(Path(td), n_files=3, n_lines=200)
        agg = _solo.analyze_paths(paths)
    print(f"parsed:  {agg.parsed}")
    print(f"skipped: {agg.skipped}")
    print("levels:")
    for level, count in sorted(agg.levels.items()):
        print(f"  {level:<6}: {count}")
    print("top paths:")
    for path, count in agg.top_paths.most_common(5):
        print(f"  {count:>4}  {path}")


if __name__ == "__main__":
    main()
