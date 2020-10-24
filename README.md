# My Circuit Python Assignments

### This is my adventure with the first time using CircuitPython, and Coding with the Python Language.
---

# First Assignment

```python
import board
import neopixel

dot = neopixel.NeoPixel(board.NEOPIXEL, 1)

print("Make it red!")

while True:
     dot.fill((255,0,0))
```python
