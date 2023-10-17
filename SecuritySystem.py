
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
speed = 0.001
times = 0

def arm():
    np.fill((255,100,0))
    print("armed")
    time.sleep(10)
def disarm():
    print("disarm")
    np.fill((0,255,0))
    time.sleep(1)
    
np.fill((0,255,0))

while True:
    if not button.value and times % 2 == 0:
        arm()
        times += 1
    elif not button.value and times % 2 == 1:
        disarm()
        times += 1
