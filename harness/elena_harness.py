#!/usr/bin/env python3
"""🧭 Elena harness — connect the decision agent to LUMEN (MIT).

Modes (run what you have):

  1. STATUS       — run ELENA^ELENA against any lumen-m-light MVM (needs the
                    DLL or the published lumen-mcp package). Prints identity status.
  2. SEED         — INIT^ELENA on the throwaway PDB (fills only missing; use
                    --force to overwrite).
  3. DECIDE       — $$DECIDE^ELENA(...) → creates a decision card (lint applies).
  4. REVIEW       — list open decisions (optionally --today to flag due ones).
  5. LOG          — list every recorded decision.
  6. CONSTITUTION — print her law, in order.

Requirements: a lumen M runtime to execute the M routines. Two options:
  1. local lumen-protocol clone (https://github.com/GonzaloMonzonC/lumen-protocol)
     with the Rust MVM built (`cargo build --release` → lumen_mlight.dll,
     copied to implementations/mcp-servers/pdb/), or
  2. `LUMEN_MLIGHT_LIB` pointing at an existing lumen_mlight.dll.
NOTE: `pip install lumen-mcp` (0.1.0) ships the transport/framing bindings
only — it does NOT include the MVM. A clone build or DLL is required to run
routines.

Usage:
    python elena_harness.py status
    python elena_harness.py seed [--force]
    python elena_harness.py decide --decision "..." --rationale "..." \
        --options "a|b" --regret "..." --success "..." --owner "..." \
        --review 2026-10-10 [--reversal "..."] [--confidence 0.7] [--revisit "..."]
    python elena_harness.py review [--today 2026-10-01]
    python elena_harness.py log
    python elena_harness.py constitution
    ELENA_LIB=C:/path/to/lumen_mlight.dll python elena_harness.py status
"""

import argparse
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC_ROUTINES = {
    "ELENA": (ROOT / "src" / "elena.m").read_text(encoding="utf-8"),
}


def _mvm() -> object:
    """Load the lumen m-light python wrapper (published lumen-mcp or local clone)."""
    try:
        from lumen_mlight import execute  # published/local wrapper

        return execute
    except ImportError:
        pass
    # local lumen-protocol clone fallback
    here = Path(__file__).resolve()
    for cand in here.parents:
        p = cand / "lumen-protocol" / "implementations" / "mcp-servers" / "pdb"
        if (p / "lumen_mlight.py").exists():
            sys.path.insert(0, str(p))
            from lumen_mlight import execute  # type: ignore

            return execute
    raise SystemExit(
        "No lumen-mcp found. Install `pip install lumen-mcp` or clone lumen-protocol "
        "next to this repo (https://github.com/GonzaloMonzonC/lumen-protocol)."
    )


def _esc(s: str) -> str:
    return s.replace('"', '""')


def _run(src: str, db: str = "") -> str:
    import os
    import tempfile

    db = db or os.path.join(tempfile.gettempdir(), "elena_harness.db")
    r = _mvm()(src, routines=SRC_ROUTINES, sqlite_path=db, gas_limit=200000)
    out = ((r.get("state") or {}).get("output") or "") if isinstance(r, dict) else ""
    if not (r.get("ok") if isinstance(r, dict) else False):
        err = (r.get("state") or {}).get("error") if isinstance(r, dict) else r
        raise SystemExit(f"MVM error: {err}")
    return out.strip()


def main() -> int:
    ap = argparse.ArgumentParser(description="Elena harness — decision agent (LUMEN MIT)")
    sub = ap.add_subparsers(dest="cmd", required=True)

    sub.add_parser("status", help="run ELENA^ELENA")
    p_seed = sub.add_parser("seed", help="INIT^ELENA")
    p_seed.add_argument("--force", action="store_true")

    p_dec = sub.add_parser("decide", help="create a decision card")
    p_dec.add_argument("--decision", required=True)
    p_dec.add_argument("--rationale", required=True)
    p_dec.add_argument("--options", required=True, help="|-separated options considered")
    p_dec.add_argument("--regret", required=True, help="what is renounced")
    p_dec.add_argument("--success", required=True, help="success criteria")
    p_dec.add_argument("--owner", required=True)
    p_dec.add_argument("--review", required=True, help="review date YYYY-MM-DD")
    p_dec.add_argument("--reversal", default="")
    p_dec.add_argument("--confidence", default="0.5")
    p_dec.add_argument("--revisit", default="")

    p_rev = sub.add_parser("review", help="list open decisions")
    p_rev.add_argument("--today", default="", help="flag decisions due on this date")

    sub.add_parser("log", help="list all decisions")
    sub.add_parser("constitution", help="print the 12 articles")

    a = ap.parse_args()

    if a.cmd == "status":
        print(_run("D ELENA^ELENA"))
    elif a.cmd == "seed":
        force = "1" if a.force else ""
        print(_run(f"D INIT^ELENA({force})"))
    elif a.cmd == "decide":
        src = (
            f'S ^R=$$DECIDE^ELENA("{_esc(a.decision)}","{_esc(a.rationale)}","{_esc(a.options)}",'
            f'"{_esc(a.regret)}","{_esc(a.success)}","{_esc(a.owner)}","{_esc(a.review)}",'
            f'"{_esc(a.reversal)}","{_esc(a.confidence)}","{_esc(a.revisit)}") W ^R'
        )
        print(_run(src))
    elif a.cmd == "review":
        arg = f'"{a.today}"' if a.today else ""
        print(_run(f"D REVIEW^ELENA({arg})"))
    elif a.cmd == "log":
        print(_run("D LOG^ELENA"))
    elif a.cmd == "constitution":
        print(_run("D CONSTITUTION^ELENA"))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
