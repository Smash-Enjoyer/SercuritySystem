
import board
import digitalio as dio
import time
from neopixel import NeoPixel
import random
import adafruit_hcsr04

sonar = adafruit_hcsr04.HCSR04(trigger_pin=board.D5, echo_pin=board.D6)

led = dio.DigitalInOut(board.LED)
led.direction = dio.Direction.OUTPUT

pir = dio.DigitalInOut(board.D3)
pir.direction = dio.Direction.INPUT

button = dio.DigitalInOut(board.D7)
button.direction = dio.Direction.INPUT

bb = dio.DigitalInOut(board.D4)
bb.direction = dio.Direction.INPUT
bb.pull = dio.Pull.UP

np = NeoPixel(board.D2, 30, auto_write = True, brightness = 0.1)

green = (0,255,0)
red = (255,0,0)
yellow = (255,100,0)
speed = 0.0001
times = 0
'''

Function: fadeOut

Description: It fades out a specified color by lower the RGB value till it goes to 0.

Parameters: color-list, speed-int

Return value: "none"

'''
def fadeOut(color = [0,0,255], speed=1):
    if speed <= 0:
        speed = 1
    fadeR = color[0]/256.0
    fadeG = color[1]/256.0
    fadeB = color[2]/256.0
    color1 = [color[0],color[1],color[2]]
    np.fill(color1)
    np.show()
    for i in range(255):
        color1[0] = int (color[0] - (fadeR*i))
        color1[1] = int (color[1] - (fadeG*i))
        color1[2] = int (color[2] - (fadeB*i))
        np.fill(color1)
        np.show()
        print(color1)
        time.sleep(speed)
'''

Function: fadeIn

Description: It fades in a specified color by increasing the RGB value from black till it goes to the specified color.

Parameters: color-list, speed-int

Return value: "none".

'''
def fadeIn(color = [0,0,255], speed=1):
    if speed <= 0:
        speed = 1
    fadeR = color[0]/256.0
    fadeG = color[1]/256.0
    fadeB = color[2]/256.0
    color1 = [0,0,0]
    np.fill(color1)
    np.show()
    print(color1)
    for i in range(255):
        color1[0] = int (fadeR*i)
        color1[1] = int (fadeG*i)
        color1[2] = int (fadeB*i)
        np.fill(color1)
        np.show()
        time.sleep(speed)
        print(color1)

def arm():
    np.fill((255,100,0))
    print("armed")
    time.sleep(10)
def disarm():
    print("disarm")
    np.fill((0,255,0))
    time.sleep(1)
    
def blink():
    for i in range(5):
        fadeOut(red,speed)
        fadeIn(red,speed)
       
np.fill((0,255,0))

while True:
    if not button.value and times == 0:
        arm()
        times += 1
    elif not button.value and times == 1:
        disarm()
        times -= 1
    if times == 0:
        np.fill(green)
    else:
        np.fill(red)
    try:
        if not bb.value or pir.value or sonar.distance < 10:
            blink()
    except RuntimeError:
        pass
        
    time.sleep(0.1)
