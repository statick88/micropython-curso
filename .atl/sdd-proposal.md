# Propuesta SDD: Actualización de evaluaciones y quizzes a SPIKE Essential Python

## Contexto
El curso de MicroPython para LEGO Education SPIKE Essential ha sido parcialmente actualizado de sintaxis Pybricks a la API oficial de SPIKE Essential. Los laboratorios y contenidos principales ya utilizan la API oficial, pero las evaluaciones y quizzes aún contienen sintaxis de Pybricks que debe actualizarse para mantener consistencia.

## Problema
Los archivos de evaluación y quizzes aún utilizan:
- Importaciones de Pybricks (`from pybricks.hubs import PrimeHub`, etc.)
- Métodos específicos de Pybricks que no existen en la API oficial de SPIKE
- Sintaxis que confunde a los estudiantes al aprender la plataforma oficial

## Objetivo
Actualizar todos los archivos de evaluación y quizzes para utilizar exclusivamente la API oficial de SPIKE Essential Python, manteniendo el mismo nivel de dificultad y objetivos educativos.

## Alcance
- `evaluaciones/eval_motores_avanzados.qmd`
- `evaluaciones/eval_sensores_adicionales.qmd` 
- `evaluaciones/eval_telemetria.qmd`
- `quizzes/quiz_unidad1.qmd`
- `quizzes/quiz_unidad2.qmd`
- `quizzes/quiz_unidad3.qmd`
- `quizzes/quiz_unidad4.qmd`
- `quizzes/quiz_unidad5.qmd`

## Beneficios
1. Consistencia total en todo el curso usando API oficial
2. Eliminación de confusión entre plataformas (Pybricks vs SPIKE)
3. Mejor alineación con la documentación oficial de LEGO Education
4. Preparación de los estudiantes para usar recursos oficiales de LEGO
5. Reducción del soporte necesario para resolver problemas de sintaxis

## Criterios de éxito
- Todos los archivos utilizan exclusivamente `import spike` y métodos de la API oficial
- Ninguna referencia a `pybricks` en el contenido principal
- Los ejercicios mantienen el mismo nivel de desafío educativo
- Se incluyen comentarios explicativos cuando sea necesario para la transición
- Se crea un apéndice opcional con referencia a Pybricks para estudiantes avanzados