from RPi import GPIO as RS           #import GPIO Module
from time import sleep as stop       #import Time Moduale
RS.setmode(RS.BOARD)                 #BOARD Pin
RS.setwarnings(False)                #Set Warnings
RS.setup(5,OUT)                      #declare Output Pin
while 1:
  RS.output(5,HIGH)                  #Led ON
  stop(1)                            #Delay 1 second
  RS.output(5,LOW)                   #Led OFF
  stop(1)                            #Delay 1 second
