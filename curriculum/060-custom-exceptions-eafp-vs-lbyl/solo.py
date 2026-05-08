"""Rung 4: Solo implement.

Topic: custom exception hierarchy + EAFP.

You're modeling a tiny library checkout system. Build:

  - LibraryError(Exception)  — base
  - BookNotFound(LibraryError)  — message "book not found: <isbn>", attr `isbn`
  - AlreadyCheckedOut(LibraryError)  — message "already checked out: <isbn>",
                                       attrs `isbn` and `borrower`

Then implement:

    def checkout(catalog: dict, isbn: str, by: str) -> dict

  - `catalog` maps isbn -> {"title": str, "borrower": str | None}.
  - On success: set borrower to `by`, return the updated record.
  - Missing isbn -> raise BookNotFound.
  - Already borrowed (borrower not None) -> raise AlreadyCheckedOut.

Use EAFP. Hidden tests in 04_solo_test.py.

Patterns: P-04 (dispatch-by-dict), P-05 (eafp-try-then-fallback).
"""


class LibraryError(Exception):
    pass


class BookNotFound(LibraryError):
    def __init__(self, isbn: str) -> None:
        raise NotImplementedError


class AlreadyCheckedOut(LibraryError):
    def __init__(self, isbn: str, borrower: str) -> None:
        raise NotImplementedError


def checkout(catalog: dict, isbn: str, by: str) -> dict:
    raise NotImplementedError
