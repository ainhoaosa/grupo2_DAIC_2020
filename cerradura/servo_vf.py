
import RPi.GPIO as GPIO
import time

#global maxi
#maxi = 30


# Configuracion del servo
servoPin = 17
#GPIO.setmode(GPIO.BOARD)
GPIO.setmode(GPIO.BCM) 
GPIO.setup(servoPin, GPIO.OUT)
pwm = GPIO.PWM(servoPin, 100)
ang_inicio = 0
ang_final = 110
DELAY = 0.05
incStep = 5
global pos
pos = 0
global posicion_actual
posicion_actual = 0


def AngleToDuty(ang):

    return float(pos)/10.+5.


def estado_cerradura(contador, maxi):

    print("CONTADOR: {}".format(contador))

    if contador >= maxi:
        estado = 1  # Cerradura cerrada
        print("Cerradura cerrada")

    if contador < maxi:
        estado = 0  # Cerradura abierta
        print("Cerradura abierta")

    return estado


# def posicion_servo(estado, posicion):
#
#     print("POSICION: {}°".format(posicion))
#
#     if estado == 1:
#         posicion = ang_final
#         print("Cerradura cerrada")
#
#     if estado == 0:
#         posicion = ang_inicio
#         print("Cerradura abierta°")
#
#     return posicion
def cambio(contador, maxi):
    global posicion_actual
    global pos

    
    estado = estado_cerradura(contador, maxi)

    if estado == 1 and posicion_actual == 0:
        pwm.start(AngleToDuty(pos))  # star pwm
        i = 1
        while i:
            for pos in range(ang_inicio, ang_final, incStep):
                duty = AngleToDuty(pos)
                pwm.ChangeDutyCycle(duty)
                time.sleep(DELAY)
            i = 0
        posicion_actual = 1
        #pwm.stop()
    if estado == 1 and posicion_actual == 1:
        posicion_actual = 1

    if estado == 0 and posicion_actual == 1:
        pwm.start(AngleToDuty(pos))  # star pwm
        i = 1
        while i:
            for pos in range(ang_final, ang_inicio, -incStep):
                duty = AngleToDuty(pos)
                pwm.ChangeDutyCycle(duty)
                time.sleep(DELAY)
            i = 0
        posicion_actual = 0
        #pwm.stop()  # stop sending value to output

    if estado == 0 and posicion_actual == 0:
        posicion_actual = 0
    return (estado)
    
#if __name__ == '__main__':
    #contador = 12
    #cambio(contador)
    #print("Contador: ")
    #contador = int(input())
    
    #cambio(contador)
    #pwm.stop()  # stop sending value to output
    #GPIO.cleanup()  # release channel
