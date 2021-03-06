# Import modules
import sys, pygame, time, math, PIL
from time import sleep
from pygame.locals import *
from PIL import *
from PIL import Image

# Initialize
maze = 'maze.png'
img = Image.open(maze)
change = 3
width = img.width * change
height = img.height * change
screen = pygame.display.set_mode((width,height))
background = pygame.image.load(maze).convert()
newscreen = pygame.transform.scale(background, (width, height))
sleep = 0

#Colors
color = (0, 188, 0)
white = (255, 255, 255)
black = (255, 255, 255, 255)
blue = (0, 0, 255)
red = (255, 0, 0)
green = (0, 188, 0)

pix = img.load()
list = []

# Locate the starting coordinate
for x in range(0,180):
    if pix[x,179] == (255, 255, 255, 255):
        list.append(x)

xvalueOfStart = list[0] * change
blockSize = len(list) * change
yvalueOfStart = height - blockSize

list = []

# Locate the ending coordinate
for x in range(0,180):
    if pix[x,0] == (255, 255, 255, 255):
        list.append(x)

xvalueOfEnd = list[0] * change

pygame.draw.rect(newscreen, color, pygame.Rect(xvalueOfStart, yvalueOfStart, blockSize, blockSize))
screen.blit(newscreen, (0, 0))
pygame.display.update()

# Function to move forward
# Function to move forward
def moveUp(x, y, blocksize, newcolor, sleep):
    pygame.draw.rect(newscreen, newcolor, pygame.Rect(x, y, blocksize, blocksize))
    pygame.draw.rect(newscreen, color, pygame.Rect(x, y - blocksize, blocksize, blocksize))
    screen.blit(newscreen, (0,0))
    pygame.display.update()
    global currentY
    global currentX
    currentY = y - blocksize
    currentX = x
    time.sleep(sleep)

# Function to move left
def moveDown(x, y, blocksize, newcolor, sleep):
    pygame.draw.rect(newscreen, newcolor, pygame.Rect(x, y, blocksize, blocksize))
    pygame.draw.rect(newscreen, color, pygame.Rect(x, y + blocksize, blocksize, blocksize))
    screen.blit(newscreen, (0,0))
    pygame.display.update()
    global currentY
    global currentX    
    currentY = y + blocksize
    currentX = x
    time.sleep(sleep)
    
# Function to move left  
def moveLeft(x, y, blocksize, newcolor, sleep):
    pygame.draw.rect(newscreen, newcolor, pygame.Rect(x, y, blocksize, blocksize))
    pygame.draw.rect(newscreen, color, pygame.Rect(x - blocksize, y, blocksize, blocksize))
    screen.blit(newscreen, (0,0))
    pygame.display.update()
    global currentX
    global currentY        
    currentX = x - blocksize
    currentY = y
    time.sleep(sleep)

# Function to move right
def moveRight(x, y, blocksize, newcolor, sleep):
    pygame.draw.rect(newscreen, newcolor, pygame.Rect(x, y, blocksize, blocksize))
    pygame.draw.rect(newscreen, color, pygame.Rect(x + blocksize, y, blocksize, blocksize))
    screen.blit(newscreen, (0,0))
    pygame.display.update()
    global currentX
    global currentY        
    currentX = x + blocksize
    currentY = y
    time.sleep(sleep)

#Initialization of currentX and currentY
def varsInit(x, y):
    global currentX
    global currentY
    global direction
    currentX = x
    currentY = y
    direction = 1

#Algorithm to determine direction to move if facing up
def up(replace):
    global direction
    if newscreen.get_at((currentX + blockSize, currentY)) == white:#right
        moveRight(currentX, currentY, blockSize, replace, sleep)
        direction = 2
    elif newscreen.get_at((currentX, currentY - blockSize)) == white:#up        
        moveUp(currentX, currentY, blockSize, replace, sleep)
        direction = 1
    elif newscreen.get_at((currentX - blockSize, currentY)) == white:#left
        moveLeft(currentX, currentY, blockSize, replace, sleep)
        direction = 3
    elif newscreen.get_at((currentX, currentY + blockSize)) == white:#down
        moveDown(currentX, currentY, blockSize, replace, sleep)
        direction = 4
    else:
        if newscreen.get_at((currentX - blockSize, currentY)) == blue:#left
            moveLeft(currentX, currentY, blockSize, (0,255,255), sleep)
            direction = 3
        elif newscreen.get_at((currentX, currentY + blockSize)) == blue:#down
            moveDown(currentX, currentY, blockSize, (0,255,255), sleep)
            direction = 4
        elif newscreen.get_at((currentX + blockSize, currentY)) == blue:#right
            moveRight(currentX, currentY, blockSize, (0,255,255), sleep)
            direction = 2
        elif newscreen.get_at((currentX, currentY - blockSize)) == blue:#up        
            moveUp(currentX, currentY, blockSize, (0,255,255), sleep)
            direction = 1
    
#Algorithm to determine direction to move if facing right
def right(replace):
    global direction
    if newscreen.get_at((currentX, currentY + blockSize)) == white:#down
        moveDown(currentX, currentY, blockSize, replace, sleep)
        direction = 4
    elif newscreen.get_at((currentX + blockSize, currentY)) == white:#right
        moveRight(currentX, currentY, blockSize, replace, sleep)
        direction = 2
    elif newscreen.get_at((currentX, currentY - blockSize)) == white:#up        
        moveUp(currentX, currentY, blockSize, replace, sleep)
        direction = 1
    elif newscreen.get_at((currentX - blockSize, currentY)) == white:#left
        moveLeft(currentX, currentY, blockSize, replace, sleep)
        direction = 3
    else:
        if newscreen.get_at((currentX, currentY - blockSize)) == blue:#up        
            moveUp(currentX, currentY, blockSize, (0,255,255), sleep)
            direction = 1
        elif newscreen.get_at((currentX - blockSize, currentY)) == blue:#left
            moveLeft(currentX, currentY, blockSize, (0,255,255), sleep)
            direction = 3
        elif newscreen.get_at((currentX, currentY + blockSize)) == blue:#down
            moveDown(currentX, currentY, blockSize, (0,255,255), sleep)
            direction = 4
        elif newscreen.get_at((currentX + blockSize, currentY)) == blue:#right
            moveRight(currentX, currentY, blockSize, (0,255,255), sleep)
            direction = 2

#Algorithm to determine direction to move if facing left
def left(replace):
    global direction
    if newscreen.get_at((currentX, currentY - blockSize)) == white:#up        
        moveUp(currentX, currentY, blockSize, replace, sleep)
        direction = 1
    elif newscreen.get_at((currentX - blockSize, currentY)) == white:#left
        moveLeft(currentX, currentY, blockSize, replace, sleep)
        direction = 3
    elif newscreen.get_at((currentX, currentY + blockSize)) == white:#down
        moveDown(currentX, currentY, blockSize, replace, sleep)
        direction = 4
    elif newscreen.get_at((currentX + blockSize, currentY)) == white:#right
        moveRight(currentX, currentY, blockSize, replace, sleep)
        direction = 2
    else:
        if newscreen.get_at((currentX, currentY + blockSize)) == blue:#down
            moveDown(currentX, currentY, blockSize, (0,255,255), sleep)
            direction = 4
        elif newscreen.get_at((currentX + blockSize, currentY)) == blue:#right
            moveRight(currentX, currentY, blockSize, (0,255,255), sleep)
            direction = 2
        elif newscreen.get_at((currentX, currentY - blockSize)) == blue:#up        
            moveUp(currentX, currentY, blockSize, (0,255,255), sleep)
            direction = 1
        elif newscreen.get_at((currentX - blockSize, currentY)) == blue:#left
            moveLeft(currentX, currentY, blockSize, (0,255,255), sleep)
            direction = 3

#Algorithm to determine direction to move if facing down
def down(replace):
    global direction
    if newscreen.get_at((currentX - blockSize, currentY)) == white:#left
        moveLeft(currentX, currentY, blockSize, replace, sleep)
        direction = 3
    elif newscreen.get_at((currentX, currentY + blockSize)) == white:#down
        moveDown(currentX, currentY, blockSize, replace, sleep)
        direction = 4
    elif newscreen.get_at((currentX + blockSize, currentY)) == white:#right
        moveRight(currentX, currentY, blockSize, replace, sleep)
        direction = 2
    elif newscreen.get_at((currentX, currentY - blockSize)) == white:#up        
        moveUp(currentX, currentY, blockSize, replace, sleep)
        direction = 1
    else:
        if newscreen.get_at((currentX + blockSize, currentY)) == blue:#right
            moveRight(currentX, currentY, blockSize, (0,255,255), sleep)
            direction = 2
        elif newscreen.get_at((currentX, currentY - blockSize)) == blue:#up        
            moveUp(currentX, currentY, blockSize, (0,255,255), sleep)
            direction = 1
        elif newscreen.get_at((currentX - blockSize, currentY)) == blue:#left
            moveLeft(currentX, currentY, blockSize, (0,255,255), sleep)
            direction = 3
        elif newscreen.get_at((currentX, currentY + blockSize)) == blue:#down
            moveDown(currentX, currentY, blockSize, (0,255,255), sleep)
            direction = 4

varsInit(xvalueOfStart, yvalueOfStart)

moveUp(currentX, currentY, blockSize, blue, sleep)

while 0 != currentY:
    pygame.event.get()
    if direction == 1:#up
        up(blue)
    elif direction == 2:
        right(blue)
    elif direction == 3:
        left(blue)
    elif direction == 4:
        down(blue)

direction = 1
currentX = blockSize
currentY = blockSize
whiteListX = []
whiteListY = []
deadEnds = 1

#-------------DEAD END FILLER------------
while True:
    pygame.event.get()
    #Define variables
    deadEnds = 0
    intersection = 0
    #Check the color of each and add location to list if white
    while currentY <= (height - blockSize):
        getCur = newscreen.get_at((currentX, currentY))
        if getCur == (0,255,255):
            whiteListX.append(currentX)
            whiteListY.append(currentY)
        currentX = currentX + blockSize
        if currentX >= (width - blockSize + 1):
            currentX = 0
            currentY = currentY + blockSize
    whiteListLength = len(whiteListX)
    #Determine if each white space is a deadend
    for x in range (0, whiteListLength):
        pygame.draw.rect(newscreen, white, pygame.Rect(whiteListX[x], whiteListY[x], blockSize, blockSize))
    screen.blit(newscreen, (0,0))
    pygame.display.update()
    break

time.sleep(5)