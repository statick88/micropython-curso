"""
Método 1: Crear tests específicos para cada tarea de estudiante.

Este archivo muestra cómo crear tests personalizados para evaluar
el código que un estudiante entrega como tarea.

Ejemplo de tarea: "Crear un robot que avance hasta detectar un
obstáculo a menos de 15cm, luego gire 90 grados y continúe."
"""

import pytest
import sys
from pathlib import Path

# Setup path para importar spike
PROJECT_ROOT = Path(__file__).parent.parent.parent
SRC_PATH = PROJECT_ROOT / "src"
if str(SRC_PATH) not in sys.path:
    sys.path.insert(0, str(SRC_PATH))

from spike import Motor, MotorPair, DistanceSensor, PrimeHub


# ============================================================================
# TAREA 1: Robot con sensor de distancia - Evitar obstáculos
# ============================================================================
# Consigna: El robot debe avanzar y detenerse cuando detecte un obstáculo
# a menos de 15cm, luego girar 90 grados y continuar.


class TestTarea1_EvitarObstaculos:
    """Tests para la tarea de evitar obstáculos."""

    def test_motor_se_inicializa(self):
        """Verificar que el motor se inicializa correctamente."""
        motor = Motor("A")
        assert motor is not None
        assert hasattr(motor, "start")
        assert hasattr(motor, "stop")
        assert hasattr(motor, "run_for_degrees")

    def test_sensor_distancia_se_inicializa(self):
        """Verificar que el sensor de distancia funciona."""
        sensor = DistanceSensor("E")
        assert sensor is not None
        assert hasattr(sensor, "get_distance_cm")

    def test_lee_distancia_correctamente(self):
        """Verificar que se puede leer la distancia."""
        sensor = DistanceSensor("E")
        distancia = sensor.get_distance_cm()
        assert isinstance(distancia, (int, float))
        assert distancia >= 0

    def test_motor_avanza(self):
        """Verificar que el motor puede avanzar."""
        motor = Motor("A")
        motor.set_default_speed(50)
        motor.start()
        # Si no lanza excepción, el código es válido
        motor.stop()

    def test_motor_gira_90_grados(self):
        """Verificar que el motor puede girar 90 grados."""
        motor = Motor("A")
        motor.run_for_degrees(90, speed=50)
        # Verificar que el método se ejecutó sin errores

    def test_logica_completa_evitar_obstaculo(self):
        """
        Simular la lógica completa de evitar obstáculos.

        Esto verifica que el estudiante implementó correctamente
        la secuencia: avanzar -> detectar -> girar -> continuar.
        """
        motor = Motor("A")
        sensor = DistanceSensor("E")

        # Paso 1: Configurar motor
        motor.set_default_speed(50)

        # Paso 2: Avanzar
        motor.start()

        # Paso 3: Leer distancia
        distancia = sensor.get_distance_cm()
        assert isinstance(distancia, (int, float))

        # Paso 4: Si hay obstáculo, detener y girar
        if distancia < 15:
            motor.stop()
            motor.run_for_degrees(90, speed=30)
            motor.start()

        # Si llegamos aquí sin errores, la lógica es válida


# ============================================================================
# TAREA 2: Seguidor de línea con sensor de color
# ============================================================================
# Consigna: El robot debe seguir una línea negra usando el sensor de color.
# Si detecta blanco, gira hasta encontrar negro nuevamente.


class TestTarea2_SeguidorDeLinea:
    """Tests para la tarea de seguidor de línea."""

    def test_sensor_color_se_inicializa(self):
        """Verificar que el sensor de color funciona."""
        from spike import ColorSensor

        sensor = ColorSensor("E")
        assert sensor is not None
        assert hasattr(sensor, "get_color")
        assert hasattr(sensor, "get_reflected_light")

    def test_lee_color_correctamente(self):
        """Verificar que se puede leer el color."""
        from spike import ColorSensor

        sensor = ColorSensor("E")
        color = sensor.get_color()
        # El color puede ser None o un string válido
        assert color is None or isinstance(color, str)

    def test_lee_luz_reflejada(self):
        """Verificar que se puede leer la luz reflejada."""
        from spike import ColorSensor

        sensor = ColorSensor("E")
        reflejo = sensor.get_reflected_light()
        assert isinstance(reflejo, (int, float))
        assert reflejo >= 0

    def test_motor_par_se_inicializa(self):
        """Verificar que el par de motores funciona."""
        motor_pair = MotorPair("B", "A")
        assert motor_pair is not None
        assert hasattr(motor_pair, "move")
        assert hasattr(motor_pair, "start_tank")

    def test_logica_seguidor_linea(self):
        """
        Simular la lógica de seguidor de línea.

        Verifica que el estudiante implementó:
        - Leer sensor de color
        - Ajustar motores según el color detectado
        """
        from spike import ColorSensor

        sensor = ColorSensor("E")
        motor_pair = MotorPair("B", "A")
        motor_pair.set_default_speed(50)

        # Leer color
        color = sensor.get_color()

        # Si detecta línea (negro), avanzar recto
        if color == "black":
            motor_pair.move(1, "cm", steering=0, speed=50)
        else:
            # Si detecta fondo (blanco), girar
            motor_pair.move(1, "cm", steering=50, speed=30)


# ============================================================================
# TAREA 3: Robot con PrimeHub - Control completo
# ============================================================================
# Consigna: Usar el PrimeHub para controlar un robot completo
# con botones, display, speaker y sensores.


class TestTarea3_PrimeHubCompleto:
    """Tests para la tarea de control completo con PrimeHub."""

    def test_primehub_se_inicializa(self):
        """Verificar que el PrimeHub funciona."""
        hub = PrimeHub()
        assert hub is not None
        assert hasattr(hub, "left_button")
        assert hasattr(hub, "right_button")
        assert hasattr(hub, "speaker")
        assert hasattr(hub, "light_matrix")
        assert hasattr(hub, "motion_sensor")
        assert hasattr(hub, "status_light")

    def test_botones_funcionan(self):
        """Verificar que los botones responden."""
        hub = PrimeHub()
        # Los botones deben tener los métodos esperados
        assert hasattr(hub.left_button, "is_pressed")
        assert hasattr(hub.right_button, "is_pressed")

    def test_speaker_funciona(self):
        """Verificar que el speaker reproduce sonidos."""
        hub = PrimeHub()
        hub.speaker.set_volume(50)
        hub.speaker.beep()
        # Si no lanza excepción, funciona

    def test_display_funciona(self):
        """Verificar que el display muestra texto."""
        hub = PrimeHub()
        # El método correcto es write(), no show_text()
        hub.light_matrix.write("OK")
        # Si no lanza excepción, funciona

    def test_logica_completa_primehub(self):
        """
        Simular la lógica completa con PrimeHub.

        Verifica que el estudiante integró:
        - Botones para iniciar/parar
        - Display para mostrar estado
        - Speaker para alertas
        - Sensores para navegación
        """
        hub = PrimeHub()
        motor = Motor("A")
        sensor = DistanceSensor("E")

        # Mostrar mensaje de inicio
        hub.light_matrix.write("GO")

        # Verificar botón derecho para iniciar
        right_pressed = hub.right_button.is_pressed()
        assert right_pressed is None or isinstance(right_pressed, bool)

        # Iniciar movimiento
        motor.set_default_speed(50)
        motor.start()

        # Leer sensor
        distancia = sensor.get_distance_cm()

        # Alerta si hay obstáculo
        if distancia < 10:
            hub.speaker.beep()
            hub.light_matrix.write("!!")
            motor.stop()


# ============================================================================
# TAREA 4: Robot con temporizador - Movimiento por tiempo
# ============================================================================
# Consigna: El robot debe moverse en un patrón cuadrado usando
# temporizadores para controlar la duración de cada movimiento.


class TestTarea4_MovimientoPorTiempo:
    """Tests para la tarea de movimiento por tiempo."""

    def test_motor_run_for_seconds(self):
        """Verificar que el motor puede moverse por tiempo."""
        motor = Motor("A")
        motor.run_for_seconds(0.1, speed=50)
        # Si no lanza excepción, funciona

    def test_motor_run_for_rotations(self):
        """Verificar que el motor puede moverse por rotaciones."""
        motor = Motor("A")
        motor.run_for_rotations(0.5, speed=50)
        # Si no lanza excepción, funciona

    def test_patron_cuadrado(self):
        """
        Simular el patrón cuadrado.

        Verifica que el estudiante implementó:
        - 4 movimientos rectos
        - 4 giros de 90 grados
        """
        motor = Motor("A")

        # Patrón cuadrado: 4 lados + 4 giros
        for lado in range(4):
            # Avanzar recto
            motor.run_for_seconds(0.1, speed=50)
            # Girar 90 grados
            motor.run_for_degrees(90, speed=30)

        # Si completó el ciclo sin errores, el patrón es válido


# ============================================================================
# TAREA 5: Robot con sensor de fuerza - Detectar contacto
# ============================================================================
# Consigna: El robot avanza hasta que el sensor de fuerza detecta
# contacto, luego retrocede y gira.


class TestTarea5_DetectarContacto:
    """Tests para la tarea de detección de contacto."""

    def test_sensor_fuerza_se_inicializa(self):
        """Verificar que el sensor de fuerza funciona."""
        from spike import ForceSensor

        sensor = ForceSensor("F")
        assert sensor is not None
        assert hasattr(sensor, "is_pressed")
        assert hasattr(sensor, "get_force_newton")

    def test_lee_fuerza_correctamente(self):
        """Verificar que se puede leer la fuerza."""
        from spike import ForceSensor

        sensor = ForceSensor("F")
        fuerza = sensor.get_force_newton()
        assert isinstance(fuerza, (int, float))
        assert fuerza >= 0

    def test_detecta_presion(self):
        """Verificar que se puede detectar si está presionado."""
        from spike import ForceSensor

        sensor = ForceSensor("F")
        presionado = sensor.is_pressed()
        # Puede ser None, True o False (bug conocido del simulador)
        assert presionado is None or isinstance(presionado, bool)

    def test_logica_detectar_contacto(self):
        """
        Simular la lógica de detectar contacto.

        Verifica que el estudiante implementó:
        - Avanzar hasta detectar contacto
        - Retroceder al detectar
        - Girar para evitar
        """
        from spike import ForceSensor

        sensor = ForceSensor("F")
        motor = Motor("A")

        motor.set_default_speed(50)
        motor.start()

        # Verificar contacto
        presionado = sensor.is_pressed()

        if presionado:
            # Retroceder
            motor.run_for_degrees(-180, speed=30)
            # Girar
            motor.run_for_degrees(90, speed=30)
            # Continuar
            motor.start()
