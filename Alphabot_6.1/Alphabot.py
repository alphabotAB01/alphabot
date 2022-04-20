import time
import RPi.GPIO as GPIO

"""
Questa è la classe che permette di interfacciare il server
con i motori dell'Alphabot
"""


class AlphaBot(object):

    def __init__(self, in1=13, in2=12, ena=6, in3=21, in4=20, enb=26):
        self.IN1 = in1
        self.IN2 = in2
        self.IN3 = in3
        self.IN4 = in4
        self.ENA = ena
        self.ENB = enb
        self.PA = 50
        self.PB = 50
        self.TEMPO_COMANDO = 0.25
        self.DR = 16
        self.DL = 19

        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(self.IN1, GPIO.OUT)
        GPIO.setup(self.IN2, GPIO.OUT)
        GPIO.setup(self.IN3, GPIO.OUT)
        GPIO.setup(self.IN4, GPIO.OUT)
        GPIO.setup(self.ENA, GPIO.OUT)
        GPIO.setup(self.ENB, GPIO.OUT)
        GPIO.setup(self.DR, GPIO.IN, GPIO.PUD_UP)
        GPIO.setup(self.DL, GPIO.IN, GPIO.PUD_UP)
        self.PWMA = GPIO.PWM(self.ENA, 500)
        self.PWMB = GPIO.PWM(self.ENB, 500)
        self.PWMA.start(self.PA)
        self.PWMB.start(self.PB)
        self.fermo()

    def sinistra(self, durata_comando=9999):
        self.PWMA.ChangeDutyCycle(self.PA)
        self.PWMB.ChangeDutyCycle(self.PB)
        GPIO.output(self.IN1, GPIO.HIGH)
        GPIO.output(self.IN2, GPIO.LOW)
        GPIO.output(self.IN3, GPIO.HIGH)
        GPIO.output(self.IN4, GPIO.LOW)
        if durata_comando == 9999:
            time.sleep(self.TEMPO_COMANDO)
            self.fermo()
            time.sleep(self.TEMPO_COMANDO)
        else:
            time.sleep(durata_comando / 1000)
            self.fermo()
            time.sleep(durata_comando / 1000)

    def fermo(self, durata_comando=9999):
        self.PWMA.ChangeDutyCycle(0)
        self.PWMB.ChangeDutyCycle(0)
        GPIO.output(self.IN1, GPIO.LOW)
        GPIO.output(self.IN2, GPIO.LOW)
        GPIO.output(self.IN3, GPIO.LOW)
        GPIO.output(self.IN4, GPIO.LOW)

    def destra(self, durata_comando=9999):
        self.PWMA.ChangeDutyCycle(self.PA)
        self.PWMB.ChangeDutyCycle(self.PB)
        GPIO.output(self.IN1, GPIO.LOW)
        GPIO.output(self.IN2, GPIO.HIGH)
        GPIO.output(self.IN3, GPIO.LOW)
        GPIO.output(self.IN4, GPIO.HIGH)
        if durata_comando == 9999:
            time.sleep(self.TEMPO_COMANDO)
            self.fermo()
            time.sleep(self.TEMPO_COMANDO)
        else:
            time.sleep(durata_comando / 1000)
            self.fermo()
            time.sleep(durata_comando / 1000)

    def avanti(self, durata_comando=9999):
        self.PWMA.ChangeDutyCycle(self.PA)
        self.PWMB.ChangeDutyCycle(self.PB)
        GPIO.output(self.IN1, GPIO.LOW)
        GPIO.output(self.IN2, GPIO.HIGH)
        GPIO.output(self.IN3, GPIO.HIGH)
        GPIO.output(self.IN4, GPIO.LOW)
        if durata_comando != 9999:
            time.sleep(durata_comando / 1000)
            self.fermo()
            time.sleep(durata_comando / 1000)

    def indietro(self, durata_comando=9999):
        self.PWMA.ChangeDutyCycle(self.PA)
        self.PWMB.ChangeDutyCycle(self.PB)
        GPIO.output(self.IN1, GPIO.HIGH)
        GPIO.output(self.IN2, GPIO.LOW)
        GPIO.output(self.IN3, GPIO.LOW)
        GPIO.output(self.IN4, GPIO.HIGH)
        if durata_comando != 9999:
            time.sleep(durata_comando / 1000)
            self.fermo()
            time.sleep(durata_comando / 1000)

    def set_pwm_a(self, value):
        if (value >= 0) and (value <= 100):
            self.PA = value
            self.PWMA.ChangeDutyCycle(self.PA)

    def set_pwm_b(self, value):
        if (value >= 0) and (value <= 100):
            self.PB = value
            self.PWMB.ChangeDutyCycle(self.PB)

    def set_pwm(self, left, right):
        if (right >= 0) and (right <= 100):
            self.PA = right
            self.PWMA.ChangeDutyCycle(self.PA)

        if (left >= 0) and (left <= 100):
            self.PB = left
            self.PWMB.ChangeDutyCycle(self.PB)

    def set_motor(self, right, left, durata_comando=0):
        if (right >= 0) and (right <= 100):
            GPIO.output(self.IN1, GPIO.LOW)
            GPIO.output(self.IN2, GPIO.HIGH)
            self.PWMA.ChangeDutyCycle(right)
        elif (right < 0) and (right >= -100):
            GPIO.output(self.IN1, GPIO.HIGH)
            GPIO.output(self.IN2, GPIO.LOW)
            self.PWMA.ChangeDutyCycle(0 - right)
        if (left >= 0) and (left <= 100):
            GPIO.output(self.IN3, GPIO.HIGH)
            GPIO.output(self.IN4, GPIO.LOW)
            self.PWMB.ChangeDutyCycle(left)
        elif (left < 0) and (left >= -100):
            GPIO.output(self.IN3, GPIO.LOW)
            GPIO.output(self.IN4, GPIO.HIGH)
            self.PWMB.ChangeDutyCycle(0 - left)

        time.sleep(durata_comando / 1000)
        self.fermo()
        time.sleep(durata_comando / 1000)


    def sensoreIR_dx(self):
        return GPIO.input(self.DR)

    def sensoreIR_sx(self):
        return GPIO.input(self.DL)

if __name__ == '__main__':

    Ab = AlphaBot()
    Ab.forward()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        GPIO.cleanup()