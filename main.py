import pygame
import time
import pip._vendor.requests
import json

pygame.init()

# RGB color definitions
black = (0, 0, 0)
white = (255, 255, 255)
red   = (255, 0, 0)
blue  = (0, 0, 255)
yellow = (255, 255, 0)


# Screen Dimensions
height = 800
width  = 500


# GUI Setup
GameScreen = pygame.display.set_mode ((width, height))
pygame.display.set_caption ('Charades!!!')

# Set GameScreen Fonts 
font1 = pygame.font.Font ('freesansbold.ttf', 32)
font2 = pygame.font.SysFont ('Arial',35)


# introduction text
Header  = font1.render ('Play Cherades!', True, black)
Directions = font2.render ('Act Out Your Given Word', True, black)




running = True
while running:
    for event in pygame.event.get():
    if event.type == pygame.QUIT:
    running = False



# Set screen color 
GameScreen.fill (white)


    
#Display gamescreen messages
GameScreen.blit (Header , (width/2-175, height/2-175))
GameScreen.blit (Directions , (width/2-185, height/2-125))
    
  
pygame.display.update ()
