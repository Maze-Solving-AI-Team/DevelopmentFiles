'''
=INTERSECTIONS=
intersections solves a maze by marking intersections and paths traveled

blue=intersection
red=path the AI came into the intersection from
green=path the AI has used already(hit dead end and came back to intersection)

- \/ this is repeated until the end \/ -
AI moves until it finds an intersection
places blue on intersection and red on path traveled
moves into white tile
if intersection is blue(traveled), then AI checks for white
if no white is present(all paths traveled), then AI travels back down red path until it hits previous intersection

- \/ special cases \/ -
+if there are consecutive intersections(no space in between)
    -AI cannot put red down(or it overwrites the blue of the other intersection)
    -if all paths are traveled and no red is present, AI checks for blue(instead of red)
+(IN PROGRESS)if there is 1 space between intersections and they connect to each other on another path(loop)
    -when AI goes around loop and goes onto first intersection,
    -it sees that there are 2 red blocks(1 correct from entering, 1 wrong from 2nd intersection)
    -then uses a log of coordinates of red to find oldest red around it and travel down the path
'''

# Import modules
import sys, pygame, time, math
from time import sleep
from pygame.locals import *
from PIL import Image
import timing
from main import sleep
from main import maze

maze=('maze10.png')
# Initialize
img = Image.open(maze)
change = 3
width = img.width * change
height = img.height * change
screen = pygame.display.set_mode((width,height))
background = pygame.image.load(maze).convert()
newscreen = pygame.transform.scale(background, (width, height))
sleepTime = sleep
#number of turns
upCount = 0
leftCount = 0
rightCount = 0

#Colors
color = (0, 188, 0)
white = (255, 255, 255)
black = (0, 0, 0, 0)
blue = (0, 0, 255)
red = (255, 0, 0)
green = (0, 188, 0)

# Recognizing black/white
#-print(width, height)
size = [img.size]
#-print(size[0])
colors = img.getcolors()
#-print(colors)
pix = img.load()
list = []

# Locate the starting coordinate
for x in range(0,180):
    if pix[x,179] == (255, 255, 255, 255):
        list.append(x)

xvalueOfStart = list[0] * change
#-print(xvalueOfStart)

blockSize = len(list) * change

yvalueOfStart = height - blockSize

list = []

# Locate the ending coordinate
for x in range(0,180):
    if pix[x,0] == (255, 255, 255, 255):
        list.append(x)

xvalueOfEnd = list[0] * change
#-print(xvalueOfEnd)

pygame.draw.rect(newscreen, color, pygame.Rect(xvalueOfStart, yvalueOfStart, blockSize, blockSize))
screen.blit(newscreen, (0,0))
pygame.display.update()
time.sleep(sleepTime)

# Function to move forward
def moveUp(x, y, blocksize, newcolor):
    pygame.draw.rect(newscreen, newcolor, pygame.Rect(x, y, blockSize, blockSize))
    pygame.draw.rect(newscreen, color, pygame.Rect(x+1, y - blocksize+1, blockSize-2, blockSize-2))
    screen.blit(newscreen, (0,0))
    pygame.display.update()
    global currentY
    global currentX
    currentY = y - blocksize
    currentX = x

# Function to move down
def moveDown(x, y, blocksize, newcolor):
    pygame.draw.rect(newscreen, newcolor, pygame.Rect(x, y, blockSize, blockSize))
    pygame.draw.rect(newscreen, color, pygame.Rect(x+1, y + blocksize+1, blockSize-2, blockSize-2))
    screen.blit(newscreen, (0,0))
    pygame.display.update()
    global currentY
    global currentX    
    currentY = y + blocksize
    currentX = x   
    
# Function to move left  
def moveLeft(x, y, blocksize, newcolor):
    pygame.draw.rect(newscreen, newcolor, pygame.Rect(x, y, blockSize, blockSize))
    pygame.draw.rect(newscreen, color, pygame.Rect(x - blocksize+1, y+1, blockSize-2, blockSize-2))
    screen.blit(newscreen, (0,0))
    pygame.display.update()
    global currentX
    global currentY        
    currentX = x - blocksize
    currentY = y

# Function to move right
def moveRight(x, y, blocksize, newcolor):
    pygame.draw.rect(newscreen, newcolor, pygame.Rect(x, y, blockSize, blockSize))
    pygame.draw.rect(newscreen, color, pygame.Rect(x + blocksize+1, y+1, blockSize-2, blockSize-2))
    screen.blit(newscreen, (0,0))
    pygame.display.update()
    global currentX
    global currentY        
    currentX = x + blocksize
    currentY = y

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
    if newscreen.get_at((currentX, currentY - blockSize)) == white:#up        
        moveUp(currentX, currentY, blockSize, replace)
        #-print("up-Move up called")
        time.sleep(sleepTime)
        direction = 1
    elif newscreen.get_at((currentX + blockSize, currentY)) == white:#right
        moveRight(currentX, currentY, blockSize, replace)
        #-print("up-Move right called")
        time.sleep(sleepTime)
        direction = 2
    elif newscreen.get_at((currentX - blockSize, currentY)) == white:#left
        moveLeft(currentX, currentY, blockSize, replace)
        #-print("up-Move left called")
        time.sleep(sleepTime)
        direction = 3
        #check for blue paths
    elif newscreen.get_at((currentX,currentY-blockSize))==blue:
        moveUp(currentX, currentY, blockSize, replace)
        #-print("up-Move up blue called")
        time.sleep(sleepTime)
        direction = 1
    elif newscreen.get_at((currentX+blockSize,currentY))==blue:
        #-print("up-Move right blue called")
        time.sleep(sleepTime)
        direction = 2
    elif newscreen.get_at((currentX-blockSize,currentY))==blue:
        moveLeft(currentX, currentY, blockSize, replace)
        #-print("up-Move left blue called")
        time.sleep(sleepTime)
        direction = 3
        #check rear
    elif newscreen.get_at((currentX, currentY + blockSize)) == white or newscreen.get_at((currentX, currentY + blockSize)) == blue:#down
        moveDown(currentX, currentY, blockSize, replace)
        #-print("up-Move down called")
        time.sleep(sleepTime)
        direction = 4
    #-print("direction-up", direction)
    
#Algorithm to determine direction to move if facing right
def right(replace):
    global direction
    if newscreen.get_at((currentX + blockSize, currentY)) == white:#right
        moveRight(currentX, currentY, blockSize, replace)
        #-print("right-Move right called")
        time.sleep(sleepTime)
        direction = 2
    elif newscreen.get_at((currentX, currentY + blockSize)) == white:#down
        moveDown(currentX, currentY, blockSize, replace)
        #-print("right-Move down called")
        time.sleep(sleepTime)
        direction = 4
    elif newscreen.get_at((currentX, currentY - blockSize)) == white:#up        
        moveUp(currentX, currentY, blockSize, replace)
        #-print("right-Move up called")
        time.sleep(sleepTime)
        direction = 1
    #check blue
    elif newscreen.get_at((currentX + blockSize, currentY)) == blue:#right
        moveRight(currentX, currentY, blockSize, replace)
        #-print("right-Move right blue called")
        time.sleep(sleepTime)
        direction = 2
    elif newscreen.get_at((currentX, currentY + blockSize)) == blue:#down
        moveDown(currentX, currentY, blockSize, replace)
        #-print("right-Move down called")
        time.sleep(sleepTime)
        direction = 4
    elif newscreen.get_at((currentX, currentY - blockSize)) == blue:#up        
        moveUp(currentX, currentY, blockSize, replace)
        #-print("right-Move up blue called")
        time.sleep(sleepTime)
        direction = 1
    #check rear
    elif newscreen.get_at((currentX - blockSize, currentY)) == white or newscreen.get_at((currentX - blockSize, currentY)) == blue:#left
        moveLeft(currentX, currentY, blockSize, replace)
        #-print("right-Move left called")
        time.sleep(sleepTime)
        direction = 3
    #-print("direction-right", direction)
    
#Algorithm to determine direction to move if facing left
def left(replace):
    global direction
    if newscreen.get_at((currentX - blockSize, currentY)) == white:#left
        moveLeft(currentX, currentY, blockSize, replace)
        #-print("left-Move left called")
        time.sleep(sleepTime)
        direction = 3
    elif newscreen.get_at((currentX, currentY - blockSize)) == white:#up
        moveUp(currentX, currentY, blockSize, replace)
        #-print("left-Move up called")
        time.sleep(sleepTime)
        direction = 1
    elif newscreen.get_at((currentX, currentY + blockSize)) == white:#down        
        moveDown(currentX, currentY, blockSize, replace)
        #-print("left-Move down called")
        time.sleep(sleepTime)
        direction = 4
        #check blue
    elif newscreen.get_at((currentX - blockSize, currentY)) == blue:#left
        moveLeft(currentX, currentY, blockSize, replace)
        #-print("left-Move left blue called")
        time.sleep(sleepTime)
        direction = 3
    elif newscreen.get_at((currentX, currentY - blockSize)) == blue:#up
        moveUp(currentX, currentY, blockSize, replace)
        #-print("left-Move up blue called")
        time.sleep(sleepTime)
        direction = 1
    elif newscreen.get_at((currentX, currentY + blockSize)) == blue:#down        
        moveDown(currentX, currentY, blockSize, replace)
        #-print("left-Move down blue called")
        time.sleep(sleepTime)
        direction = 4
        #check rear
    elif newscreen.get_at((currentX + blockSize, currentY)) == white or newscreen.get_at((currentX + blockSize, currentY)) == blue:#right
        moveRight(currentX, currentY, blockSize, replace)
        #-print("left-Move right called")
        time.sleep(sleepTime)
        direction = 2
    #-print("direction-left", direction)

#Algorithm to determine direction to move if facing down
def down(replace):
    global direction
    if newscreen.get_at((currentX, currentY + blockSize)) == white:#down
        moveDown(currentX, currentY, blockSize, replace)
        #-print("down-Move down called")
        time.sleep(sleepTime)
        direction = 4
    elif newscreen.get_at((currentX - blockSize, currentY)) == white:#left
        moveLeft(currentX, currentY, blockSize, replace)
        #-print("down-Move left called")
        time.sleep(sleepTime)
        direction = 3
    elif newscreen.get_at((currentX + blockSize, currentY)) == white:#right
        moveRight(currentX, currentY, blockSize, replace)
        #-print("down-Move right called")
        time.sleep(sleepTime)
        direction = 2
        #check blue
    elif newscreen.get_at((currentX, currentY + blockSize)) == blue:#down
        moveDown(currentX, currentY, blockSize, replace)
        #-print("down-Move down blue called")
        time.sleep(sleepTime)
        direction = 4
    elif newscreen.get_at((currentX - blockSize, currentY)) == blue:#left
        moveLeft(currentX, currentY, blockSize, replace)
        #-print("down-Move left blue called")
        time.sleep(sleepTime)
        direction = 3
    elif newscreen.get_at((currentX + blockSize, currentY)) == blue:#right
        moveRight(currentX, currentY, blockSize, replace)
        #-print("down-Move right blue called")
        time.sleep(sleepTime)
        direction = 2
        #check rear
    elif newscreen.get_at((currentX, currentY - blockSize)) == white or newscreen.get_at((currentX, currentY - blockSize)) == blue:#up        
        moveUp(currentX, currentY, blockSize, replace)
        #-print("down-Move up called")
        time.sleep(sleepTime)
        direction = 1
    #-print("direction-down", direction)

#returns boolean if current tile is intersection
def isIntersection():
    global direction
    paths = 0 
    #-print("isIntersection")
    if newscreen.get_at((currentX, currentY - blockSize)) == white or newscreen.get_at((currentX, currentY - blockSize)) == red or newscreen.get_at((currentX, currentY - blockSize)) == green or newscreen.get_at((currentX, currentY - blockSize)) == blue:
        paths = paths + 1
        #-print("returnUp")
    if newscreen.get_at((currentX - blockSize, currentY)) == white or newscreen.get_at((currentX - blockSize, currentY)) == red or newscreen.get_at((currentX - blockSize, currentY)) == green or newscreen.get_at((currentX - blockSize, currentY)) == blue:
        paths = paths + 1
        #-print("returnLeft")
    if newscreen.get_at((currentX + blockSize, currentY)) == white or newscreen.get_at((currentX + blockSize, currentY)) == red or newscreen.get_at((currentX + blockSize, currentY)) == green or newscreen.get_at((currentX + blockSize, currentY)) == blue:
        paths = paths + 1
        #-print("returnRight")
    if  newscreen.get_at((currentX, currentY + blockSize)) == white or newscreen.get_at((currentX, currentY + blockSize)) == red or newscreen.get_at((currentX, currentY + blockSize)) == green or newscreen.get_at((currentX, currentY + blockSize)) == blue:
        paths = paths + 1
        #-print("returnDown")
    #-print("direction-isIntersection", direction)
    
    if paths > 2:
        #-print(paths)
        #-print("isIntersection-TRUE")
        return True
    else:
        #-print(paths)
        #-print("isIntersection-FALSE")
        return False

varsInit(xvalueOfStart, yvalueOfStart)

moveUp(currentX, currentY, blockSize, white)

direction = 1

def checkSurround(color):#returns direction or 0 if no color present on intersection paths
    global direction
    paths=0
    x=0
    if newscreen.get_at((currentX, currentY - blockSize)) == color:#up
        #direction = 4
        #-print("checkRed-red up-AI faces down")#debug
        paths+=1
        x=1
    if newscreen.get_at((currentX + blockSize, currentY)) == color:#right
        #direction = 3
        #-print("checkRed-red right-AI faces left")#debug
        paths+=1
        x=2
    if newscreen.get_at((currentX - blockSize, currentY)) == color:#left
        #direction = 2
        #-print("checkRed-red left-AI faces right")#debug
        paths+=1
        x=3
    if newscreen.get_at((currentX,currentY+blockSize))==color:#down
        #direction = 1
        #-print("checkRed-red down-AI faces up")#debug
        paths+=1
        x=4
    if paths>1:
        x=5
    #-print("checkRed-no red present")#debug
    return x
    #-print("direction-checkRed", direction)

def addCount(isInt,directionMove,firstTime):
    global direction,rightCount,upCount,leftCount
    #direction=direction coming into intersection
    #directionMove=direction leaving intersection
    if isInt:
        #-print("addCount-isIntersection-TRUE")#debug
        #-print("addCount-checkRed output",checkSurround(red))
        if checkSurround(red)==4:#AI faces up
            #-print("addCount-AI up")#debug
            if directionMove==1:#up
                upCount+=1
            if directionMove==3:#left
                leftCount+=1
            if directionMove==2:#right
                rightCount+=1
            if direction==4:#AI comes from top
                upCount-=1
            if direction==3:#AI comes from right
                rightCount-=1
            if direction==2:#AI comes from left
                leftCount-=1
        if checkSurround(red)==3:#AI faces right
            #-print("addCount-AI right")#debug
            if directionMove==2:#right
                upCount+=1
            if directionMove==1:#up
                leftCount+=1
            if directionMove==4:#down
                rightCount+=1
            if direction==3:#AI comes from right
                upCount-=1
            if direction==1:#AI comes from bottom
                rightCount-=1
            if direction==4:#AI comes from top
                leftCount-=1
        if checkSurround(red)==2:#AI faces left
            #-print("addCount-AI left")#debug
            if directionMove==3:#left
                upCount+=1
            if directionMove==4:#down
                leftCount+=1
            if directionMove==1:#up
                rightCount+=1
            if direction==2:#AI comes from left
                upCount-=1
            if direction==4:#AI comes from top
                rightCount-=1
            if direction==1:#AI comes from bottom
                leftCount-=1
        if checkSurround(red)==1:#AI faces down
            #-print("addCount-AI down")#debug
            if directionMove==4:#down
                upCount+=1
            if directionMove==2:#right
                leftCount+=1
            if directionMove==3:#left
                rightCount+=1
            if direction==1:#AI comes from bottom
                upCount-=1
            if direction==2:#AI comes from left
                rightCount-=1
            if direction==3:#AI comes from right
                leftCount-=1
        #check blue
        if checkSurround(red)==0:
            if checkSurround(blue)==4:#AI faces up
                #-print("addCount-AI up")#debug
                if directionMove==1:#up
                    upCount+=1
                if directionMove==3:#left
                    leftCount+=1
                if directionMove==2:#right
                    rightCount+=1
                if direction==4:#AI comes from top
                    upCount-=1
                if direction==3:#AI comes from right
                    rightCount-=1
                if direction==2:#AI comes from left
                    leftCount-=1
            if checkSurround(red)==3:#AI faces right
                #-print("addCount-AI right")#debug
                if directionMove==2:#right
                    upCount+=1
                if directionMove==1:#up
                    leftCount+=1
                if directionMove==4:#down
                    rightCount+=1
                if direction==3:#AI comes from right
                    upCount-=1
                if direction==1:#AI comes from bottom
                    rightCount-=1
                if direction==4:#AI comes from top
                    leftCount-=1
            if checkSurround(red)==2:#AI faces left
                #-print("addCount-AI left")#debug
                if directionMove==3:#left
                    upCount+=1
                if directionMove==4:#down
                    leftCount+=1
                if directionMove==1:#up
                    rightCount+=1
                if direction==2:#AI comes from left
                    upCount-=1
                if direction==4:#AI comes from top
                    rightCount-=1
                if direction==1:#AI comes from bottom
                    leftCount-=1
            if checkSurround(red)==1:#AI faces down
                #-print("addCount-AI down")#debug
                if directionMove==4:#down
                    upCount+=1
                if directionMove==2:#right
                    leftCount+=1
                if directionMove==3:#left
                    rightCount+=1
                if direction==1:#AI comes from bottom
                    upCount-=1
                if direction==2:#AI comes from left
                    rightCount-=1
                if direction==3:#AI comes from right
                    leftCount-=1


intersectionX=[]
intersectionY=[]
intersectionNum=0
# Check if all paths of an intersection have been travelled. If so, go back on red
def intersection(isInt,firstTime):
    global direction, upCount, rightCount, leftCount, intersectionX,intersectionY
    
    if firstTime:#if first time at intersection, then add x/y cordinates of red
        if direction==1:#facing up
            intersectionX.append(currentX)
            intersectionY.append(currentY+blockSize)
        elif direction==2:#facing right
            intersectionX.append(currentX-blockSize)
            intersectionY.append(currentY)
        elif direction==3:#facing left
            intersectionX.append(currentX+blockSize)
            intersectionY.append(currentY)
        elif direction==4:#facing down
            intersectionX.append(currentX)
            intersectionY.append(currentY-blockSize)
    print("X-",intersectionX)
    print(" y-",intersectionY)
    #pygame.draw.rect(newscreen, (100,100,100), pygame.Rect(currentX-blockSize, currentY-blockSize, blockSize, blockSize))
    print("intersectionNum",intersectionNum)
    time.sleep(2)
    
    
    if newscreen.get_at((currentX, currentY - blockSize)) == white:#up
        addCount(isInt,1,firstTime)
        direction = 1
        moveUp(currentX, currentY, blockSize, blue)
        print("int-move-up")
    elif newscreen.get_at((currentX + blockSize, currentY)) == white:#right
        addCount(isInt,2,firstTime)
        direction = 2
        moveRight(currentX, currentY, blockSize, blue)
        print("int-move-right")
    elif newscreen.get_at((currentX - blockSize, currentY)) == white:#left
        addCount(isInt,3,firstTime)
        direction = 3
        moveLeft(currentX, currentY, blockSize, blue)
        print("int-move-left")
    elif newscreen.get_at((currentX, currentY + blockSize)) == white:#down
        addCount(isInt,4,firstTime)
        direction = 4
        moveDown(currentX, currentY, blockSize, blue)
        print("int-move-down")
    else:
        if checkSurround(red)==5:#more than 1 red path
            print("more than 1 red path")
            for z in range(0,len(intersectionX)):
                if intersectionX[z]==currentX-blockSize:#left
                    if intersectionY[z]==currentY:
                        addCount(isInt,3,firstTime)
                        direction=3
                        moveLeft(currentX,currentY,blockSize,blue)
                        print("int-to red-left")
                        break
                elif intersectionX[z]==currentX+blockSize:#right
                    if intersectionY[z]==currentY:
                        addCount(isInt,2,firstTime)
                        direction=2
                        moveRight(currentX,currentY,blockSize,blue)
                        print("int-to red-right")
                        break
                elif intersectionY[z]==currentY-blockSize:#up
                    if intersectionX[z]==currentX:
                        addCount(isInt,1,firstTime)
                        direction=1
                        moveUp(currentX,currentY,blockSize,blue)
                        print("int-to red-up")
                        break
                elif intersectionY[z]==currentY+blockSize:#down
                    if intersectionX[z]==currentX:
                        addCount(isInt,4,firstTime)
                        direction=4
                        moveDown(currentX,currentY,blockSize,blue)
                        print("int-to red-down")
                        break
            print("z-",z)
        else:#1 red path
            print("only 1 red path")
        '''
        print("intersection-length",len(intersectionX))
        print("intersectionX",intersectionX[intersectionNum-1])
        print("currentX",currentX)
        if intersectionX[intersectionNum-1]>currentX:#left
            addCount(isInt,3,firstTime)
            direction=3
            moveLeft(currentX,currentY,blockSize,blue)
            print("GHASJFHFJWHAUJSHFWAHSDJNWAJSKFJWHANMSDKWASIJD")
            '''
        '''
        if checkSurround(red) == 0:#no red
            if newscreen.get_at((currentX, currentY - blockSize)) == blue:#up
                addCount(isInt,1,firstTime)
                direction = 1
                moveUp(currentX, currentY, blockSize, blue)
            elif newscreen.get_at((currentX + blockSize, currentY)) == blue:#right
                addCount(isInt,2,firstTime)
                direction=2
                moveRight(currentX, currentY, blockSize, blue)
            elif newscreen.get_at((currentX - blockSize, currentY)) == blue:#left
                addCount(isInt,3,firstTime)
                direction=3
                moveLeft(currentX, currentY, blockSize, blue)
            elif newscreen.get_at((currentX, currentY + blockSize)) == blue:#down
                addCount(isInt,4,firstTime)
                direction = 4
                moveDown(currentX, currentY, blockSize, blue)
        elif checkSurround(red)==1:
            addCount(isInt,1,firstTime)
            direction = 1
            moveUp(currentX, currentY, blockSize, blue)
        elif checkSurround(red)==2:
            addCount(isInt,2,firstTime)
            direction = 2
            moveRight(currentX, currentY, blockSize, blue)
        elif checkSurround(red)==3:
            addCount(isInt,3,firstTime)
            direction = 3
            moveLeft(currentX, currentY, blockSize, blue)
        elif checkSurround(red)==4:
            addCount(isInt,4,firstTime)
            direction = 4
            moveDown(currentX, currentY, blockSize, blue)
            '''
        time.sleep(5)

# ------------- OUR ALGORITHM -------------

while 0 != currentY:
    pygame.event.get()
#for x in range(0,10):
    getCur = newscreen.get_at((currentX, currentY))
    isInt=isIntersection()
    if direction == 1:#up
        if isInt:
            if getCur == blue:#blue=intersection tile
                moveDown(currentX, currentY, blockSize, blue)
                moveUp(currentX, currentY, blockSize, green)#green=used path
                intersection(isInt,False)
            else:
                if newscreen.get_at((currentX, currentY + blockSize)) != blue:#down
                    pygame.draw.rect(newscreen, red, pygame.Rect(currentX, currentY+blockSize, blockSize, blockSize))#set red path into intersection
                pygame.draw.rect(newscreen, blue, pygame.Rect(currentX, currentY, blockSize, blockSize))#set current space to blue
                intersectionNum+=1
                intersection(isInt,True)
        else:
            if newscreen.get_at((currentX, currentY - blockSize)) == blue:
                moveUp(currentX, currentY, blockSize, white)
            else:
                up(white)
    elif direction == 2:#right
        if isInt:
            if getCur == blue:#blue=intersection tile
                moveLeft(currentX, currentY, blockSize, blue)
                moveRight(currentX, currentY, blockSize, green)#green=used path
                intersection(isInt,False)
            else:
                if newscreen.get_at((currentX-blockSize, currentY)) != blue:#left
                    pygame.draw.rect(newscreen, red, pygame.Rect(currentX-blockSize, currentY, blockSize, blockSize))#set red path into intersection
                pygame.draw.rect(newscreen, blue, pygame.Rect(currentX, currentY, blockSize, blockSize))#set current space to blue
                intersectionNum+=1
                intersection(isInt,True)
        else:
            if newscreen.get_at((currentX + blockSize, currentY)) == blue:
                moveRight(currentX, currentY, blockSize, white)
            else:
                right(white)
    elif direction == 3:#left
        if isInt:
            if getCur == blue:#blue=intersection tile
                moveRight(currentX, currentY, blockSize, blue)
                moveLeft(currentX, currentY, blockSize, green)#green=used path
                intersection(isInt,False)
            else:
                if newscreen.get_at((currentX+blockSize, currentY)) != blue:#right
                    pygame.draw.rect(newscreen, red, pygame.Rect(currentX+blockSize, currentY, blockSize, blockSize))#set red path into intersection
                pygame.draw.rect(newscreen, blue, pygame.Rect(currentX, currentY, blockSize, blockSize))#set current space to blue
                intersectionNum+=1
                intersection(isInt,True)
        else:
            if newscreen.get_at((currentX - blockSize, currentY)) == blue:
                moveLeft(currentX, currentY, blockSize, white)
            else:
                left(white)
    elif direction == 4:#down
        if isInt:
            if getCur == blue:#blue=intersection tile
                moveUp(currentX, currentY, blockSize, blue)
                moveDown(currentX, currentY, blockSize, green)#green=used path               
                intersection(isInt,False)
            else:
                if newscreen.get_at((currentX, currentY - blockSize)) != blue:#up
                    pygame.draw.rect(newscreen, red, pygame.Rect(currentX, currentY-blockSize, blockSize, blockSize))#set red path into intersection
                pygame.draw.rect(newscreen, blue, pygame.Rect(currentX, currentY, blockSize, blockSize))#set current space to blue
                intersectionNum+=1
                intersection(isInt,True)
        else:
            if newscreen.get_at((currentX, currentY + blockSize)) == blue:
                moveDown(currentX, currentY, blockSize, white)
            else:
                down(white)
    #-print("direction-main", direction)
