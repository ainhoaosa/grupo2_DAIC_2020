#!/usr/bin/env python3

import time
from rpi_ws281x import Color
from grove_ws2813_rgb_led_strip import GroveWS2813RgbStrip
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(16,GPIO.IN)
global num
num=0
# connect to pin 12(slot PWM)
PIN   = 12
# For Grove - WS2813 RGB LED Strip Waterproof - 30 LED/m
# there is 30 RGB LEDs.
COUNT = 10
strip = GroveWS2813RgbStrip(PIN, COUNT)


def procesar(numcanal):
    print('Detectado')
    global num
    num= num+1
    if (num==10):
        num=0
GPIO.add_event_detect(16, GPIO.RISING,
callback=procesar)

def colorWipe1(strip, color,i,  wait_ms=1000):
    """Wipe color across display a pixel at a time."""
    if num ==0:
        for i in range(0, strip.numPixels(), 1):
            strip.setPixelColor(i, Color(0, 0, 0))
        i=0
    strip.setPixelColor(i, color)
    strip.show()
    time.sleep(wait_ms/1000.0)
      
print ('Color wipe animations.')

while True:
    
    colorWipe1(strip, Color(255, 0, 0), num)  # Red wipe
    colorWipe1(strip, Color(0, 255, 0), num)  # Blue wipe
    colorWipe1(strip, Color(0, 0, 255), num)  # Green wipe
