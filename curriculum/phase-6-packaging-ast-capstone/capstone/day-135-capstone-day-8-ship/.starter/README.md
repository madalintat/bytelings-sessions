# habit

Track tiny daily habits from the command line. One JSON file, zero
fuss.

## Install

    uv tool install .

(From a clone of this repo. To uninstall: `uv tool uninstall habit`.)

## Use

    habit done meditate         # mark today done
    habit list                  # see your streaks
    habit list --sort streak    # longest streaks first
    habit recent                # last 14 days as a grid
    habit reset meditate --yes  # wipe one habit

Data lives in `~/.config/habit/data.json`. Override with the
`HABIT_DATA` environment variable.

## Why

I wanted a habit tracker that lives in my terminal next to `git`, not
in a separate app. I built it in 8 days as the capstone of a Python
curriculum. It does what I need and nothing else.

## License

MIT
