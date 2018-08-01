# Import modules
import sys, pygame, time, math
from time import sleep
from PIL import Image

# Display background image
image = 'start.png'
change = 1
img = Image.open(image)
width = img.width * change
height = img.height * change
screen = pygame.display.set_mode((width,height))
background = pygame.image.load(image).convert()
newscreen = pygame.transform.scale(background, (width, height))
screen.blit(newscreen, (0,0))
pygame.display.update()

# Start page
running = True
while running:
    event = pygame.event.wait()
    if event.type == pygame.MOUSEBUTTONUP:
        if event.button == 1:
            x,y = pygame.mouse.get_pos()
            if 147 <= x <= 441 and 440 <= y <= 526:
                running = False

#Settings Page
background = pygame.image.load('settings.png').convert()
newscreen = pygame.transform.scale(background, (width, height))
screen.blit(newscreen, (0,0))
pygame.display.update()

sleep = 0.02
maze = 'maze.png'
running = True
while running:
    event = pygame.event.wait()
    if event.type == pygame.MOUSEBUTTONUP:
        if event.button == 1:
            x,y = pygame.mouse.get_pos()
            if 190 <= x <= 470 and 514 <= y <= 628: #Next
                running = False
            if 28 <= x <= 210 and 435 <= y <= 478: #0.5x
                sleep = 0.03
            if 234 <= x <= 415 and 435 <= y <= 478: #1.0x
                sleep = 0.02
            if 441 <= x <= 622 and 435 <= y <= 478: #1.5x
                sleep = 0.01
            if 29 <= x <= 124 and 113 <= y <= 207: #maze1
                maze = 'maze.png'
            if 156 <= x <= 250 and 113 <= y <= 207: #maze2
                maze = 'maze2.png'
            if 282 <= x <= 377 and 113 <= y <= 207: #maze3
                maze = 'maze3.png'
            if 406 <= x <= 498 and 113 <= y <= 207: #maze4
                maze = 'maze4.png'
            if 528 <= x <= 621 and 113 <= y <= 207: #maze5
                maze = 'maze5.png'
            if 29 <= x <= 124 and 239 <= y <= 333: #maze6
                maze = 'maze6.png'
            if 156 <= x <= 250 and 239 <= y <= 333: #maze7
                maze = 'maze7.png'
            if 282 <= x <= 377 and 239 <= y <= 333: #maze8
                maze = 'maze8.png'
            if 406 <= x <= 498 and 239 <= y <= 333: #maze9
                maze = 'maze9.png' 
            if 528 <= x <= 621 and 239 <= y <= 333: #maze10
                maze = 'maze10.png'

#Information Page
background = pygame.image.load('information.png').convert()
newscreen = pygame.transform.scale(background, (width, height))
screen.blit(newscreen, (0,0))
pygame.display.update()

running = True
while running:
    event = pygame.event.wait()
    if event.type == pygame.MOUSEBUTTONUP:
        if event.button == 1:
            x,y = pygame.mouse.get_pos()
            if 190 <= x <= 469 and 516 <= y <= 628:
                running = False

#Run mazes
import rightturn
import deadend
import intersection
import priorities

#Results page
background = pygame.image.load('results.png').convert()
newscreen = pygame.transform.scale(background, (width, height))
screen.blit(newscreen, (0,0))
pygame.display.update()

time.sleep(5)