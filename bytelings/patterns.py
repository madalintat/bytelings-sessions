"""Pattern Catalog — bytelings' numbered inventory of recurring patterns.

Adapted from Charles Severance's "four loop patterns" and NeetCode's
pattern-graph: the curriculum's deepest claim is that fluency in
programming is fluency in *recognition*. We name the patterns out
loud, give each a number, and let solo/apply rungs tag the numbers
they exercise. Over 135 days a learner accumulates a vocabulary, not
just a list of solved problems.

Tagging discipline (added gradually during M5 + M7):
    "\"\"\"Day 18 — Build a word frequency counter.

    Patterns: P-07 (accumulator-into-dict), P-12 (filter-then-map).
    \"\"\""

CLI: `bytelings patterns` lists; `bytelings patterns P-07` shows one.
"""
from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class Pattern:
    id: str                 # canonical "P-NN"
    name: str               # short slug, e.g. "accumulator-into-dict"
    description: str        # one paragraph (1-3 sentences)
    canonical: str          # ~3-6 line code example
    when: str               # one-line "when to reach for it"
    days: tuple[int, ...]   # day numbers (per info.toml) that exercise it


PATTERNS: tuple[Pattern, ...] = (
    Pattern(
        id="P-01",
        name="sentinel-loop",
        description=(
            "Loop until a sentinel value (None, EOF, empty line) tells "
            "you to stop. The sentinel is a return value the loop body "
            "agrees to interpret specially."
        ),
        canonical=(
            'while True:\n'
            '    line = input()\n'
            '    if line == "":\n'
            '        break\n'
            '    process(line)'
        ),
        when="reading from a stream where the producer signals end-of-input.",
        days=(1, 11, 53, 71),
    ),
    Pattern(
        id="P-02",
        name="in-place-vs-returning",
        description=(
            "Pick between mutating an argument (returns None) and "
            "returning a fresh value (leaves input untouched). "
            "list.sort() vs sorted(), list.reverse() vs reversed() — "
            "Python uses naming as the marker."
        ),
        canonical=(
            "lst.sort()                   # in-place, returns None\n"
            "new = sorted(lst)            # returns new list, lst unchanged"
        ),
        when="when designing a function that modifies a collection.",
        days=(13, 15, 25, 49),
    ),
    Pattern(
        id="P-03",
        name="walrus-in-condition",
        description=(
            "Use `:=` to bind a value AND test it in the same "
            "expression. Removes the read-then-test idiom that "
            "duplicates the call."
        ),
        canonical=(
            "while (chunk := f.read(8192)):\n"
            "    handle(chunk)"
        ),
        when="reading until empty / falsy without restating the call.",
        days=(53, 71, 95),
    ),
    Pattern(
        id="P-04",
        name="dispatch-by-dict",
        description=(
            "Replace an if/elif chain with a dict lookup keyed on the "
            "discriminator. Adds: clearer extension point, faster "
            "lookup at scale, declarative shape."
        ),
        canonical=(
            'HANDLERS = {"+": add, "-": sub, "*": mul}\n'
            'return HANDLERS[op](a, b)'
        ),
        when="branching on a small finite set of named cases.",
        days=(20, 60, 116, 127),
    ),
    Pattern(
        id="P-05",
        name="eafp-try-then-fallback",
        description=(
            "Easier to Ask Forgiveness than Permission: try the "
            "happy path, catch the specific failure, fall back. "
            "Pythonic alternative to LBYL (Look Before You Leap), "
            "preferred when the success rate is high."
        ),
        canonical=(
            "try:\n"
            "    return cache[key]\n"
            "except KeyError:\n"
            "    return load(key)"
        ),
        when="dict/list/attr access where missing is rare.",
        days=(59, 60, 65),
    ),
    Pattern(
        id="P-06",
        name="sliding-window",
        description=(
            "Maintain a contiguous window over a sequence, advancing "
            "the right edge and (sometimes) the left. The window's "
            "aggregate updates O(1) per step rather than O(window) "
            "from scratch."
        ),
        canonical=(
            "left = 0\n"
            "running = 0\n"
            "for right, x in enumerate(arr):\n"
            "    running += x\n"
            "    while running > target:\n"
            "        running -= arr[left]; left += 1"
        ),
        when="longest/shortest/best-K subarray meeting a property.",
        days=(108,),
    ),
    Pattern(
        id="P-07",
        name="accumulator-into-dict",
        description=(
            "Build a dict by iterating and updating by key. Each item "
            "derives a key; the value accumulates (count, sum, list of "
            "items, max-so-far). Severance's master pattern."
        ),
        canonical=(
            "counts: dict[str, int] = {}\n"
            "for word in words:\n"
            "    counts[word] = counts.get(word, 0) + 1"
        ),
        when="any 'count / group / index / aggregate by Y' question.",
        days=(18, 19, 20, 35, 65, 95, 113, 130),
    ),
    Pattern(
        id="P-08",
        name="two-pointer-from-ends",
        description=(
            "Two indices walk from opposite ends, moving inward. Each "
            "step decides which pointer advances based on a comparison. "
            "O(n) replaces O(n²) for sorted-array problems."
        ),
        canonical=(
            "lo, hi = 0, len(a) - 1\n"
            "while lo < hi:\n"
            "    if a[lo] + a[hi] == target: return (lo, hi)\n"
            "    if a[lo] + a[hi] < target: lo += 1\n"
            "    else: hi -= 1"
        ),
        when="paired-element queries on a sorted sequence.",
        days=(107,),
    ),
    Pattern(
        id="P-09",
        name="two-pointer-fast-slow",
        description=(
            "One pointer advances faster than the other. The gap "
            "encodes the answer (cycle detection, midpoint, k-th from "
            "end of a linked list)."
        ),
        canonical=(
            "slow = fast = head\n"
            "while fast and fast.next:\n"
            "    slow = slow.next\n"
            "    fast = fast.next.next"
        ),
        when="linked-list cycle / midpoint / 'distance behind' queries.",
        days=(84, 85, 107),
    ),
    Pattern(
        id="P-10",
        name="visit-set-for-dedup",
        description=(
            "Track items already seen in a set. O(1) membership test "
            "trades memory for speed. Foundation of dedup, cycle "
            "detection in graphs, and 'first repeat' problems."
        ),
        canonical=(
            "seen: set[int] = set()\n"
            "for x in arr:\n"
            "    if x in seen: return x\n"
            "    seen.add(x)"
        ),
        when="any 'has this been seen?' question over an unbounded stream.",
        days=(15, 19, 95, 110, 111, 112),
    ),
    Pattern(
        id="P-11",
        name="reduce-with-identity",
        description=(
            "Fold a sequence into a single value with an explicit "
            "starting identity (0 for sum, 1 for product, [] for "
            "concat, math.inf for min). Identity makes the empty case "
            "handled for free."
        ),
        canonical=(
            "from functools import reduce\n"
            "total = reduce(operator.mul, nums, 1)"
        ),
        when="fold/aggregate where the empty case must produce a sensible default.",
        days=(33, 116),
    ),
    Pattern(
        id="P-12",
        name="filter-then-map",
        description=(
            "Comprehension that filters first, then transforms. Reads "
            "as 'transformed item for each item in source if condition'. "
            "More efficient than map then filter when the predicate is "
            "cheap."
        ),
        canonical=(
            "evens_squared = [x * x for x in nums if x % 2 == 0]"
        ),
        when="building a derived list from a source under a constraint.",
        days=(32, 33, 35),
    ),
    Pattern(
        id="P-13",
        name="enumerate-for-index",
        description=(
            "Use enumerate() instead of `for i in range(len(seq))` + "
            "indexing. Eliminates a class of off-by-one bugs and "
            "preserves iteration's safety properties."
        ),
        canonical=(
            "for i, value in enumerate(items, start=1):\n"
            "    print(f'{i}. {value}')"
        ),
        when="needing both index and value in a loop body.",
        days=(14, 16, 32, 33),
    ),
    Pattern(
        id="P-14",
        name="zip-parallel-walk",
        description=(
            "Walk two (or more) sequences in lockstep. zip() stops at "
            "the shortest unless you reach for itertools.zip_longest. "
            "Tuple-unpack the loop variable for readability."
        ),
        canonical=(
            "for name, score in zip(names, scores):\n"
            "    record(name, score)"
        ),
        when="paired iteration where positions align.",
        days=(14, 32, 42),
    ),
    Pattern(
        id="P-15",
        name="unpacking-into-named",
        description=(
            "Tuple-unpack right-side values into named variables. "
            "Replaces a[0]/a[1] indexing with documented-by-name "
            "binding. Star-prefix collects the rest."
        ),
        canonical=(
            "first, second, *rest = lst\n"
            "(name, count), *_ = ranked.items()"
        ),
        when="when the positions are fixed and would otherwise be magic numbers.",
        days=(14, 42, 45),
    ),
    Pattern(
        id="P-16",
        name="yield-from-passthrough",
        description=(
            "Delegate one generator's output into another via "
            "`yield from`. Replaces a manual for+yield trampoline "
            "and forwards .send() / .throw() / return-value cleanly."
        ),
        canonical=(
            "def flatten(nested):\n"
            "    for chunk in nested:\n"
            "        yield from chunk"
        ),
        when="composing generators or recursing through a tree.",
        days=(34, 35, 88, 100),
    ),
    Pattern(
        id="P-17",
        name="closure-over-counter",
        description=(
            "Inner function captures and mutates an outer variable "
            "(via `nonlocal`) to maintain state without a class. "
            "The outer function returns the inner — that's the "
            "closure."
        ),
        canonical=(
            "def make_counter():\n"
            "    n = 0\n"
            "    def tick():\n"
            "        nonlocal n; n += 1; return n\n"
            "    return tick"
        ),
        when="needing per-instance mutable state but a class is overkill.",
        days=(25, 26),
    ),
    Pattern(
        id="P-18",
        name="decorator-as-wrapper",
        description=(
            "@decorator replaces a function with a wrapped version. "
            "Use for cross-cutting concerns: timing, caching, "
            "logging, retry, auth checks. functools.wraps preserves "
            "name/docstring."
        ),
        canonical=(
            "def timed(fn):\n"
            "    @functools.wraps(fn)\n"
            "    def wrapper(*a, **kw):\n"
            "        t0 = time.perf_counter(); r = fn(*a, **kw)\n"
            "        print(time.perf_counter() - t0); return r\n"
            "    return wrapper"
        ),
        when="adding behavior around many functions without rewriting them.",
        days=(27, 28, 72),
    ),
    Pattern(
        id="P-19",
        name="context-manager-protocol",
        description=(
            "`with` block calls __enter__ / __exit__ pairwise around "
            "a body. Guarantees teardown even on exception — the "
            "cleanest 'open then always close' idiom."
        ),
        canonical=(
            "with open(path) as f:\n"
            "    process(f.read())"
        ),
        when="acquire-then-release semantics: file, lock, transaction, mock.",
        days=(51, 52, 65),
    ),
    Pattern(
        id="P-20",
        name="dataclass-as-record",
        description=(
            "@dataclass turns a class into a record: __init__, __repr__, "
            "__eq__ generated. With frozen=True, you also get __hash__ "
            "and immutability — a value object."
        ),
        canonical=(
            "@dataclass(frozen=True)\n"
            "class Point:\n"
            "    x: float\n"
            "    y: float"
        ),
        when="data-shaped class with no behavior beyond construction.",
        days=(43, 44, 47),
    ),
    Pattern(
        id="P-21",
        name="protocol-as-interface",
        description=(
            "typing.Protocol declares a structural interface — any "
            "object with the matching methods passes the type check. "
            "Duck-typing made explicit and tooling-friendly."
        ),
        canonical=(
            "class Closeable(Protocol):\n"
            "    def close(self) -> None: ..."
        ),
        when="typing a parameter without forcing a concrete base class.",
        days=(45, 49),
    ),
    Pattern(
        id="P-22",
        name="cached-property",
        description=(
            "@functools.cached_property computes once on first access "
            "and stores the result on the instance. Cheaper than a "
            "@property when the computation is expensive and idempotent."
        ),
        canonical=(
            "class Repo:\n"
            "    @functools.cached_property\n"
            "    def commits(self) -> list[Commit]: ...  # parses git log once"
        ),
        when="derived attribute computed from immutable state.",
        days=(48,),
    ),
    Pattern(
        id="P-23",
        name="dispatch-by-type",
        description=(
            "functools.singledispatch picks an implementation by the "
            "first argument's type. Replaces if-isinstance chains with "
            "a registry. Each handler is added with @fn.register."
        ),
        canonical=(
            "@functools.singledispatch\n"
            "def render(x): ...\n"
            "@render.register\n"
            "def _(x: int): return str(x)"
        ),
        when="behavior depends on argument's runtime type.",
        days=(28, 49),
    ),
    Pattern(
        id="P-24",
        name="sentinel-default",
        description=(
            "Use a unique sentinel object as a default to distinguish "
            "'not provided' from 'explicitly None'. Avoids the "
            "mutable-default-argument trap."
        ),
        canonical=(
            "_MISSING = object()\n"
            "def fn(x=_MISSING):\n"
            "    if x is _MISSING: x = []  # fresh per call"
        ),
        when="default arg where None is a legitimate value the caller might pass.",
        days=(24,),
    ),
    Pattern(
        id="P-25",
        name="deque-rotating-buffer",
        description=(
            "collections.deque with maxlen= is a fixed-size FIFO ring. "
            "Append-overflow auto-evicts the oldest. O(1) on both ends."
        ),
        canonical=(
            "from collections import deque\n"
            "buf = deque(maxlen=100)\n"
            "for line in stream:\n"
            "    buf.append(line)  # last 100"
        ),
        when="last-N items, sliding history, bounded log.",
        days=(50, 82, 86),
    ),
    Pattern(
        id="P-26",
        name="bfs-from-source",
        description=(
            "Breadth-first traversal explores nodes layer by layer "
            "from a source. Queue + visited set. Finds shortest path "
            "in unweighted graphs."
        ),
        canonical=(
            "q = deque([(start, 0)]); seen = {start}\n"
            "while q:\n"
            "    node, dist = q.popleft()\n"
            "    for nb in neighbors(node):\n"
            "        if nb not in seen:\n"
            "            seen.add(nb); q.append((nb, dist + 1))"
        ),
        when="shortest-path / shortest-edge-count on unweighted graph.",
        days=(111, 121),
    ),
    Pattern(
        id="P-27",
        name="dfs-with-explicit-stack",
        description=(
            "Depth-first traversal with an explicit list-as-stack "
            "instead of recursion. Avoids stack-overflow on deep "
            "graphs and gives explicit control over visit order."
        ),
        canonical=(
            "stack = [start]; seen = {start}\n"
            "while stack:\n"
            "    node = stack.pop()\n"
            "    for nb in neighbors(node):\n"
            "        if nb not in seen:\n"
            "            seen.add(nb); stack.append(nb)"
        ),
        when="DFS where recursion depth is unsafe or order matters.",
        days=(110, 112, 113, 126),
    ),
    Pattern(
        id="P-28",
        name="memoize-recursive",
        description=(
            "@functools.lru_cache (or @cache) memoizes a recursive "
            "function so each subproblem is solved at most once. "
            "Top-down DP in one decorator."
        ),
        canonical=(
            "@functools.cache\n"
            "def fib(n):\n"
            "    return n if n < 2 else fib(n-1) + fib(n-2)"
        ),
        when="recursive function with overlapping subproblems.",
        days=(99, 100, 114, 115, 118),
    ),
    Pattern(
        id="P-29",
        name="binary-search-on-answer",
        description=(
            "Binary search over a *value* (not an index). Define a "
            "monotonic predicate is_feasible(x); search for the "
            "smallest x where is_feasible(x) flips True."
        ),
        canonical=(
            "lo, hi = 1, max_capacity\n"
            "while lo < hi:\n"
            "    mid = (lo + hi) // 2\n"
            "    if feasible(mid): hi = mid\n"
            "    else: lo = mid + 1\n"
            "return lo"
        ),
        when="optimization where the answer is bounded and monotone.",
        days=(103, 104),
    ),
    Pattern(
        id="P-30",
        name="ast-walker-visitor",
        description=(
            "ast.NodeVisitor subclass walks a parsed Python AST. Each "
            "visit_<NodeType> method handles one node kind. Combined "
            "with a scope stack, this is the spine of every linter and "
            "static analyzer."
        ),
        canonical=(
            "class FindDef(ast.NodeVisitor):\n"
            "    def visit_FunctionDef(self, node):\n"
            "        self.results.append(node.name)\n"
            "        self.generic_visit(node)"
        ),
        when="any 'analyze code as data' task — linters, refactor tools, codemods.",
        days=(126, 127, 128, 129, 130, 131, 132),
    ),
    Pattern(
        id="P-31",
        name="string-build-via-list-then-join",
        description=(
            "Append substrings to a list, then ''.join(...) once at "
            "the end. Avoids the O(n²) trap of repeated string += "
            "in a loop (each += copies the whole prefix)."
        ),
        canonical=(
            "parts = []\n"
            "for line in lines:\n"
            "    parts.append(transform(line))\n"
            "result = '\\n'.join(parts)"
        ),
        when="building a long string in a loop.",
        days=(8, 18, 35, 95),
    ),
)


def by_id(pattern_id: str) -> Pattern | None:
    """Look up a pattern by canonical ID (e.g. 'P-07'). Case-insensitive."""
    target = pattern_id.upper().strip()
    for p in PATTERNS:
        if p.id == target:
            return p
    return None
