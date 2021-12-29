# Modules:

from tkinter import READABLE
import pygame
from pygame import *
from PIL import Image

# Setting some things up:

screen = pygame.display.set_mode((700, 500))

pygame.init()

image.load("C:\\Users\\ascom\\Desktop\\Resturantimgs\\Banana2.png")

running = True
while running:
    for event in pygame.event.get():
     if event.type == pygame.QUIT:
      running = False
    if running == False:
     pygame.quit()
     exit()



def drawRect():
    global RED   
    global BLUE          
    global YELLOW
    YELLOW = (255, 255, 0)
    BLUE = (0, 17, 255)
    RED = (255, 0, 0)
    size = (50, 50)
    rect_border = pygame.Surface(size)  # Create a Surface to draw on
    pygame.draw.rect(rect_border, RED, rect_border.get_rect(), 10)  # Draw on it.
    rect_filled = pygame.Surface(size)
    pygame.draw.rect(rect_filled, RED, rect_filled.get_rect())

    
    

drawRect()
pygame.display.flip()


