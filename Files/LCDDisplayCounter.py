from lcd.lcd import LCD
from lcd.i2c_pcf8574_interface import I2CPCF8574Interface
# some LCDs are 0x3f... some are 0x27.
lcd = LCD(I2CPCF8574Interface(0x3f), num_rows=2, num_cols=16)
import touchio
import board
import time
import touchio

touch_A0 = touchio.TouchIn(board.A0)  # Defines the pin which the first wire is in.
touch_A1 = touchio.TouchIn(board.A1)  # Defines which pin the second wire is in.

x = 0
y = 1

while True:
    if touch_A0.value:
        lcd.clear()
        x = x + 1
        lcd.print(str(x))
        while touch_A0.value:
            print("HelloA0")
    if touch_A1.value:
        lcd.clear()
        x = x - 1
        lcd.print(str(x))
        while touch_A1.value:
            print("HelloA1")