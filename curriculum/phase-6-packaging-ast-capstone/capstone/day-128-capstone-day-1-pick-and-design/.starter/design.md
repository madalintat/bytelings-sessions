# Design — <your project name>

Replace the placeholders. Keep this short. One page.

## 1. What does it do?

<One paragraph. What's the elevator pitch? Who uses it? What problem
does it solve?>

## 2. Commands

```text
<prog> <verb> <args>
```

| Command | Args | What it does |
|---|---|---|
| `habit done` | `<name>` | Record that habit was done today |
| `habit list` | (none) | Print current habits + streaks |
| `habit reset` | `<name>` | Wipe the history for one habit |

(Edit this table for your project.)

## 3. Data shape

```json
{
  "habits": {
    "meditate": {"created": "2026-05-08", "log": ["2026-05-08", "2026-05-09"]},
    "read": {"created": "2026-05-08", "log": ["2026-05-09"]}
  }
}
```

Where lives this file? Default: `~/.config/<prog>/data.json`.

## 4. Failure modes

What can go wrong? Be honest:

- [ ] Config dir doesn't exist on first run — create it.
- [ ] JSON file is malformed — fail loudly, suggest backup.
- [ ] Habit name with spaces / unicode — accept or reject? Decide.
- [ ] Two `habit done X` in the same day — silently dedupe? Or warn?
- [ ] System clock is wrong — out of scope; trust the OS.

## 5. Out of scope for v1

Write what you are NOT building. This is the most important section.

- No reminders / notifications
- No sync between machines
- No web UI
- No multi-user / sharing
- No charts (just text streak counts)
