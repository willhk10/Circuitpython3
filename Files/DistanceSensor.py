import time
import board
import neopixel
from adafruit_hcsr04 import HCSR04
trig = board.D3
echo = board.D4
sonar = HCSR04(trig, echo)
dot = neopixel.NeoPixel(board.NEOPIXEL, 1)
red = 225
green = 0
blue = 0

distance =0

while True:
    dot.fill((red, green, blue))
    if distance<=20:
       red = 255-(12*distance)
       blue = 0+(12*distance)
       green = 0

    elif distance >20:
        green = 0+(12*(distance-20))
        blue = 225-(12*(distance-20))
        red = 0

    if red<=0:
        red =0

    if blue >=225:
        blue =225

    if blue <=0:
        blue = 0

    if green >=225:
        green = 225


    try:
        print (int(sonar.distance))
        distance = (int(sonar.distance))
    except RuntimeError:
        pass
    time.sleep(0.05)