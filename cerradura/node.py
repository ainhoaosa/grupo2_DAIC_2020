from grove.grove_ultrasonic_ranger import GroveUltrasonicRanger
from grove.factory import Factory
import time
from datetime import datetime
import math
import sys
import time
from grove.adc import ADC
 
sonar = GroveUltrasonicRanger(5)
boton_pin = 18
tiempo=0
button = Factory.getButton("GPIO-HIGH", boton_pin)
contador=0
class GroveGasSensorMQ2:
 
    def __init__(self, channel):
        self.channel = channel
        self.adc = ADC()
 
    @property
    def MQ2(self):
        value = self.adc.read(self.channel)
        return value
print('Detecting distance...')
sensor = GroveGasSensorMQ2(0)
while True:
    
    distancia = sonar.get_distance()
    d1 = datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ')
    
    print("date and time =", d1)
    print(distancia)
    if distancia<=50:
        while tiempo<30 and button.is_pressed()==0:
            tiempo= tiempo+1
            time.sleep(1)
            pass
        if button.is_pressed():
            contador= contador+1
    elif button.is_pressed():
        print("saliendo")
        while tiempo<30 and distancia>=50:
            tiempo= tiempo+1
            distancia = sonar.get_distance()
            time.sleep(1)
            pass
        if distancia<=50 and contador>0:
            contador= contador-1
    tiempo=0
    print('Gas value: {0}'.format(sensor.MQ2))
    print(contador)
    time.sleep(1)
