"""Day 2 checkpoint tests."""
import importlib.util
from pathlib import Path

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_app"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "app.py")
app = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(app)

DATA = _HERE / "data.csv"


def test_day2_find_by_email(capsys):
    rc = app.main(["app.py", "find", str(DATA), "--email", "alice@example.com"])
    assert rc == 0
    out = capsys.readouterr().out.strip()
    assert out.startswith("Alice Wonderland,alice@example.com,")


def test_day2_find_by_email_uppercase_input_works(capsys):
    """The query email should be normalized too."""
    rc = app.main(["app.py", "find", str(DATA), "--email", "ALICE@EXAMPLE.COM"])
    assert rc == 0


def test_day2_find_by_email_missing_returns_1():
    rc = app.main(["app.py", "find", str(DATA), "--email", "nope@nope"])
    assert rc == 1


def test_day2_find_by_regex(capsys):
    rc = app.main(["app.py", "find", str(DATA), "--regex", "^Bob"])
    assert rc == 0
    out_lines = capsys.readouterr().out.strip().splitlines()
    # Bob Smith and Bob Smithson both match
    assert any("Bob Smith" == line.split(",")[0] for line in out_lines)
    assert any("Bob Smithson" == line.split(",")[0] for line in out_lines)


def test_day2_dupes_finds_bobs(capsys):
    rc = app.main(["app.py", "dupes", str(DATA)])
    assert rc == 0
    out = capsys.readouterr().out
    # Bob Smith / Bob Smithson share initials 'bs' + phone 4155550102
    # John Smith shares the phone but initials are different ('js') — not grouped
    assert "Bob Smith" in out
    assert "Bob Smithson" in out


def test_day2_export_round_trip(tmp_path):
    out = tmp_path / "clean.csv"
    rc = app.main(["app.py", "export", str(DATA), str(out)])
    assert rc == 0
    # Re-load the exported file; should have the same count and names
    again = app.load_csv(out)
    original = app.load_csv(DATA)
    assert len(again) == len(original)
    assert {c["email"] for c in again if c["email"]} == {
        c["email"] for c in original if c["email"]
    }


def test_day2_timed_prints_to_stderr(capsys):
    app.main(["app.py", "find", str(DATA), "--regex", "^Bob"])
    err = capsys.readouterr().err
    assert "[timed]" in err
