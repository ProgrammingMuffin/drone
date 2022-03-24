import RPi.GPIO as GPIO


duty_cycle = 0
pwm = None

def init_gpio():
    global pwm
    GPIO.setwarnings(True)
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(12, GPIO.OUT)
    pwm = GPIO.PWM(12, 100)


def clear_gpio():
    global pwm
    pwm.stop()
    GPIO.cleanup()

def change_duty_cycle(duty):
    global pwm, duty_cycle
    response = dict()
    prev_duty_cycle = duty_cycle
    duty_cycle = duty
    pwm.ChangeDutyCycle(duty_cycle)
    response['prev_duty_cycle'] = prev_duty_cycle
    response['duty_cycle'] = duty_cycle
    return response


