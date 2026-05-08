"""Tests for scripts/migrate_v1_to_v2.py — exercises on a synthetic v1 tree."""
import importlib.util
import sys
from pathlib import Path

from bytelings import info_toml

# Load the migration script as a module (it lives outside bytelings/).
_MIGRATE = Path(__file__).resolve().parents[1] / "scripts" / "migrate_v1_to_v2.py"
_spec = importlib.util.spec_from_file_location("_migrate", _MIGRATE)
migrate = importlib.util.module_from_spec(_spec)
sys.modules["_migrate"] = migrate
_spec.loader.exec_module(migrate)


def _build_v1_tree(root: Path) -> None:
    """Build a synthetic 2-day v1 curriculum + .starter shadows."""
    day1 = root / "curriculum" / "phase-1-python-core" / "module-01-setup-and-values" / "day-001-uv-setup-and-pytest"
    day1.mkdir(parents=True)
    for fname in ("concept.md", "02_fluency.py", "02_fluency_test.py",
                  "03_guided.py", "03_guided_test.py",
                  "04_solo.py", "04_solo_test.py", "05_apply.py"):
        (day1 / fname).write_text(f"# day-001 {fname}\n")
    starter1 = day1 / ".starter"
    starter1.mkdir()
    for fname in ("concept.md", "02_fluency.py", "02_fluency_test.py",
                  "03_guided.py", "03_guided_test.py",
                  "04_solo.py", "04_solo_test.py", "05_apply.py"):
        (starter1 / fname).write_text(f"# day-001 starter {fname}\n")

    day2 = root / "curriculum" / "phase-1-python-core" / "module-01-setup-and-values" / "day-002-numbers-and-ops"
    day2.mkdir(parents=True)
    for fname in ("concept.md", "02_fluency.py", "02_fluency_test.py",
                  "03_guided.py", "03_guided_test.py",
                  "04_solo.py", "04_solo_test.py", "05_apply.py"):
        (day2 / fname).write_text(f"# day-002 {fname}\n")
    starter2 = day2 / ".starter"
    starter2.mkdir()
    for fname in ("concept.md", "02_fluency.py", "02_fluency_test.py",
                  "03_guided.py", "03_guided_test.py",
                  "04_solo.py", "04_solo_test.py", "05_apply.py"):
        (starter2 / fname).write_text(f"# day-002 starter {fname}\n")


def test_migrate_creates_new_layout(tmp_path: Path):
    _build_v1_tree(tmp_path)
    migrate.run(tmp_path)

    # New layout exists.
    new1 = tmp_path / "curriculum" / "001-uv-setup-and-pytest"
    assert (new1 / "README.md").exists()           # was concept.md
    assert (new1 / "fluency.py").exists()
    assert (new1 / "fluency_test.py").exists()
    assert (new1 / "guided.py").exists()
    assert (new1 / "guided_test.py").exists()
    assert (new1 / "solo.py").exists()
    assert (new1 / "solo_test.py").exists()
    assert (new1 / "apply.py").exists()

    # Solutions mirror exists with the .starter content.
    sol1 = tmp_path / "solutions" / "001-uv-setup-and-pytest"
    assert (sol1 / "README.md").exists()
    assert (sol1 / "fluency.py").read_text() == "# day-001 starter 02_fluency.py\n"


def test_migrate_writes_info_toml(tmp_path: Path):
    _build_v1_tree(tmp_path)
    migrate.run(tmp_path)
    entries = info_toml.load(tmp_path / "curriculum" / "info.toml")
    assert len(entries) == 2
    assert entries[0].slug == "001-uv-setup-and-pytest"
    assert entries[0].old_slug == "day-001-uv-setup-and-pytest"
    assert entries[0].day_number == 1
    assert entries[1].day_number == 2


def test_migrate_deletes_old_phase_module_dirs(tmp_path: Path):
    _build_v1_tree(tmp_path)
    migrate.run(tmp_path)
    assert not (tmp_path / "curriculum" / "phase-1-python-core").exists()


def test_migrate_deletes_starter_shadows(tmp_path: Path):
    _build_v1_tree(tmp_path)
    migrate.run(tmp_path)
    starters = list((tmp_path / "curriculum").rglob(".starter"))
    assert starters == []


def test_migrate_is_idempotent(tmp_path: Path):
    _build_v1_tree(tmp_path)
    migrate.run(tmp_path)
    migrate.run(tmp_path)  # second run should be a no-op
    assert (tmp_path / "curriculum" / "001-uv-setup-and-pytest" / "README.md").exists()
