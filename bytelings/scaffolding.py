"""Scaffold the 135-day curriculum skeleton from in-code constants.

Run with: uv run python -m swe.scaffolding
"""
from __future__ import annotations

from pathlib import Path

CURRICULUM_ROOT = Path("curriculum")


# (phase_dir, module_dir, [day_slugs])
SKELETON: list[tuple[str, str, list[str]]] = [
    # ---------- PHASE 1 — Python Core Fluency (28+3=31 days) ----------
    ("phase-1-python-core", "module-01-setup-and-values", [
        "001-uv-setup-and-pytest",
        "002-numbers-and-ops",
        "003-booleans-truthiness-none",
        "004-names-vs-values",
        "005-repl-and-type-hints",
    ]),
    ("phase-1-python-core", "module-02-strings-deep", [
        "006-string-indexing-and-slicing",
        "007-string-methods-and-fstrings",
        "008-string-immutability-and-concat-traps",
        "009-encoding-bytes-vs-str",
        "010-regex-essentials",
        "011-string-parsing-patterns",
    ]),
    # M6 reorder: hashing-first. Big-O moves from end-of-module-03 to
    # end-of-module-04 (Day 22), so it lands AFTER learners have built
    # the bucket-list mental model on Day 17 and used dict/set/Counter
    # in Days 18-20. 'Amortized constant' earns concrete picture.
    ("phase-1-python-core", "module-03-lists-and-counting", [
        "012-list-basics",
        "013-list-slicing-deep",
        "014-iteration-idioms-enumerate-zip",
        "015-list-methods-and-mutation",
        "016-linear-search-and-counting-ops",
    ]),
    ("phase-1-python-core", "module-04-hashing-dicts-sets-and-bigo", [
        "017-what-is-hashing",          # was 021 — kicks off module 4
        "018-dict-basics",              # named instance of hashmap from Day 17
        "019-set-operations",
        "020-defaultdict-and-counter",
        "021-dict-vs-list-decision",    # was 022
        "022-bigo-notation-intro",      # was 017 — lands with worked example
    ]),
    ("phase-1-python-core", "module-05-functions-closures-decorators", [
        "023-defining-and-calling-functions",
        "024-args-kwargs-defaults",
        "025-scope-legb-and-closures",
        "026-first-class-functions-and-lambdas",
        "027-decorators-basics",
        "028-decorators-with-args-and-type-hints",
    ]),
    ("phase-1-python-core", "phase-1-project-contacts-manager", [
        "029-project-day-1-design-and-scaffold",
        "030-project-day-2-build-core",
        "031-project-day-3-test-and-ship",
    ]),
    # ---------- PHASE 2 — Pythonic Tools & I/O (24+3=27 days) ----------
    ("phase-2-pythonic-tools", "module-06-comprehensions-iterators-generators", [
        "032-list-dict-set-comprehensions",
        "033-generator-expressions",
        "034-iterator-protocol",
        "035-yield-and-lazy-evaluation",
    ]),
    ("phase-2-pythonic-tools", "module-07-async-await", [
        "036-why-async-event-loop-intuition",
        "037-async-def-await-asyncio-run",
        "038-gather-tasks-cancellation",
        "039-async-iterators-and-async-for",
        "040-real-world-async-with-httpx",
        "041-async-pitfalls-and-patterns",
    ]),
    ("phase-2-pythonic-tools", "module-08-tuples-dataclasses-types-deep", [
        "042-tuples-and-namedtuples",
        "043-dataclasses-and-frozen",
        "044-equality-identity-hashing-semantics",
        "045-type-hints-deep-generic-typevar-protocol",
        "046-type-hints-deep-literal-typeddict-annotated",
    ]),
    ("phase-2-pythonic-tools", "module-09-classes-dunders-context-managers", [
        "047-classes-init-repr",
        "048-properties-eq-hash",
        "049-inheritance-and-composition",
        "050-iter-len-contains-dunders",
        "051-context-managers-via-classes",
        "052-contextlib-and-decorator-context-managers",
    ]),
    ("phase-2-pythonic-tools", "module-10-files-paths-json-csv-toml", [
        "053-pathlib-and-file-io",
        "054-json-csv-toml",
        "055-real-world-io-patterns",
    ]),
    ("phase-2-pythonic-tools", "phase-2-project-async-snapshotter", [
        "056-project-day-1-design-and-scaffold",
        "057-project-day-2-build-core",
        "058-project-day-3-test-and-ship",
    ]),
    # ---------- PHASE 3 — Quality & Production-Grade (18+3=21 days) ----------
    ("phase-3-quality-production", "module-11-errors-eafp-debugging", [
        "059-exception-hierarchy-try-except",
        "060-custom-exceptions-eafp-vs-lbyl",
        "061-pdb-and-breakpoint",
        "062-systematic-debugging-mindset",
    ]),
    ("phase-3-quality-production", "module-12-testing-with-pytest", [
        "063-pytest-basics-assert",
        "064-fixtures-and-parametrize",
        "065-mocks-and-monkeypatch",
        "066-property-based-testing-intro",
    ]),
        # M8: Module 13 retargeted as "refactor what YOU wrote in earlier
    # modules." Days 67-69 each refactor specific prior-module code:
    #   67 reads/refactors the decorator from Day 27 (Module 5)
    #   68 reads/refactors the context manager from Day 51 (Module 9)
    #   69 reads/refactors the test fixture from Day 64 (Module 12)
    #   70 stays as the meta refactor-a-codebase capstone
    # Day count + slugs unchanged so progress.json stays valid.
    ("phase-3-quality-production", "module-13-refactor-in-context", [
        "067-reading-code-you-didnt-write",
        "068-refactoring-katas",
        "069-pythonic-style-and-idioms",
        "070-refactor-a-codebase",
    ]),
    ("phase-3-quality-production", "module-14-logging-profiling-perf", [
        "071-logging-done-right",
        "072-profiling-with-cprofile",
        "073-why-is-this-slow",
    ]),
    ("phase-3-quality-production", "module-15-concurrency-in-practice", [
        "074-the-gil-and-concurrent-futures",
        "075-threads-vs-async-vs-procs",
        "076-multiprocessing-patterns",
    ]),
    ("phase-3-quality-production", "phase-3-project-log-analyzer", [
        "077-project-day-1-design-and-scaffold",
        "078-project-day-2-build-core",
        "079-project-day-3-test-and-ship",
    ]),
    # ---------- PHASE 4 — Data Structures (16+3=19 days) ----------
    ("phase-4-data-structures", "module-16-stacks-queues-deques", [
        "080-stack-from-list",
        "081-queue-and-why-list-queue-is-slow",
        "082-deque-and-real-uses",
        "083-balanced-parens-project",
    ]),
    ("phase-4-data-structures", "module-17-linked-lists", [
        "084-singly-linked-list",
        "085-doubly-linked-list",
        "086-lru-cache-project",
    ]),
    # M11 reorder: trees + recursion interleave. Recursion-formal pulled
    # FORWARD into the trees arc (Day 89), so tree-traversals (Day 88)
    # and BST insert/delete (Days 90/91) lean on a recursion concept the
    # learner has already been taught.
    ("phase-4-data-structures", "module-18-trees-recursion-bst", [
        "087-binary-tree-basics",
        "088-tree-traversals",
        "089-base-and-recursive-cases",       # was 099 — recursion FORMAL
        "090-bst-insert-search",              # was 089
        "091-bst-delete-and-balance",         # was 090
    ]),
    ("phase-4-data-structures", "module-19-heaps-and-hash-tables", [
        "092-heap-invariant-and-heapq",       # was 091
        "093-build-your-own-heap-and-top-k",  # was 092
        "094-hash-table-chaining",            # was 093
        "095-hash-table-open-addressing",     # was 094
        "096-hash-function-design-and-word-counter",  # was 095
    ]),
    # ---------- PHASE 5 — Algorithms (22+3=25 days) ----------
    ("phase-5-algorithms", "module-20-recursion-tail", [
        "097-tracing-recursion",              # was 100
        "098-recursion-vs-iteration",         # was 101
        "099-stack-depth-and-python-limits",  # was 102
    ]),
    ("phase-4-data-structures", "phase-4-project-tiny-database", [
        "100-project-day-1-design-and-scaffold",  # was 096
        "101-project-day-2-build-core",            # was 097
        "102-project-day-3-test-and-ship",         # was 098
    ]),
    ("phase-5-algorithms", "module-21-searching-sorting", [
        "103-binary-search-and-variants",
        "104-bubble-insertion-selection",
        "105-merge-sort-and-quick-sort",
        "106-sort-stability-timsort-keys",
    ]),
    ("phase-5-algorithms", "module-22-two-pointer-sliding-window-prefix", [
        "107-two-pointer-pattern",
        "108-sliding-window",
        "109-prefix-sums",
    ]),
    ("phase-5-algorithms", "module-23-graphs", [
        "110-graph-representations",
        "111-bfs",
        "112-dfs-and-cycle-detection",
        "113-topo-sort-and-dependency-graph",
    ]),
    ("phase-5-algorithms", "module-24-dp-greedy-backtracking", [
        "114-recursion-to-memoization",
        "115-memoization-to-tabulation",
        "116-1d-dp",
        "117-2d-dp",
        "118-string-dp",
        "119-greedy-intuition-and-failures",
        "120-backtracking-template-and-pruning",
    ]),
    ("phase-5-algorithms", "phase-5-project-pathfinder", [
        "121-project-day-1-design-and-scaffold",
        "122-project-day-2-build-core",
        "123-project-day-3-test-and-ship",
    ]),
    # ---------- PHASE 6 — Packaging, AST, Capstone (12 days) ----------
    ("phase-6-packaging-ast-capstone", "module-25-packaging-with-uv", [
        "124-pyproject-and-deps",
        "125-console-scripts-and-distribution",
    ]),
    ("phase-6-packaging-ast-capstone", "module-26-ast-and-static-analysis", [
        "126-ast-module-and-code-as-data",
        "127-build-a-tiny-linter",
    ]),
    ("phase-6-packaging-ast-capstone", "capstone", [
        "128-capstone-day-1-pick-and-design",
        "129-capstone-day-2-scaffold",
        "130-capstone-day-3-build-core",
        "131-capstone-day-4-build-features",
        "132-capstone-day-5-test",
        "133-capstone-day-6-refactor",
        "134-capstone-day-7-polish",
        "135-capstone-day-8-ship",
    ]),
]


CONCEPT_PLACEHOLDER = """\
---
day: {day_slug}
phase: {phase}
module: {module}
style: TODO  # one of: story, pain, compare, tour, trace, build-it, metaphor, detective
---
# {day_slug}

<!-- TODO: write the concept page in the chosen style. 300-600 words. -->

The day's topic, in one sentence.

## A small example

```python
# TODO
```

## Now: open `02_fluency.py` and start the drill.
"""


FLUENCY_PLACEHOLDER = '''\
"""Rung 2: Fluency drill. Fix the broken bits.

Topic: {day_slug}
"""


def add(a: int, b: int) -> int:
    return a + b
'''


FLUENCY_TEST_PLACEHOLDER = '''\
"""Hidden tests for {day_slug} — rung 2."""
import importlib.util
from pathlib import Path

_HERE = Path(__file__).parent
_NAME = f"_{{_HERE.name}}_rung_2"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "02_fluency.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


def test_placeholder_passes():
    assert ex.add(2, 3) == 5
'''


GUIDED_PLACEHOLDER = '''\
"""Rung 3: Guided implement. Fill in the body.

Topic: {day_slug}
"""


def double(x: int) -> int:
    """Return x doubled.

    >>> double(3)
    6
    """
    raise NotImplementedError
'''


GUIDED_TEST_PLACEHOLDER = '''\
"""Hidden tests for {day_slug} — rung 3."""
import importlib.util
from pathlib import Path

_HERE = Path(__file__).parent
_NAME = f"_{{_HERE.name}}_rung_3"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "03_guided.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


def test_double_zero():
    assert ex.double(0) == 0


def test_double_positive():
    assert ex.double(3) == 6


def test_double_negative():
    assert ex.double(-4) == -8
'''


SOLO_PLACEHOLDER = '''\
"""Rung 4: Solo implement. No scaffold.

Topic: {day_slug}

Write a function `triple(x: int) -> int` that returns x * 3.
"""


def triple(x: int) -> int:
    raise NotImplementedError
'''


SOLO_TEST_PLACEHOLDER = '''\
"""Hidden tests for {day_slug} — rung 4 (do not peek before solving)."""
import importlib.util
from pathlib import Path

_HERE = Path(__file__).parent
_NAME = f"_{{_HERE.name}}_rung_4"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "04_solo.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


def test_triple_zero():
    assert ex.triple(0) == 0


def test_triple_positive():
    assert ex.triple(3) == 9


def test_triple_negative():
    assert ex.triple(-2) == -6
'''


APPLY_PLACEHOLDER = '''\
"""Rung 5: Apply. A small project chunk that uses today's concept.

Topic: {day_slug}
"""

if __name__ == "__main__":
    print("Replace this with your project chunk.")
'''


def _new_filenames() -> dict[str, str]:
    """Map placeholder constants to their v2 filenames."""
    return {
        "README.md": CONCEPT_PLACEHOLDER,
        "fluency.py": FLUENCY_PLACEHOLDER,
        "fluency_test.py": FLUENCY_TEST_PLACEHOLDER,
        "guided.py": GUIDED_PLACEHOLDER,
        "guided_test.py": GUIDED_TEST_PLACEHOLDER,
        "solo.py": SOLO_PLACEHOLDER,
        "solo_test.py": SOLO_TEST_PLACEHOLDER,
        "apply.py": APPLY_PLACEHOLDER,
    }


def scaffold_day(
    day_dir: Path, sol_dir: Path, day_slug: str, phase: str, module: str
) -> None:
    """Create curriculum/<slug>/ + solutions/<slug>/ from placeholders."""
    day_dir.mkdir(parents=True, exist_ok=True)
    sol_dir.mkdir(parents=True, exist_ok=True)
    for name, template in _new_filenames().items():
        content = template.format(day_slug=day_slug, phase=phase, module=module)
        for target_dir in (day_dir, sol_dir):
            target = target_dir / name
            if not target.exists():
                target.write_text(content)


def scaffold_all(root: Path = Path(".")) -> list[tuple[str, str, str, int]]:
    """Walk SKELETON; produce curriculum/ and solutions/. Return manifest seed.

    Returns a list of (slug, phase, module, day_number) tuples that the
    caller can hand to bytelings.info_toml.dump for info.toml.
    """
    curriculum = root / "curriculum"
    solutions = root / "solutions"
    manifest: list[tuple[str, str, str, int]] = []
    for phase, module, day_slugs in SKELETON:
        for slug in day_slugs:
            day_number = int(slug.split("-")[0])
            scaffold_day(
                day_dir=curriculum / slug,
                sol_dir=solutions / slug,
                day_slug=slug,
                phase=phase,
                module=module,
            )
            manifest.append((slug, phase, module, day_number))
    return manifest


if __name__ == "__main__":
    from .info_toml import DayEntry, dump as dump_info_toml
    manifest = scaffold_all()
    entries = [
        DayEntry(
            slug=slug,
            path=f"curriculum/{slug}",
            day_number=n,
            phase=phase,
            module=module,
            old_slug=f"day-{slug}",
            patterns=[],
        )
        for slug, phase, module, n in manifest
    ]
    dump_info_toml(entries, Path("curriculum") / "info.toml")
    print(f"Scaffolded {len(manifest)} days + info.toml.")
