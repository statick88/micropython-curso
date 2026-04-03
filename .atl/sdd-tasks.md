# Desglose de Tareas para Actualización de Evaluaciones y Quizzes a SPIKE Essential Python

## Fase 1: Preparación y Análisis

### Tarea 1.1: Crear propuesta SDD
- Descripción: Crear documento de propuesta que describa el problema, objetivo y alcance
- Archivo de salida: .atl/sdd-proposal.md
- Criterios de aceptación: Propuesta creada y revisada

### Tarea 1.2: Definir especificaciones técnicas
- Descripción: Crear documento detallado de requerimientos funcionales y no funcionales
- Archivo de salida: .atl/sdd-spec.md
- Criterios de aceptación: Especificaciones completas y revisadas

### Tarea 1.3: Diseñar solución técnica
- Descripción: Crear documento de diseño con mapeo de transformaciones y arquitectura
- Archivo de salida: .atl/sdd-design.md
- Criterios de aceptación: Diseño técnico completado

### Tarea 1.4: Desglosar en tareas específicas
- Descripción: Crear este documento de tareas específicas para cada archivo
- Archivo de salida: .atl/sdd-tasks.md
- Criterios de aceptación: Todas las tareas identificadas y estimadas

## Fase 2: Actualización de Evaluaciones

### Tarea 2.1: Actualizar eval_motores_avanzados.qmd
- Descripción: Convertir de sintaxis Pybricks a SPIKE Essential en evaluación de motores avanzados
- Archivo de entrada: evaluaciones/eval_motores_avanzados.qmd
- Archivo de salida: evaluaciones/eval_motores_avanzados.qmd (actualizado)
- Criterios de aceptación:
  - Ninguna importación de pybricks
  - Uso exclusivo de API oficial de SPIKE
  - Ejercicios mantienen mismo nivel de dificultad
  - Comentarios explicativos cuando sea necesario

### Tarea 2.2: Actualizar eval_sensores_adicionales.qmd
- Descripción: Convertir de sintaxis Pybricks a SPIKE Essential en evaluación de sensores adicionales
- Archivo de entrada: evaluaciones/eval_sensores_adicionales.qmd
- Archivo de salida: evaluaciones/eval_sensores_adicionales.qmd (actualizado)
- Criterios de aceptación:
  - Uso oficial de ColorSensor, DistanceSensor, ForceSensor
  - Métodos como get_color(), get_distance_cm(), is_pressed()
  - Ninguna referencia a métodos de Pybricks como .reflection(), .distance()
  - Ejercicios de telemetría preservados

### Tarea 2.3: Actualizar eval_telemetria.qmd
- Descripción: Convertir de sintaxis Pybricks a SPIKE Essential en evaluación de telemetría
- Archivo de entrada: evaluaciones/eval_telemetria.qmd
- Archivo de salida: evaluaciones/eval_telemetria.qmd (actualizado)
- Criterios de aceptación:
  - Uso oficial de PrimeHub (botones, light_matrix, speaker)
  - Métodos como is_pressed(), show_image(), beep()
  - Uso oficial de motores y sensores
  - Ejercicios de telemetría de batería preservados

## Fase 3: Actualización de Quizzes

### Tarea 3.1: Revisar y actualizar quiz_unidad1.qmd
- Descripción: Verificar que quiz de unidad 1 use sintaxis oficial de SPIKE
- Archivo de entrada: quizzes/quiz_unidad1.qmd
- Archivo de salida: quizzes/quiz_unidad1.qmd (actualizado si es necesario)
- Criterios de aceptación:
  - No hay importaciones de pybricks
  - Preguntas referencian métodos oficiales
  - Nivel de dificultad mantenido

### Tarea 3.2: Revisar y actualizar quiz_unidad2.qmd
- Descripción: Verificar que quiz de unidad 2 use sintaxis oficial de SPIKE
- Archivo de entrada: quizzes/quiz_unidad2.qmd
- Archivo de salida: quizzes/quiz_unidad2.qmd (actualizado si es necesario)
- Criterios de aceptación:
  - Consistencia con SPIKE API
  - Preguntas válidas respecto a la documentación oficial
  - Mismo nivel de dificultad conceptual

### Tarea 3.3: Revisar y actualizar quiz_unidad3.qmd
- Descripción: Verificar que quiz de unidad 3 use sintaxis oficial de SPIKE
- Archivo de entrada: quizzes/quiz_unidad3.qmd
- Archivo de salida: quizzes/quiz_unidad3.qmd (actualizado si es necesario)
- Criterios de aceptación:
  - Uso correcto de terminología oficial
  - Preguntas que puedan responderse con documentación oficial
  - Ninguna confusión entre plataformas

### Tarea 3.4: Revisar y actualizar quiz_unidad4.qmd
- Descripción: Verificar que quiz de unidad 4 use sintaxis oficial de SPIKE
- Archivo de entrada: quizzes/quiz_unidad4.qmd
- Archivo de salida: quizzes/quiz_unidad4.qmd (actualizado si es necesario)
- Criterios de aceptación:
  - Referencias correctas a sensores oficiales
  - Preguntas sobre métodos reales de la API
  - Ejemplos de código válidos

### Tarea 3.5: Revisar y actualizar quiz_unidad5.qmd
- Descripción: Verificar que quiz de unidad 5 use sintaxis oficial de SPIKE
- Archivo de entrada: quizzes/quiz_unidad5.qmd
- Archivo de salida: quizzes/quiz_unidad5.qmd (actualizado si es necesario)
- Criterios de aceptación:
  - Consistencia con proyecto final
  - Preguntas apropiadas para nivel avanzado
  - Uso oficial de toda la API estudiada

## Fase 4: Creación de Recursos de Referencia

### Tarea 4.1: Crear apéndice de métodos alternativos
- Descripción: Crear documento de referencia opcional con equivalencias Pybricks→SPIKE
- Archivo de salida: apendice_pybricks_referencia.qmd
- Criterios de aceptación:
  - Claro marcado como "REFERENCIA OPCIONAL"
  - Tabla de equivalencias de importaciones
  - Tabla de equivalencias de métodos comunes
  - Notas sobre diferencias conceptuales
  - No interfiere con aprendizaje principal

## Fase 5: Verificación y Cierre

### Tarea 5.1: Verificación final de consistencia
- Descripción: Revisar todo el curso para confirmar uso exclusivo de SPIKE API en contenido principal
- Archivos a revisar: Todos los .qmd en contenido/, evaluaciones/, quizzes/
- Criterios de aceptación:
  - Contenido principal usa exclusivamente API oficial
  - Referencias a Pybricks solo en apéndices claramente marcados
  - Ningún estudiante se confundirá por mezclas de sintaxis

### Tarea 5.2: Actualizar registro de cambios SDD
- Descripción: Documentar lo accomplished y preparar para archivado
- Archivo de salida: .atl/sdd-status.md (opcional)
- Criterios de aceptación: Registro de lo completado para trazabilidad

## Estimación de Esfuerzo

### Evaluaciones (3 archivos)
- eval_motores_avanzados.qmd: 2 horas
- eval_sensores_adicionales.qmd: 2.5 horas  
- eval_telemetria.qmd: 2 horas
- **Subtotal evaluaciones: 6.5 horas**

### Quizzes (5 archivos)
- Cada quiz: ~0.5-1 hora dependiendo de la cantidad de código
- **Subtotal quizzes: 3-5 horas**

### Apéndice de referencia: 1.5 horas

### Preparación y verificación: 2 horas

### **TOTAL ESTIMADO: 13-15 horas**

## Dependencias

- Ninguna tarea depende de otra excepto las tareas de preparación (1.1-1.4) que deben completarse antes de las fases 2-4
- Las tareas dentro de cada fase pueden realizarse en paralelo
- La tarea 5.1 (verificación final) debe realizarse después de completar todas las actualizaciones