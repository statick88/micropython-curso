# Diseño Técnico para Actualización de Evaluaciones y Quizzes a SPIKE Essential Python

## Arquitectura de la Solución

La actualización seguirá un enfoque de transformación directa de archivos, donde cada archivo será analizado y sus referencias a Pybricks serán reemplazadas por equivalentes en la API oficial de SPIKE Essential Python.

### Principios de Diseño

1. **Consistencia con el curso existente**: Utilizar las mismas convenciones y estilo que los archivos ya actualizados
2. **Minimalismo en cambios**: Cambiar únicamente lo necesario para lograr la actualización
3. **Preservación de objetivos educativos**: Mantener el mismo nivel de dificultad y conceptos enseñados
4. **Separación de preocupaciones**: Mantener el contenido principal separado de referencias opcionales

### Mapeo de Transformaciones Pybricks → SPIKE

#### Importaciones
- `from pybricks.hubs import PrimeHub` → `from spike import PrimeHub`
- `from pybricks.pupdevices import Motor, ColorSensor, DistanceSensor, ForceSensor` → `from spike import Motor, ColorSensor, DistanceSensor, ForceSensor`
- `from pybricks.parameters import Port, Direction, Stop, Color` → `from spike import Port` (Nota: SPIKE maneja puertos como strings)
- `from pybricks.robotics import DriveBase` → `from spike import MotorPair`
- `from pybricks.tools import wait` → `from spike.control import wait`

#### Puertos
- `Port.A` → `'A'` (string)
- `Port.B` → `'B'` (string)
- etc.

#### Motores
- `Motor(Port.A)` → `Motor('A')`
- `DriveBase(left_motor, right_motor, wheel_diameter, axle_track)` → `MotorPair('A', 'B')`
- `drive_base.straight(distance)` → `motor_pair.move(trotations, 0, speed)` o equivalente
- `drive_base.turn(angle)` → `motor_pair.move(trotations, 100, speed)` para giro

#### Sensores
- `ColorSensor(Port.S3)` → `ColorSensor('C')` (Nota: mapeo de puertos S1-S4 a A-D)
- `color.reflection()` → `color_sensor.get_reflected_light()`
- `color.color()` → `color_sensor.get_color()`
- `color.ambient()` → `color_sensor.get_ambient_light()`
- `DistanceSensor(Port.S4)` → `DistanceSensor('D')`
- `distance.distance()` → `distance_sensor.get_distance_cm()`
- `distance.distance(inches=True)` → `distance_sensor.get_distance_inches()`
- `ForceSensor(Port.S1)` → `ForceSensor('A')`
- `force.force()` → `force_sensor.get_force()`
- `force.pressed()` → `force_sensor.is_pressed()`

#### PrimeHub
- `hub.buttons.pressed()` → Verificar botones individuales: `hub.left_button.is_pressed()`, etc.
- `hub.display` → `hub.light_matrix`
- `display.pixel()` → `light_matrix.set_pixel()`
- `display.off()` → `light_matrix.off()`
- `speaker.beep()` → Mantener igual (ya es oficial)

### Estructura de Archivos

Cada archivo se actualizará manteniendo su estructura original:
- Títulos y descripciones permanecerán iguales
- Los ejercicios se actualizarán en su código pero mantendrán el mismo objetivo
- Los bloques de código se convertirán de Pybricks a SPIKE
- Se agregarán comentarios explicativos cuando sea necesario para clarificar la transición

### Manejo de Incompatibilidades

Cuando no exista un equivalente directo en SPIKE:
1. Buscar la alternativa más cercana en la API oficial
2. Si es necesario cambiar el enfoque del ejercicio, mantener el mismo concepto enseñado
3. Documentar la razón del cambio en comentarios si es significativa
4. En casos extremos, crear un ejercicio equivalente que enseñe el mismo concepto

### Apéndice de Referencia Opcional

Se creará un nuevo archivo: `apendice_pybricks_referencia.qmd` que contendrá:
- Tabla de equivalencias de importaciones
- Tabla de equivalencias de puertos
- Tabla de equivalencias de métodos comunes
- Notas importantes sobre diferencias conceptuales
- Claro marcado como "REFERENCIA OPCIONAL - Solo para estudiantes avanzados que ya conocen Pybricks"

## Detalles Técnicos por Tipo de Archivo

### Para Archivos .qmd (Quarto Markdown)
- Preservar la sintaxis de Quarto (--- para metadata, ## para títulos)
- Los bloques de código se identificaran por ```python y ``` 
- Solo se modificarán los contenidos dentro de los bloques de código
- El texto explicativo alrededor permanecerá igual excepto para actualizar referencias a métodos

### Proceso de Actualización
1. Lectura del archivo original
2. Identificación de bloques de código Python
3. Aplicación de transformaciones según el mapeo definido
4. Verificación de que el código resultante sea válido según la API oficial
5. Escritura del archivo actualizado
6. Revisión manual de casos especiales

## Herramientas y Recursos

- Documentación oficial de SPIKE Essential Python: https://spike.legoeducation.com/essential/help/lls-help-python
- Los archivos ya actualizados en el curso como referencia de estilo
- El conocimiento de las diferencias entre plataformas adquirido durante la actualización previa

## Consideraciones de Calidad

1. **Testing implícito**: Cada bloque de código actualizado debería ser conceptualmente válido (aunque no se ejecute automáticamente)
2. **Consistencia de estilo**: Seguir el mismo estilo de comentarios y formato que los archivos ya actualizados
3. **Documentación de cambios**: Los cambios significativos se documentarán en comentarios dentro del código cuando ayuden a la comprensión
4. **Backup implícito**: El sistema de git proporciona versionado, por lo que siempre se puede regresar si es necesario