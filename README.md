# My Circuit Python Assignments

### This is my adventure with the first time using CircuitPython, and Coding with the Python Language.

# Table of Contents
* [SteadyRed LED](#FirstAssignment)
---

# FirstAssignment - Get RGB LED working

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

# Second Assignment - Servo Capacitive Touch
