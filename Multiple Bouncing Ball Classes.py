'''
Program to make a ball bounce around inside the window

Revisions
V2  changed from jpeg to circle
    changed to have a random starting position
    improved exiting of the program
    changed to have a random angle of bounce
    fixed bug where posx or y could be outside limits of screen
    added random choice of colour change
V3  refactored into classes
V4  added multiple balls
    changed to use len colour for random colour selection if no. colours increases
'''

import pygame
from sys import exit
from pygame.locals import *
import random


''' CLASSES  '''
class BouncingBall:

  def __init__(self, sizex, sizey):
    self.sizex = sizex
    self.sizey = sizey
    self.x = random.randint(0,sizex)
    self.y = random.randint(0,sizey)
    # increments for x and y, will be set to +1 or - 1 initially
    self.incx = 1
    self.incy = 1
    # sign values to know if x and y are +ve or -ve
    self.signx = +1
    self.signy = +1
    # colours of the circle
    self.colour = [[255,255,255],[255,0,0],[0,0,255],[0,255,0]]
    self.choice = self.colour[0]
    return

  def DrawCircle(self, window):
    self.window = window
    self.x = self.x + self.incx
    if self.x > self.sizex or self.x < 0:
      self.incx = random.randint(1,3) * self.signx
      self.signx = self.signx * -1
      # ensures the position of x is never outside the window
      if self.x > self.sizex:
        self.x = self.sizex
      elif self.x < 0:
        self.x = 0
      #print('increment, position of X:', self.incx, ':', self.x)   #DEBUG
      self.choice = self.colour[random.randint(0, len(self.colour)-1)]
      #print ('Colour Choice in X:',self.choice)

    self.y = self.y + self.incy
    if self.y > self.sizey or self.y < 0:
      self.incy = random.randint(1,3) * self.signy
      self.signy = self.signy * -1
      # ensures the position of y is never outsdie the window
      if self.y > self.sizey:
        self.y = self.sizey
      elif self.y < 0:
        self.y = 0
      #print('increment, position of y:', self.incy, ':', self.y)    #DEBUG
      self.choice = self.colour[random.randint(0,len(self.colour)-1)]
      #print ('Colour Choice in Y:',self.choice)
      
    # draw the circle
    pygame.draw.circle(self.window, self.choice, (self.x, self.y), 5, 0)
    # draw a black circle bigger with a border to remove the old one
    pygame.draw.circle(self.window, (0,0,0), (self.x, self.y), 15, 10)
    #print('Position of ball X:', self.x, ' Y:', self.y)   #DEBUG
    return

  def ChangeColour(self):
    self.choice = self.colour[random.randint(0,len(self.colour)-1)]
    

# screen size variables
sizex = 750
sizey = 500

pygame.init()

screen = pygame.display.set_mode((sizex,sizey))
screen.fill((0,0,0))
pygame.display.set_caption('Bouncing Ball')

#TODO convert ball to a collection of Bouncing Balls
ball = [BouncingBall(sizex, sizey)]

while True:

  pygame.display.update()

  for b in ball:
    b.DrawCircle(screen)

  for event in pygame.event.get():
    if event.type == QUIT:
      pygame.quit()
      exit()
    if event.type == KEYDOWN:
      #print('Event Key response',event.key)    #DEBUG
      if event.key == K_DOWN:
        ball = ball + [BouncingBall(sizex, sizey)]
      elif event.key == K_UP:
        b.ChangeColour()      

