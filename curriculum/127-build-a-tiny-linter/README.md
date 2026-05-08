---
day: day-127-build-a-tiny-linter
phase: phase-6-packaging-ast-capstone
module: module-26-ast-and-static-analysis
style: story
---
# Day 127 — The shadow lint script

It's Tuesday morning. You're reviewing a teammate's PR and you spot it:
a function definition with `mutable_default=[]` as a parameter. You
leave a comment, link the docs, suggest `None` + `if x is None: x = []`
inside.

Forty minutes later, you spot the same bug in a different file. You
sigh. You leave the same comment.

That afternoon you read three more PRs. You catch the same bug twice
more. That's four times in one day.

This is exactly the kind of thing computers should do.

## You write a linter

Tonight, you sit down with the `ast` module from yesterday. You write
a function called `lint(source)` that returns a list of issues. Each
issue has a line number, a rule code, and a message:

```python
@dataclass
class Issue:
    line: int
    code: str
    message: str
```

The first rule, `M001` (you make up the code), is "mutable default
argument." You walk every `FunctionDef` and check `node.args.defaults`
for `List`, `Dict`, or `Set` literal nodes. Five lines of code:

```python
for fn in funcs:
    for default in fn.args.defaults:
        if isinstance(default, (ast.List, ast.Dict, ast.Set)):
            issues.append(Issue(default.lineno, "M001",
                f"mutable default in {fn.name}"))
```

You point it at your team's repo. It finds 11 instances. Six are real
bugs. The other five are "intentional but yikes." You open a single PR
that fixes all eleven.

## What just happened

You replaced a thing humans were doing badly (catching a known pattern
during code review) with a thing computers do perfectly (recognizing
a known pattern). The cost was forty minutes of your time *once*, and
the savings are forever.

This is the whole pitch for static analysis. It's not magic. It's a
small script that walks an AST and complains. **The hard part is
deciding which patterns are worth checking.** The implementation is
boring on purpose — that's a good thing.

## A second rule, just so you see two

`M002` — "function with too many parameters." Pick a threshold (six is
common). Walk `FunctionDef` nodes, check `len(node.args.args) +
len(node.args.posonlyargs) + len(node.args.kwonlyargs)`:

```python
total = (len(fn.args.args)
         + len(fn.args.posonlyargs)
         + len(fn.args.kwonlyargs))
if total > 6:
    issues.append(Issue(fn.lineno, "M002",
        f"{fn.name} has {total} parameters (limit: 6)"))
```

Two rules in. You could ship this.

## How real linters compose

`ruff`, `flake8`, `pylint` — they're all *thousands* of these tiny
checks. Each rule:

1. Listens for one or more node types.
2. Checks a condition.
3. Emits an issue with line/col + code + message.

That's the entire architectural pattern. The rest is a runner that
loads rules, parses files, walks once, dispatches each node to every
interested rule, and pretty-prints the issues.

## Today

You'll build a tiny linter with two rules and a dispatcher. By rung 5
it accepts a file path and prints `path:line: CODE message` lines —
the format every editor's "jump to next problem" hotkey already knows
how to parse.

## Now: open `fluency.py`
