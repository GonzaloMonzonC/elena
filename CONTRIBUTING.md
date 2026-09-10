# Contributing — Elena

Gracias por querer contribuir. Elena es un agente MIT y su diseño está pensado para que **cualquiera pueda forkearlo y crear su propia decidora**.

## Principios que NO se negocian

Toda contribución debe respetar el contrato de Elena (ver `docs/DECISION_SCHEMA.md`):

1. **Toda decisión es contrato** — criterio + dueño + fecha + confianza + reversión. El lint lo verifica: sin los cinco, no es decisión.
2. **Nunca en falso, nunca sorda** — los falsos de Astrid son cota dura; el log de opciones es obligatorio.
3. **La renuncia se nombra** — una decisión sin `regret_log` no es de Elena.
4. **Separación ontológica** — la evidencia es de Astrid, las opciones de Iris; Elena solo decide y responde.
5. **Sin lore privado** — este repo es autocontenido: nada de URLs, claves o rutas del ecosistema privado.

## Cómo contribuir

### Reportar un problema
Abre un issue describiendo: qué esperabas, qué pasó, cómo reproducirlo (los tests son el mejor formato).

### Proponer un cambio
1. Fork + rama descriptiva (`feat/lo-que-sea`, `fix/lo-que-sea`).
2. **Los tests deben pasar**: `python tests/run_tests.py` (exit 0). Toda funcionalidad nueva, con su check.
3. Mantén la identidad sincronizada: `src/elena.m` ↔ `personalities/elena.md` (la suite lo verifica).
4. Comandos M portables: solo M-Light (sin dependencias de rutinas externas del ecosistema).
5. Pull request con una frase clara: **qué decisión nueva permite cerrar o qué invariante protege**.

### Ideas bienvenidas
- Formatos de revisión (disparadores de `revisit_trigger`, vencimientos, re-decisiones).
- **Diálogos canónicos** entre las tres (Astrid–Elena en fricción, Iris–Elena en poda) como golden examples.
- Traducciones de docs (patrón actual: `X.md` + `X.es.md`).

## Entorno de desarrollo

```
python tests/run_tests.py     # suite completa (necesita un runtime lumen M)
python harness/elena_harness.py status    # estado de la personalidad
```

Requiere un runtime MVM: clona [lumen-protocol](https://github.com/GonzaloMonzonC/lumen-protocol) al lado (o `pip install lumen-mcp` + `LUMEN_MLIGHT_LIB`).

## Licencia

Al contribuir aceptas que tu contribución se publica bajo la licencia MIT del repositorio.
