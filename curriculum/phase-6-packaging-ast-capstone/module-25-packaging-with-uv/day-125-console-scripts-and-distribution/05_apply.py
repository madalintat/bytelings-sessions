"""Rung 5: Apply.

Tie the day together: a real (toy) installer.

`fake_install(scripts: dict[str, str], bin_dir: Path)` writes a shim
file per entry-point spec into `bin_dir`. After this runs, you could
literally chmod +x and execute them — they're real Python.

We won't actually chmod (it'd cause cross-platform pain), but you can
inspect the files in /tmp after running.

    uv run python 05_apply.py
"""
from __future__ import annotations
import tempfile
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path

_HERE = Path(__file__).parent
_g = spec_from_file_location("_guided", _HERE / "03_guided.py")
_guided = module_from_spec(_g)
_g.loader.exec_module(_guided)


def fake_install(scripts: dict[str, str], bin_dir: Path) -> list[Path]:
    bin_dir.mkdir(parents=True, exist_ok=True)
    written: list[Path] = []
    for name, spec in scripts.items():
        shim = _guided.make_shim(spec)
        path = bin_dir / name
        path.write_text(shim, encoding="utf-8")
        written.append(path)
    return written


def main() -> None:
    bin_dir = Path(tempfile.mkdtemp(prefix="fake-bin-"))
    scripts = {
        "pyproject-summary": "habit_cli.cli:main",
        "habit": "habit_cli.cli:run_habit_cmd",
    }
    written = fake_install(scripts, bin_dir)
    print(f"wrote {len(written)} shim(s) to {bin_dir}")
    for p in written:
        print(f"\n--- {p.name} ---")
        print(p.read_text(encoding="utf-8").rstrip())


if __name__ == "__main__":
    main()
