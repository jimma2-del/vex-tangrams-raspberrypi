'''
This code is based on this YouTube video:
https://www.youtube.com/watch?v=YEYBbFdus-Q&list=PLMoSUbG1Q_r-So6ocbQhMFM8vIByvnRWG&index=5
'''

import pygame

def init():
  pygame.init()
  win = pygame.display.set_mode((100,100))


def getKey(keyName):
  ans = False
  for eve in pygame.event.get():pass
  keyInput = pygame.key.get_pressed()
  myKey = getattr(pygame, 'K_{}'.format(keyName))
  if keyInput [myKey]:
    ans = True
  pygame.display.update()

  return


def main():
  if getKey('q'):
    print('q')
  if getKey('e'):
    print('e')
  if getKey('w'):
    print('w')
  if getKey('s'):
    print('s')
  if getKey('a'):
    print('a')
  if getKey('d'):
    print('d')


if __name__ == '__main__':
  init()
  while True:
    main()