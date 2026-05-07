"""Storage edge-case tests using tmp_path + monkeypatch."""
from datetime import date

import pytest


def test_load_missing_returns_empty(tmp_path, storage_mod):
    assert storage_mod.load(tmp_path / "absent.json") == {}


def test_save_then_load_equal(tmp_path, storage_mod, core_mod):
    path = tmp_path / "data.json"
    h = core_mod.Habit("read", date(2026, 5, 1),
                       log=[date(2026, 5, 8), date(2026, 5, 9)])
    storage_mod.save(path, {"read": h})
    assert storage_mod.load(path) == {"read": h}


def test_save_creates_parent_dir(tmp_path, storage_mod, core_mod):
    path = tmp_path / "nested" / "more" / "data.json"
    storage_mod.save(path, {"a": core_mod.Habit("a", date(2026, 5, 1))})
    assert path.is_file()


def test_corrupt_json_raises(tmp_path, storage_mod):
    path = tmp_path / "data.json"
    path.write_text("not json at all", encoding="utf-8")
    with pytest.raises(Exception):  # ValueError or json.JSONDecodeError
        storage_mod.load(path)


def test_atomic_save_overwrites(tmp_path, storage_mod, core_mod):
    """Save twice — the second save fully replaces the first."""
    path = tmp_path / "data.json"
    storage_mod.save(path, {"first_habit": core_mod.Habit("first_habit", date(2026, 5, 1))})
    first = path.read_text()
    storage_mod.save(path, {"second_habit": core_mod.Habit("second_habit", date(2026, 5, 2))})
    second = path.read_text()
    assert first != second
    assert "second_habit" in second
    assert "first_habit" not in second  # no leftover state


def test_unknown_top_level_keys_ignored(tmp_path, storage_mod):
    """Forward compat: extra top-level keys don't break load."""
    path = tmp_path / "data.json"
    path.write_text(
        '{"habits": {}, "future_field": "ignore me", "version": 99}',
        encoding="utf-8",
    )
    assert storage_mod.load(path) == {}
