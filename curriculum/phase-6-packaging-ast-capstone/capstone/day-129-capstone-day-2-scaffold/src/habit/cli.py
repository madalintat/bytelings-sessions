"""CLI entry point. Today: just enough to print help and exit 0."""
from __future__ import annotations

import click

__version__ = "0.1.0"


@click.group()
@click.version_option(__version__, package_name="habit")
def main() -> None:
    """Track tiny daily habits."""


@main.command(name="list")
def list_cmd() -> None:
    """List all habits and their streaks."""
    click.echo("(no habits yet — try `habit done <name>`)")


@main.command()
@click.argument("name")
def done(name: str) -> None:
    """Mark <name> done for today."""
    click.echo(f"TODO: record {name} done today")


@main.command()
@click.argument("name")
def reset(name: str) -> None:
    """Wipe history for <name>."""
    click.echo(f"TODO: reset {name}")


if __name__ == "__main__":
    main()
