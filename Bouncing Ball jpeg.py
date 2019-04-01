'''
Program to make a ball bounce around inside the window

Change to take into account the size of the image
Change to use a random number so the bounce off the wall is not a repeatable pattern
Change to set the starting position randomally
'''

import pygame
from sys import exit
from pygame.locals import *

# starting positions for the ball

posx = 100
posy = 0

# increments for x and y, will be set to +1 or - 1
incx = 1
incy = 1

# screen size variables
sizex = 750
sizey = 500

pygame.init()

screen = pygame.display.set_mode((sizex,sizey))
screen.fill((0,0,0))
pygame.display.set_caption('Bouncing Ball')

ball = pygame.image.load('small-ball.png').convert()

while True:
  
  pygame.display.update()
  screen.blit(ball, (posx,posy))

  for event in pygame.event.get():
    if event.type == QUIT:
      exit()

  posx = posx + incx
  if posx > sizex or posx < 0:
    incx = incx * -1
    print("increment X:", incx)   #DEBUG

  posy = posy + incy
  if posy > sizey or posy < 0:
    incy = incy * -1
    print ("increment y:", incy)    #DEBUG
  
      
                 

