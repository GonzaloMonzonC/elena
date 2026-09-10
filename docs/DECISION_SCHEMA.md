# Decision Card — canonical schema

> Elena's output contract. Every decision she makes is emitted as a **decision card**:
> a decision, its rationale, and the *price paid* — the options it killed.
>
> A decision without a card is not a decision. It is an opinion.

---

## 1. Format

A decision card is a flat record with the following fields. All fields are **required**
unless marked optional — the decision lint enforces this (see §3).

| Field | Type | Meaning |
|---|---|---|
| `decision_id` | string | `d_<seq>_<rev>` — stable id of the decision (revisions increment `rev`) |
| `ts` | ISO date | when the decision was made |
| `decision` | string | what will be done — one sentence, imperative, no hedging |
| `rationale` | string | *why*, in the terms that mattered (may cite Astrid truths / Iris options) |
| `options_considered` | string[] | the live options at the time (≥1). The log proves she did not decide deaf |
| `regret_log` | string | what is being **renounced** and why — the price of the decision |
| `success_criteria` | string | how we will know it worked |
| `owner` | string | who carries it out and answers for it |
| `review_date` | date | when the decision is revisited *by default* |
| `reversal_condition` | string | the condition under which it is undone / redone |
| `confidence` | number 0–1 | declared confidence — *"decido con 0.6 y esto me haría cambiar"* |
| `revisit_trigger` | string | signal that reopens deliberation before `review_date` |
| `status` | enum | `open` · `reviewed` · `reversed` · `expired` |

## 2. Example

```json
{
  "decision_id": "d_0001_0",
  "ts": "2026-09-10",
  "decision": "Launch the creative-ceiling experiment with 12 rounds and N=25.",
  "rationale": "Truth sufficient: h_6170_0 is well-formed and falsifiable; the plan is executable. Further evidence would cost more than the experiment itself.",
  "options_considered": [
    "Launch as designed (12 rounds, 3 conditions)",
    "Launch a reduced pilot (4 rounds) first",
    "Keep waiting for better metrics"
  ],
  "regret_log": "Renounced: the reduced pilot (cheaper signal, weaker slope fit) and the wait (zero cost now, unknown cost of delay). Chose full design because the judge cost is linear and the ceiling signal needs K≥10 points.",
  "success_criteria": "Slope estimates with CI95 for all 3 conditions + ceiling verdict on h_6170_0.",
  "owner": "Lisa (execution) · Hermes (blind judge)",
  "review_date": "2026-10-10",
  "reversal_condition": "If judge cost exceeds budget cap or generation collapses below 80% yield.",
  "confidence": 0.7,
  "revisit_trigger": "Any condition showing novelty rising ≥5% after round 8.",
  "status": "open"
}
```

## 3. The lint

`tests/lint_decisions.py` fails on any card that:

- misses `success_criteria`, `owner` or `review_date` — **regla 5: sin criterio + dueño + fecha no es decisión, es opinión**;
- misses `regret_log` or `options_considered` — prove she did not decide deaf;
- has `confidence` outside [0, 1], or no declared confidence;
- contradicts a hard `false` from Astrid's record without a reformulated hypothesis (§ constitution r.3).

The lint is *eat your own dogfood*: changes to the constitution itself are decisions,
logged as cards, and linted too.

## 4. Storage

In the Lab's PDB, cards live at:

```
^DECISION("d_0001_0","decision")          = "..."
^DECISION("d_0001_0","rationale")         = "..."
^DECISION("d_0001_0","options")           = "a|b|c"     (|-joined)
^DECISION("d_0001_0","regret")            = "..."
^DECISION("d_0001_0","success_criteria")  = "..."
^DECISION("d_0001_0","owner")             = "..."
^DECISION("d_0001_0","review_date")       = "YYYY-MM-DD"
^DECISION("d_0001_0","reversal_condition")= "..."
^DECISION("d_0001_0","confidence")        = 0.7
^DECISION("d_0001_0","revisit_trigger")   = "..."
^DECISION("d_0001_0","status")            = "open"
^DECISION("d_0001_0","ts")                = "2026-09-10"
```

`REVIEW^ELENA` lists cards whose `review_date` has passed or whose `revisit_trigger` fired.
