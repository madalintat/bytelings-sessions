"""Day 1 checkpoint tests."""
import importlib.util
import io
import sys
from pathlib import Path

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_app"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "app.py")
app = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(app)

DATA = _HERE / "data.csv"


def test_day1_loads_sample_csv():
    contacts = app.load_csv(DATA)
    assert len(contacts) == 10
    assert contacts[0]["name"] == "Alice Wonderland"


def test_day1_normalizes_emails():
    contacts = app.load_csv(DATA)
    bob = next(c for c in contacts if c["name"] == "Bob Smith")
    assert bob["email"] == "bob@example.com"


def test_day1_normalizes_phones():
    contacts = app.load_csv(DATA)
    alice = next(c for c in contacts if c["name"] == "Alice Wonderland")
    assert alice["phone"] == "4155550101"
    maria = next(c for c in contacts if c["name"] == "maria de la cruz")
    assert maria["phone"] == "14155550104"


def test_day1_list_command_runs(capsys):
    rc = app.main(["app.py", "list", str(DATA)])
    assert rc == 0
    out = capsys.readouterr().out.splitlines()
    # First name alphabetically: 'Alice Wonderland'
    assert out[0] == "Alice Wonderland"
    assert len(out) == 10


def test_day1_unknown_command_exits_2(capsys):
    rc = app.main(["app.py", "wat", str(DATA)])
    assert rc == 2


def test_day1_missing_file_exits_2(capsys):
    rc = app.main(["app.py", "list", "/no/such/file.csv"])
    assert rc == 2
