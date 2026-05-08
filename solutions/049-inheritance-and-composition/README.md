---
day: 049-inheritance-and-composition
phase: phase-2-pythonic-tools
module: module-09-classes-dunders-context-managers
style: compare
---
# Day 49 — Same feature, two designs

You're modeling a logger that writes to a file. Read both designs, then
guess which one is easier to change next month.

```python
# A — inheritance
class FileWriter:
    def __init__(self, path):
        self.f = open(path, "a")
    def write(self, line):
        self.f.write(line + "\n")

class Logger(FileWriter):
    def info(self, msg):
        self.write(f"INFO: {msg}")
```

```python
# B — composition
class FileWriter:
    def __init__(self, path):
        self.f = open(path, "a")
    def write(self, line):
        self.f.write(line + "\n")

class Logger:
    def __init__(self, writer):
        self.writer = writer
    def info(self, msg):
        self.writer.write(f"INFO: {msg}")
```

Both work. Then someone says: "Can the logger also write to stdout in
tests, and to a Slack webhook in production?"

In design A, you'd refactor `Logger` to stop inheriting from
`FileWriter`, plus update every place that constructed a `Logger`. In
design B, you swap in a different writer:

```python
log = Logger(StdoutWriter())
log = Logger(FileWriter("/var/log/app.log"))
log = Logger(SlackWriter(webhook_url))
```

`Logger`'s code didn't change. You just gave it a different collaborator.
This is **composition over inheritance**, and most modern Python style
guides put it as the default.

## When inheritance still earns its keep

Inheritance is the right tool when:

- You're modeling a true "is-a" — `class AdminUser(User)`. Admins
  really *are* users with extra powers.
- You're writing a base class that defines a small protocol and child
  classes fill in two or three methods. (Phase 4 will use this pattern
  for trees and graphs.)
- You're plugging into a framework that mandates inheritance:
  `class MyView(View)` in Django, `class MyTest(unittest.TestCase)`.

## When composition wins

Almost everything else. Especially:

- "X has-a Y" relationships — a Logger has-a writer, a Cart has-a
  customer, a Game has-a Board.
- When the relationship between two pieces will change.
- When you want to swap implementations for testing (mock the
  collaborator, don't subclass it).

## `super()` and the diamond

If you do inherit, `super()` is how you call the parent's method:

```python
class B(A):
    def __init__(self, x):
        super().__init__(x)   # calls A.__init__
        self.b_extra = "..."
```

For single inheritance you'll use `super()` ~all the time and never
think about it twice. Multiple inheritance brings in the **MRO**
(method resolution order, the rules Python uses to pick which parent
runs `super()`'s call). Multiple inheritance in app code is rarely
worth the headache; mixins and Protocols handle most of what people
reach for it for.

## Rule of thumb for the rest of this module

Reach for composition first. If you find yourself making three or
four nearly-identical small classes that each redefine the same one
method, *that's* when inheritance might shorten things — not before.

## Now: open `fluency.py`

A small `Logger` written with inheritance. Refactor it to composition.
