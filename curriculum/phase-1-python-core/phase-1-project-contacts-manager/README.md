# Phase 1 Project — Contacts Manager CLI

A 3-day project that consolidates Phase 1: strings, lists, dicts,
sets, functions, decorators, type hints, and a tiny grasp of Big-O.

## The Scenario

You've been hired by a small consultancy. They've kept their client
contact list in a series of CSV files exported from various tools
over the years — vendors, ex-employees, lead trackers. The files are
inconsistent. Some have semicolons, some have commas, some are
double-quoted. Names are in different orders. Phone numbers are
random shapes. Emails sometimes have stray uppercase.

Your job: build a **single command-line tool**, `contacts`, that:

1. Loads any of those CSVs into a clean in-memory roster.
2. Lets the user search by name, email, phone, or regex.
3. Detects duplicates (fuzzy match by name + same phone digits).
4. Exports a normalized CSV.

Everything is local — no database, no web server. One Python file to
start (Day 1), grown into a small package by Day 3, with a real test
suite and a clean CLI.

## Requirements (functional)

- [ ] **Load**: read a CSV with columns `name, email, phone` (commas
  OR semicolons; auto-detect).
- [ ] **Normalize on load**: trim whitespace, lowercase emails, reduce
  phone numbers to digits.
- [ ] **Search by exact field**: `contacts find --email alice@x.io`.
- [ ] **Search by regex**: `contacts find --regex "^al"`.
- [ ] **List all** (sorted by name): `contacts list`.
- [ ] **Detect dupes**: `contacts dupes` — group by (lowercased
  full-name initial-letters, phone digits) and show groups of size > 1.
- [ ] **Export normalized**: `contacts export out.csv`.
- [ ] **Help**: `contacts --help` lists subcommands and options.

## Concepts checklist (mapping to Phase 1 modules)

- **Module 1** (setup): `uv` env, pytest, type hints on every public
  function.
- **Module 2** (strings): split/strip parsing, regex search, the
  filter-and-rejoin idiom for phone digits.
- **Module 3** (lists + Big-O): linear scan vs. dict index — choose
  consciously and write a one-line note in the design doc explaining
  each choice.
- **Module 4** (dicts/sets): indices for O(1) lookups by email/phone;
  set arithmetic for "contacts in A but not B."
- **Module 5** (functions/decorators): a `@timed` decorator on the
  search command for the rubric's "perf-aware" check.

## Day-by-day plan

### Day 1 — Design + scaffold
- Sketch a `Contact` shape and the `Roster` class that owns
  `list[Contact]` plus two indices (by email, by phone).
- Build the project skeleton: `app.py` with stub functions, the CSV
  loader returning normalized contacts, and a basic CLI parser
  (using argv directly — no Click yet).
- Get **`contacts list <file.csv>`** working end-to-end.

### Day 2 — Build core
- Add `find` (exact + regex), `dupes`, `export`.
- Apply the `@timed` decorator to the search path.
- Hand-roll the dupe key (name initials + phone digits) and the
  grouping using `defaultdict(list)`.

### Day 3 — Test + ship
- Write pytest covering: loader, normalize, find, dupes, export,
  round-trip.
- Add error handling: missing file, malformed CSV, empty input.
- Polish the CLI: a friendly `--help`, exit codes, a tiny banner.
- Self-eval against the rubric below.

## Graduated hints

<details><summary>Hint 1 — How should I structure the data?</summary>

A `Contact` is best as a `dict[str, str]` for now (we haven't covered
dataclasses yet — that's Phase 2). The `Roster` is a class that wraps
`list[Contact]` plus `dict[str, Contact]` indices.

```python
class Roster:
    def __init__(self, contacts: list[dict]) -> None:
        self.contacts = contacts
        self.by_email = {c["email"]: c for c in contacts if c["email"]}
        self.by_phone_digits = {c["phone"]: c for c in contacts if c["phone"]}
```
</details>

<details><summary>Hint 2 — How do I auto-detect comma vs. semicolon?</summary>

Read the first line. If it has more `;` than `,`, treat `;` as the
separator. Otherwise `,`. Don't reach for `csv.Sniffer` until you've
hit a real edge case it solves.
</details>

<details><summary>Hint 3 — How do I detect duplicates?</summary>

Build a dupe key per contact: `(name_initials, phone_digits)`. Group
all contacts by that key (`defaultdict(list)`). Any group with > 1
contact is a duplicate cluster.

```python
def dupe_key(c: dict) -> tuple[str, str]:
    initials = "".join(p[:1] for p in c["name"].lower().split())
    return (initials, c["phone"])
```
</details>

<details><summary>Hint 4 — Where does the @timed decorator go?</summary>

Wrap the `find` and `dupes` functions, not the `load`. The point is
to demonstrate that you instrumented the *search path* — the part
users perceive as "fast" or "slow." Print the elapsed time to stderr
so it doesn't pollute the search results going to stdout.
</details>

<details><summary>Hint 5 — What should the regex search match against?</summary>

Match against `name` first, then `email`. Don't match phone numbers
with regex — phones are already normalized to digits, so `find --phone 4155551212` is just exact.
</details>

## Stretch goals

- Add `contacts add NAME EMAIL PHONE` (in-memory; persists with
  `--save`).
- Add a `--csv` output option to `find` and `dupes` so they pipe into
  other tools.
- Use `Counter.most_common` to show the most-shared area code in
  `contacts stats`.
- Write a property test: round-trip `load → export → load` is the
  identity (after normalization) for any randomly generated roster.

## Self-evaluation rubric

Run through these *before* you mark the project complete:

- [ ] **Correctness**: every command works on the sample data with no
  Python tracebacks.
- [ ] **Tests**: at least 8 test functions; all green; cover the
  loader, normalize, find, dupes, and export.
- [ ] **Type hints**: every public function has hints; mypy in
  default mode finds nothing.
- [ ] **Big-O reasoning**: in `app.py`'s docstring header, you wrote
  one paragraph identifying the slowest path and explaining why it
  *is or isn't* fast enough.
- [ ] **CLI feel**: `--help` is readable; bad usage exits with code 2
  and a useful message.
- [ ] **Reuse from Phase 1**: at least one decorator, at least one
  dict-comprehension index, at least one regex, at least one set
  operation.

If all six boxes are checked, you've shipped Phase 1's project.
