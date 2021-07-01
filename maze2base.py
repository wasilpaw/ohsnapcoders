import mcpi.minecraft as minecraft
import mcpi.block as block
import time
from datetime import datetime

ORIGIN_X = 246      #coordinates of the first corner of the maze
ORIGIN_Y = 63
ORIGIN_Z = 194
player_X = ORIGIN_X #default player position will be the first block of the maze
player_Z = ORIGIN_Z
TREASURE = block.DIAMOND_BLOCK.id
FLOOR = block.BEDROCK.id
isTreasureFound = False

def buildMaze():
    global player_X, player_Z
    z = ORIGIN_Z
    file = open("maze1.csv","r")
    for line in file.readlines():   #read the content of the file and iterate on lines
        data = line.split(",")      #split the line into individual values
        x = ORIGIN_X                
        for cell in data:           #iterate on each value in the line
            if cell == "0":
                b = block.AIR.id
            elif cell == "X":
                b = TREASURE
            elif cell == "P":
                b = block.AIR.id
                player_X = x
                player_Z = z
            else:
                b = block.GOLD_BLOCK.id
            mc.setBlock(x,ORIGIN_Y,z,b)
            mc.setBlock(x,ORIGIN_Y+1,z,b)
            mc.setBlock(x,ORIGIN_Y-1,z,FLOOR)
            x = x + 1
        z = z + 1

def isPlayerInMaze():
    return False

def detectTreasureHit():
    pass

def calculateResult():
    return 0

def saveScore(timeInMaze):
    pass

mc = minecraft.Minecraft.create()
buildMaze()
mc.player.setTilePos(player_X,ORIGIN_Y,player_Z)    #teleport player to the coordinates indicated as "P" in the csv file
startTime = datetime.now()                          #record the time to be used for final score calculation   
while isPlayerInMaze() == True:                     #as long as player inside maze, keep checking if treasure was found
    detectTreasureHit()
if isTreasureFound == True:                         #once player outside of maze calculate the time if treasure found
    timeInMaze = calculateResult()
    saveScore(timeInMaze) 
else:
    mc.postToChat("You did not find the treasure")
    
