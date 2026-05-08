# solutions/ — pristine curriculum mirror

This directory mirrors `curriculum/` and stores the *original* version
of every rung file. It's what `bytelings reset <day>` copies back over
the working files when a learner wants a fresh start, and what
`bytelings solution <day>` (M2) reads from.

It's auto-populated by `scripts/migrate_v1_to_v2.py` (Task 11 of the M1
plan). Until that runs, only this README lives here so the wheel build
has a non-empty force-include target.

Do not edit files in this tree by hand.
