"""Tests for rung 3."""
import importlib.util
from pathlib import Path

import pytest

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_3"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "03_guided.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


@pytest.fixture
def populated_cache() -> "ex.Cache":
    """A fresh cache with three known entries.

    Note: this fixture runs ONCE PER TEST (default function scope),
    so mutations in one test don't leak into the next.
    """
    c = ex.Cache()
    c.set("alpha", "1")
    c.set("beta", "2")
    c.set("gamma", "3")
    return c


def test_get_existing(populated_cache):
    assert populated_cache.get("alpha") == "1"
    assert populated_cache.get("beta") == "2"


def test_get_missing(populated_cache):
    assert populated_cache.get("nope") is None


def test_size(populated_cache):
    assert populated_cache.size() == 3


def test_set_overwrites(populated_cache):
    populated_cache.set("alpha", "100")
    assert populated_cache.get("alpha") == "100"
    assert populated_cache.size() == 3


def test_delete(populated_cache):
    populated_cache.delete("beta")
    assert populated_cache.get("beta") is None
    assert populated_cache.size() == 2


def test_delete_missing_no_error(populated_cache):
    populated_cache.delete("never seen")
    assert populated_cache.size() == 3


def test_isolation_between_tests(populated_cache):
    """If function-scope is working, this test sees a fresh cache
    even though the previous test deleted a key."""
    assert populated_cache.size() == 3
    assert populated_cache.get("beta") == "2"
