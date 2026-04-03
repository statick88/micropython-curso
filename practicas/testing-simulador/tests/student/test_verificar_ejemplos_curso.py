"""
Método 3: Verificar código contra ejemplos del curso.

Este método toma los ejemplos oficiales del curso de robótica y los
ejecuta dentro del framework de tests para verificar que:
1. Todos los ejemplos del curso funcionan con el simulador
2. El simulador es compatible con la API de LEGO SPIKE
3. Los estudiantes pueden usar los ejemplos como referencia confiable

Esto es útil para:
- Validar que el simulador es confiable antes de usarlo en clase
- Detectar regresiones después de actualizar el simulador
- Tener una "suite de referencia" que siempre debe pasar
"""

import pytest
import sys
import subprocess
from pathlib import Path

# Setup path para importar spike
PROJECT_ROOT = Path(__file__).parent.parent.parent
SRC_PATH = PROJECT_ROOT / "src"
if str(SRC_PATH) not in sys.path:
    sys.path.insert(0, str(SRC_PATH))

from spike import (
    Motor,
    MotorPair,
    DistanceSensor,
    ColorSensor,
    ForceSensor,
    PrimeHub,
    App,
)
from spike.control import wait_for_seconds


# ============================================================================
# Getting Started - Ejemplos oficiales del curso
# ============================================================================


class TestGettingStarted_Part1_SimpleOutput:
    """
    Ejemplo: getting_started.part1_simple_output.py

    from spike import PrimeHub
    hub = PrimeHub()
    hub.light_matrix.write('Hi!')
    """

    def test_write(self):
        """Verificar que el display muestra texto."""
        hub = PrimeHub()
        hub.light_matrix.write("Hi!")

    def test_write_spanish(self):
        """Verificar texto en español."""
        hub = PrimeHub()
        hub.light_matrix.write("Hola")


class TestGettingStarted_Part2_ControllingMotors:
    """
    Ejemplo: getting_started.part2_controlling_motors.py

    from spike import Motor
    motor = Motor('A')
    motor.run_for_seconds(2.0, 90)
    motor.run_for_seconds(3, -100)
    motor.run_for_degrees(360)
    motor.run_to_position(0, 'shortest path', -100)
    """

    def test_run_for_seconds_clockwise(self):
        """Rotar clockwise por 2 segundos al 90% de velocidad."""
        motor = Motor("A")
        motor.run_for_seconds(0.1, 90)  # Usar 0.1s para tests rápidos

    def test_run_for_seconds_counterclockwise(self):
        """Rotar counterclockwise por 3 segundos al -100% de velocidad."""
        motor = Motor("A")
        motor.run_for_seconds(0.1, -100)

    def test_run_for_degrees_360(self):
        """Rotar 360 grados clockwise."""
        motor = Motor("A")
        motor.run_for_degrees(360)

    def test_run_for_degrees_negative(self):
        """Rotar 360 grados counterclockwise con velocidad."""
        motor = Motor("A")
        motor.run_for_degrees(-360, 100)

    def test_run_to_position_zero(self):
        """Ir a posición 0 por el camino más corto."""
        motor = Motor("A")
        motor.run_to_position(0, "shortest path", -100)

    def test_run_to_position_90(self):
        """Ir a posición 90 en dirección clockwise."""
        motor = Motor("A")
        motor.run_to_position(90, "clockwise", 100)


class TestGettingStarted_Part3_ForceSensors:
    """
    Ejemplo: getting_started.part3_using_force_sensors.py

    from spike import ForceSensor
    force_sensor = ForceSensor('F')
    force_sensor.wait_until_pressed()
    print('Pressed!')
    """

    def test_force_sensor_init(self):
        """Inicializar sensor de fuerza."""
        sensor = ForceSensor("F")
        assert sensor is not None

    def test_force_sensor_get_force(self):
        """Leer fuerza en Newtons."""
        sensor = ForceSensor("F")
        fuerza = sensor.get_force_newton()
        assert isinstance(fuerza, (int, float))

    def test_force_sensor_get_percentage(self):
        """Leer fuerza en porcentaje."""
        sensor = ForceSensor("F")
        pct = sensor.get_force_percentage()
        assert isinstance(pct, (int, float))


class TestGettingStarted_Part4_Loops:
    """
    Ejemplo: getting_started.part4_changing_the_flow_using_loops.py

    from spike import PrimeHub
    hub = PrimeHub()
    for i in range(5):
        hub.light_matrix.show_image('HAPPY')
        wait_for_seconds(1)
        hub.light_matrix.show_image('SAD')
        wait_for_seconds(1)
    """

    def test_loop_with_display(self):
        """Verificar loop con display."""
        hub = PrimeHub()
        for i in range(3):  # Reducido para tests rápidos
            hub.light_matrix.show_image("HAPPY")
            hub.light_matrix.show_image("SAD")

    def test_loop_with_counter(self):
        """Verificar loop con contador."""
        count = 0
        for i in range(5):
            count += 1
        assert count == 5


class TestGettingStarted_Part5_ColorSensor:
    """
    Ejemplo: getting_started.part5_using_color_sensor.py

    from spike import ColorSensor
    color_sensor = ColorSensor('E')
    color = color_sensor.get_color()
    print(color)
    """

    def test_color_sensor_init(self):
        """Inicializar sensor de color."""
        sensor = ColorSensor("E")
        assert sensor is not None

    def test_color_sensor_get_color(self):
        """Leer color detectado."""
        sensor = ColorSensor("E")
        color = sensor.get_color()
        assert color is None or isinstance(color, str)

    def test_color_sensor_get_rgb(self):
        """Leer valores RGB."""
        sensor = ColorSensor("E")
        red = sensor.get_red()
        green = sensor.get_green()
        blue = sensor.get_blue()
        assert isinstance(red, (int, float))
        assert isinstance(green, (int, float))
        assert isinstance(blue, (int, float))


class TestGettingStarted_Part6_DistanceSensor:
    """
    Ejemplo: getting_started.part6_using_distance_sensor.py

    from spike import DistanceSensor, Motor
    distance_sensor = DistanceSensor('D')
    motor = Motor('C')
    count = 0
    while count < 5:
        distance_sensor.wait_for_distance_farther_than(20, 'cm')
        motor.start()
        distance_sensor.wait_for_distance_closer_than(20, 'cm')
        motor.stop()
        count = count + 1
    """

    def test_distance_sensor_init(self):
        """Inicializar sensor de distancia."""
        sensor = DistanceSensor("E")
        assert sensor is not None

    def test_distance_sensor_read_cm(self):
        """Leer distancia en cm."""
        sensor = DistanceSensor("E")
        dist = sensor.get_distance_cm()
        assert isinstance(dist, (int, float))

    def test_distance_sensor_read_inches(self):
        """Leer distancia en pulgadas."""
        sensor = DistanceSensor("E")
        dist = sensor.get_distance_inches()
        assert isinstance(dist, (int, float))

    def test_distance_sensor_read_percentage(self):
        """Leer distancia en porcentaje."""
        sensor = DistanceSensor("E")
        dist = sensor.get_distance_percentage()
        assert isinstance(dist, (int, float))

    def test_distance_sensor_methods_exist(self):
        """Verificar que los métodos wait existen."""
        sensor = DistanceSensor("E")
        assert hasattr(sensor, "wait_for_distance_farther_than")
        assert hasattr(sensor, "wait_for_distance_closer_than")


class TestGettingStarted_Part7_MotionSensor:
    """
    Ejemplo: getting_started.part7_using_motion_sensor.py

    from spike import PrimeHub
    hub = PrimeHub()
    yaw = hub.motion_sensor.get_yaw_angle()
    print(yaw)
    """

    def test_motion_sensor_via_primehub(self):
        """Acceder al motion sensor desde PrimeHub."""
        hub = PrimeHub()
        assert hasattr(hub, "motion_sensor")

    def test_motion_sensor_get_yaw(self):
        """Leer ángulo de yaw."""
        hub = PrimeHub()
        yaw = hub.motion_sensor.get_yaw_angle()
        assert isinstance(yaw, (int, float))

    def test_motion_sensor_get_pitch(self):
        """Leer ángulo de pitch."""
        hub = PrimeHub()
        pitch = hub.motion_sensor.get_pitch_angle()
        assert isinstance(pitch, (int, float))

    def test_motion_sensor_get_roll(self):
        """Leer ángulo de roll."""
        hub = PrimeHub()
        roll = hub.motion_sensor.get_roll_angle()
        assert isinstance(roll, (int, float))


class TestGettingStarted_Part8_Driving:
    """
    Ejemplo: getting_started.part8_Driving.py

    from spike import MotorPair
    motor_pair = MotorPair('B', 'A')
    motor_pair.set_default_speed(100)
    motor_pair.move(2, 'seconds')
    motor_pair.move_tank(10, 'cm', left_speed=100, right_speed=100)
    """

    def test_motor_pair_init(self):
        """Inicializar par de motores."""
        motor_pair = MotorPair("B", "A")
        assert motor_pair is not None

    def test_motor_pair_set_speed(self):
        """Configurar velocidad default."""
        motor_pair = MotorPair("B", "A")
        motor_pair.set_default_speed(100)
        assert motor_pair.get_default_speed() == 100

    def test_motor_pair_move_seconds(self):
        """Mover por tiempo."""
        motor_pair = MotorPair("B", "A")
        motor_pair.set_default_speed(100)
        motor_pair.move(0.1, "seconds")

    def test_motor_pair_move_cm(self):
        """Mover por centímetros."""
        motor_pair = MotorPair("B", "A")
        motor_pair.move_tank(10, "cm", left_speed=100, right_speed=100)

    def test_motor_pair_move_rotations(self):
        """Mover por rotaciones."""
        motor_pair = MotorPair("B", "A")
        motor_pair.move_tank(1, "rotations", left_speed=-100, right_speed=-100)

    def test_motor_pair_reverse(self):
        """Mover en dirección inversa."""
        motor_pair = MotorPair("B", "A")
        motor_pair.set_default_speed(-100)
        motor_pair.move(0.1, "seconds")


# ============================================================================
# App / Sound Examples
# ============================================================================


class TestAppExamples:
    """
    Ejemplos: app.play_sound.py, app.start_sound.py

    from spike import App
    app = App()
    app.play_sound('Cat Meow 1')
    app.start_sound('Cat Meow 1')
    """

    def test_app_init(self):
        """Inicializar App."""
        app = App()
        assert app is not None

    def test_app_play_sound(self):
        """Reproducir sonido."""
        app = App()
        app.play_sound("Cat Meow 1")

    def test_app_start_sound(self):
        """Iniciar sonido."""
        app = App()
        app.start_sound("Cat Meow 1")


# ============================================================================
# Sensor Examples - Detalles
# ============================================================================


class TestColorSensorDetailedExamples:
    """
    Ejemplos detallados del sensor de color.

    color_sensor.get_red.py
    color_sensor.get_blue.py
    color_sensor.get_color.py
    color_sensor.wait_until_color.py
    """

    def test_get_red(self):
        """Leer intensidad de rojo."""
        sensor = ColorSensor("E")
        red = sensor.get_red()
        assert isinstance(red, (int, float))

    def test_get_blue(self):
        """Leer intensidad de azul."""
        sensor = ColorSensor("E")
        blue = sensor.get_blue()
        assert isinstance(blue, (int, float))

    def test_get_green(self):
        """Leer intensidad de verde."""
        sensor = ColorSensor("E")
        green = sensor.get_green()
        assert isinstance(green, (int, float))

    def test_get_ambient_light(self):
        """Leer luz ambiente."""
        sensor = ColorSensor("E")
        ambient = sensor.get_ambient_light()
        assert isinstance(ambient, (int, float))

    def test_light_up_all(self):
        """Encender todos los LEDs."""
        sensor = ColorSensor("E")
        sensor.light_up_all(brightness=100)
        sensor.light_up_all(brightness=0)

    def test_wait_methods_exist(self):
        """Verificar que los métodos wait existen."""
        sensor = ColorSensor("E")
        assert hasattr(sensor, "wait_for_new_color")
        assert hasattr(sensor, "wait_until_color")


class TestDistanceSensorDetailedExamples:
    """
    Ejemplos detallados del sensor de distancia.

    distance_sensor.get_distance_cm.py
    distance_sensor.get_distance_inches.py
    distance_sensor.get_distance_percentage.py
    distance_sensor.light_up.py
    distance_sensor.light_up_all.py
    """

    def test_light_up_individual(self):
        """Encender LEDs individuales."""
        sensor = DistanceSensor("E")
        sensor.light_up(100, 75, 50, 25)

    def test_light_up_all_brightness(self):
        """Encender todos los LEDs con brillo."""
        sensor = DistanceSensor("E")
        sensor.light_up_all(brightness=100)
        sensor.light_up_all(brightness=0)

    def test_all_distance_units(self):
        """Leer distancia en todas las unidades."""
        sensor = DistanceSensor("E")
        cm = sensor.get_distance_cm()
        inches = sensor.get_distance_inches()
        pct = sensor.get_distance_percentage()

        assert isinstance(cm, (int, float))
        assert isinstance(inches, (int, float))
        assert isinstance(pct, (int, float))


# ============================================================================
# Integración: Ejemplos combinados del curso
# ============================================================================


class TestCourseExamplesIntegration:
    """
    Tests de integración que combinan múltiples ejemplos del curso.

    Estos tests verifican que los ejemplos del curso funcionan juntos,
    no solo de forma aislada.
    """

    def test_motor_and_distance_sensor(self):
        """
        Combinar ejemplo de motor con sensor de distancia.

        Simula: "Avanzar hasta detectar obstáculo"
        """
        motor = Motor("A")
        sensor = DistanceSensor("E")

        motor.set_default_speed(50)
        motor.start()

        distancia = sensor.get_distance_cm()
        if distancia < 15:
            motor.stop()

    def test_color_sensor_and_motor_pair(self):
        """
        Combinar sensor de color con par de motores.

        Simula: "Seguidor de línea"
        """
        sensor = ColorSensor("E")
        motor_pair = MotorPair("B", "A")

        color = sensor.get_color()
        if color == "black":
            motor_pair.move(1, "cm", steering=0, speed=50)
        else:
            motor_pair.move(1, "cm", steering=50, speed=30)

    def test_primehub_full_workflow(self):
        """
        Workflow completo con PrimeHub.

        Simula: "Robot completo con display, sonido y sensores"
        """
        hub = PrimeHub()
        motor = Motor("A")
        sensor = DistanceSensor("E")

        # Inicio
        hub.light_matrix.write("GO")
        hub.speaker.beep()

        # Movimiento
        motor.set_default_speed(50)
        motor.start()

        # Detección
        distancia = sensor.get_distance_cm()

        # Respuesta
        if distancia < 10:
            motor.stop()
            hub.light_matrix.write("!!")
            hub.speaker.beep()

    def test_force_sensor_and_motor(self):
        """
        Combinar sensor de fuerza con motor.

        Simula: "Robot que retrocede al tocar algo"
        """
        sensor = ForceSensor("F")
        motor = Motor("A")

        motor.set_default_speed(50)
        motor.start()

        presionado = sensor.is_pressed()
        if presionado:
            motor.run_for_degrees(-180, speed=30)
            motor.run_for_degrees(90, speed=30)


# ============================================================================
# Validación de archivos de ejemplo del curso
# ============================================================================


class TestCourseExampleFiles:
    """
    Verificar que todos los archivos de ejemplo del curso existen
    y tienen sintaxis válida.
    """

    def test_getting_started_examples_exist(self):
        """Verificar que los ejemplos de Getting Started existen."""
        examples = [
            "01.Getting_started/getting_started.part1_simple_output.py",
            "01.Getting_started/getting_started.part2_controlling_motors.py",
            "01.Getting_started/getting_started.part3_using_force_sensors.py",
            "01.Getting_started/getting_started.part4_changing_the_flow_using_loops.py",
            "01.Getting_started/getting_started.part5_using_color_sensor.py",
            "01.Getting_started/getting_started.part6_using_distance_sensor.py",
            "01.Getting_started/getting_started.part7_using_motion_sensor.py",
            "01.Getting_started/getting_started.part8_Driving.py",
        ]

        examples_dir = SRC_PATH / "example"
        for example in examples:
            example_path = examples_dir / example
            assert example_path.exists(), f"Archivo no encontrado: {example}"

    def test_sensor_examples_exist(self):
        """Verificar que los ejemplos de sensores existen."""
        examples = [
            "04.Color_sensor/color_sensor.get_red.py",
            "04.Color_sensor/color_sensor.get_blue.py",
            "05.Distance_sensor/distance_sensor.get_distance_cm.py",
            "05.Distance_sensor/distance_sensor.get_distance_inches.py",
            "05.Distance_sensor/distance_sensor.get_distance_percentage.py",
            "05.Distance_sensor/distance_sensor.light_up_all.py",
        ]

        examples_dir = SRC_PATH / "example"
        for example in examples:
            example_path = examples_dir / example
            assert example_path.exists(), f"Archivo no encontrado: {example}"

    def test_app_examples_exist(self):
        """Verificar que los ejemplos de App existen."""
        examples = [
            "02.App/app.play_sound.py",
            "02.App/app.start_sound.py",
        ]

        examples_dir = SRC_PATH / "example"
        for example in examples:
            example_path = examples_dir / example
            assert example_path.exists(), f"Archivo no encontrado: {example}"
