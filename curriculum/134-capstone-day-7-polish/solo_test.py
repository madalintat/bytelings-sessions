"""HIDDEN tests for rung 4 — do not peek before solving solo.py."""
import importlib.util
from pathlib import Path

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_4"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "solo.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


CLEAN = """\
name: Release
on:
  push:
    tags: ["v*"]
jobs:
  pypi-publish:
    runs-on: ubuntu-latest
    permissions:
      id-token: write
    environment:
      name: pypi
      url: https://pypi.org/project/my-linter/
    steps:
      - uses: actions/checkout@v4
      - uses: pypa/gh-action-pypi-publish@release/v1
"""

MISSING_ID_TOKEN = CLEAN.replace("      id-token: write\n", "")
MISSING_ENV = "\n".join(
    line for line in CLEAN.splitlines()
    if "environment:" not in line
    and "name: pypi" not in line
    and "url: https://" not in line
) + "\n"
WITH_REPO_URL = CLEAN + "        with:\n          repository-url: --repository-url https://test.pypi.org/legacy/\n"
WITH_PASSWORD = CLEAN + "          password: ${{ secrets.PYPI_TOKEN }}\n"


def test_clean_returns_empty():
    assert ex.validate_publish_workflow(CLEAN) == []


def test_missing_id_token():
    result = ex.validate_publish_workflow(MISSING_ID_TOKEN)
    assert any("id-token" in c for c in result)


def test_missing_environment():
    result = ex.validate_publish_workflow(MISSING_ENV)
    assert any("environment" in c for c in result)


def test_repository_url_flagged():
    result = ex.validate_publish_workflow(WITH_REPO_URL)
    assert any("repository-url" in c or "Trusted" in c for c in result)


def test_password_flagged():
    result = ex.validate_publish_workflow(WITH_PASSWORD)
    assert any("password" in c or "credential" in c for c in result)
