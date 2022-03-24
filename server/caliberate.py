import RPi.GPIO as GPIO
import time

GPIO.setwarnings(True)
GPIO.setmode(GPIO.BOARD)

GPIO.setup(12, GPIO.OUT)
pwm = GPIO.PWM(12, 100)

pwm.start(14)

time.sleep(5)
pwm.ChangeDutyCycle(0)
time.sleep(5)
pwm.ChangeDutyCycle(7)

time.sleep(5)
pwm.stop()

GPIO.cleanup()

