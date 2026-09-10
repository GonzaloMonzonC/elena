# Elena

**Astrid limits. Iris expands. Elena closes.**

Elena is the **decision agent** — the third leg of the Cadences Lab tríada, alongside [Astrid](https://github.com/GonzaloMonzonC/astrid) and [Iris](https://github.com/GonzaloMonzonC/iris):

| Agent | Question | Faculty |
|---|---|---|
| **Astrid** | *Is it true?* | *episteme* — facts, anchored (source + CID + signature). Evidence on record, or silence. |
| **Iris** | *What if…?* | *poiesis* — falsifiable hypotheses, never claims. |
| **Elena** | ***So what do we do — now?*** | ***phronesis*** — decisions with their renouncement assumed. |

> Two voices that deliberate; one that closes. Without the third, truth becomes paralysis and ideas become smoke.

## The contract in one sentence

Elena **does not deliberate blindly**: she converts *sufficient truth* plus *open options* into a **decision card** — decision, rationale, options log, confidence, owner, review date, reversal condition, and the price paid (**what she leaves out**). A decision without a card is not a decision. It is an opinion.

## Usage

```bash
python tests/run_tests.py                        # full suite (exit 0 = green)
python harness/elena_harness.py status           # personality status
python harness/elena_harness.py seed             # seed ^PERSONALITY("elena")
python harness/elena_harness.py decide \
    --decision "Launch experiment X" \
    --rationale "Truth sufficient: falsifiable and cheap" \
    --options "full design|reduced pilot|wait" \
    --regret "renounce the reduced pilot and the wait" \
    --success "slope CI95 + ceiling verdict" \
    --owner "Lisa" --review 2026-10-10 \
    --confidence 0.7                 # create a decision card
python harness/elena_harness.py review           # open decisions
python harness/elena_harness.py review --today 2026-10-01   # those due
python harness/elena_harness.py constitution     # her law, in order
```

## Layout

| Path | Content |
|---|---|
| `src/elena.m` | The M routine: personality + decision contract (M-Light, no external deps) |
| `personalities/elena.md` | Human-readable personality (constitution, voice, dynamics) |
| `harness/elena_harness.py` | Connects Elena to a lumen MVM runtime (status/seed/decide/review/log) |
| `tests/run_tests.py` | Full suite against a real MVM (throwaway PDB, no external services) |
| `docs/DECISION_SCHEMA.md` | The decision card contract (schema v1 + lint) |
| `DESIGN.md` | Design & role: the Decididora (phronesis), tríada dynamics, differentiation |

## Requirements

A lumen MVM runtime: clone [lumen-protocol](https://github.com/GonzaloMonzonC/lumen-protocol) next to this repo (recommended) or install `lumen-mcp` + point `LUMEN_MLIGHT_LIB` at your `lumen_mlight.dll`/`.so`.

## Status

**v0.1.0** — personality + decision contract + green suite. Elena also lives as an ecosystem agent (`mode: elena` in Poli, routing `^AGENTES("routing","elena")`).

## License

MIT — Copyright (c) 2026 Gonzalo Monzón · Cadences Lab
