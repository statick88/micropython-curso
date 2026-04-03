# Especificaciones para actualización de evaluaciones y quizzes a SPIKE Essential Python

## Requisitos Funcionales

### RF1: Actualización de evaluaciones
El sistema debe actualizar los archivos de evaluación para utilizar exclusivamente la API oficial de SPIKE Essential Python.

#### RF1.1: eval_motores_avanzados.qmd
- Reemplazar todas las importaciones de `pybricks` por `spike`
- Convertir `Motor(Port.A)` a `Motor('A')`
- Convertir `DriveBase` a `MotorPair`
- Actualizar métodos de sensores según la API oficial
- Mantener los mismos ejercicios y objetivos de aprendizaje

#### RF1.2: eval_sensores_adicionales.qmd
- Actualizar uso de ColorSensor, DistanceSensor, ForceSensor
- Utilizar métodos oficiales: `get_color()`, `get_distance_cm()`, `is_pressed()`
- Eliminar referencias a métodos de Pybricks como `.reflection()`, `.distance()`
- Preservar los ejercicios de telemetría y evitación de obstáculos

#### RF1.3: eval_telemetria.qmd
- Actualizar uso de PrimeHub (botones, light_matrix, speaker)
- Utilizar métodos oficiales: `is_pressed()`, `show_image()`, `beep()`
- Convertir uso de motores a métodos oficiales de SPIKE
- Mantener ejercicios de telemetría de batería y estado del hub

### RF2: Actualización de quizzes
El sistema debe asegurar que todos los quizzes utilizan sintaxis oficial de SPIKE.

#### RF2.1: Consistencia en quizzes
- Verificar que no haya importaciones de `pybricks`
- Asegurar que las preguntas referencien métodos oficiales
- Mantener el mismo nivel de dificultad conceptual
- Actualizar ejemplos de código en las preguntas

#### RF2.2: Formato de preguntas
- Las preguntas de opción múltiple deben referirse a métodos oficiales
- Los ejercicios de completado deben usar sintaxis SPIKE
- Las preguntas de verdadero/falso deben ser precisas respecto a la API oficial

### RF3: Creación de apéndice de referencia
El sistema debe crear un apéndice opcional que référence métodos de Pybricks para estudiantes avanzados.

#### RF3.1: Apéndice de métodos alternativos
- Documentar equivalencias entre Pybricks y SPIKE donde aplique
- Marcar claramente como referencia opcional
- Incluir únicamente para estudiantes que ya conocen Pybricks
- No interferir con el aprendizaje principal de SPIKE

## Requisitos No Funcionales

### RNF1: Consistencia educativa
- Mantener los mismos objetivos de aprendizaje en todas las actualizaciones
- Preservar el nivel de dificultad de los ejercicios
- No reducir la rigurosidad académica al cambiar de sintaxis

### RNF2: Claridad y legibilidad
- El código debe ser claro y seguir las convenciones de SPIKE
- Comentarios explicativos cuando sea necesario para la transición
- Uso consistente de nombramiento y formato

### RNF3: Complejidad mínima
- Realizar los cambios mínimos necesarios para lograr la actualización
- No reestructurar ejercicios a menos que sea absolutamente necesario por incompatibilidad de API
- Preservar la estructura original siempre que sea posible

## Criterios de Aceptación

### AC1: Actualización de evaluaciones
- [ ] eval_motores_avanzados.qmd utiliza exclusivamente API oficial de SPIKE
- [ ] eval_sensores_adicionales.qmd utiliza exclusivamente API oficial de SPIKE  
- [ ] eval_telemetria.qmd utiliza exclusivamente API oficial de SPIKE
- [ ] Ningún archivo contiene la palabra "pybricks" en el contenido principal (excepto en apéndices de referencia)
- [ ] Todos los ejercicios son resolubles con la documentación oficial de SPIKE

### AC2: Actualización de quizzes
- [ ] Todos los quizzes utilizan exclusivamente API oficial de SPIKE
- [ ] Las preguntas hacen referencia correcta a métodos oficiales
- [ ] Ningún quiz contiene sintaxis de Pybricks en preguntas o respuestas
- [ ] El nivel de dificultad conceptual se mantiene

### AC3: Apéndice de referencia
- [ ] Se crea un apéndice opcional con referencia a Pybricks
- [ ] Está claramente marcado como referencia opcional/avanzada
- [ ] No aparece en el flujo principal del curso
- [ ] Contiene equivalencias útiles para estudiantes que vienen de Pybricks

### AC4: Verificación final
- [ ] Revisión completa de todo el curso confirma uso exclusivo de SPIKE API en contenido principal
- [ ] Los apéndices de referencia están separados y claramente identificados
- [ ] Ningún estudiante se confundirá por mezclas de sintaxis en el material principal