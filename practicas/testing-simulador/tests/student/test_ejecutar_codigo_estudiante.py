"""
Método 2: Ejecutar código del estudiante directamente.

Este método permite tomar el archivo .py que entregó el estudiante
y ejecutarlo dentro del framework de tests para verificar que:
1. No tiene errores de sintaxis
2. Importa correctamente los módulos de spike
3. Se ejecuta sin lanzar excepciones

Instrucciones:
1. Copiar el archivo .py del estudiante en este directorio
   Ejemplo: cp /ruta/tarea_estudiante.py tests/student/tarea_estudiante.py
2. Ejecutar: python3 -m pytest tests/student/ -v
"""

import pytest
import sys
import importlib.util
from pathlib import Path

# Setup path para importar spike
PROJECT_ROOT = Path(__file__).parent.parent.parent
SRC_PATH = PROJECT_ROOT / "src"
if str(SRC_PATH) not in sys.path:
    sys.path.insert(0, str(SRC_PATH))


def load_student_module(file_path):
    """
    Carga un módulo de Python desde un archivo sin ejecutarlo como script principal.

    Args:
        file_path: Ruta al archivo .py del estudiante

    Returns:
        El módulo cargado o None si falla
    """
    file_path = Path(file_path)
    if not file_path.exists():
        return None

    spec = importlib.util.spec_from_file_location(file_path.stem, file_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


# ============================================================================
# Ejemplo 1: Código de estudiante - Motor básico
# ============================================================================
# Este es un ejemplo de código que un estudiante podría entregar.
# En la práctica, reemplace este código con el archivo real del estudiante.

STUDENT_CODE_MOTOR = """
from spike import Motor

# Tarea: Hacer que el motor gire 360 grados
motor = Motor('A')
motor.set_default_speed(50)
motor.run_for_degrees(360)
"""

STUDENT_CODE_SENSOR = """
from spike import DistanceSensor, Motor

# Tarea: Robot que avanza y frena ante obstáculo
motor = Motor('A')
sensor = DistanceSensor('E')

motor.set_default_speed(50)
motor.start()

distancia = sensor.get_distance_cm()
if distancia < 15:
    motor.stop()
    print(f"Obstáculo detectado a {distancia} cm")
"""

STUDENT_CODE_PRIMEHUB = """
from spike import PrimeHub, Motor

# Tarea: Controlar robot con PrimeHub
hub = PrimeHub()
motor = Motor('A')

# Mostrar mensaje de inicio (usar write() en lugar de show_text())
hub.light_matrix.write("GO")

# Iniciar motor
motor.set_default_speed(50)
motor.start()

# Verificar botón
pressed = hub.right_button.is_pressed()
if pressed:
    hub.speaker.beep()
    motor.stop()
"""


class TestEjecutarCodigoEstudiante:
    """Tests para ejecutar código de estudiantes directamente."""

    def test_codigo_motor_basico(self):
        """
        Ejemplo: Ejecutar código básico de motor.

        Este test simula cargar y ejecutar el código que un estudiante
        entregaría como archivo .py
        """
        # Crear un módulo temporal con el código del estudiante
        import types

        student_module = types.ModuleType("student_motor")

        # Ejecutar el código del estudiante en el contexto del módulo
        exec(STUDENT_CODE_MOTOR, student_module.__dict__)

        # Verificar que se crearon las variables esperadas
        assert hasattr(student_module, "motor")
        assert student_module.motor is not None

    def test_codigo_sensor_distancia(self):
        """
        Ejemplo: Ejecutar código con sensor de distancia.
        """
        import types

        student_module = types.ModuleType("student_sensor")

        exec(STUDENT_CODE_SENSOR, student_module.__dict__)

        # Verificar que se crearon las variables esperadas
        assert hasattr(student_module, "motor")
        assert hasattr(student_module, "sensor")
        assert hasattr(student_module, "distancia")

    def test_codigo_primehub(self):
        """
        Ejemplo: Ejecutar código con PrimeHub completo.
        """
        import types

        student_module = types.ModuleType("student_primehub")

        exec(STUDENT_CODE_PRIMEHUB, student_module.__dict__)

        # Verificar que se crearon las variables esperadas
        assert hasattr(student_module, "hub")
        assert hasattr(student_module, "motor")


class TestCargarArchivoEstudiante:
    """
    Tests para cargar archivos .py reales de estudiantes.

    Uso:
    1. Copiar el archivo del estudiante en tests/student/
    2. Agregar un test aquí que apunte al archivo
    """

    def test_cargar_archivo_existente(self):
        """
        Ejemplo de cómo cargar un archivo real del estudiante.

        Descomente y ajuste la ruta para usar con un archivo real.
        """
        # Ejemplo:
        # student_file = Path(__file__).parent / "tarea_juan_perez.py"
        # if student_file.exists():
        #     module = load_student_module(student_file)
        #     assert module is not None
        #     assert hasattr(module, "motor")  # Verificar variable esperada
        pass

    def test_verificar_sintaxis_archivo(self):
        """
        Verificar que un archivo .py del estudiante tiene sintaxis válida.

        Este test solo verifica que el archivo se puede compilar,
        no que se ejecute correctamente.
        """
        import py_compile

        # Verificar que los ejemplos del curso tienen sintaxis válida
        examples_dir = SRC_PATH / "example"

        # Verificar algunos ejemplos clave
        examples_to_check = [
            "01.Getting_started/getting_started.part2_controlling_motors.py",
            "01.Getting_started/getting_started.part6_using_distance_sensor.py",
            "01.Getting_started/getting_started.part8_Driving.py",
        ]

        for example in examples_to_check:
            example_path = examples_dir / example
            if example_path.exists():
                # py_compile.compile lanza SyntaxError si hay errores
                try:
                    py_compile.compile(str(example_path), doraise=True)
                except py_compile.PyCompileError as e:
                    pytest.fail(f"Error de sintaxis en {example}: {e}")


class TestCodigoEstudianteConFixture:
    """
    Tests usando fixtures para evaluar código de estudiantes.

    Este enfoque es útil cuando quiere evaluar múltiples estudiantes
    con los mismos criterios.
    """

    @pytest.fixture
    def student_motor_code(self):
        """Fixture con código de ejemplo de motor."""
        return """
from spike import Motor
motor = Motor('A')
motor.set_default_speed(75)
motor.run_for_seconds(1, 75)
"""

    @pytest.fixture
    def student_sensor_code(self):
        """Fixture con código de ejemplo de sensor."""
        return """
from spike import DistanceSensor
sensor = DistanceSensor('E')
distancia = sensor.get_distance_cm()
"""

    def test_evaluar_motor(self, student_motor_code):
        """Evaluar código de motor del estudiante."""
        import types

        module = types.ModuleType("eval_motor")
        exec(student_motor_code, module.__dict__)
        assert hasattr(module, "motor")

    def test_evaluar_sensor(self, student_sensor_code):
        """Evaluar código de sensor del estudiante."""
        import types

        module = types.ModuleType("eval_sensor")
        exec(student_sensor_code, module.__dict__)
        assert hasattr(module, "sensor")
        assert hasattr(module, "distancia")


# ============================================================================
# Función helper para agregar nuevos estudiantes rápidamente
# ============================================================================


def crear_test_estudiante(nombre, archivo_py):
    """
    Función helper para crear tests de estudiantes rápidamente.

    Uso en un archivo separado:

    from tests.student.test_ejecutar_codigo_estudiante import crear_test_estudiante

    class TestJuanPerez(crear_test_estudiante("Juan Perez", "tarea_juan.py")):
        pass

    Args:
        nombre: Nombre del estudiante (para mensajes de error)
        archivo_py: Nombre del archivo .py en este directorio

    Returns:
        Una clase de test que verifica el código del estudiante
    """
    student_file = Path(__file__).parent / archivo_py

    class StudentTest:
        def test_codigo_compila(self):
            """Verificar que el código compila sin errores de sintaxis."""
            import py_compile

            if not student_file.exists():
                pytest.skip(f"Archivo no encontrado: {archivo_py}")

            try:
                py_compile.compile(str(student_file), doraise=True)
            except py_compile.PyCompileError as e:
                pytest.fail(f"[{nombre}] Error de sintaxis: {e}")

        def test_codigo_ejecuta(self):
            """Verificar que el código se ejecuta sin excepciones."""
            if not student_file.exists():
                pytest.skip(f"Archivo no encontrado: {archivo_py}")

            module = load_student_module(student_file)
            assert module is not None, f"[{nombre}] No se pudo cargar el módulo"

    return StudentTest
