"""Rung 5: Apply — full findings pipeline.

    uv run python apply.py

Parses a hardcoded findings log, generates the graduation summary,
prints it, and asserts key substrings are present.

Pattern: P-07 (accumulator-into-dict).
"""
from __future__ import annotations
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path

_HERE = Path(__file__).parent

_g = spec_from_file_location("_guided", _HERE / "guided.py")
_guided = module_from_spec(_g)
_g.loader.exec_module(_guided)

_s = spec_from_file_location("_solo", _HERE / "solo.py")
_solo = module_from_spec(_s)
_s.loader.exec_module(_solo)


FINDINGS_LOG = """\
src/main.py:10:4: bare-except: bare `except:` catches everything
src/main.py:22:0: unused-import: `os` imported but never used
src/main.py:45:0: mutable-default: mutable default argument `[]`
src/utils.py:5:8: bare-except: bare `except:` catches everything
src/utils.py:31:0: unused-import: `sys` imported but never used
src/cli.py:14:0: unused-import: `json` imported but never used
src/cli.py:20:0: bare-except: bare `except:` catches everything
src/cli.py:30:4: bare-except: bare `except:` catches everything
src/cli.py:50:0: mutable-default: mutable default argument `{}`
src/models.py:7:0: unused-import: `typing` imported but never used
src/models.py:88:12: bare-except: bare `except:` catches everything
src/models.py:100:0: mutable-default: mutable default argument `[]`
"""


def main() -> None:
    findings = _guided.parse_findings_log(FINDINGS_LOG)
    assert len(findings) == 12, f"Expected 12 parsed findings, got {len(findings)}"

    report = _solo.summary(findings)
    print(report)

    assert "Total: 12" in report, "Summary should include 'Total: 12'"
    assert "bare-except" in report
    assert "unused-import" in report
    assert "mutable-default" in report
    assert "src/cli.py" in report
    assert "src/models.py" in report

    print("✓ findings pipeline works.")


if __name__ == "__main__":
    main()
