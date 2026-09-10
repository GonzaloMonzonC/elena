# Security Policy — Elena

## Modelo de seguridad

Elena es la **decidora** de la tríada A–I–E: por diseño **no gestiona secretos, no toca el registro de evidencia y no actúa fuera de su mandato**. Su superficie de riesgo es deliberadamente mínima.

### Lo que Elena NUNCA hace (garantías del contrato)

1. **No escribe en el registro de evidencia** de Astrid (`^EVIDENCE`) ni firma claims de hechos.
2. **No accede a credenciales**: no almacena ni procesa claves, tokens ni URLs privadas.
3. **No decide en falso ni a ciegas**: toda decisión lleva su *decision card* — opciones consideradas, renuncia nombrada, confianza declarada y condición de reversión. El lint del repo lo verifica.
4. **No ejecuta acciones externas**: las funciones de este repo operan solo sobre un MVM local (PDB de prueba o la del ecosistema, en lectura/escritura de su propio namespace `^DECISION`).
5. **No usurpa**: los valores, la soberanía y lo irreversible personal del operador se **elevan, no se toman**. El *contenido* del decision log es del operador — el repo publica persona y protocolos, nunca decisiones reales.

### Qué hacer si encuentras un problema

- **Repositorio**: abre un issue privado o escribe a los mantenedores (ver perfil del repo) sin incluir detalles explotables en público.
- **Contenido**: si un decision log contiene algo sensible, puede eliminarse de `^DECISION` sin afectar a nada más (los logs son del operador; el repo solo publica el esquema y la personalidad — esa separación es una garantía, no solo de diseño).
- Tiempo de respuesta objetivo: 72h.

### Alcance

Este repositorio contiene **código fuente y personalidad**, no datos operativos. El runtime (MVM, PDB) vive en [lumen-protocol](https://github.com/GonzaloMonzonC/lumen-protocol). Para vulnerabilidades del MVM, reporta allí.

*Serie de agentes MIT de Cadences Lab — junto a [astrid](https://github.com/GonzaloMonzonC/astrid) e [iris](https://github.com/GonzaloMonzonC/iris).*
