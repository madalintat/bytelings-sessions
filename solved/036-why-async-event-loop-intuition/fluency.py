"""Rung 2: Fluency — solved version.

Sequential (blocking) work: 3 chickens × 40 min = 120 min.
Concurrent (event-loop style): all three ovens start together;
elapsed time = max(40, 40, 40) = 40 min.
"""

SYNC_MINUTES = 120
ASYNC_MINUTES = 40
