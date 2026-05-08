"""Rung 5: Apply — solved version.

The apply has no TODO; once solo.py's `count_files` is implemented,
this file just runs and prints the count (8 for SAMPLE_PROJECT).
"""
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path

_spec = spec_from_file_location(
    "_solo", Path(__file__).parent / "solo.py"
)
_solo = module_from_spec(_spec)
_spec.loader.exec_module(_solo)


SAMPLE_PROJECT = {
    "README.md": "file",
    "pyproject.toml": "file",
    "src": {
        "app": {
            "main.py": "file",
            "models.py": "file",
            "views": {
                "home.py": "file",
                "auth.py": "file",
            },
        },
        "tests": {
            "test_main.py": "file",
            "test_views.py": "file",
        },
    },
    "docs": {},
}


def main() -> None:
    n = _solo.count_files(SAMPLE_PROJECT)
    print(f"{n} files in the sample project tree.")


if __name__ == "__main__":
    main()
