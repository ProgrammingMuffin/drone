import RPi.GPIO as GPIO


duty_cycle = 0
pwm_first = None
pwm_second = None

def init_gpio():
    global pwm_first, pwm_second
    GPIO.setwarnings(True)
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(12, GPIO.OUT)
    GPIO.setup(11, GPIO.OUT)
    pwm_first = GPIO.PWM(12, 100)
    pwm_second = GPIO.PWM(33, 100)
    pwm_first.start(0)
    pwm_second.start(0)


def clear_gpio():
    global pwm_first, pwm_second
    pwm_first.stop()
    pwm_second.stop()
    GPIO.cleanup()

def change_duty_cycle(duty):
    global pwm_first, pwm_second, duty_cycle
    response = dict()
    prev_duty_cycle = duty_cycle
    duty_cycle = duty
    pwm_first.ChangeDutyCycle(duty_cycle)
    pwm_second.ChangeDutyCycle(duty_cycle)
    response['prev_duty_cycle'] = prev_duty_cycle
    response['duty_cycle'] = duty_cycle
    return response


