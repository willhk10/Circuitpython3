# My Circuit Python Assignments

### This is my adventure with the first time using CircuitPython, and Coding with the Python Language.
---

# First Assignment

The goal of this assignment was to get the board up and running, and to get the RGB to hold a steady, red color. We had to use libraries, which we imported through the [Python help site](https://circuitpython.org/board/metro_m0_express/)

```python
import board
import neopixel

dot = neopixel.NeoPixel(board.NEOPIXEL, 1)

print("Make it red!")

while True:
     dot.fill((255,0,0))
```python
