from MotorModule import Motor
import KeyPressModule as kp
import JoyStickModule as js
import PowerModule as pr
from time import sleep
import numpy as np

# Initialize motors (assign GPIO pins)
# motor1 = Motor(21,16,20)
# motor2 = Motor(8,7,1)
# motor3 = Motor(14,18,15)
# motor4 = Motor(4,3,2)
# motor5 = Motor(17,22,27)
# motor6 = Motor(13,6,5)

# Modify GPIO pins based on the pins used
# 12, 13, 18, 19 support hardware PWM functionality on RPi 3B
motor1 = Motor(Ena=12, In1=5, In2=6)
motor2 = Motor(Ena=13, In1=7, In2=8)
motor3 = Motor(Ena=18, In1=9, In2=10)

# Decide to use keyboard or controller
movement = 'KeyBoard' #['KeyBoard', 'Joystick']


def main():

# Move robot
  if movement == 'Joystick':
    jsVal = js.getJS()
    # CCW Rotation
    if jsVal['axis3']>0.5:
      motor1.move(0.3,0.1)
      motor2.move(0.3,0.1)
      motor3.move(0.3,0.1)
    # CW Rotation
    elif jsVal['axis3']<-0.5:
      motor1.move(-0.3,0.1)
      motor2.move(-0.3,0.1)
      motor3.move(-0.3,0.1)
    # Translation
    else:
      # Get joystick value
      input = np.array([-(jsVal['axis1']),(jsVal['axis2'])])
      # Find power given to each motor
      motorPower = pr.calcPower(input)
      # Output power to each motor
      motor1.move(motorPower[0,:],0.1)
      motor2.move(motorPower[1,:],0.1)
      motor3.move(motorPower[2,:],0.1)
  else:
    # Create window to use pygame key functions
    kp.init()
    # CCW Rotation
    #if kp.getKey('q'):
    motor1.move(0.1,0.1)
    #   motor2.move(0.1,0.1)
    #   motor3.move(0.1,0.1)
    # # CW Rotation
    # elif kp.getKey('e'):
    #   motor1.move(-0.1,0.1)
    #   motor2.move(-0.1,0.1)
    #   motor3.move(-0.1,0.1)
    # # Translation
    # elif kp.getKey('w'):
    #   input = np.array([0,-1])
    #   motorPower = pr.calcPower(input)
    #   motor1.move(motorPower[0,:],0.1)
    #   motor2.move(motorPower[1,:],0.1)
    #   motor3.move(motorPower[2,:],0.1)
    # elif kp.getKey('s'):
    #   input = np.array([0,1])
    #   motorPower = pr.calcPower(input)
    #   motor1.move(motorPower[0,:],0.1)
    #   motor2.move(motorPower[1,:],0.1)
    #   motor3.move(motorPower[2,:],0.1)
    # elif kp.getKey('a'):
    #   input = np.array([1,0])
    #   motorPower = pr.calcPower(input)
    #   motor1.move(motorPower[0,:],0.1)
    #   motor2.move(motorPower[1,:],0.1)
    #   motor3.move(motorPower[2,:],0.1)
    # elif kp.getKey('d'):
    #   input = np.array([-1,0])
    #   motorPower = pr.calcPower(input)
    #   motor1.move(motorPower[0,:],0.1)
    #   motor2.move(motorPower[1,:],0.1)
    #   motor3.move(motorPower[2,:],0.1)
    # else:
    #   for motor in [motor1, motor2, motor3]:
    #     motor.stop(0.1) 


if __name__ == '__main__':
  while True:
    main()