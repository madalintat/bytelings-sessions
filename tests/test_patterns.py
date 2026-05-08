"""Tests for bytelings.patterns — Pattern Catalog v1 integrity."""
import re

from bytelings import patterns as pat


def test_catalog_has_at_least_30_patterns():
    """The catalog ships with ≥30 entries; we currently aim for 31."""
    assert len(pat.PATTERNS) >= 30


def test_every_pattern_has_canonical_id_shape():
    pattern_id_re = re.compile(r"^P-\d{2}$")
    for p in pat.PATTERNS:
        assert pattern_id_re.match(p.id), f"{p.id} doesn't match P-NN"


def test_pattern_ids_are_unique():
    ids = [p.id for p in pat.PATTERNS]
    assert len(ids) == len(set(ids)), "duplicate pattern IDs"


def test_pattern_ids_are_sequential_and_zero_padded():
    """P-01, P-02, … P-NN with no gaps. Catches forgotten entries when
    the catalog grows."""
    expected = [f"P-{n:02d}" for n in range(1, len(pat.PATTERNS) + 1)]
    actual = [p.id for p in pat.PATTERNS]
    assert actual == expected, f"non-sequential IDs: {actual} vs {expected}"


def test_every_pattern_has_required_fields():
    for p in pat.PATTERNS:
        assert p.name, f"{p.id} missing name"
        assert p.description, f"{p.id} missing description"
        assert p.canonical, f"{p.id} missing canonical"
        assert p.when, f"{p.id} missing 'when'"
        assert isinstance(p.days, tuple), f"{p.id} days is not a tuple"


def test_by_id_finds_known_pattern():
    p = pat.by_id("P-07")
    assert p is not None
    assert p.name == "accumulator-into-dict"


def test_by_id_is_case_insensitive():
    assert pat.by_id("p-07") == pat.by_id("P-07")
    assert pat.by_id("P-07 ") == pat.by_id("P-07")


def test_by_id_returns_none_for_unknown():
    assert pat.by_id("P-99") is None
    assert pat.by_id("not-a-pattern") is None


def test_canonical_examples_are_at_most_8_lines():
    """Pattern catalog is reference material — a long example smells
    like 'this should be its own day, not a pattern entry'."""
    for p in pat.PATTERNS:
        line_count = len(p.canonical.splitlines())
        assert line_count <= 8, (
            f"{p.id} ({p.name}) has {line_count}-line canonical; "
            "patterns should be <= 8 lines"
        )


def test_days_referenced_are_in_curriculum_range():
    """Every day reference is an int in [1, 135] — the curriculum's range."""
    for p in pat.PATTERNS:
        for d in p.days:
            assert isinstance(d, int), f"{p.id} has non-int day {d!r}"
            assert 1 <= d <= 135, f"{p.id} cites day {d}, out of [1, 135]"
