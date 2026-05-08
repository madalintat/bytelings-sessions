"""Tests for rung 3 — green after find_unused_imports is implemented."""
import importlib.util
import sys
from pathlib import Path

from _byte import diagnose

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_3"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "guided.py")
ex = importlib.util.module_from_spec(_spec)
sys.modules[_NAME] = ex
_spec.loader.exec_module(ex)


def test_returns_list():
    result = ex.find_unused_imports("import os\n")
    diagnose(
        isinstance(result, list),
        f"find_unused_imports returned {type(result).__name__!r}, expected list.",
    )


def test_unused_import_returned():
    result = ex.find_unused_imports("import os\n")
    diagnose(
        result == ["os"],
        f"Expected ['os'], got {result!r}.",
        (lambda: result == [],
         "Got empty list — did you implement the two passes? "
         "Pass 1 collects import names; Pass 2 collects uses."),
    )


def test_used_import_not_returned():
    src = "import os\nos.getcwd()\n"
    result = ex.find_unused_imports(src)
    diagnose(
        result == [],
        f"Expected [], got {result!r} — os is used via os.getcwd().",
        (lambda: "os" in result,
         "os.getcwd() uses 'os' via an Attribute node. Make sure Pass 2 "
         "walks the .value chain of Attribute nodes to reach the root Name."),
    )


def test_result_is_sorted():
    src = "import sys\nimport os\n"
    result = ex.find_unused_imports(src)
    diagnose(
        result == sorted(result),
        f"Result {result!r} is not sorted. Return sorted(unused).",
    )


def test_alias_tracked():
    src = "import os as operating_system\n"
    result = ex.find_unused_imports(src)
    diagnose(
        "operating_system" in result,
        f"Alias 'operating_system' not in result {result!r}.",
        (lambda: "os" in result,
         "Got 'os' instead of 'operating_system' — use alias.asname "
         "when it is set."),
    )


def test_multiple_mixed():
    src = "import os\nimport sys\nimport re\nprint(sys.argv)\n"
    result = ex.find_unused_imports(src)
    diagnose(
        set(result) == {"os", "re"},
        f"Expected ['os', 're'], got {result!r}.",
    )
    diagnose(
        result == sorted(result),
        f"Result {result!r} not sorted.",
    )


def test_no_imports():
    diagnose(
        ex.find_unused_imports("x = 1\n") == [],
        "Expected [] for source with no imports.",
    )
