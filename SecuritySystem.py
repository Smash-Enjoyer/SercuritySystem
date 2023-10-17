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

bb = dio.DigitalInOut(board.D4)
bb.direction = dio.Direction.INPUT
bb.pull = dio.Pull.UP

np = NeoPixel(board.D2, 30, auto_write = True, brightness = 1)


playgroundPixels = 10
bright = 1

circuitPlayground = NeoPixel(board.NEOPIXEL, playgroundPixels, auto_write = False, brightness = bright)
fOrange1 = (255,54,0)
fOrange3 = (255,34,0)
halloweenGreen = (100,255,45)
halloweenWhite = (158,190,255)
halloweenColors = [halloweenGreen,fOrange1,fOrange3]
speed = 0.001
times = 5
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
'''

Function: fire

Description: Cycles through a list of colors at random interviews betwwen 0 and 4 seconds. 

Parameters: color-list, speed-int

Return value: "none".

'''
def fire(colors, speed = 0.1, times = 1):
    for i in range(times):
        led = [random.randint(0,playgroundPixels-1) for i in range(playgroundPixels)]
        for i in led:
            delay = random.random()/2
            np[i] = colors[random.randint(0,2)]
            time.sleep(delay)
            np.show()
'''

Function: lightning

Description: Flashes a color at a random intervals. 

Parameters: color-list, lColor-list, speed-int

Return value: "none".

'''
def lightning(color,lColors, delay = 5, speed = 0.1):
    delay = random.random()*delay + 0.5
    np.fill(color)
    np.show()
    time.sleep(delay)
    ind = random.randint(0, len(lColors)-1)
    for i in range(random.randint(1,4)):
        np.fill(lColors[ind])
        np.show()
        time.sleep(0.1)
        np.fill([0,0,0])
        np.show()
    np.fill(color)
    np.show()
'''

Function: colorCycle

Description: Fades in and out into different colors. 

Parameters: colorList-list, speed-int

Return value: "none".

'''
def colorCycle(colorList, speed = 0.01):
    for i in range(len(colorList)):
        fadeIn(colorList[i], speed)
        fadeOut(colorList[i], speed)
np.fill((0,0,0))
np.show()

while True:
    distance = sonar.distance
    print(distance)
    try:
        if distance > 100:
            np.fill((255,0,0))
            np.show()
        elif distance >= 50:
            np.fill((255,255,0))
            np.show()
        else:
            np.fill((0,255,0))
            np.show()
        
    except RuntimeError:
        print("Retrying!")
    time.sleep(0.1)
'''    
    try:
        if sonar.distance < 15:
            colorCycle(halloweenColors)
            fadeIn(fOrange1, speed)
            fire(halloweenColors, speed, times)
            fadeOut(fOrange3,speed)
            fadeIn(halloweenWhite,speed)
            lightning(halloweenWhite, halloweenColors, speed)
            fadeOut(halloweenWhite, speed)
    except RuntimeError:
        print("Retrying!")
    np.fill((0,0,0))
    time.sleep(0.1)

    if not bb.value:
        print(bb.value)
        lightning(fOrange3, (255,255,255), 1, speed)
    else:
        np.fill((0,0,0))
    print(bb.value)
    time.sleep(0.5)

    if pir.value == True:
        colorCycle(halloweenColors)
        fadeIn(fOrange1, speed)
        fire(halloweenColors, speed, times)
        fadeOut(fOrange3,speed)
        fadeIn(halloweenWhite,speed)
        lightning(halloweenWhite, halloweenColors, speed)
        fadeOut(halloweenWhite, speed)
    time.sleep(1)
'''
