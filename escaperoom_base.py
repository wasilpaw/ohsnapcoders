from mcpi import minecraft, block
import time

X=266      # coordinates of the escape room corner
Y=69
Z=10
WIDTH = 10 #size of the escape room
ORANGE = 1 #id of of a wool colour
YELLOW = 4 #id of of a wool colour
BLUE = 11  #id of of a wool colour

mc = minecraft.Minecraft.create()

# this function builds the escape room
def buildEscapeRoom():
    mc.setBlocks(X,Y-30,Z,X+WIDTH,Y+5, Z+WIDTH,block.BEDROCK)       # walls, lower floor and roof
    mc.setBlocks(X+1,Y-29,Z+1,X+WIDTH-1,Y+4, Z+WIDTH-1,block.AIR)   # to carve out inner space
    mc.setBlocks(X+1,Y-29,Z+1,X+WIDTH-1,Y-28, Z+WIDTH-1,block.LAVA) # lava pit
    mc.setBlocks(X,Y,Z,X+WIDTH,Y,Z+WIDTH,block.WOOD_PLANKS)         # floor 
    mc.setBlock(X+1,Y+1,Z+1,block.TORCH)                            # 1st torch
    mc.setBlock(X+1,Y+1,Z+WIDTH-1,block.TORCH)                      # 2nd torch
    mc.setBlock(X+WIDTH-1,Y+1,Z+1,block.TORCH)                      # 3rd torch
    mc.setBlock(X+WIDTH-1,Y+1,Z+WIDTH-1,block.TORCH)                # 4th torch
    mc.setBlock(X+WIDTH/2-1,Y+2,Z+WIDTH/2,block.WOOL.id,ORANGE)     # 1st answer block
    mc.setBlock(X+WIDTH/2,Y+2,Z+WIDTH/2,block.WOOL.id,YELLOW)       # 2nd answer block
    mc.setBlock(X+WIDTH/2+1,Y+2,Z+WIDTH/2,block.WOOL.id,BLUE)       # 3rd answer block
    mc.player.setPos(X+WIDTH/2,Y+1,Z+3)                             # teleport player inside the room    

# this function removes the floor and causes player to fall into the lava pit
def releaseFloor():
    mc.setBlocks(X,Y,Z,X+WIDTH,Y,Z+WIDTH,block.AIR)

# this function creates a whole in a wall allowing player to escape the room
def openDoor():
    mc.setBlocks(X+WIDTH/2-1,Y+1,Z,X+WIDTH/2+1,Y+2,Z,block.AIR)
    
buildEscapeRoom()

