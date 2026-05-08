---
day: day-062-systematic-debugging-mindset
phase: phase-3-quality-production
module: module-11-errors-eafp-debugging
style: story
---
# Day 62 — The bug that took six hours and the one that took six minutes

A friend tells you about her week. Monday, the order-processing
service started double-charging customers. She spent six hours on it.
Wednesday, a slightly worse bug — refunds going to the wrong account
— she fixed in six minutes.

What was different? Not the bugs. Her **process**.

## Monday — the desperate way

She read the code, formed a theory ("must be the retry loop"),
changed the retry loop, ran the tests, they passed, she shipped. The
bug came back at 3 PM. She formed another theory ("must be the
idempotency key"), changed *that*, shipped. Bug came back. Repeat for
six hours. The fix she finally landed at 9 PM was a one-line
correction in a function she'd skimmed past three times.

The pattern: **theorize, change, hope.** No measurement. No proof.
Just guesses, dressed up as engineering.

## Wednesday — the systematic way

Now the refunds bug. This time she runs five steps, in order:

1. **Reproduce reliably.** "Refund $5 with account A, money goes to
   account B" — repeatable in a test in 90 seconds. *Without a
   reliable repro, you cannot debug. You can only guess.*
2. **Bisect the surface.** Where is the wrongness first observable?
   She prints the destination account at three points: API entry,
   service layer, DB call. The wrong account appears at the service
   layer, not the API. The bug lives in *one* function.
3. **Form one falsifiable theory.** "The service layer overwrites
   `dest_account` from a stale variable in scope." She can prove or
   disprove this in one minute.
4. **Test the theory cheaply.** A `print(dest_account)` before and
   after the suspect line. Yep — it changes.
5. **Fix, then prove the fix.** Patch. Re-run the repro. Refund goes
   to A. Add a regression test that locks in the behavior forever.

Six minutes, including writing the test.

## The mindset, condensed

| Bad habit | Replacement |
|---|---|
| "I think it's the cache." | "Here's a print/log/assertion that proves where the wrongness starts." |
| Change three things at once. | Change one thing. Re-run. Observe. |
| Ship the fix, move on. | Add a test that fails before the fix, passes after. |
| "Works on my machine." | Reproduce *in* the environment, or add logging until you can. |
| Read code looking for bugs. | Run code looking for *evidence*. |

This isn't a personality trait. It's a checklist. The checklist is the
skill. The fastest debuggers you'll ever meet aren't smarter — they
just stop guessing earlier.

## The "binary search the diff" trick

If a bug appeared between two known-good and known-bad commits and you
have no theory, **don't read code**. Run `git bisect`. It cuts the
search space in half each step. A 200-commit window becomes ~8 builds.
Combined with a reliable repro (step 1), bisect finds bugs while
you're still forming your first theory.

## Now: open `02_fluency.py`

You'll add a regression test that locks in a fix.
