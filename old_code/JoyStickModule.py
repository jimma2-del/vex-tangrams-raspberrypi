'''
This code is based on this YouTube video
https://www.youtube.com/watch?v=TMBfiS7LNnU&list=PLMoSUbG1Q_r-So6ocbQhMFM8vIByvnRWG&index=7
'''

'''
Install drivers by running these lines of code in the terminal of the RP:

1. sudo apt install pipx

Install Ds4:

2. sudo pipx install ds4drv
3. sudo wget https://raw.githubusercontent.com/chrippa/ds4drv/master/udev/50-ds4drv.rules
4. sudo udevadm control --reload-rules
5. sudo udevadm trigger
6. sudo nano /etc/rc.local

(add after # By default this script does nothing. line, add a new line:
/user/local/bin/ds4drv &)
'''

import pygame
from time import sleep
pygame.init()
pygame.init()
controller = pygame.joystick.Joystick(0)
controller.init()
buttons = {'x':0, 'o':0, 't':0, 's':0,
           'L1':0, 'R1':0, 'L2':0, 'R2':0,
           'share':0, 'options':0,
           'axis1':0., 'axis2':0., 'axis3':0., 'axis4':0.}
axiss=[0.,0.,0.,0.,0.,0.]

def getJS(name=''):

  global buttons
  #r retrieve any events ...
  for event in pygame.event.get():                              # Analog Sticks
    if event.type == pygame.JOYAXISMOTION:
      axiss[event.axis] = round(event.value,2)
    elif event.type == pygame.JOYBUTTONDOWN:                    # When button pressed
      #print(event.dict, event.joy, event.button, 'PRESSED')
      for x,(key,val) in enumerate(buttons.items()):
        if x<10:
          if controller.get_button(x): buttons[key]=1
    elif event.type == pygame.JOYBUTTONUP:
        #print(event.dict, event.joy, event.button, 'released')
        for x,(key,val) in enumerate(buttons.items()):
            if x<10:
                if event.button == x: buttons[key]=0

  # to remove element 2 since axis numbers are 0 1 3 4
  buttons['axis1'],buttons['axis2'],buttons['axis3'],buttons['axis4'] = [axiss[0],axiss[1],axiss[3],axiss[4]]
  if name == '':
    return buttons
  else:
    return buttons[name]

def main():
  print(getJS())
  sleep(0.05)

if __name__ == '__main__':
  while True:
    main()