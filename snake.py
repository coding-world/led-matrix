import RPi.GPIO as gpio
import time
import max7219.led as led
from random import randint

gpio.setmode(gpio.BCM)

taster = [14,15,18,23]
matrix = led.matrix()

def startSpiel():
  global snake, richtung, apfel
  snake = [[randint(2,5),randint(2,5)]]
  richtung = [0,0]
  while richtung == [0,0]:
    matrix.show_message("READY")
  neuerApfel()

def steuerung(gpio):
  global richtung
  if(gpio == 14):   #rechts
    richtung = [1,0]
  elif(gpio == 15): #oben
    richtung = [0,-1]
  elif(gpio == 18): #unten
     richtung = [0,1]
  elif(gpio == 23): #links
    richtung = [-1,0]

for i in taster:
  gpio.setup(i,gpio.IN,pull_up_down=gpio.PUD_UP)
  gpio.add_event_detect(i, gpio.FALLING, callback=steuerung)

def neuerApfel():
  global apfel, snake
  apfelSnake = False
  while apfelSnake == False:
    apfelSnake = True
    apfel = [randint(0,7),randint(0,7)]
    for i in snake:
      if(i == apfel):
        apfelSnake = False

def endOfGame():
  for i in range(0,2):
    matrix.clear()
    for i in range(0,8):
      for j in range(0,8):
        matrix.pixel(i,j,1)
        time.sleep(0.01)
    time.sleep(0.1)
  matrix.show_message("GAME OVER")
  punkte = len(snake)-1
  matrix.show_message(str(punkte)+" PUNKTE", delay=0.1)
  startSpiel()


startSpiel()


while True:
  keinePause = False
  newSnake = [snake[0][0]+richtung[0],
              snake[0][1]+richtung[1]]
  for i in snake:
    if(i == newSnake):
      endOfGame()
      pass
  
  if(newSnake == apfel):
     neuerApfel()
     keinePause = True
  else:
     snake.pop()
  snake.insert(0,newSnake)  

    
  if(snake[0][0] >= 8 or snake[0][1] >=8
	or snake[0][0] < 0 or snake[0][1] < 0 ):
    endOfGame()
    pass
 
  matrix.clear()
  for i in snake:
    matrix.pixel(i[0],i[1], 1)
  matrix.pixel(apfel[0],apfel[1],1)
  if(keinePause == False):
    newLength = (len(snake)-2)*0.01
    time.sleep(0.8-newLength)
  else:
    time.sleep(0.4)

