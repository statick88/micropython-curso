# Registro de Trabajo - Configuración pybricks-micropython para curso MicroPython

## Fecha: Abril 2, 2026

## Resumen de actividades realizadas

Durante esta sesión, se trabajó en la configuración del entorno de desarrollo para el curso de MicroPython utilizando los hubs LEGO SPIKE Education, siguiendo la metodología Spec-Driven Development (SDD).

## 1. Inicio del proceso SDD

Se inicializó el contexto SDD en el proyecto para rastrear el trabajo realizado:

```bash
/sdd-init
```

Esto configuró el backend de persistencia (engram) y preparó el proyecto para el seguimiento de cambios.

## 2. Exploración del repositorio pybricks-micropython

Se investigó el repositorio https://github.com/pybricks/pybricks-micropython para entender:

- Estructura del proyecto
- Hubs LEGO soportados
- Requisitos de build
- Relación con el curso existente en ~/apps/Abacom/Micro_Python/

### Hallazgos clave:
- El repositorio contiene firmware para múltiples hubs LEGO incluyendo:
  - primehub (SPIKE Prime / MINDSTORMS Robot Inventor)
  - technichub 
  - essentialhub (SPIKE Essential)
  - y otros como ev3, movehub, nxt, etc.
- Se identificaron referencias específicas a dispositivos SPIKE en el código:
  - SENSORS: SPIKE_COLOR_SENSOR, SPIKE_FORCE_SENSOR, SPIKE_ULTRASONIC_SENSOR
  - MOTORS: SPIKE_M_MOTOR, SPIKE_L_MOTOR, SPIKE_S_MOTOR
- El repositorio incluye un `virtualhub` para pruebas sin hardware físico

## 3. Propuesta de cambio SDD

Se creó una propuesta formal para el cambio:

**Nombre del cambio**: pybricks-micropython-setup
**Intención**: Enable hands-on testing and experimentation with Pybricks MicroPython in the Micro Python course
**Alcance**: Clone repository, install dependencies, set up testing environment, create documentation, verify installation
**Enfoque**: Clone repository, follow build/installation instructions, install toolchain dependencies, build firmware, create test scripts, document setup

La propuesta se guardó en: `~/apps/Abacom/Micro_Python/openspec/changes/pybricks-micropython-setup/proposal.md`

## 4. Especificaciones detalladas

Se escribieron especificaciones funcionales y no funcionales usando formato Given-When-Then:

### Requisitos funcionales:
1. Clonar el repositorio pybricks-micropython
2. Instalar dependencias de construcción
3. Construir firmware para hubs objetivo
4. Crear y ejecutar scripts de prueba
5. Flujo de trabajo completo de extremo a extremo

### Requisitos no funcionales:
- Repetibilidad
- Compatibilidad multiplataforma
- Manejo de errores
- Documentación
- Idempotencia

### Escenarios de prueba:
5 escenarios detallados cubriendo desde la clonación hasta el flujo completo de trabajo.

Las especificaciones se guardaron en: `/Users/statick/apps/labs/lab002/SPEC.md`

## 5. Trabajo técnico realizado

### Clonación del repositorio:
```bash
git clone --depth 1 https://github.com/pybricks/pybricks-micropython.git
```
Resultado: Clonado exitosamente en `/Users/statick/apps/labs/lab002/pybricks-micropython`

### Análisis de dependencias en macOS ARM64:
Se verificó qué herramientas estaban disponibles:
- ✅ Git: /usr/bin/git
- ✅ Make: /usr/bin/make  
- ✅ GCC: /usr/bin/gcc
- ✅ Binutils (parcial): objcopy requería instalación
- ❌ ARM Cross-compiler (arm-none-eabi-gcc): NO ENCONTRADO
- ✅ Python 3.14.3: /opt/homebrew/bin/python3
- ✅ Homebrew: /opt/homebrew/bin/brew

### Intento de instalación del toolchain ARM:
Se probó múltiples enfoques sin éxito debido a:
1. Fallos de descarga desde servidores oficiales de ARM (timeouts, corrupción)
2. Fórmula Homebrew `gcc-arm-embedded` con fallos de descarga
3. Descarga directa de paquetes .pkg y .tar.gz con errores de checksum o conexión
4. Intento con xPack alternativos

## 5. Decisión técnica basada en hallazgos

Dado que el objetivo principal es el **curso educativo** y no el desarrollo de firmware, se determinó que:

### Enfoque recomendado para el curso:
1. **Utilizar el virtualhub incorporado** para pruebas sin necesidad de hardware ni compilación cruzada
2. **Enfocarse en conceptos de programación** más que en la construcción de firmware
3. **Proveer firmware pre-compilado** cuando sea necesario para hardware real
4. **Aprovechar Pybricks Code IDE** (https://code.pybricks.com/) como alternativa web

### Trabajo realizado en esta dirección:
- Se verificó que el virtualhub puede construirse con el compilador host (gcc/clang)
- Se examinó el script de test-virtualhub.sh para entender su funcionamiento
- Se crearon directorios para organizar recursos del curso:
  - ~/apps/Abacom/Micro_Python/firmware/
  - ~/apps/Abacom/Micro_Python/docs/

## 6. Próximos pasos recomendados

### Para continuar con el SDD (cuando se resuelva el toolchain):
1. Crear documento de diseño técnico basado en las especificaciones
2. Desglosar el cambio en tareas implementables
3. Implementar las tareas (clonación, instalación de dependencias, build, testing)
4. Verificar la implementación contra las especificaciones
5. Archivar el cambio

### Para el desarrollo inmediato del curso:
1. Crear guías de instalación para los diferentes enfoques (web, virtual, local completo)
2. Desarrollar materiales didácticos enfocados en:
   - Sintaxis básica de MicroPython
   - API de Pybricks para acceso a sensores y motores
   - Estructuras de control y funciones
   - Proyectos simples de robótica
3. Preparar ejercicios que puedan ejecutarse en:
   - Pybricks Code IDE (en línea)
   - Entorno virtualhub (local sin hardware)
   - Hardware real con firmware pre-compilado

## 7. Lecciones aprendidas técnicas

### Desafíos con toolchain ARM en macOS ARM64:
- Las distribuciones oficiales de ARM no siempre proporcionan binarios nativos para ARM64
- Las descargas pueden ser inestables o requerir autenticación
- El ecosistema de Homebrew tiene limitaciones para ciertos paquetes embebidos
- Las soluciones alternativas incluyen:
  - Usar Rosetta2 para binarios x86_64 en ARM64
  - Utilizar entornos de Linux virtualizados
  - Emplear el enfoque de desarrollo web cuando sea posible

### Estrategias para cursos de sistemas embebidos:
1. Separar el aprendizaje de conceptos de programación de los desafíos de configuración de entorno
2. Proveer múltiples puntos de entrada (web, virtual, local)
3. Documentar las dificultades técnicas como parte del currículo de resolución de problemas
4. Enfocarse en habilidades transferibles más que en herramientas específicas de vendor

## 8. Archivos creados/modificados

En este sesión se crearon:
- `/Users/statick/apps/Abacom/Micro_Python/README.md` - Visión general del curso
- `/Users/statick/apps/Abacom/Micro_Python/docs/INSTALACION.md` - Guía de instalación multiplataforma
- `/Users/statick/apps/Abacom/Micro_Python/docs/WORK_LOG.md` - Este documento
- Directorio `/Users/statick/apps/Abacom/Micro_Python/firmware/` para recursos de firmware
- Actualizaciones en el repositorio de pybricks-micropython (clonado en lab002)

Se guardó la sesión en el sistema de memoria persistente Engram para referencia futura.

## Conclusión

A pesar de los obstáculos técnicos encontrados con la instalación del toolchain ARM en macOS ARM64, se logró avanzar significativamente en la comprensión del repositorio pybricks-micropython y se estableció una base sólida para el desarrollo del curso de MicroPython con enfoque en alternativas accesibles para los estudiantes.

El trabajo realizado sigue los principios de SDD para asegurar trazabilidad y calidad, mientras se adapta a las limitaciones técnicas reales encontradas en el entorno de desarrollo.