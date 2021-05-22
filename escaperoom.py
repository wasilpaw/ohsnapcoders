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

# this function compares the colour of the first wool block hit
# returns True if colours match and False otherwise 
def checkAnswer(colour):
    while True:
        time.sleep(1)
        events = mc.events.pollBlockHits()
        for e in events:                        #check every event from the list
            blockHit = mc.getBlockWithData(e.pos.x,e.pos.y,e.pos.z)
            if blockHit.id == block.WOOL.id:    #ignore hits on non wool blocks
                if blockHit.data == colour:     #compare the colour of the block to the argument 
                    mc.postToChat("Correct")
                    return True
                else:
                    mc.postToChat("Ooops")
                    return False
    
buildEscapeRoom()
mc.postToChat("Welcome to the Minecraft Escape Room")
mc.postToChat("Right click on the right block to answer the question")
time.sleep(4)
mc.postToChat("What's the capital city of USA?")
mc.postToChat("BLUE: New York")
mc.postToChat("YELLOW: Washington")
mc.postToChat("ORANGE: Hollywood")
if checkAnswer(YELLOW) == False:
    releaseFloor()
time.sleep(4)
mc.postToChat("What's the name of the current UK Prime Minister?") # in May 2021 :)
mc.postToChat("BLUE: Boris Jonhson")
mc.postToChat("YELLOW: Theresa May")
mc.postToChat("ORANGE: David Cameron")
if checkAnswer(BLUE) == False:
    releaseFloor()
else:
    openDoor()
    
