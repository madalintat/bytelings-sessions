"""HIDDEN tests for rung 4."""
import importlib.util
from pathlib import Path

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_4"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "04_solo.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


def test_make_files_count(tmp_path):
    paths = ex.make_files(tmp_path, n_files=3, n_lines=10, seed=0)
    assert len(paths) == 3
    for p in paths:
        assert p.exists()
        assert p.read_text().count("\n") == 10


def test_make_files_lines_parse(tmp_path):
    """Every generated line must be parseable by yesterday's parser."""
    paths = ex.make_files(tmp_path, n_files=1, n_lines=50, seed=1)
    text = paths[0].read_text()
    # Use the parser from day-078 rung 3.
    from importlib.util import module_from_spec, spec_from_file_location
    parser_path = (
        Path(__file__).parent.parent
        / "day-078-project-day-2-build-core"
        / "03_guided.py"
    )
    spec = spec_from_file_location("_p", parser_path)
    p = module_from_spec(spec)
    spec.loader.exec_module(p)
    for line in text.splitlines():
        # Should not raise.
        p.parse_line(line)


def test_triple_zero(tmp_path):
    paths = []
    serial, parallel, equal = ex.triple(paths)
    assert equal is True
    assert serial.parsed == 0
    assert parallel.parsed == 0


def test_triple_positive(tmp_path):
    paths = ex.make_files(tmp_path, n_files=4, n_lines=200, seed=7)
    serial, parallel, equal = ex.triple(paths)
    assert equal is True, (
        f"parallel disagrees with serial: "
        f"{serial.parsed=} {parallel.parsed=} "
        f"{serial.levels=} {parallel.levels=}"
    )
    assert serial.parsed == 4 * 200


def test_triple_negative(tmp_path, monkeypatch):
    """Sanity: if we deliberately break the parallel path, equal becomes False.
    We monkeypatch the parallel function inside the test module to
    return a different aggregate."""
    paths = ex.make_files(tmp_path, n_files=1, n_lines=20, seed=2)
    real_parallel = ex.analyze_paths_parallel

    def fake_parallel(paths, **kw):
        agg = real_parallel(paths, **kw)
        agg.parsed += 1  # introduce a difference
        return agg

    monkeypatch.setattr(ex, "analyze_paths_parallel", fake_parallel)
    serial, parallel, equal = ex.triple(paths)
    assert equal is False
