---
day: day-046-type-hints-deep-literal-typeddict-annotated
phase: phase-2-pythonic-tools
module: module-08-tuples-dataclasses-types-deep
style: tour
---
# Day 46 — A code tour of `Literal`, `TypedDict`, `Annotated`

Three more pieces of the typing toolkit. Each one earns its keep in
real code. Read the snippet, then we walk it.

```python
from typing import Annotated, Literal, TypedDict

Mode = Literal["read", "write", "append"]

class UserDict(TypedDict):
    id: int
    name: str
    email: str

PortNumber = Annotated[int, "1..65535"]

def open_user(mode: Mode, user: UserDict, port: PortNumber) -> None:
    print(f"opening {user['name']} ({mode}) on port {port}")
```

## `Literal[...]` — when a string really IS one of three things

Lots of APIs take strings that are secretly enums: `mode="read"`,
`level="info"`, `direction="asc"`. Without `Literal`, the type is
just `str` and a typo (`mode="raed"`) sneaks past.

```python
Mode = Literal["read", "write", "append"]

def open(mode: Mode) -> None: ...

open("read")    # ok
open("raed")    # type checker: error
```

`Literal` is a *type* whose only valid values are the listed constants.
It works for strings, ints, bools, and bytes. It's the cheapest, most
useful step up from `: str`.

## `TypedDict` — a dict whose keys you actually know

You're parsing JSON. The result is a `dict`, but you and the future
reader both know it has specific keys. Type it.

```python
class UserDict(TypedDict):
    id: int
    name: str
    email: str

def email_of(u: UserDict) -> str:
    return u["email"]      # type checker knows this is str
```

A `TypedDict` is still a plain `dict` at runtime — it's just a typing
declaration. Use it when:

- You're modeling JSON or external data that arrives as a dict.
- You can't migrate to a dataclass (third-party API, etc.).
- You need fields that look up by `obj["key"]` because the rest of the
  codebase already does.

If the data is yours and freshly constructed, prefer a `@dataclass` —
it's friendlier (`u.email` over `u["email"]`).

You can mark optional keys with `total=False` or per-key with
`NotRequired`:

```python
class UserDict(TypedDict):
    id: int
    name: str
    email: NotRequired[str]   # may be missing
```

## `Annotated[T, ...]` — extra metadata on a type

`Annotated` is a wrapper. The first argument is the real type. Any
extra arguments are metadata — strings, dataclasses, validator
objects, whatever you (or a library) want.

```python
from typing import Annotated

PortNumber = Annotated[int, "must be 1..65535"]
```

To Python and most type checkers, `PortNumber` is `int` — nothing
changes about runtime behavior. The metadata is for tools that
*do* read it: FastAPI uses it to declare query parameters; Pydantic
uses it for validators; mypy plugins read it for stricter rules.

You don't need `Annotated` every day. When you see it in someone
else's code, now you know — it's "this type, plus some bonus info
the framework will read."

## When to reach for which

- **Literal** — a parameter that's one of a small fixed set of constants.
- **TypedDict** — modeling a JSON-ish dict you can't dataclass-ify.
- **Annotated** — passing extra info to a framework that knows about it.

## Now: open `fluency.py`

A function takes `mode: str` and a `dict`. Tighten the types.
