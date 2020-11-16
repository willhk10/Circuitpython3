# My CircuitPython Assignments

### This is my adventure with the first time using CircuitPython, and Coding with the Python Language.

## TableofContents
* [SteadyRed LED](#FirstAssignment)
* [Servo with Capacitive Touch](#SecondAssignment)
---

# FirstAssignment 
## - Get RGB LED working

## Description
The goal of this assignment was to get the board up and running, and to get the onboard RGB to hold a steady, red color. We had to use libraries, which we imported through the [Python help site](https://circuitpython.org/board/metro_m0_express/).

## [Code](https://github.com/willhk10/Circuitpython3/blob/main/Files/SteadyRed.py)

```python
import board
import neopixel

dot = neopixel.NeoPixel(board.NEOPIXEL, 1)

print("Make it red!")

while True:
     dot.fill((255,0,0))
```

## Problemos
First of all, I had to download [Mu](https://codewith.mu/en/downloadOne). This was fairly self explanatory, as you click the link and then whichever software you have will pertain to the download you need to get. The only real problem that I was continuously having was that the library "Neopixel" was not being recognized by my MetroM0. In order to fix this problem, I had to go to a [website](https://circuitpython.org/libraries) and download the libraries there. I downloaded v5 so that I got all the new ones.

After this, it worked like a charm!
<img src="Pictures/MetroM0.png" width="300px" /> 


-----

# SecondAssignment 
## - Servo Capacitive Touch

## Description
This assignment was to use a continuous servo and the MetroExpress Capacitive Touch feature. The goal of the assignment was to use two wires and have the servo move forwards and backwards by touching each wire.

## [Code](https://github.com/willhk10/Circuitpython3/blob/main/Files/ServoCapacitiveTouch.py)

## Important snippets of code and what they mean
```python
import touchio
```
#### Importance -
This allows for the code that you write to incorporate capacitive touch.
---
```python
min_val = 0
max_val = 180
val = myServo.angle
myServo.angle = 5


def constrain(val, min_val, max_val):

    if val < min_val:
        return min_val
    if val > max_val:
        return max_val
    return val
```
### Importance -
Prevents error messages if the value being sent to the servo exceeds the mins or maxes that the servo can understand
---
```python
while True:
    if touch_A0.value:
        print("Forward! ; " , myServo.angle) #Allows me to see which wire is being touched in the Serial Monitor, and what the value is..
        myServo.angle = constrain((myServo.angle +4), min_val , max_val) # Moves it to 180
        time.sleep(0.1)
    if touch_A1.value:
        print("Backward! ; " , myServo.angle)#Allows me to see which wire is being touched in the Serial Monitor, and what the value is.
        myServo.angle = constrain((myServo.angle -4), min_val , max_val) #Moves it to 0
        time.sleep(0.1)
```
### Importance - 
This makes the servo move back and forth, and prints the value that the servo is processing to the serial monitor for debugging.
---
## Pictures 
<img src="Pictures/POVServo1.jpg" width="400px" height="300px" /> 
<img src="Pictures/POVServo2.jpg" width="400px" height="300px /> 

## Problemos
big probloim

[BACK TO TOP](#TableOfContents)






