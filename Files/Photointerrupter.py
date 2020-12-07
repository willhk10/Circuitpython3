import board
import math
import time
import digitalio
import adafruit_bus_device


photoPin = digitalio.DigitalInOut(board.D8)
photoPin.direction = digitalio.Direction.INPUT
photoPin.pull = digitalio.Pull.UP

lastTime = time.monotonic()

isInterrupted = True
counter = 0

while True:
    if time.monotonic() > lastTime + 4:
        lastTime = time.monotonic()
        print('         ')
        print(str(counter))
    if photoPin.value and not isInterrupted:
        counter += 1
        isInterrupted = True
    if not photoPin.value:
        isInterrupted = False