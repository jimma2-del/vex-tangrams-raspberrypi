'''
This code is based on this YouTube video:
https://www.youtube.com/watch?v=0lXY87NwVIc&list=PLMoSUbG1Q_r-So6ocbQhMFM8vIByvnRWG&index=3
'''

import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

class Motor():
  def __init__(self, Ena, In1, In2):
    self.Ena = Ena
    self.In1 = In1
    self.In2 = In2

    GPIO.setup(self.Ena,GPIO.OUT)
    GPIO.setup(self.In1,GPIO.OUT)
    GPIO.setup(self.In2,GPIO.OUT)

    self.pwmA = GPIO.PWM(self.Ena, 100)
    self.pwmA.start(0)


  def move(self,speed=0.5,t=0):
    speed *= 100

    self.pwmA.ChangeDutyCycle(abs(speed))

    if speed>0: GPIO.output(self.In1,GPIO.HIGH), GPIO.output(self.In2,GPIO.LOW)
    else: GPIO.output(self.In1,GPIO.LOW), GPIO.output(self.In2,GPIO.HIGH)

    sleep(t)


  def stop(self,t=0):
    self.pwmA.ChangeDutyCycle(0);
    sleep(t)


def main():
  motor1.move(0.3,2)
  motor1.stop(2)


if __name__ == '__main__':
  motor1 = Motor(12,16,20)
  main()