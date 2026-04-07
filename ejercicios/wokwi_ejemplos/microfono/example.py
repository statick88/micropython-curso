from spike import PrimeHub, Motor, MotorPair, DistanceSensor
from spike.control import wait_for_seconds, wait_until

# 1. Inicialización de componentes
hub = PrimeHub()
movimiento = MotorPair('C', 'D') # Motores en C y D
motor_e = Motor('E')            # Motor de dirección/sensor en E
sensor_distancia = DistanceSensor('F') # Sensor de distancia en F

# 2. Configuración inicial
movimiento.set_default_speed(30) # Velocidad al 30%
d1 = 200 # Valor inicial de la variable D1

while True:
    # Ir a posición 0 por la ruta más corta
    motor_e.run_to_position(0, 'shortest path')
    
    # Mostrar flecha hacia arriba en la matriz
    hub.light_matrix.show_image('ARROW_N')
    
    # Empezar a mover hacia adelante
    movimiento.start()
    
    # Esperar hasta que la distancia sea menor a 35 cm
    # Se añade validación para evitar errores si el sensor devuelve None
    wait_until(lambda: sensor_distancia.get_distance_cm() is not None and 
               sensor_distancia.get_distance_cm() < 35)
    
    # Parar el movimiento
    movimiento.stop()
    
    # Mostrar cuadrado central (Stop)
    hub.light_matrix.show_image('SQUARE')
    
    # Girar motor E a 270 grados
    motor_e.run_to_position(270, 'shortest path')
    wait_for_seconds(0.2)
    
    # Guardar lectura actual en la variable D1
    lectura_actual = sensor_distancia.get_distance_cm()
    if lectura_actual is not None:
        d1 = lectura_actual
        
    # Girar motor E a 90 grados
    motor_e.run_to_position(90, 'shortest path')
    wait_for_seconds(0.2)
    
    # Lógica de comparación y decisión
    distancia_final = sensor_distancia.get_distance_cm()
    
    if distancia_final is not None and distancia_final > d1:
        # Si hay más espacio a la derecha
        hub.light_matrix.show_image('ARROW_E')
        # Mover derecha -0.5 rotaciones (giro sobre eje)
        movimiento.move(-0.5, 'rotations', steering=100)
    else:
        # Si hay más espacio a la izquierda (o igual)
        hub.light_matrix.show_image('ARROW_W')
        # Mover izquierda -0.5 rotaciones
        movimiento.move(-0.5, 'rotations', steering=-100)