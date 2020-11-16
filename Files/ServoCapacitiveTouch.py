import board
import servo
import time
import pulseio
import touchio #capacitive touch

pwm = pulseio.PWMOut(board.A2, duty_cycle=2 ** 15, frequency=50) #Setting the PWM

#myServo = servo.ContinuousServo(pwm) #Defines the servo as a continuous servo rather than a standard
myServo = servo.Servo(pwm)

touch_A0 = touchio.TouchIn(board.A0)  # Defines the pin which the first wire is in.
touch_A1 = touchio.TouchIn(board.A1)  # Defines which pin the second wire is in.

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

while True:
    if touch_A0.value:
        print("Forward! ; " , myServo.angle) #Allows me to see which wire is being touched in the Serial Monitor.
        ##myServo.angle = 180 #Does the same thing as myServo.throttle, but will finish the action even if the other wire is touched before finishing the motion.
        myServo.angle = constrain((myServo.angle +4), min_val , max_val) # Moves it to 180
        time.sleep(0.1)
    if touch_A1.value:
        print("Backward! ; " , myServo.angle)#Allows me to see which wire is being touched in the Serial Monitor.
        myServo.angle = constrain((myServo.angle -4), min_val , max_val) #Moves it to 0
        time.sleep(0.1)