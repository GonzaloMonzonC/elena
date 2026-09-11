# Changelog

## [0.1.2] — 2026-09-11

### Añadido
- 🧭 **Landing — [elena.cadences.app](https://elena.cadences.app)**: single-file (EN/ES),
  su personaje (la decision card real, la ley en 12 artículos) y *su realidad sobre LUMEN*
  (la sala de cierre: cards firmadas, el reloj, la cota dura de Astrid), OG, favicon;
  cross-links de la tríada.
- Landing: **firma visual v1** — brújula/reloj (marca de agua) + línea de hitos bajo el titular.

### Docs
- README (+ ES): 🌐 landing link.

## [0.1.1] — 2026-09-10

### Notas
- **Bautismo firmado (2026-09-10)**: primera decision card real en producción —
  decisión, opciones, renuncia, criterio, dueño, fecha y revisit trigger
  completos (revisit **2026-09-17**). El lint constitucional se ejerció en la
  propia firma: la Decididora queda operativa.
- Repaso de tríada: referencias cruzadas verificadas (Astrid · Iris · Elena) y
  licencia MIT consistente en los tres repos.

## [0.1.0] — 2026-09-10

Primera release. Elena nace como tercera pata de la tríada **A–I–E**.

### Diseño (ronda del equipo)
- **La brecha**: Astrid (*episteme*) e Iris (*poiesis*) son bucles que no terminan — regresión epistémica y
  generativa infinitas. Falta **phronesis**: la Decididora que clausura.
- Análisis multi-asesor (Javier · Pamies · Porto): el «basta» como **frontera de umbral** (no desautorización
  del rigor), la renuncia como artículo propio, el no en **tres tiempos** (No / Hasta que / Entonces sí),
  **falso bloqueante vs declarable**, «el silencio es el presupuesto corriendo», y «Elena es el embrague».
- Voces de las hermanas: Iris — *"portera, no jueza"*, todo no con plan B y fecha de caducidad; Astrid —
  *"registro qué es, no qué se hizo"*, arbitraje con claim + confidence.
- Decisión de Gonzalo: **agente real, repo propio** (no protocolo). Nombre: **Elena**.

### Contrato M (`src/elena.m`)
- `DECIDE` con **lint constitucional embebido**: sin decisión + opciones + renuncia + criterio + dueño +
  fecha + confianza → `rechazada:<razon>`.
- `REVIEW` con fechas ISO (decisiones vencidas), `LOG`, `CONSTITUTION` (12 artículos en orden), `COUNT`.
- Estado como zona persistente (`status`), verificado cross-exec.

### Herramientas
- `tests/run_tests.py` — suite completa contra MVM real (PDB desechable, sin servicios externos).
- `harness/elena_harness.py` — status / seed / decide / review / log / constitution.
- `docs/DECISION_SCHEMA.md` — el contrato de la decision card + lint.

### Notas
- Primera decisión registrada de Elena: *cómo se llama* (ironía intencional del equipo).
- Diálogos canónicos entre las tres (golden examples) — pendientes como siguiente iteración.
