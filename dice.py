import RPi.GPIO as gpio
import time
import max7219.led as led
from random import randint
from max7219.font import proportional, SINCLAIR_FONT, TINY_FONT, CP437_FONT

gpio.setmode(gpio.BCM)

taster = 14
tasterStatus = 0
gpio.setup(taster,gpio.IN,pull_up_down=gpio.PUD_UP)

matrix = led.matrix()


def neue_zahl(channel):
  matrix.letter(0, ord(str(randint(1,6))))

gpio.add_event_detect(taster, gpio.RISING, callback=neue_zahl)

matrix.letter(0, ord("?"))

while True:
  time.sleep(0.1)
