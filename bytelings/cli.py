"""Click-based CLI for the bytelings runner."""
from __future__ import annotations

import shutil
from importlib import resources
from pathlib import Path

import click

from . import locator
from . import progress as progress_mod
from . import ui

WELCOME_TEXT = """\
[bold]Welcome to bytelings.[/bold]

Small daily exercises that make you fluent at writing and reading code.
Inspired by [cyan]Rustlings[/cyan]; built for Python today, with C, C++,
Rust, and Go on the roadmap.

Each day is one concept taught in 5 rungs:
  1. Read a short concept page
  2. Fix a broken file (fluency drill)
  3. Fill a function body (guided)
  4. Implement from scratch (solo, hidden tests)
  5. Apply the concept in a tiny project chunk

Run [cyan]bytelings[/cyan] (no args) to start the watcher. Save your
file → tests run → green panel → next rung. That's the loop.

Other commands:
  [cyan]bytelings init[/cyan]      — create ./bytelings/ with curriculum + scaffold
  [cyan]bytelings today[/cyan]     — what you're working on now
  [cyan]bytelings progress[/cyan]  — streak + completion bar
  [cyan]bytelings hint[/cyan]      — show today's concept page
  [cyan]bytelings run[/cyan]       — run current rung's tests once
  [cyan]bytelings done[/cyan]      — manually mark current rung done
  [cyan]bytelings reset DAY[/cyan] — reset a day's progress
"""

PRE_INIT_HINT = """\
[bold yellow]No curriculum/ folder here.[/bold yellow]

Run [cyan]bytelings init[/cyan] to create a [cyan]./bytelings/[/cyan] project folder, then
[cyan]cd bytelings && uv sync && bytelings[/cyan] to start the watcher.
"""


def _bundled_dir(name: str, *, required: bool = False) -> Path | None:
    """Locate a bundled top-level directory (curriculum/, solutions/, scaffold/).

    Checks the installed wheel's `bytelings/_<name>/` first, then falls
    back to the repo's `<name>/` for editable / dev installs. Returns
    None if missing; if `required`, raises a click error instead.
    """
    bundled = resources.files("bytelings") / f"_{name}"
    if bundled.is_dir():
        return Path(str(bundled))
    repo = Path(__file__).resolve().parent.parent / name
    if repo.is_dir():
        return repo
    if required:
        raise click.ClickException(
            f"Could not locate {name}/. Reinstall bytelings or run from the repo root."
        )
    return None


def _curriculum_source() -> Path:
    src = _bundled_dir("curriculum", required=True)
    assert src is not None  # required=True raises on miss
    return src


def _scaffold_source() -> Path | None:
    return _bundled_dir("scaffold")


def _solutions_source() -> Path | None:
    return _bundled_dir("solutions")


def _solved_source() -> Path | None:
    return _bundled_dir("solved")


@click.group(invoke_without_command=True)
@click.pass_context
def cli(ctx: click.Context) -> None:
    """bytelings — small daily exercises to make you fluent at code.

    Run with no subcommand to launch the watcher.
    """
    if ctx.invoked_subcommand is not None:
        return
    if not Path("curriculum").is_dir():
        ui.console.print(PRE_INIT_HINT)
        ctx.exit(1)
    from . import watcher  # lazy — keeps CLI tests off watchdog
    watcher.watch()


@cli.command()
@click.option(
    "--target", "-t", default="bytelings",
    help="Project directory to create (default: ./bytelings).",
    type=click.Path(file_okay=False, path_type=Path),
)
@click.option(
    "--force", is_flag=True,
    help="Overwrite an existing target directory.",
)
def init(target: Path, force: bool) -> None:
    """Create TARGET project directory (default ./bytelings) with the
    bundled curriculum and a uv-ready pyproject.toml inside.

    Then: cd TARGET && uv sync && bytelings
    """
    src = _curriculum_source()
    if target.exists():
        if not force:
            raise click.ClickException(
                f"{target} already exists. Re-run with --force to overwrite."
            )
        shutil.rmtree(target)
    shutil.copytree(src, target / "curriculum")

    sol_src = _solutions_source()
    if sol_src is not None:
        shutil.copytree(sol_src, target / "solutions")

    solved_src = _solved_source()
    if solved_src is not None:
        shutil.copytree(solved_src, target / "solved")

    scaffold_src = _scaffold_source()
    shipped: list[str] = []
    if scaffold_src is not None:
        for fname in ("pyproject.toml", "uv.lock"):
            f = scaffold_src / fname
            if not f.is_file():
                continue
            shutil.copy2(f, target / fname)
            shipped.append(fname)

    display_target = target if target.is_absolute() else Path("./") / target
    ui.console.print(f"[bold green]✔ Created {display_target}/[/bold green]")
    if sol_src is not None:
        ui.console.print("  solutions/ mirror copied (used by `bytelings reset`)")
    if solved_src is not None:
        ui.console.print("  solved/ mirror copied (used by `bytelings solution`)")
    if shipped:
        ui.console.print(f"  shipped: {', '.join(shipped)}")
    ui.console.print(
        f"\n[dim]Next:[/dim] [cyan]cd {target} && uv sync && bytelings[/cyan]"
    )


@cli.command()
def welcome() -> None:
    """Print the one-time onboarding intro."""
    ui.console.print(WELCOME_TEXT)


@cli.command()
def today() -> None:
    """Show today's day and rung plan."""
    p = progress_mod.load()
    day = locator.current_or_next_day(p)
    if day is None:
        ui.header("All 135 days complete! 🎉")
        click.echo("Or — run `bytelings init` to scaffold the curriculum.")
        return
    ui.header(f"{day.slug}")
    rungs = locator.rungs_of(day)
    ui.rung_table(rungs, p.current_rung, p.completed_rungs_today)
    click.echo(
        f"\nPhase: {day.phase}    Module: {day.module}\n"
        f"Run `bytelings` to start the watcher."
    )


@cli.command(name="progress")
def progress_cmd() -> None:
    """Show streak and overall progress."""
    p = progress_mod.load()
    days = locator.all_days()
    total = len(days)
    completed = len(p.completed_days)
    ui.progress_summary(completed, total, p.streak_days, p.longest_streak)


@cli.command()
def watch() -> None:
    """Run the watcher (the main loop). Ctrl-C to stop."""
    from . import watcher
    watcher.watch()


@cli.command()
@click.argument("day_slug", required=False)
def run(day_slug: str | None) -> None:
    """Run the current rung's tests once (no watch).

    With DAY_SLUG, run that day's current rung instead of today's.
    """
    from . import watcher
    p = progress_mod.load()
    day = locator.find_day(day_slug) if day_slug else locator.current_or_next_day(p)
    if day is None:
        click.echo(f"Day not found: {day_slug}" if day_slug else "No day to run.")
        return
    rungs = locator.rungs_of(day)
    rung = locator.rung_for(p, rungs)
    if rung.test_file is None or not rung.test_file.exists():
        click.echo(f"Rung {rung.number} has no automated tests.")
        return
    result = watcher.run_pytest(rung.test_file)
    if result.passed:
        ui.banner_pass(f"Rung {rung.number}: {rung.name}")
    else:
        ui.banner_fail(result.summary)


@cli.command()
@click.argument("day_slug", required=False)
def hint(day_slug: str | None) -> None:
    """Show the current (or named) day's concept page.

    The concept page is your hint — read it whenever you're stuck.
    """
    p = progress_mod.load()
    day = locator.find_day(day_slug) if day_slug else locator.current_or_next_day(p)
    if day is None:
        click.echo(f"Day not found: {day_slug}" if day_slug else "No day to hint.")
        return
    concept = day.path / "README.md"
    if not concept.is_file():
        click.echo(f"No README.md for {day.slug}.")
        return
    ui.header(f"Concept: {day.slug}")
    ui.console.print(concept.read_text())


@cli.command()
def done() -> None:
    """Manually mark the current rung complete (escape hatch)."""
    p = progress_mod.load()
    day = locator.current_or_next_day(p)
    if day is None:
        click.echo("No day in progress.")
        return
    p.current_day = day.slug
    rung = p.current_rung
    next_day = next(
        (d for d in locator.all_days()
         if d.slug not in p.completed_days and d.slug != day.slug),
        None,
    )
    p = progress_mod.advance_after_pass(
        p, day.slug, rung, next_day.slug if next_day else None
    )
    progress_mod.save(p)
    if rung == progress_mod.TOTAL_RUNGS:
        ui.banner_day_complete(day.slug, p.streak_days)
    else:
        ui.banner_marked_done(f"Rung {rung}")


@cli.command(name="next")
def next_cmd() -> None:
    """Skip to next rung without finishing the current one."""
    p = progress_mod.load()
    if p.current_rung < progress_mod.TOTAL_RUNGS:
        p.current_rung += 1
        progress_mod.save(p)
        click.echo(f"Skipped to rung {p.current_rung}.")
    else:
        click.echo("Already on rung 5. Use `bytelings done` to finish the day.")


@cli.command()
@click.argument("day_slug")
def reset(day_slug: str) -> None:
    """Reset progress + restore pristine files for a specific day.

    Progress: clears day from completed and resets rung state if current.
    Files: copies from solutions/<slug>/ over the working curriculum/<slug>/
    files, so the learner gets a fresh starter. v1 slugs are accepted —
    locator.find_day handles the back-compat lookup.
    """
    p = progress_mod.load()
    day = locator.find_day(day_slug)
    if day is None:
        raise click.ClickException(f"Day not found: {day_slug}")

    if day.slug in p.completed_days:
        p.completed_days.remove(day.slug)
    if day_slug in p.completed_days:  # also handle if user passed v1 slug
        p.completed_days.remove(day_slug)
    if p.current_day in (day.slug, day_slug):
        p.current_rung = 1
        p.completed_rungs_today = []
    progress_mod.save(p)

    sol_dir = Path("solutions") / day.slug
    if sol_dir.is_dir():
        for fname in locator.RUNG_FILES:
            src = sol_dir / fname
            if src.is_file():
                shutil.copy2(src, day.path / fname)
        click.echo(f"Reset {day.slug}: progress cleared + files restored.")
    else:
        click.echo(f"Reset {day.slug}: progress cleared (no solutions/ mirror).")


@cli.command()
@click.argument("day_slug_or_number")
def start(day_slug_or_number: str) -> None:
    """Jump the watcher to a specific day. Pass the slug or the day number.

    Examples: `bytelings start day-007-string-methods-and-fstrings`
              `bytelings start 7`
    """
    days = locator.all_days()
    if not days:
        raise click.ClickException("No curriculum scaffolded. Run `bytelings init` first.")
    target = None
    if day_slug_or_number.isdigit():
        n = int(day_slug_or_number)
        target = next((d for d in days if d.number == n), None)
    else:
        target = next((d for d in days if d.slug == day_slug_or_number), None)
    if target is None:
        raise click.ClickException(f"No such day: {day_slug_or_number}")
    p = progress_mod.load()
    p.current_day = target.slug
    p.current_rung = 1
    p.completed_rungs_today = []
    progress_mod.save(p)
    click.echo(f"Now on {target.slug}. Run `bytelings` to start the watcher.")


@cli.command()
def list() -> None:
    """List every day in the curriculum with completion markers."""
    p = progress_mod.load()
    days = locator.all_days()
    if not days:
        click.echo("No curriculum scaffolded. Run `bytelings init` first.")
        return
    completed = set(p.completed_days)
    for d in days:
        marker = "[green]✔[/green]" if d.slug in completed else "[dim]○[/dim]"
        line = f"{marker} {d.slug}  [dim]({d.module})[/dim]"
        ui.console.print(line)


@cli.command()
@click.argument("pattern_id", required=False)
def patterns(pattern_id: str | None) -> None:
    """List the Pattern Catalog or show one entry by ID.

    Usage:
        bytelings patterns          # list all
        bytelings patterns P-07     # show one
    """
    from . import patterns as p_module

    if pattern_id is None:
        for p in p_module.PATTERNS:
            head = p.description.split(".")[0]
            ui.console.print(f"[cyan]{p.id}[/cyan] [bold]{p.name}[/bold] — {head}.")
        ui.console.print(
            f"\n[dim]({len(p_module.PATTERNS)} patterns. "
            "`bytelings patterns P-NN` for one entry.)[/dim]"
        )
        return

    p = p_module.by_id(pattern_id)
    if p is None:
        raise click.ClickException(f"No pattern with id {pattern_id!r}.")
    ui.console.print(f"[bold cyan]{p.id} — {p.name}[/bold cyan]\n")
    ui.console.print(p.description + "\n")
    ui.console.print("[dim]Canonical:[/dim]")
    for line in p.canonical.splitlines():
        ui.console.print(f"    {line}")
    ui.console.print(f"\n[dim]When to reach for it:[/dim] {p.when}")
    days_str = ", ".join(str(d) for d in p.days) if p.days else "(none yet)"
    ui.console.print(f"[dim]Days that exercise it:[/dim] {days_str}")


# Derive {rung_number: source_filename} from locator's canonical specs.
# Reveal targets are the source files, never the test files.
_RUNG_FILENAMES = {n: src for n, src, _, _ in locator._RUNG_SPECS}


@cli.command()
@click.argument("day_slug")
@click.option(
    "--rung", "-r", "rung", type=click.IntRange(1, 5), required=True,
    help="Which rung to reveal (1=README, 2=fluency, 3=guided, 4=solo, 5=apply).",
)
@click.option(
    "--yes", "-y", is_flag=True,
    help="Skip the friction prompt. Useful in scripts; not recommended for learners.",
)
def solution(day_slug: str, rung: int, yes: bool) -> None:
    """Reveal a rung's solved (or starter) file, gated by a friction prompt.

    Lookup order:
      1. solved/<slug>/<rung>.py  — the canonical answer (when authored)
      2. solutions/<slug>/<rung>.py  — the pristine starter (always present)

    The friction prompt is the point: a learner has to *decide* to look.
    Default at the prompt is `h` (re-read the hint instead).

    Solved-content authoring is incremental. Days with no solved/ entry
    fall back to the starter — still useful when a learner has deleted
    a docstring or hint by accident.
    """
    day = locator.find_day(day_slug)
    if day is None:
        raise click.ClickException(f"No such day: {day_slug!r}")
    fname = _RUNG_FILENAMES[rung]

    solved_src = Path("solved") / day.slug / fname
    starter_src = Path("solutions") / day.slug / fname
    if solved_src.is_file():
        src = solved_src
        kind = "solved"
    elif starter_src.is_file():
        src = starter_src
        kind = "starter"
    else:
        raise click.ClickException(
            f"No solution file at {solved_src} or {starter_src}. "
            "Run `bytelings init` to scaffold, or check the day slug."
        )

    if not yes:
        ui.console.print(
            f"\n[bold yellow]You're about to read the rung-{rung} file for "
            f"{day.slug}.[/bold yellow]\n"
            "This is the highest-friction door — once you read it, the "
            "discovery is gone.\n"
        )
        choice = click.prompt(
            "  [Y]es show me  /  [n]o I'll keep trying  /  [h]int instead",
            default="h",
            show_default=True,
            type=click.Choice(["y", "Y", "n", "N", "h", "H"], case_sensitive=False),
        ).lower()
        if choice == "h":
            ui.console.print(
                f"\n[dim]Skipping reveal. Try [cyan]bytelings hint {day.slug}[/cyan] "
                "for the concept page instead.[/dim]"
            )
            return
        if choice == "n":
            ui.console.print(
                "\n[dim]Good. Keep going. The discovery is the lesson.[/dim]"
            )
            return
        # Fall through on 'y'/'Y'.

    ui.header(f"{day.slug} — Rung {rung} ({fname}) — {kind}")
    ui.console.print(src.read_text())


@cli.command(name="phase-project")
def phase_project() -> None:
    """Open the README for the current phase project (if at a boundary)."""
    p = progress_mod.load()
    day = locator.first_unfinished_day(p)
    if day is None:
        click.echo("All days complete.")
        return
    phase_dir = Path("curriculum") / day.phase
    candidates = list(phase_dir.glob("phase-*-project-*/README.md"))
    if candidates:
        click.echo(f"Phase project: {candidates[0]}")
    else:
        click.echo(f"No phase project found for {day.phase}.")


if __name__ == "__main__":
    cli()
