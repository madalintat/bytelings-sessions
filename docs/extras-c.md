# Approach C — extras for the world-class teach-via-exercises product

This document is the **roadmap for the eight high-leverage moves** that
push bytelings from "best Python curriculum for aspiring SWEs" (the
shipped 0.4.0 product) to "world's best teach-via-exercises product,
period."

Each move below has: where it came from, the concrete implementation
sketch, the touched files, and an honest effort estimate. None of
these is shipped in 0.4.0. They are intentionally deferred as
content-authoring work that benefits from dedicated focus per move,
not parallel batching.

## C-1. Persistent dataset across Days 30-90

**Source:** Charles Severance, *Python for Everybody*. He threads
`mbox.txt` from chapter 6 (strings) through chapter 14 (databases),
so each new construct lands as "here is what we couldn't do last
chapter on the same data."

**Why:** every `apply.py` rung today operates on a disposable toy
input. A learner who finishes Day 18 has built a word counter; a
learner who finishes Day 35 has built a lazy generator pipeline. In
the current product they never see those touch the same artifact.
With a persistent dataset, Day 18 reads `orders.csv`, Day 35 yields
order events lazily, Day 65 mocks the time-of-day field, Day 95
hashes the customer id. Compounding motivation.

**The dataset:** a fictional small consultancy's `orders.csv`. ~5000
rows, ~60 KB. Columns: `order_id, customer, line_items, total,
status, created_at, shipped_at, refunded_at`. Hand-curated to contain
the patterns each day exercises:

| Day | What the dataset enables |
|---|---|
| 18 | aggregate by customer (P-07 accumulator-into-dict) |
| 19 | customer set diff between Q1 and Q2 |
| 20 | `Counter` of statuses |
| 33 | generator pipeline filtering refunded orders |
| 35 | lazy `pairwise` over chronological events |
| 50 | RingBuffer of last-100 orders |
| 53 | open the CSV with pathlib + csv |
| 54 | round-trip JSON / CSV / TOML representations |
| 60 | EAFP vs LBYL on missing optional fields |
| 65 | monkeypatch `datetime.now()` for time-window queries |
| 72 | profile aggregation hot-spots |
| 95 | hash quality on customer-id distribution |

**Files:**
- `curriculum/_data/orders.csv` — the canonical dataset. Bundled in
  the wheel via `pyproject.toml`'s force-include.
- `curriculum/_data/README.md` — describes the schema, the
  pedagogical thread, and how new days pick fields.
- Updates to ~30 day READMEs to reference the dataset and update
  the day's apply rung to read from it.
- `bytelings.testing` gains `load_dataset() -> list[dict]` so test
  files don't reimplement CSV parsing.

**Effort:** ~3 weeks of content authoring. The dataset itself is
~1 day of design + curation. Each day's rewrite is 30-60 min.

**Why deferred:** changing apply rungs in batch breaks the M4
audit-cited rewrites (Days 5/15/35/50/65/70 already exercise the
day's NEW concept in fresh contexts; the dataset version would
recontextualize them again). Worth doing, but in a single focused
content sprint with a clear "before this PR, M4 apply rungs work;
after, they all read from orders.csv."

## C-2. Spiral problems revisited at Days 10/40/90

**Source:** MIT 6.0001 (John Guttag). One problem (Newton's method,
hangman, Fibonacci) recurs at three increasing levels of mastery.

**Why:** the curriculum currently treats each day as isolated. A
spiral problem turns Days 10/40/90 into a meta-arc the learner
notices: "I've seen this before; I write it differently now."

**The four spiral problems:**

| Problem | Day 10 | Day 40 | Day 90 |
|---|---|---|---|
| Word frequency counter | naive list traversal, O(n²) | dict accumulator, O(n) | ranked top-K via heap, O(n log k) |
| Fibonacci | recursive, exponential | memoized, O(n) | matrix exponentiation, O(log n) |
| Path through grid | hardcoded test paths | DP table, O(rc) | A* with priority queue, optimal |
| Anagram detector | sort-and-compare | Counter | character-frequency tuple hash |

Each spiral introduces ONE new technique while preserving the
problem statement. The learner's three solutions live together in
their working folder and they can `diff` them.

**Files:**
- `curriculum/010-regex-essentials/spiral.py` (and matching `_test.py`)
- `curriculum/040-real-world-async-with-httpx/spiral.py`
- `curriculum/090-bst-delete-and-balance/spiral.py`
- The spiral file is rung 6 (after apply). It's optional: the watcher
  shows it as `→ 6  Spiral (revisit)` if `spiral.py` exists. Skips
  silently otherwise.
- `bytelings/locator.py:_RUNG_SPECS` extended with rung 6.
- `bytelings/watcher.py:on_save` handles missing rung-6 files
  gracefully (already does for missing apply_test.py).

**Effort:** ~1 week of content authoring. The four spirals require
careful problem selection so each level genuinely teaches something
new. Spiral choice is the hard part; implementation is mechanical.

**Why deferred:** rung-6 is a structural change. It interacts with
the Pattern Catalog (a spiral could be tagged with multiple patterns
across its three rungs). Worth doing as its own dedicated milestone.

## C-3. Environment-diagram drawing rungs

**Source:** Berkeley CS61A (John DeNero), *Composing Programs*.
Every introductory lesson asks the student to draw the call stack
and namespace bindings BY HAND before running code.

**Why:** Python beginners often run code without a model of what's
happening. They debug by trial and error because they don't know
where to *look*. Forcing them to draw the diagram first (frame
boxes, name-to-value arrows, parent-frame pointers) builds the
mental model.

**The implementation:**
- New `curriculum/<slug>/trace.md` artifact per day where applicable
  (~30 days: scope/closure days, recursion days, mutability days,
  generator state days).
- `trace.md` shows code with line numbers. Below, a sequence of
  "what does the call stack look like RIGHT BEFORE line N
  executes" snapshots, but with blanks for the learner to fill.
- The watcher gets a new key `t` (trace) that opens `trace.md` in
  the pager. Learner writes in their own diagram (paper, iPad,
  whatever), then presses `enter` to reveal the answer panels.

**Files:**
- `bytelings/watcher.py`: add `t` key handler that pages `trace.md`
  with reveal interactions (blocks of `<details>` shown one at a
  time on keypress).
- `curriculum/<slug>/trace.md` for the relevant days.
- `bytelings/locator.py`: add `trace_file: Path | None` to `Day`.

**Effort:** ~2 weeks. Pure content; the runtime is small.

**Why deferred:** the trace.md authoring is hand-art per day.
Quality matters more than quantity here; rushing produces
unhelpful diagrams.

## C-4. Felt-problem 2-sentence opener every day

**Source:** CS50 (David Malan). Every lecture opens with a problem
the student *feels*: a phone book they have to look up someone in,
a misbehaving program they have to debug, a sorted vs unsorted
deck of cards.

**Why:** "Pretend Python doesn't have this. How would you build it?"
is bytelings' Karpathy move. The CS50 move is tighter: "What is
the problem you'd encounter where this concept would save your
day?" Two sentences max, before any code.

**The implementation:** every README's first prose paragraph
(currently varies in shape: some do this, most don't) gets a
**Felt:** prefix that is exactly two sentences. The prose below it
can do whatever the day's style chose.

**Authoring discipline:**

```markdown
**Felt:** It's 2 AM. The deploy keeps failing because the same
config key is parsed differently in two places.
```

That replaces the current openers across ~135 days. Each one is a
~5-minute rewrite per day.

**Effort:** ~1 week. Pure content-authoring; tooling-free.

**Why deferred:** boring grunt work; benefits from a single focused
afternoon, not interspersing with other work.

## C-5. Pre-mortem "common bugs" section every day

**Source:** Allen Downey, *Think Python*. Every chapter has a
"Debugging" appendix listing the 3-5 mistakes a learner is most
likely to hit. Pre-mortem, not post-mortem.

**Why:** when the test fails and the learner is stuck, having a list
of "you probably did one of these five things" turns a frustrating
30 minutes into a 2-minute checklist.

**The implementation:** every README gets a `## Common bugs you'll
hit` section (3-5 bullets). Each bullet states the mistake and a
one-line how-to-spot-it.

**Authoring discipline:** these emerge naturally from the Day's
diagnose helper. Whatever wrong-answer messages live in
`fluency_test.py`'s `diagnose(...)` calls — mirror them up into the
README as the pre-mortem checklist.

**Effort:** ~1 week. Mostly mechanical lift from the test files.

**Why deferred:** depends on having all the diagnose tests written
first. Days 6-135 of solved/ + the test files come first.

## C-6. LLM-as-mentor sixth pass on idiom

**Source:** exercism.io's mentoring model. After your code passes
the tests, a human (or an LLM) reviews it for *idiom*: did you reach
for the most Pythonic shape, or just one that works?

**Why:** the curriculum graduates students who write CORRECT code.
This pass would graduate them writing IDIOMATIC code — the
difference between a 2-year-experience Python dev and a 5-year one.

**The implementation:**
- A new `bytelings critique <day> --rung N` subcommand. Runs the
  learner's `<rung>.py` through an LLM with a prompt template:
  "Compare against the canonical solved/<day>/<rung>.py. List up to
  3 idiom upgrades the learner could make. Be specific. Don't suggest
  changes that don't materially improve readability or performance."
- API: pluggable provider behind a thin interface so any chat-completion
  service works. User supplies their own API key via env var.
- Caches per-rung critiques so re-runs on unchanged code don't
  re-call the API.

**Files:**
- `bytelings/critique.py` (new)
- `bytelings/cli.py`: register `critique` subcommand
- `pyproject.toml`: optional dep on `anthropic` SDK behind a
  `[project.optional-dependencies] critique = ["anthropic>=..."]`
  group; user installs with `uv tool install bytelings[critique]`.
- Tests: mock the API call in CI.

**Effort:** ~1 week of engineering + provider design. Content-free.

**Why deferred:** the only Approach C move that is engineering, not
content. It's tractable but adds a runtime dependency and a paid-API
story that needs careful UX design ("how does a learner without an
API key still get value?").

## C-7. Explicit named "reinvention days" per phase

**Source:** Andrej Karpathy, *Neural Networks: Zero to Hero*. The
core teaching move is "build the thing from scratch in a notebook,
then realize you've reinvented PyTorch."

**Why:** bytelings already does this 9 times across the curriculum
(Days 10/21/45/50/80/92/103/125/126). It's the signature move. Today
it's implicit. Making it explicit, named, and per-phase gives
learners a recognition handle.

**The implementation:**
- Each phase ends with one explicit `Reinvention day` marker. The
  9 days above get a `style: reinvention` frontmatter tag.
- `bytelings list` shows reinvention days with a 🔨 marker.
- `bytelings reinventions` is a new subcommand that lists them with
  one-line summaries: "Day 10 — regex from scratch (state machine).
  Day 21 — dict from a list of buckets. ..."

**Files:**
- `bytelings/cli.py`: `reinventions` subcommand, ~30 lines
- 9 README frontmatter updates
- `bytelings/locator.py`: parse `style:` field from frontmatter

**Effort:** ~2 days. Pure tooling + light frontmatter touch.

**Why deferred:** small but it touches a CLI command surface and
the README frontmatter parser. Worth doing as a self-contained PR.

## C-8. Public web Pattern Catalog

**Source:** the existing CLI Pattern Catalog (M5) is great for
learners mid-curriculum, but not for someone googling "what's a
sliding window pattern" who hasn't installed bytelings. A web
artifact extends bytelings' reach beyond installed users.

**Why:** the Pattern Catalog is the highest-leverage piece of the
curriculum. Putting it on the web, indexed by search engines, brings
people to the curriculum. It also turns into a reference URL the
community can share ("see bytelings P-07 for accumulator-into-dict").

**The implementation:**
- Generate a static HTML site from `bytelings/patterns.py` via a
  small `scripts/build_pattern_site.py`. Each pattern gets its own
  page with the canonical example, "when to reach for it", and the
  list of days that exercise it.
- Host on GitHub Pages from the same repo.
- Cross-link to the bytelings PyPI page (for installation) and to
  the curriculum on GitHub (for the actual exercises).
- New GitHub Actions workflow `pages.yml` builds and deploys on
  push to main when `bytelings/patterns.py` changes.

**Files:**
- `scripts/build_pattern_site.py`
- `web/templates/` (HTML + CSS, intentionally minimal)
- `.github/workflows/pages.yml`
- `web/index.html`, `web/<pattern-id>.html` (generated)

**Effort:** ~3 days of engineering + design.

**Why deferred:** scope creep beyond the curriculum-runner's
mission. Worth doing once the curriculum is fully content-complete
(Days 6-135 of solved/, all rung rewrites done) so the catalog has
real day-references to link to.

## Sequencing recommendation

If a future contributor (or future me) asks "which one first?" the
right order is:

1. **C-7** (reinvention days) — smallest, immediate
   recognition-vocabulary boost, no content debt.
2. **C-4** (felt-problem opener) — purely content, drop-in to every
   README.
3. **C-5** (pre-mortem common bugs) — content; depends on C-4 being
   in place so the section sits in a stable spot.
4. **C-6** (LLM mentor critique) — engineering work; can run in
   parallel with content work above.
5. **C-1** (persistent dataset) — major content rewrite; needs
   focused 3-week sprint.
6. **C-2** (spiral problems) — structural change to rung shape;
   should land after dataset so spirals can use it.
7. **C-3** (environment diagrams) — heaviest content; pure quality
   move.
8. **C-8** (web pattern catalog) — last, when the catalog has all
   135 days' tags landed.

## What success looks like

A learner who finishes 135 days, having done all C extras, has:

- An installed CLI tool they shipped to PyPI
- A published GitHub Pages site for their own pattern catalog
- An `orders.csv` working folder that's been the protagonist of
  60 days of exercises
- Three solutions to the same spiral problem at three skill levels
- Trace diagrams of their own recursion stacks
- Idiom critiques from an LLM mentor on their solo solutions
- An explicit list of nine "reinvent before you import" wins

That graduate isn't a Python hobbyist. They're a software engineer
who shipped a real tool and has the receipts.
