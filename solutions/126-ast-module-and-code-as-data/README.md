---
day: day-126-ast-module-and-code-as-data
phase: phase-6-packaging-ast-capstone
module: module-26-ast-and-static-analysis
style: build-it
---
# Day 126 — Build a tree-walker yourself

Pretend Python doesn't have static analysis. You want to count how
many functions a file defines without importing it (because importing
runs side effects). How would you do it?

You could grep for `def `. That works until someone writes
`my_def_thing = ...` or has `def` inside a string. Strings always
break grep.

The right answer is to **parse** the code into a tree and walk the
tree. That's what every linter, formatter, type checker, and codemod
tool you've ever used does. Python ships the parser as `ast`.

## Code is data

```python
import ast

source = "x = 1 + 2"
tree = ast.parse(source)
print(ast.dump(tree, indent=2))
```

Output:

```text
Module(
  body=[
    Assign(
      targets=[Name(id='x', ctx=Store())],
      value=BinOp(left=Constant(value=1), op=Add(), right=Constant(value=2)))],
  type_ignores=[])
```

Every node is an object. Every object has children in well-named
attributes (`body`, `targets`, `value`, `left`, `right`). The shape is
documented in the [`ast` module docs](https://docs.python.org/3/library/ast.html)
and you can ask any node for its `_fields` at runtime.

## Two ways to walk the tree

**`ast.walk(tree)`** — yields every node, depth-first, no order
guarantee on siblings. Great for "find all the X in this file":

```python
funcs = [n for n in ast.walk(tree) if isinstance(n, ast.FunctionDef)]
```

**`ast.NodeVisitor`** — a class you subclass. Define `visit_X` for
each node type `X` you care about. The visitor recurses into children
automatically (call `self.generic_visit(node)` to keep going):

```python
class FunctionCounter(ast.NodeVisitor):
    def __init__(self):
        self.count = 0
    def visit_FunctionDef(self, node):
        self.count += 1
        self.generic_visit(node)  # also count nested functions
```

Use `walk` for one-off scans. Use `NodeVisitor` when the logic gets
state-y or you want different behavior per node type.

## What you can NOT do with `ast`

The AST has structure but no values from runtime — you can't tell
what `x` will *be* when the code runs. You only see the *shape*:
"there's a function named `add` with two parameters." That's still a
lot. It's enough to write linters, complexity analyzers, dead-code
detectors, and import sorters.

For "what type is `x` at runtime?" you want a type checker (mypy),
which does its own deeper analysis on top of the AST.

## Two AST gotchas

1. **Nodes are not strings.** `node.name` (on `FunctionDef`) is a
   string. `node.value` (on `Assign`) is *another node*. Mixing the
   two is the most common ast bug.
2. **Line numbers exist.** Every node has `node.lineno` and
   `node.col_offset`. This is how linters point to "line 42, column 8."
   You'll use these tomorrow.

## Today's drill

You'll build helpers that count things in source code: function
definitions, top-level imports, longest-named variable assigned to.
Tomorrow you'll wire them into a real linter.

## Now: open `fluency.py`
