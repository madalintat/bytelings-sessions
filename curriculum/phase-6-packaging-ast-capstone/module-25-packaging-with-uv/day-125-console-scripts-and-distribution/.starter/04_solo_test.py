"""HIDDEN tests for rung 4 — do not peek before solving 04_solo.py."""
import importlib.util
from pathlib import Path

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_4"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "04_solo.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


def make_capturing_out():
    captured = []
    def out(s):
        captured.append(s)
    return captured, out


def hello(args):
    return 0


def fail(args):
    return 7


def echo(args):
    return len(args)


SCRIPTS = {"hello": hello, "fail": fail, "echo": echo}


def test_dispatches_handler():
    captured, out = make_capturing_out()
    rc = ex.dispatch(SCRIPTS, ["prog", "hello"], out=out)
    assert rc == 0


def test_passes_handler_return_code():
    captured, out = make_capturing_out()
    rc = ex.dispatch(SCRIPTS, ["prog", "fail"], out=out)
    assert rc == 7


def test_passes_remaining_args():
    captured, out = make_capturing_out()
    rc = ex.dispatch(SCRIPTS, ["prog", "echo", "a", "b", "c"], out=out)
    assert rc == 3


def test_unknown_command():
    captured, out = make_capturing_out()
    rc = ex.dispatch(SCRIPTS, ["prog", "nope"], out=out)
    assert rc == 2
    joined = "\n".join(captured)
    assert "unknown" in joined.lower()
    assert "nope" in joined


def test_no_command_prints_usage():
    captured, out = make_capturing_out()
    rc = ex.dispatch(SCRIPTS, ["prog"], out=out)
    assert rc == 2
    joined = "\n".join(captured)
    assert "usage" in joined.lower()


def test_lists_commands_sorted():
    captured, out = make_capturing_out()
    ex.dispatch(SCRIPTS, ["prog"], out=out)
    joined = "\n".join(captured)
    # echo, fail, hello — alphabetical
    assert joined.index("echo") < joined.index("fail") < joined.index("hello")
