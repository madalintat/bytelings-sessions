"""Day 3 test suite — covers Day 1, Day 2, and Day 3 work."""
import importlib.util
from pathlib import Path

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_app"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "app.py")
app = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(app)

DATA = _HERE / "data.csv"


# ---------- Day 1 checkpoints ----------

def test_day1_loads_sample_csv():
    contacts = app.load_csv(DATA)
    assert len(contacts) == 10


def test_day1_normalizes_emails():
    contacts = app.load_csv(DATA)
    bob = next(c for c in contacts if c["name"] == "Bob Smith")
    assert bob["email"] == "bob@example.com"


def test_day1_normalizes_phones():
    contacts = app.load_csv(DATA)
    alice = next(c for c in contacts if c["name"] == "Alice Wonderland")
    assert alice["phone"] == "4155550101"


def test_day1_list_command_runs(capsys):
    rc = app.main(["app.py", "list", str(DATA)])
    assert rc == 0
    out = capsys.readouterr().out.splitlines()
    assert out[0] == "Alice Wonderland"


# ---------- Day 2 checkpoints ----------

def test_day2_find_by_email(capsys):
    rc = app.main(["app.py", "find", str(DATA), "--email", "alice@example.com"])
    assert rc == 0


def test_day2_find_by_email_normalizes_query():
    contacts = app.load_csv(DATA)
    r = app.Roster(contacts)
    assert r.find_by_email("ALICE@EXAMPLE.COM") is not None


def test_day2_find_by_regex(capsys):
    rc = app.main(["app.py", "find", str(DATA), "--regex", "^Bob"])
    assert rc == 0


def test_day2_dupes_finds_bobs(capsys):
    rc = app.main(["app.py", "dupes", str(DATA)])
    assert rc == 0
    out = capsys.readouterr().out
    assert "Bob Smith" in out and "Bob Smithson" in out


def test_day2_export_round_trip(tmp_path):
    out = tmp_path / "clean.csv"
    rc = app.main(["app.py", "export", str(DATA), str(out)])
    assert rc == 0
    assert app.load_csv(out) == app.load_csv(DATA)


def test_day2_timed_prints_to_stderr(capsys):
    app.main(["app.py", "find", str(DATA), "--regex", "^Bob"])
    err = capsys.readouterr().err
    assert "[timed]" in err


# ---------- Day 3 hardening ----------

def test_day3_empty_csv_loads_to_empty(tmp_path):
    f = tmp_path / "empty.csv"
    f.write_text("name,email,phone\n", encoding="utf-8")
    assert app.load_csv(f) == []


def test_day3_malformed_line_skipped(tmp_path):
    f = tmp_path / "bad.csv"
    f.write_text("name,email,phone\nA,a@x.io,1\nbroken_line\nB,b@x.io,2\n",
                 encoding="utf-8")
    out = app.load_csv(f)
    assert [c["name"] for c in out] == ["A", "B"]


def test_day3_regex_no_match_exits_1():
    rc = app.main(["app.py", "find", str(DATA), "--regex", "ZZZNOMATCH"])
    assert rc == 1


def test_day3_help_runs(capsys):
    rc = app.main(["app.py", "--help"])
    assert rc == 0
    err = capsys.readouterr().err
    assert "contacts" in err.lower()


def test_day3_find_with_no_flag_exits_2():
    rc = app.main(["app.py", "find", str(DATA)])
    assert rc == 2


def test_day3_export_no_path_exits_2():
    rc = app.main(["app.py", "export", str(DATA)])
    assert rc == 2


def test_day3_bad_regex_exits_2():
    rc = app.main(["app.py", "find", str(DATA), "--regex", "[unterminated"])
    assert rc == 2


def test_day3_dupes_deterministic_order(capsys):
    """Cluster order must be stable across runs (sorted by first name)."""
    rc1 = app.main(["app.py", "dupes", str(DATA)])
    out1 = capsys.readouterr().out
    rc2 = app.main(["app.py", "dupes", str(DATA)])
    out2 = capsys.readouterr().out
    assert rc1 == rc2 == 0
    assert out1 == out2
