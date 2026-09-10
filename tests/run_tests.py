#!/usr/bin/env python3
"""🧭 Elena — full test suite (MIT, single command).

Runs every check against a REAL lumen MVM on a throwaway PDB. No external
services, no credentials, no Poli needed — only a lumen M runtime (see
harness/elena_harness.py for how to provide one).

Checks:
  1. INIT seeds the canonical personality (idempotent)
  2. ELENA status: active=1, version, counts at zero
  3. identity_len in range
  4. DECIDE creates a decision card: status=open, fields stored, id d_*
  5. DECIDE lint: rejects without success criteria / owner / review date /
     renunciation / confidence / options (regla 5 + no sorda)
  6. LOG lists all decisions
  7. REVIEW lists open (all) and flags due ones by date (ISO compare)
  8. CONSTITUTION prints the 12 articles in order
  9. Persistence: card survives across independent executions
  10. Sync: mother phrase present in src/elena.m and personalities/elena.md

Usage:  python tests/run_tests.py          (exit 0 = all green)
"""

import os
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
HARNESS = ROOT / "harness"
sys.path.insert(0, str(HARNESS))
from elena_harness import _mvm, SRC_ROUTINES  # noqa: E402  (shared loader)

DB = os.path.join(tempfile.gettempdir(), "elena_tests.db")
if os.path.exists(DB):
    os.remove(DB)

FAILURES: list[str] = []


def check(label: str, cond: bool, detail: str = ""):
    status = "PASS" if cond else "FAIL"
    print(f"[{status}] {label}" + (f" — {detail}" if detail and not cond else ""))
    if not cond:
        FAILURES.append(label)


def run(src: str, expect_ok: bool = True) -> str:
    r = _mvm()(src, routines=SRC_ROUTINES, sqlite_path=DB, gas_limit=200000)
    out = ((r.get("state") or {}).get("output") or "") if isinstance(r, dict) else ""
    ok = r.get("ok") if isinstance(r, dict) else False
    if expect_ok and not ok:
        raise RuntimeError(f"MVM ejecución falló: {src[:80]}… out={out[:200]}")
    return out


print("═══ 1. INIT ═══")
out = run("D INIT^ELENA")
check("INIT siembra (mensaje)", "elena sembrada" in out)
run("D INIT^ELENA")  # idempotente: no debe romper
out = run('W $G(^PERSONALITY("elena","name"))')
check("idempotente (name intacto)", "elena" in out)

print("═══ 2. STATUS ═══")
out = run("D ELENA^ELENA")
check("status activo", "active=1" in out)
check("status versión", "v0.1.0" in out)
check("status counts a cero", "decisiones_open=0 reviewed=0" in out)
import re  # noqa: E402
m = re.search(r"identity_len=(\d+)", out)
check("identity_len en rango", bool(m) and 600 <= int(m.group(1)) <= 1400, f"len={m.group(1) if m else '?'}")

print("═══ 3. DECIDE (contrato de decisión) ═══")
out = run('S ^R=$$DECIDE^ELENA("Lanzar el experimento del techo creativo","Verdad suficiente: falsable y barato","diseno completo|pilot reducido|esperar","renuncio al pilot reducido y a esperar","pendiente CI95 + veredicto","Lisa","2026-10-10","coste juez sobre presupuesto","0.7","novedad sube tras ronda 8") W ^R')
did = out.strip()
check("DECIDE devuelve id", did.startswith("d_"), f"id={did}")
out = run(f'W $G(^DECISION("{did}","status"))_"/"_$G(^DECISION("{did}","review_date"))_"/"_$G(^DECISION("{did}","confidence"))')
check("card: open / fecha / confianza", out.strip() == "open/2026-10-10/0.7", out.strip())
out = run(f'W $L($G(^DECISION("{did}","regret")))>0')
check("renuncia registrada", out.strip().startswith("1"), out.strip())

print("═══ 4. LINT constitucional (rechazos) ═══")
cases = [
    ("sin_criterio_de_exito", '$$DECIDE^ELENA("d","r","o","g","","dueno","2026-10-10","x","0.5","t")'),
    ("sin_dueno", '$$DECIDE^ELENA("d","r","o","g","c","","2026-10-10","x","0.5","t")'),
    ("sin_fecha_de_revision", '$$DECIDE^ELENA("d","r","o","g","c","dueno","","x","0.5","t")'),
    ("sin_renuncia_declarada", '$$DECIDE^ELENA("d","r","o","","c","dueno","2026-10-10","x","0.5","t")'),
    ("sin_confianza", '$$DECIDE^ELENA("d","r","o","g","c","dueno","2026-10-10","x","","t")'),
    ("sin_opciones_consideradas", '$$DECIDE^ELENA("d","r","","g","c","dueno","2026-10-10","x","0.5","t")'),
]
for label, call in cases:
    out = run(f"W {call}")
    check(f"rechazo {label}", f"rechazada:{label}" in out, out.strip())

print("═══ 5. LOG / REVIEW ═══")
out = run("D LOG^ELENA")
check("LOG lista la decisión", did in out)
run('S ^R=$$DECIDE^ELENA("Decisión antigua para review","e2e","a|b","renuncio a nada","existe","hermes","2026-09-20","-","0.5","-") W ^R')
out = run("D REVIEW^ELENA")
check("REVIEW todas lista", did in out and "rev:" in out)
out = run('D REVIEW^ELENA("2026-10-01")')
check("REVIEW vencidas marca la vieja", "VENCIDA" in out and "2026-09-20" in out)
check("REVIEW vencidas no marca la futura", "2026-10-10" not in out.split("VENCIDA")[-1] if "VENCIDA" in out else True)

print("═══ 6. CONSTITUCIÓN ═══")
out = run("D CONSTITUTION^ELENA")
check("constitución presente", "Constitucion de Elena" in out)
out = run('W $G(^PERSONALITY("elena","critical_rules","01"))')
check("artículo 01 (Umbral)", "Umbral" in out)
out = run('W $G(^PERSONALITY("elena","critical_rules","10"))')
check("artículo 10 (Poda protegida)", "Poda" in out)
out = run('W $O(^PERSONALITY("elena","critical_rules",""),-1)')
check("12 artículos (última clave)", out.strip().endswith("12"), out.strip())

print("═══ 7. PERSISTENCIA cross-exec ═══")
out = run(f'W "status=",$G(^DECISION("{did}","status"))')
check("card persiste en exec nuevo", "status=open" in out)

print("═══ 8. SYNC identidad ═══")
src = (ROOT / "src" / "elena.m").read_text(encoding="utf-8")
pers = (ROOT / "personalities" / "elena.md").read_text(encoding="utf-8")
check("frase madre en la rutina", "Con esto alcanza" in src or "con esto alcanza" in src.lower())
check("frase madre en la personalidad", "Con esto alcanza" in pers)

print()
if FAILURES:
    print(f"❌ {len(FAILURES)} FAIL(S): {FAILURES}")
    sys.exit(1)
print("🎉 TODO VERDE — Elena lista para cerrar ciclos")
