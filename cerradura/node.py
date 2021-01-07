from grove.grove_ultrasonic_ranger import GroveUltrasonicRanger
from grove.factory import Factory
import time
from datetime import datetime
import math
import sys
import time
from grove.adc import ADC
import pytz
from influxdb import InfluxDBClient
sonar = GroveUltrasonicRanger(5)
boton_pin = 18
emergencia_pin= 16
emergencia= Factory.getButton("GPIO-HIGH", emergencia_pin)
button = Factory.getButton("GPIO-HIGH", boton_pin)

global maxi
maxi = 30
global porcentaje
porcentaje = 60
client = InfluxDBClient('localhost', 8086, 'root', 'root', 'cerradura')
def aforo():
    global porcentaje
    global maxi
    print("El aforo maximo de la tienda es" ,maxi, " y la restricción es del", porcentaje, "%")
    print("Es correcto, S/N")
    respuesta = input()
    if respuesta =='S':
        pass
    else:
        print("Seleccione el aforo maximo")
        maxi = int(input())
        print("Seleccione la restrcción")
        porcentaje = int(input())
    
    
class GroveGasSensorMQ2:
 
    def __init__(self, channel):
        self.channel = channel
        self.adc = ADC()
 
    @property
    def MQ2(self):
        value = self.adc.read(self.channel)
        return value

def main():
    sensor = GroveGasSensorMQ2(0)
    tiempo=0
    contador=0
    calidad=1
    
    global maxi
    maxi = 30
    global porcentaje
    porcentaje = 60
    aforo()
    maxi= int(maxi*(porcentaje/100))
    print(maxi)
    while emergencia.is_pressed()==0:
        
        distancia = sonar.get_distance()
        d1 = datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ')
        
        print("date and time =", d1)
        print(distancia)
        if distancia<=50:
            while tiempo<10 and button.is_pressed()==0:
                tiempo= tiempo+1
                time.sleep(1)
                pass
            if button.is_pressed() and contador <maxi:
                contador= contador+1
        elif button.is_pressed():
            print("saliendo")
            while tiempo<10 and distancia>=50:
                tiempo= tiempo+1
                distancia = sonar.get_distance()
                time.sleep(1)
                pass
            if distancia<=50 and contador>0:
                contador= contador-1
        tiempo=0
        print('Gas value: {0}'.format(sensor.MQ2))
        gas= sensor.MQ2
        print(contador)
        json_data = [{
            "measurement": "contador",
            "time": d1,
            "fields": {
                "value": contador
            }
        }]
        if gas<500:
            calidad =1
        elif gas<1000:
            calidad = 2
        else:
            calidad = 3
        
        client.write_points(json_data)
        json_data = [{
            "measurement": "co2",
            "time": d1,
            "fields": {
                "value": calidad
            }
        }]
        client.write_points(json_data)
        
        json_data = [{
            "measurement": "max",
            "time": d1,
            "fields": {
                "value": maxi
            }
            }]
        client.write_points(json_data)
        time.sleep(0.5)
        while emergencia.is_pressed():
            print("Emergencia cerradura abierta")
            contador = 0
if __name__ == '__main__':
    main()