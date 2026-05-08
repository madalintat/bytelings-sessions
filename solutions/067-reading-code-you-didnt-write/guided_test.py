"""Tests for rung 3."""
import importlib.util
import textwrap
from pathlib import Path

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_3"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "guided.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


SAMPLE = textwrap.dedent(
    """
    import os
    import sys
    from pathlib import Path
    from os import path  # noqa
    import os  # duplicate

    CONST = 1

    class Job:
        def run(self):
            pass

    class Result:
        pass

    def main():
        pass

    async def fetch():
        pass
    """
).strip()


def test_imports_order_and_dedup():
    out = ex.outline(SAMPLE)
    assert out["imports"] == ["os", "sys", "pathlib"]


def test_classes():
    out = ex.outline(SAMPLE)
    assert out["classes"] == ["Job", "Result"]


def test_functions_includes_async_excludes_methods():
    out = ex.outline(SAMPLE)
    assert out["functions"] == ["main", "fetch"]
    assert "run" not in out["functions"]


def test_empty_module():
    assert ex.outline("") == {"imports": [], "classes": [], "functions": []}
