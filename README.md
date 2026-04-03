# Curso de MicroPython con LEGO SPIKE Essential

## 📖 Visión General

Este curso integral enseña programación **MicroPython** aplicada a la robótica educativa utilizando el **LEGO SPIKE Essential Hub (45678)**. Diseñado específicamente para docentes y estudiantes de niveles básicos e intermedios, el curso combina teoría sólida con práctica hands-on para desarrollar competencias en pensamiento computacional, resolución de problemas y creatividad tecnológica.

El enfoque pedagógico parte de analogías del mundo real antes de introducir código, siguiendo el método socrático para fomentar el descubrimiento activo en lugar de la memorización pasiva. Cada concepto se presenta primero con ejemplos concretos de la vida cotidiana (construcción, medicina, mecánica) antes de su implementación técnica.

## 🎯 Objetivos de Aprendizaje

Al completar este curso, los participantes podrán:

1. **Comprender los fundamentos** de la robótica educativa y el rol del Hub como "cerebro" del robot
2. **Programar en MicroPython** utilizando la API oficial de LEGO SPIKE Essential
3. **Controlar motores y sensores** para crear comportamientos robóticos complejos
4. **Implementar estructuras de control** (condicionales, bucles, funciones)
5. **Diagnosticar y depurar código** utilizando herramientas profesionales como el debugger de Thonny
6. **Diseñar y ejecutar proyectos integrales** que combinen múltiples sensores y actuadores
7. **Documentar y presentar soluciones** técnicas de manera clara y profesional
8. **Transferir conocimientos** a otros entornos de programación y plataformas de robótica

## 📚 Estructura del Curso

El curso está organizado en **6 unidades progresivas** que construyen conocimientos de manera acumulativa:

```
Micro_Python/
├── 📁 contenido/           # Lecciones y materiales didácticos principales
│   ├── 📁 unidad0/         # Preparación y competencias docentes
│   ├── 📁 unidad1/         # Introducción al Hub LEGO y primer contacto
│   ├── 📁 unidad2/         # Salida: pantalla, luces y sonidos
│   ├── 📁 unidad3/         # Movimiento: control de motores
│   ├── 📁 unidad4/         # Entrada: sensores y telemetría
│   ├── 📁 unidad5/         # Proyecto final: integración y creatividad
│   ├── 📁 diagramas/       # Visuales explicativos y esquemas
│   ├── 📁 apendices/       # Recursos adicionales y referencia
│   └── 📄 sistema_logros.qmd # Sistema de gamificación y logros
├── 📁 evaluaciones/        # Exámenes y rúbricas de evaluación
│   ├── eval_motores_avanzados.qmd
│   ├── eval_sensores_adicionales.qmd
│   └── eval_telemetria.qmd
├── 📁 quizzes/             # Cuestionarios de autoevaluación por unidad
│   ├── quiz_unidad1.qmd
│   ├── quiz_unidad2.qmd
│   ├── quiz_unidad3.qmd
│   ├── quiz_unidad4.qmd
│   └── quiz_unidad5.qmd
├── 📁 ejersicios/          # Prácticas guiadas y desafíos
├── 📁 firmware/            # Firmware pre-compilado para hubs SPIKE
├── 📁 docs/                # Documentación técnica y guías de instalación
├── 📁 pybricks-setup/      # Recursos para configuración del entorno de desarrollo
├── 📄 about.qmd            # Información sobre el curso y el instructor
├── 📄 license.qmd          # Detalles de licencia (CC BY 4.0)
├── 📄 index.qmd            # Página principal del curso
└── 📄 README.md            # Este archivo
```

### 📖 Unidad por Unidad

#### **Unidad 0: Preparación Docente**
- Competencias necesarias para impartir el curso
- Recursos y preparación del entorno de aprendizaje
- Estrategias de manejo de aula para actividades de robótica

#### **Unidad 1: El Hub LEGO - Desde Cero**
- ¿Qué es un Hub y por qué es el "cerebro" del robot?
- Componentes físicos del LEGO Technic Large Hub (45601)
- Instalación de Thonny y configuración del entorno
- Primer programa: "Hola Mundo" en la pantalla 5x5 LEDs
- Uso del debugger básico para verificación de código

#### **Unidad 2: Salida - Comunicación con el Mundo**
- Control de la matriz 5x5 LEDs para texto e iconos
- Manejo del LED de estado (colores y patrones)
- Generación de sonidos y melodías con el altavoz
- Animaciones secuenciales y sincronización temporal
- Proyecto: Créate tu propio emoticono robótico

#### **Unidad 3: Movimiento - Control de Motores**
- Tipos de motores en SPIKE Essential y sus aplicaciones
- Control preciso de velocidad, dirección y posición
- Uso de MotorPair para movimiento diferencial (robots con 2 ruedas)
- Implementación de frenado suave y de emergencia
- Proyecto: Robot que navega un laberinto siguiendo líneas

#### **Unidad 4: Entrada - Sensores y Percepción**
- Sensor de color: detección de reflejo y luz ambiental
- Sensor de distancia: medición ultrasónica en centímetros
- Sensor de fuerza: detección de presión y tacto
- Sensor de movimiento (IMU): orientación, giro y aceleración
- Lectura de batería y telemetría del sistema
- Proyecto: Robot que evita obstáculos y responde al tacto

#### **Unidad 5: Proyecto Final - Integración y Creatividad**
- Diseño de especificaciones técnicas para un desafío abierto
- Planificación y ejecución utilizando metodología de proyecto
- Integración de todos los componentes aprendidos
- Documentación técnica y presentación de resultados
- Evaluación por pares y retroalimentación constructiva

### 📋 Recursos Adicionales

#### **Apéndices de Referencia**
- **Apéndice Pybricks → SPIKE**: Mapeo completo de equivalencias entre APIs
- **Apéndice Thonny Debugger**: Guía profesional de depuración paso a paso
- **Apéndice Recursos Alternativos**: Plataformas económicas como micro:bit y OpenBot
- **Apéndice Compilación DIY**: Cómo compilar firmware personalizado
- **Apéndice Simuladores**: Opciones para practicar sin hardware físico

#### **Materiales de Soporte**
- Diagramas explicativos en formato QMD con visuales claros
- Guías de instalación para múltiples sistemas operativos
- Rúbricas de evaluación detalladas con criterios específicos
- Sistema de logros y gamificación para motivación estudiantil

## 🛠️ Requisitos y Opciones de Implementación

### ✅ Enfoque Recomendado: Entorno Web (Cero Instalación)
Para un inicio rápido y sin barreras técnicas:
1. Navegador web moderno (Chrome, Firefox, Safari, Edge)
2. Acceso a [Pybricks Code](https://code.pybricks.com/) - IDE oficial en línea
3. Cable USB-C (el que viene con el Hub LEGO)
4. LEGO SPIKE Essential Hub (45678) o LEGO Technic Large Hub (45601)

### 💻 Opción Local: Instalación Completa
Para quienes prefieren trabajar localmente o necesitan funcionalidad avanzada:
- **Sistema operativo**: Windows 10/11, macOS 12+, o Linux (Ubuntu/Debian recomendado)
- **Python 3.12+** (para herramientas de desarrollo local)
- **Git** (para versionado y actualización de materiales)
- **Thonny IDE** (versión 4.0+ recomendada)
- **Cable USB-C** y **Hub LEGO SPIKE Essential/Technic**

### 📱 Opciones Alternativas y de Bajo Costo
Documentadas en los apéndices para contextos con limitaciones presupuestarias:
- **BBC micro:bit V2** ($20-25) - MicroPython nativo, excelente para začátečníky
- **OpenBot** (~$50) - Usa tu smartphone Android como cerebro robótico
- **ESP-LEGO-SPIKE-Simulator** - Simulador open source para práctica sin hardware
- **Simulador básico en Thonny** - Práctica lógica sin ningún hardware

## 🧠 Metodología de Enseñanza

### 🔑 Principios Pedagógicos Fundamentales

#### 1. **Analogías Primero** (`ANALÓGICAS PRIMERO`)
Cada concepto técnico se introduce primero con ejemplos de la vida cotidiana:
- El Hub como cerebro humano
- Los motores como músculos
- Los sensores como ojos, oídos y piel
- La batería como sistema digestivo que proporciona energía

#### 2. **Método Socrático** (`MÉTODO SOCRÁTICO`)
En lugar de dar respuestas directas, se plantean preguntas que guían al descubrimiento:
- "¿Qué crees que pasaría si cambiamos este valor?"
- "¿Cómo podríamos hacer que el robot detenga su movimiento más suavemente?"
- "¿Qué sensor sería más adecuado para detectar esta situación específica?"

#### 3. **Código como Comunicación** (`CODE IS COMMUNICATION`)
Enfoque en la legibilidad y intención plutôt que en la mera funcionalidad:
- Nombres descriptivos que revelan propósito (`velocidad_maxima` vs `vm`)
- Comentarios que explican el *por qué*, no el *qué*
- Estructura lógica que sigue el flujo natural de pensamiento

#### 4. **Pensamiento Atómico** (`ATOMIC THINKING`)
Descomposición de problemas complejos en piezas manejables:
- Funciones pequeñas con una sola responsabilidad
- Módulos independientes que pueden probarse por separado
- Interfaces claras entre componentes

#### 5. **Aprendizaje Basado en Desafíos** (`CHALLENGE-DRIVEN LEARNING`)
El 70% del tiempo se dedica a resolver problemas prácticos:
- Desafíos graduados desde muy simples hasta proyectos integrales
- Solución primero, comprensión después (después de intentar, se explica la teoría)
- Retroalimentación inmediata a través del comportamiento del robot físico

#### 6. **Enfoque Práctico** (`ENFOQUE PRÁCTICO`)
"Enséñame, no solo cuéntame":
- Laboratorios con comandos específicos para escribir y ejecutar
- Proyectos que producen resultados tangibles y visibles
- Evitar ejemplos teóricos desconectados de la aplicación real

#### 7. **Excelencia en Prompt Engineering** (Para recursos visuales)
Cuando se generan diagramas o ilustraciones:
- Uso del marco R-C-T-R-F (Role, Context, Task, Restrictions, Format)
- Prevención de errores comunes de IA con negativos específicos
- Alineación de estilo-anatomía para apropiado nivel de detalle
- Consistencia de marca y credibilidad en todo material visual

## 📊 Sistema de Evaluación

### 📋 Tipos de Evaluación

#### **Evaluaciones Formativas** (Durante el aprendizaje)
- Quizzes cortos al final de cada unidad (5-10 preguntas)
- Laboratorios guiados con verificación de resultados
- Ejercicios de depuración y corrección de código
- Participación activa en discusiones y desafíos en clase

#### **Evaluaciones Sumativas** (Al final de cada bloque)
- **Evaluación de Motores Avanzados**: Control preciso, calibración y odometría
- **Evaluación de Sensores Adicionales**: Integración múltiple y toma de decisiones basada en sensores
- **Evaluación de Telemetría**: Monitoreo de sistema, diagnóstico y reporte de estado

#### **Evaluación Final**
- **Proyecto Integrador**: Diseño, construcción, programación y presentación de un robot que resuelva un desafío abierto
- **Rúbrica detallada** con criterios en: funcionalidad, calidad de código, documentación, trabajo en equipo y creatividad

### 📈 Criterios de Evaluación

| Criterio | Descripción | Peso |
|----------|-------------|------|
| **Funcionalidad** | El robot cumple con los requisitos específicados | 30% |
| **Calidad de Código** | Legibilidad, estructura, nombres descriptivos, comentarios útiles | 25% |
| **Documentación** | Explicación clara de diseño, decisiones y resultados | 20% |
| **Trabajo en Equipo** | Colaboración, distribución equitativa de tareas, comunicación | 15% |
| **Creatividad e Innovación** | Soluciones originales, mejoras al requerimiento básico | 10% |

## 🚀 Cómo Empezar

### Para Estudiantes
1. **Revisa la guía de instalación** en `docs/INSTALACION.md` según tu entorno preferido
2. **Comienza con la Unidad 1** en `contenido/unidad1/guia_hub_desde_cero.qmd`
3. **Completa el Laboratorio 1** (`contenido/unidad1/lab1_hola_mundo.qmd`)
4. **Haz el Quiz de la Unidad 1** en `quizzes/quiz_unidad1.qmd` para autoevaluarte
5. **Continúa secuencialmente** por las unidades 2 a 5

### Para Docentes
1. **Revisa las Competencias Docentes** en `contenido/unidad0/competencias_docente.qmd`
2. **Prepara el ambiente** siguiendo las recomendaciones de gestión de aula
3. **Revisa las rúbricas de evaluación** en el directorio `evaluaciones/`
4. **Adapta el ritmo** según las características y conocimientos previos de tu grupo
5. **Utiliza el Sistema de Logros** (`contenido/sistema_logros.qmd`) para motivación

### Para Autodidactas
1. **Elige tu entorno de implementación** (Web recomendado para empezar)
2. **Sigue el curso en orden** desde la Unidad 1 hasta la Unidad 5
3. **Completa todos los laboratorios** antes de pasar a la siguiente unidad
4. **Utiliza los apéndices** como referencia cuando necesites detalles específicos
5. **Participa en la comunidad** de Pybricks para compartir tus proyectos y aprender de otros

## 🔧 Soporte y Solución de Problemas

### 📚 Documentación de Soporte
- **Guía de Instalación**: `docs/INSTALACION.md` - Pasos detallados para todos los enfoques
- **Solución de Problemas Comunes**: `docs/TROUBLESHOOTING.md` - Errores frecuentes y sus soluciones
- **Referencia de Sintaxis SPIKE**: `contenido/referencia_sintaxis_spike.qmd` - API completa con ejemplos
- **Apéndice Thonny Debugger**: `contenido/apendice_thonny_debugger.qmd` - Depuración profesional paso a paso

### 🤝 Comunidad y Recursos Externos
- **Comunidad Oficial Pybricks**: https://pybricks.com/ - Foros, ejemplos y documentación
- **Repositorio GitHub Pybricks**: https://github.com/pybricks - Código fuente y contribuciones
- **LEGO Education SPIKE Essential**: https://education.lego.com/es-es/productos/essential - Información oficial del hardware
- **MicroPython Official Site**: https://micropython.org - Documentación del lenguaje base

## 📄 Licencia y Derechos de Uso

Este curso se distribuye bajo la licencia **Creative Commons Attribution 4.0 International (CC BY 4.0)**.

### 📋 ¿Qué significa CC BY 4.0?
- **Compartir**: Puedes copiar y redistribuir el material en cualquier medio o formato
- **Adaptar**: Puedes mezclar, transformar y crear a partir del material para cualquier propósito, incluso comercial
- **Atribución requerida**: Debes dar el crédito apropiado, proporcionar un enlace a la licencia y indicar si se hicieron cambios
- **Sin restricciones adicionales**: No puedes aplicar términos legales o medidas tecnológicas que restrinjan legalmente a otros hacer lo que la licencia permite

### 🏛️ Atribución Requerida
Al usar este material, debes atribuir de la siguiente manera:
```
Curso de MicroPython con LEGO SPIKE Essential por Diego Saavedra Garcia
Licencia: CC BY 4.0
```

## 👨‍🏫 Sobre el Instructor

**Diego Saavedra Garcia** es profesor de Ciencias de la Computación en la Escuela Superior Politécnica del Litoral (ESPE) y capacitador en ABACOM Capacitación y Servicios. Con más de 10 años de experiencia en desarrollo full-stack, arquitectura de software y ciberseguridad, combina su expertise técnico con una pasión genuina por la educación.

### Experiencia Docente
- **ESPE** (2023-2024): Desarrollo de Software, Seguridad Informática
- **ABACOM** (2022-Presente): Cursos de Ética Hacking, Pentesting y Ciberseguridad
- **Codings Academy** (2024): FullStack Development, DevOps y Web Development
- **IST Juan Montalvo** (2019-2022): Programación, TI y Robótica Educativa
- **Universidad del Zulia** (Académico): Investigación y Educación Superior

### Certificaciones Profesionales
- **CKA**: Certified Kubernetes Administrator (KodeKloud)
- **CKS**: Certified Kubernetes Security Specialist (En progreso)
- **eWPTXv2**: Web Application Penetration Testing (En progreso)

## 📅 Próximos Pasos y Actualizaciones

Este curso es un documento vivo que se actualiza periódicamente basado en:
- Retroalimentación de estudiantes y docentes
- Nuevas versiones del firmware LEGO SPIKE Essential
- Avances en la API de Pybricks y MicroPython
- Tendencias emergentes en robótica educativa

### 🔄 Última Actualización
**Abril 2026** - Conversión completa a LEGO SPIKE Essential API oficial, con referencia opcional a Pybricks.

### 📣 Sugerencias y Mejoras
Valiosísimamente apreciadas. Por favor:
1. Revisa si tu sugerencia ya está implementada en la versión actual
2. Verifica que esté alineada con los objetivos pedagógicos del curso
3. Envía tus propuestas a través del sistema de issues de este repositorio
4. Incluye ejemplos concretos y justificación pedagógica cuando sea posible

---

## 🎉 ¡Listo para Empezar!

Recuerda: **La robótica no es solo sobre construir máquinas que se mueven, es sobre resolver problemas reales con creatividad y perseverancia.**

Tu viaje comienza ahora. Conecta tu Hub, abre tu editor, y escribe esas primeras líneas de código que darán vida a tu primer robot.

**¡Éxitos en tu aventura de aprendizaje!** — Diego Saavedra Garcia  
Profesor, Investigador y Apasionado de la Educación Tecnológica  
Abril 2026

---

*Este README fue generado automáticamente basado en la estructura y contenido actual del curso. Para la información más actualizada, siempre revisa los archivos fuente en el repositorio.*