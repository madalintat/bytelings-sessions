"""Tests for rung 2 — green after the Attribute-chain fix."""
import importlib.util
import sys
from pathlib import Path

from _byte import diagnose

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_2"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "fluency.py")
ex = importlib.util.module_from_spec(_spec)
sys.modules[_NAME] = ex
_spec.loader.exec_module(ex)


def test_unused_bare_import_detected():
    src = "import os\n"
    result = ex.find_unused_imports(src)
    diagnose(
        "os" in result,
        f"Expected 'os' in unused imports, got {result!r}.",
    )


def test_used_bare_name_not_flagged():
    src = "import os\nprint(os)\n"
    result = ex.find_unused_imports(src)
    diagnose(
        "os" not in result,
        f"'os' should be used (bare Name), but got {result!r}.",
    )


def test_attribute_access_counts_as_use():
    src = "import os\npath = os.path.join('a', 'b')\n"
    result = ex.find_unused_imports(src)
    diagnose(
        "os" not in result,
        f"'os' is used via os.path.join but was flagged as unused: {result!r}. "
        "Fix the Attribute-chain extraction in Pass 2.",
        (lambda: "os" in result,
         "'os' was still flagged as unused — the TODO for ast.Attribute "
         "nodes has not been implemented. Walk the .value chain down to "
         "the root ast.Name and collect its .id."),
    )


def test_multiple_imports_one_used():
    src = "import os\nimport sys\nprint(sys.argv)\n"
    result = ex.find_unused_imports(src)
    diagnose(
        "os" in result and "sys" not in result,
        f"Expected {{'os'}} unused and sys used, got {result!r}.",
        (lambda: "sys" in result,
         "'sys' is used via sys.argv (Attribute) but is marked unused. "
         "The Attribute-chain fix is needed."),
    )


def test_alias_unused():
    src = "import os as operating_system\n"
    result = ex.find_unused_imports(src)
    diagnose(
        "operating_system" in result,
        f"Expected 'operating_system' in unused, got {result!r}.",
    )


def test_no_imports_empty_result():
    src = "x = 1\n"
    diagnose(
        ex.find_unused_imports(src) == set(),
        f"Expected empty set for source with no imports, "
        f"got {ex.find_unused_imports(src)!r}.",
    )
