# 🧪 Práctica: Testing del Simulador ESP-LEGO-SPIKE

## Descripción

Esta práctica contiene el **framework de pruebas automatizado** para el ESP-LEGO-SPIKE-Simulator, integrado al curso de MicroPython para el Aula de ABACOM.

## Contenido

```
practicas/testing-simulador/
├── pytest.ini                          # Configuración de pytest
├── src -> ../../../ESP-LEGO-SPIKE-Simulator/src  # Link al código del simulador
└── tests/
    ├── conftest.py                     # Fixtures y mocks globales
    ├── test_infrastructure.py          # 7 tests de infraestructura
    ├── test_motor.py                   # 70 tests de motor
    ├── test_motor_pair.py              # 27 tests de par de motores
    ├── test_distance_sensor.py         # 25 tests de sensor de distancia
    ├── test_color_sensor.py            # 29 tests de sensor de color
    ├── test_force_sensor.py            # 21 tests de sensor de fuerza
    ├── test_light_matrix.py            # 71 tests de matriz de luces
    ├── test_buttons.py                 # 22 tests de botones
    ├── test_speaker.py                 # 34 tests de speaker
    ├── test_integration.py             # 38 tests de integración
    ├── test_utils/                     # Módulos mock
    │   ├── mock_machine.py
    │   ├── mock_time.py
    │   ├── mock_random.py
    │   ├── mock_framebuf.py
    │   ├── mock_neopixel.py
    │   └── mock_ustruct.py
    └── student/                        # Tests para evaluar estudiantes
        ├── test_tareas_estudiantes.py          # Método 1: Tests por tarea (23 tests)
        ├── test_ejecutar_codigo_estudiante.py  # Método 2: Código directo (7 tests)
        └── test_verificar_ejemplos_curso.py   # Método 3: Ejemplos del curso (50 tests)
```

## Instalación

```bash
cd practicas/testing-simulador

# Crear entorno virtual
python3 -m venv venv
source venv/bin/activate

# Instalar pytest
pip install pytest
```

## Ejecutar Tests

```bash
# Todos los tests
python3 -m pytest tests/ -v

# Solo tests unitarios
python3 -m pytest tests/ -m unit -v

# Solo tests de integración
python3 -m pytest tests/ -m integration -v

# Tests de estudiantes
python3 -m pytest tests/student/ -v
```

## Ubicación en el Curso

Esta práctica se encuentra en la **Unidad 5: Proyecto Final** del curso de MicroPython para el Aula.

Documento: `contenido/unidad5/2_practica_testing_simulador.qmd`

## Total de Tests

| Categoría | Tests |
|-----------|-------|
| Unitarios | 312 |
| Integración | 38 |
| Estudiantes | 80 |
| **TOTAL** | **430** |

---

*Práctica de Testing - MicroPython para el Aula - ABACOM - Diego Saavedra 2026*
