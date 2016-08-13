import RPi.GPIO as gpio
import max7219.led as led
from random import randint
import time

matrix = led.matrix()

while True:
  for i in range(8):
    for j in range(8):
      matrix.pixel(i,j,randint(0,1))
      time.sleep(0.0002)
