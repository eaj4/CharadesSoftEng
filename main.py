import pygame
import time
import pip._vendor.requests
import json

pygame.init()

# RGB color definitions
black = (0, 0, 0)
white = (255, 255, 255)
red   = (255, 0, 0)
lightRed   = (255, 204, 203)
purple  = (255, 0, 255)
lightPurple  = (193, 153, 190)
yellow = (255, 255, 0)

#timer variables
clock = pygame.time.Clock()
counter, timer_text = 60, '60'.rjust(3)
pygame.time.set_timer(pygame.USEREVENT, 1000)
timer_font = pygame.font.SysFont('Consolas', 30)

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
Header  = font1.render ('Play Charades!', True, black)
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
GameScreen.blit (Header , (width/2-150, height/2-175))
GameScreen.blit (Directions , (width/2-185, height/2-125))

#create quit button
pygame.draw.rect(GameScreen,lightRed,[width/2-125, height/2+100,80,40])
GameScreen.blit (quit , (width/2-125, height/2+100))
   
#create next button
pygame.draw.rect(GameScreen,lightPurple,[width/2+25, height/2+100,85,40])
GameScreen.blit (nextWord , (width/2+25, height/2+100))


getResponse = json.loads (randWord.text)
getResponse = json.dumps (getResponse)
displayRandWord = font1.render (getResponse , True , yellow)  
#Display Random Word
GameScreen.blit (displayRandWord, (width/2-115, height/2-25))    

    
  
pygame.display.update ()

running = True
while running:
    getResponse = json.loads (randWord.text)
    getResponse = json.dumps (getResponse)
    displayRandWord = font1.render (getResponse , True , yellow)
    
    for event in pygame.event.get():
        if event.type == pygame.USEREVENT: 
            counter -= 1
            timer_text = str(counter).rjust(3) if counter > 0 else 'Time is up!'
        if event.type == pygame.QUIT:
            running = False
            

    # mouse click check
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Quit button press
            if 125 <= mouse [0] <= 205 and 400 <= mouse [1] <= 440:
                pygame.quit ()
           
            # next button press
            if 200 <= mouse [0] <= 250 and 300 <= mouse [1] <= 350:
                randWord = pip._vendor.requests.get ("https://random-word-api.herokuapp.com/word?number=1");
                  
                  
                  
    GameScreen.fill((255, 255, 255))
    GameScreen.blit (Header , (width/2-175, height/2-175))
    GameScreen.blit (Directions , (width/2-185, height/2-125))
    GameScreen.blit(timer_font.render(timer_text, True, (0, 0, 0)), (32, 48))
    GameScreen.blit (quit , (width/2-50, height/2+100))
    GameScreen.blit (nextWord , (width/2+50, height/2+100))
    pygame.display.flip()
    clock.tick(60)
            
