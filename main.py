import pygame
import time
import pip._vendor.requests
import json

pygame.init()

# RGB color definitions
black = (0, 0, 0)
white = (255, 255, 255)
red   = (255, 0, 0)
purple  = (255, 0, 255)
yellow = (255, 255, 0)


# Screen Dimensions
height = 600
width  = 400


# GUI Setup
GameScreen = pygame.display.set_mode ((width, height))
pygame.display.set_caption ('Charades!!!')

# Set GameScreen Fonts 
font1 = pygame.font.Font ('freesansbold.ttf', 32)
font2 = pygame.font.SysFont ('Arial',35)


# introduction text
Header  = font1.render ('Play Cherades!', True, black)
Directions = font2.render ('Act Out Your Given Word', True, black)

# buttons 
nextWord = font2.render ('NEXT' , True , purple)
quit = font2.render ('QUIT' , True , red)


# Return 1 word from random word generator
randWord = pip._vendor.requests.get ("https://random-word-api.herokuapp.com/word?number=1");



# Get mouse Position
mouse = pygame.mouse.get_pos ()


# Set screen color 
GameScreen.fill (white)

#Display gamescreen messages
GameScreen.blit (Header , (width/2-175, height/2-175))
GameScreen.blit (Directions , (width/2-185, height/2-125))

#create quit button
gameScreen.blit (quit , (width/2-50, height/2+100))
   
#create next button
gameScreen.blit (nextWord , (width/2+50, height/2+100))

#actual Charades word
gameScreen.blit (RandWord, (width/2, height/2))
    

    
  
pygame.display.update ()

running = True
while running:
    getResponse = json.loads (randWord.text)
    getResponse = json.dumps (getResponse)
    displayRandWord = font1.render (getResponse , True , Yellow)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    # mouse click check
        if ev.type == pygame.MOUSEBUTTONDOWN:
            # Quit button press
            if 100 <= mouse [0] <= 150 and 300 <= mouse [1] <= 350:
                pygame.quit ()
           
            # next button press
            if 200 <= mouse [0] <= 250 and 300 <= mouse [1] <= 350:
                randWord = pip._vendor.requests.get ("https://random-word-api.herokuapp.com/word?number=1");
            
