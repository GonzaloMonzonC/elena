# Elena

**Astrid limita. Iris expande. Elena cierra.**

Elena es la **agente decidora** — la tercera pata de la tríada de Cadences Lab, junto a [Astrid](https://github.com/GonzaloMonzonC/astrid) e [Iris](https://github.com/GonzaloMonzonC/iris):

| Agente | Pregunta | Facultad |
|---|---|---|
| **Astrid** | *¿Es verdad?* | *episteme* — hechos anclados (fuente + CID + firma). Evidencia registrada o silencio. |
| **Iris** | *¿Y si…?* | *poiesis* — hipótesis falsables, nunca claims. |
| **Elena** | ***¿Y ahora qué?*** | ***phronesis*** — decisiones con su renuncia asumida. |

> Dos voces que deliberan; una que cierra. Sin la tercera, la verdad se vuelve parálisis y las ideas se vuelven humo.

## El contrato en una frase

Elena no delibera a ciegas: convierte *verdad suficiente* + *opciones abiertas* en una **decision card** — decisión, rationale, log de opciones, confianza, dueño, fecha de revisión, condición de reversión y el precio pagado (**lo que deja afuera**). Una decisión sin tarjeta no es una decisión: es una opinión.

## Uso

```bash
python tests/run_tests.py                        # suite completa (exit 0 = verde)
python harness/elena_harness.py status           # estado de la personalidad
python harness/elena_harness.py seed             # siembra ^PERSONALITY("elena")
python harness/elena_harness.py decide \
    --decision "Lanzar el experimento X" \
    --rationale "Verdad suficiente: falsable y barato" \
    --options "diseño completo|pilot reducido|esperar" \
    --regret "renuncio al pilot reducido y a esperar" \
    --success "pendiente CI95 + veredicto de techo" \
    --owner "Lisa" --review 2026-10-10 \
    --confidence 0.7                 # crea una decision card
python harness/elena_harness.py review           # decisiones abiertas
python harness/elena_harness.py review --today 2026-10-01   # las vencidas
python harness/elena_harness.py constitution     # su ley, en orden
```

## Estructura

| Ruta | Contenido |
|---|---|
| `src/elena.m` | La rutina M: personalidad + contrato de decisión (M-Light, sin dependencias) |
| `personalities/elena.md` | Personalidad legible (constitución, voz, dinámicas con las hermanas) |
| `harness/elena_harness.py` | Conecta Elena a un runtime lumen MVM (status/seed/decide/review/log) |
| `tests/run_tests.py` | Suite completa contra MVM real (PDB desechable, sin servicios externos) |
| `docs/DECISION_SCHEMA.md` | El contrato de la decision card (schema v1 + lint) |
| `DESIGN.md` | Diseño y rol: la Decididora (phronesis), dinámica de la tríada, diferenciación |

## Requisitos

Un runtime lumen MVM: clona [lumen-protocol](https://github.com/GonzaloMonzonC/lumen-protocol) junto a este repo (recomendado) o instala `lumen-mcp` + apunta `LUMEN_MLIGHT_LIB` a tu `lumen_mlight.dll`/`.so`.

## Estado

**v0.1.0** — personalidad + contrato de decisión + suite verde. Elena vive además como agente del ecosistema (`mode: elena` en Poli, routing `^AGENTES("routing","elena")`).

## Licencia

MIT — Copyright (c) 2026 Gonzalo Monzón · Cadences Lab
