"""Tests for rung 3."""
import importlib.util
from pathlib import Path

import pytest

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_3"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "03_guided.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


EXPECTED = (
    "#!/usr/bin/env python\n"
    "import sys\n"
    "from habit_cli.cli import main\n"
    "sys.exit(main())\n"
)


def test_basic_shim():
    assert ex.make_shim("habit_cli.cli:main") == EXPECTED


def test_top_level_module():
    out = ex.make_shim("tool:run")
    assert out.startswith("#!/usr/bin/env python\n")
    assert "from tool import run" in out
    assert "sys.exit(run())" in out
    assert out.endswith("\n")


def test_dotted_module():
    out = ex.make_shim("a.b.c.d:go")
    assert "from a.b.c.d import go" in out


def test_invalid_raises():
    with pytest.raises(ValueError):
        ex.make_shim("no_colon")


def test_empty_side_raises():
    with pytest.raises(ValueError):
        ex.make_shim(":main")
    with pytest.raises(ValueError):
        ex.make_shim("habit_cli:")
