---
day: 011-string-parsing-patterns
phase: phase-1-python-core
module: module-02-strings-deep
style: story
---
# Day 11 — A vendor sends you a CSV with `;` in it

Friday afternoon. A new vendor emails you a "CSV" of contacts:

```text
Smith;John;john.s@acme.com;+1 (415) 555-1212
O'Hara;Aoife ;aoife@example.io ;415.555.0144
de la Cruz;María;maria@vox.es;
```

The fields are semicolon-separated. Some have leading/trailing spaces.
Some are missing. Phone numbers are all over the place. The vendor will
"clean it up next week" but you need to load it *now*.

You don't reach for regex. You don't reach for pandas. You reach for
the parsing pattern you've been building all week:

```python
def parse_contact(line: str) -> dict[str, str]:
    parts = [p.strip() for p in line.split(";")]
    last, first, email, phone = (parts + [""] * 4)[:4]
    digits = "".join(c for c in phone if c.isdigit())
    return {
        "name":  f"{first} {last}".strip(),
        "email": email.lower(),
        "phone": digits,
    }
```

Read it as four steps — that's the **parse-and-shape** pattern.

## Step 1: Split on a known separator

`line.split(";")` returns a list. We don't know how many fields the
vendor will actually send (some lines were 4, what if the next batch
is 5?), so we always *expect a list*, not a fixed tuple.

## Step 2: Strip every part

The list comprehension `[p.strip() for p in parts]` is your daily
parser bread. It runs the strip on each item and gives you back a
list. Without it, `" john " ` slips through with leading whitespace.

## Step 3: Pad and unpack

`(parts + [""] * 4)[:4]` is a tiny idiom to **safely unpack 4 values**
even if some are missing. It says: "tack 4 empty strings on the end,
then take the first 4." Now `last, first, email, phone =` never raises.

## Step 4: Sanitize each field

The phone-number line, `"".join(c for c in phone if c.isdigit())`,
keeps only digits. That's the **filter-and-rejoin** pattern: walk a
string, keep what you want, glue it back. It's the whole answer to
"normalize this messy string."

## When to reach for what

| Tool | Use it when |
|---|---|
| `.split(sep)` | The separator is consistent and unambiguous |
| `csv` module | The data is real CSV with quotes/escapes |
| `re.findall` | You're extracting *something inside* free text |
| filter-and-rejoin | You want to keep/drop chars by predicate |
| `str.replace` | Single fixed substitution, no patterns |

The big lesson: **most "parsing" is not regex**. It's split, strip,
pad, and a tiny filter. Reach for regex only when the structure is
genuinely irregular.

## Now: open `fluency.py`

Three small parsers are wrong in ways the tests will pinpoint. Fix
each by composing the patterns above.
