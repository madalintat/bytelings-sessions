"""CLI — wires storage + core into Click commands."""
from __future__ import annotations
from datetime import date

import click

from . import storage


@click.group()
@click.version_option("0.1.0", package_name="habit")
def main() -> None:
    """Track tiny daily habits."""


@main.command(name="list")
def list_cmd() -> None:
    """List all habits and their streaks."""
    path = storage.default_data_path()
    habits = storage.load(path)
    if not habits:
        click.echo("(no habits yet — try `habit done <name>`)")
        return
    today = date.today()
    for name, habit in sorted(habits.items()):
        click.echo(f"{name}: {habit.streak(today)}-day streak")


@main.command()
@click.argument("name")
def done(name: str) -> None:
    """Mark <name> done for today."""
    path = storage.default_data_path()
    habits = storage.load(path)
    today = date.today()
    habit = storage.mark_done(habits, name, today)
    storage.save(path, habits)
    click.echo(f"recorded {name} on {today.isoformat()} ({habit.streak(today)}-day streak)")


@main.command()
@click.argument("name")
def reset(name: str) -> None:
    """Wipe history for <name>."""
    click.echo(f"TODO: reset {name}")
