---
day: day-068-refactoring-katas
phase: phase-3-quality-production
module: module-13-reading-refactoring-style
style: pain
---
# Day 68 — The 80-line function nobody wants to touch

You inherited this:

```python
def process_order(order):
    if order["country"] == "US":
        if order["state"] in ("CA", "NY", "WA"):
            tax = order["total"] * 0.08
        else:
            tax = order["total"] * 0.05
    elif order["country"] in ("DE", "FR", "IT", "ES"):
        tax = order["total"] * 0.20
    elif order["country"] == "UK":
        tax = order["total"] * 0.20
    else:
        tax = 0
    if order["customer_type"] == "vip":
        discount = order["total"] * 0.15
    elif order["customer_type"] == "regular" and order["total"] > 100:
        discount = order["total"] * 0.05
    else:
        discount = 0
    final = order["total"] + tax - discount
    if final < 0:
        final = 0
    if order["currency"] == "EUR":
        final = final * 1.08
    elif order["currency"] == "GBP":
        final = final * 1.25
    return round(final, 2)
```

Three weeks later, finance asks: "what's the tax for Quebec?" You
read the function. You can't *find* the tax logic — it's tangled with
discount logic and currency conversion. **A function this dense is a
function whose bugs you'll never find.**

## What refactoring is (and isn't)

Refactoring is **changing structure without changing behavior**. The
tests pass before and after. The function takes the same inputs and
returns the same outputs. You haven't shipped a new feature. You've
made the next feature safe.

The trap: people use "refactor" to mean "rewrite from scratch and
hope." That's not refactoring — that's a high-risk replacement. Real
refactoring is small, mechanical, reversible steps with tests after
each one.

## Three moves that fix 80% of bad functions

### 1. Extract function

When a chunk of a function does ONE thing, lift it out:

```python
def tax_for(order):
    if order["country"] == "US":
        return order["total"] * (0.08 if order["state"] in ("CA","NY","WA") else 0.05)
    if order["country"] in ("DE", "FR", "IT", "ES", "UK"):
        return order["total"] * 0.20
    return 0
```

Now `process_order` calls `tax_for(order)`. The tax logic has a name,
a place, and its own little testable home.

### 2. Replace conditional with a table

Long `if/elif` chains over fixed values are usually a dict in disguise:

```python
CURRENCY_RATES = {"USD": 1.0, "EUR": 1.08, "GBP": 1.25}
final *= CURRENCY_RATES.get(order["currency"], 1.0)
```

Adding a new currency is now editing data, not code. That's the win.

### 3. Replace primitive with a guard

A `if final < 0: final = 0` line is a clamp. Use the `clamp(value, 0,
math.inf)` from Day 64, or extract a `_floor_at_zero(x)` helper. Names
beat magic numbers.

## The mechanic, not the muse

Refactor in small, testable steps:

1. Run tests. Green.
2. Make ONE change (rename, extract one block).
3. Run tests. Still green?
4. If yes, repeat. If no, undo and try smaller.

You don't need a refactoring epiphany. You need the tests to be the
seatbelt. **Without tests, you're not refactoring — you're hoping.**

## Now: open `fluency.py`

A small but tangled function. Apply *extract function* once. The
behavior tests must keep passing.
