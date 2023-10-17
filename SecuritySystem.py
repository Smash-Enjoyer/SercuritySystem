
import board
import digitalio as dio
import time
from neopixel import NeoPixel
import random
import adafruit_hcsr04

sonar = adafruit_hcsr04.HCSR04(trigger_pin=board.D4, echo_pin=board.D5)

led = dio.DigitalInOut(board.LED)
led.direction = dio.Direction.OUTPUT

pir = dio.DigitalInOut(board.D3)
pir.direction = dio.Direction.INPUT

button = dio.DigitalInOut(board.D7)
button.direction = dio.Direction.INPUT

bb = dio.DigitalInOut(board.D6)
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
    
def blink():
    for i in range(100):
        delay = random.random() + 0.01
        np.fill(red)
        np.show()
        time.sleep(0.5)
        for i in range(random.randint(1,2)):
            np.fill(red)
            np.show()
            time.sleep(0.1)
            np.fill([0,0,0])
            np.show()
        np.fill(red)
        np.show()
        time.sleep(0.5)
       
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
        if bb.value == False or pir.value == True or sonar.distance < 10:
            blink()
            
        
        
        
        
