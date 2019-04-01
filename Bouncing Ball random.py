'''
Program to make a ball bounce around inside the window

Revisions
V2  changed from jpeg to circle
    changed to have a random starting position
    improved exiting of the program
    changed to have a random angle of bounce
    fixed bug where posx or y could be outside limits of screen
    added random choice of colour change
'''

import pygame
from sys import exit
from pygame.locals import *
import random


# increments for x and y, will be set to +1 or - 1 initially
incx = 1
incy = 1

# sign values to know if x and y are +ve or -ve
signx = +1
signy = +1

# screen size variables
sizex = 750
sizey = 500

# colours of the circle
colour = [[255,255,255],[255,0,0],[0,0,255],[0,255,0]]
choice = colour[0]

# starting positions for the ball
posx = random.randint(0,sizex)
posy = random.randint(0,sizey)

pygame.init()

screen = pygame.display.set_mode((sizex,sizey))
screen.fill((0,0,0))
pygame.display.set_caption('Bouncing Ball')

while True:
  
  pygame.display.update()
  # draw the circle
  pygame.draw.circle(screen, choice, (posx, posy), 5, 0)
  # draw a black circle bigger with a border to remove the old one
  pygame.draw.circle(screen, (0,0,0), (posx, posy), 15, 10)

  for event in pygame.event.get():
    if event.type == QUIT:
      pygame.quit()
      exit()
    if event.type == KEYUP:
      choice = colour[random.randint(0,3)]

  posx = posx + incx
  if posx > sizex or posx < 0:
    incx = random.randint(1,3) * signx
    signx = signx * -1
    # ensures the position of x is never outsdie the window
    if posx > sizex:
      posx = sizex
    elif posx < 0:
      posx = 0
    #print('increment, position of X:', incx, ':', posx)   #DEBUG
    choice = colour[random.randint(0,3)]

  posy = posy + incy
  if posy > sizey or posy < 0:
    incy = random.randint(1,3) * signy
    signy = signy * -1
    # ensures the position of y is never outsdie the window
    if posy > sizey:
      posy = sizey
    elif posy < 0:
      posy = 0
    #print('increment, position of y:', incy, ':', posy)    #DEBUG
    choice = colour[random.randint(0,3)]
  


                 

