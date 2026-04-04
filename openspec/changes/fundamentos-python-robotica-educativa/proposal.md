# Proposal: Fundamentos de Python para Robótica Educativa con LEGO Spike Prime

## Intent

Crear un módulo introductorio enfocado en los fundamentos de Python necesarios para comprender y trabajar efectivamente con la robótica educativa utilizando LEGO Spike Prime. Este módulo abordará la brecha entre conocimientos básicos de programación y la aplicación específica en robótica, preparando a los estudiantes con los conceptos esenciales antes de iniciar el trabajo práctico con el hardware.

## Scope

### In Scope
- Conceptos básicos de Python: variables, tipos de datos, operadores
- Estructuras de control: condicionales, bucles, funciones
- Manejo de errores y depuración básica
- Trabajo con listas y diccionarios sencillos
- Entrada/salida básica en consola
- Aplicación de estos conceptos a problemas simples de robótica
- Ejercicios prácticos sin necesidad de hardware (usando simuladores o ejercicios teóricos)

### Out of Scope
- Programación avanzada de LEGO Spike Prime (API específica)
- Trabajo directo con sensores y motores
- Compilación y flashing de firmware
- Integración con Thonny u otros IDEs específicos
- Proyectos complejos que requieran múltiples sensores actuando simultáneamente

## Approach

El módulo seguirá la metodología de enseñanza de Diego Saavedra:
1. **Analogías Primero**: Cada concepto se introducirá con ejemplos de la vida cotidiana antes de mostrar código
2. **Método Socrático**: Se plantearán preguntas guiantes para fomentar el descubrimiento
3. **Código como Comunicación**: Enfoque en nombres descriptivos y comentarios que expliquen el "por qué"
4. **Pensamiento Atómico**: Descomposición de problemas en piezas pequeñas y manejables
5. **Aprendizaje Basado en Desafíos**: 70% práctica, 30% teoría - resolver primero, comprender después
6. **Enfoque Práctico**: Ejercicios que produzcan resultados visibles inmediatamente
7. **Prompt Engineering Excellence**: Para generar visuales y diagramas educativos

Los conceptos se enseñarán mediante ejemplos relacionados con robótica (incluso sin hardware) para crear conexión inmediata con el objetivo final.

## Affected Areas

| Area | Impact | Description |
|------|--------|-------------|
| `contenido/unidad0/` | Modified | Se agregará un nuevo subdirectorio `fundamentos_python/` con los materiales del módulo |
| `contenido/unidad0/competencias_docente.qmd` | Modified | Se actualizará para incluir las nuevas competencias relacionadas con los fundamentos de Python |
| `evaluaciones/` | Nueva | Se crearán nuevas evaluaciones formativas específicas para este módulo |
| `quizzes/` | Nueva | Se crearán nuevos quizzes para autoevaluación de los fundamentos de Python |
| `ejersicios/` | Nueva | Se agregarán ejercicios prácticos enfocados en los conceptos de Python aplicados a robótica |

## Risks

| Risk | Likelihood | Mitigation |
|------|------------|------------|
| Los estudiantes pueden encontrar aburrido aprender conceptos sin ver aplicación inmediata en hardware | Medio | Usar analogías fuertes y ejemplos que conecten claramente con robótica incluso sin hardware |
| Sobrelapamiento con contenido existente de la Unidad 0 | Bajo | Revisar y coordinar con el contenido existente para evitar redundancias |
| Dificultad para evaluar comprensión sin ejecución de código real | Medio | Crear ejercicios de predicción de salida y corrección de código que validen comprensión lógica |
| Resistencia de docentes acostumbrados a comenzar directamente con el hardware | Bajo | Mostrar cómo una base sólida en Python reduce frustración y aumenta éxito posterior |

## Rollback Plan

1. Remover el directorio `contenido/unidad0/fundamentos_python/` creado
2. Revertir cambios en `contenido/unidad0/competencias_docente.qmd` a su estado anterior
3. Eliminar cualquier evaluación, quiz o ejercicio creado específicamente para este módulo
4. Notificar a los docentes sobre el cambio y proporcionar materiales de respaldo si es necesario

## Dependencies

- Ninguna dependencia externa específica - el módulo está diseñado para ser independiente de hardware
- Se recomienda acceso a un intérprete de Python (puede ser en línea como https://www.python.org/shell/)
- Para los ejercicios visuales, se utilizará la capacidad de generación de imágenes mediante IA con el marco R-C-T-R-F

## Success Criteria

- [ ] Estudiantes pueden explicar conceptos básicos de Python usando analogías relacionadas con robótica
- [ ] Estudiantes pueden escribir y predecir la salida de programas simples de Python
- [ ] Estudiantes pueden identificar y corregir errores sintácticos básicos en código de Python
- [ ] Estudiantes pueden aplicar estructuras de control a problemas simples de lógica de robótica
- [ ] Al menos el 80% de los estudiantes aprueba las evaluaciones formativas del módulo
- [ ] Feedback positivo de docentes sobre la preparación que brinda este módulo para el trabajo posterior con hardware
