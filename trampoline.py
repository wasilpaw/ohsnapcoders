from mcpi import minecraft, block
import time

TRAMP_X = 110       # coordinates of the trampoline
TRAMP_Y = 66
TRAMP_Z = 325
TRAMP_WIDTH = 6
TRAMP_HEIGHT = 15 #how high the player will bounce
 
mc = minecraft.Minecraft.create()

#build the trampoline
mc.setBlocks(TRAMP_X, TRAMP_Y, TRAMP_Z, TRAMP_X + TRAMP_WIDTH, TRAMP_Y, TRAMP_Z + TRAMP_WIDTH, block.WOOD)

def bounce():
    pos = mc.player.getPos()
    for i in range(1,TRAMP_HEIGHT): #lift the player incrementally
        time.sleep(0.01*i) #the time slept will increase with each iteration
        mc.player.setPos(pos.x,pos.y+i,pos.z)
 
while True:
    pos = mc.player.getPos()
    block_beneath = mc.getBlock(pos.x, pos.y-1, pos.z)
    if block_beneath==block.WOOD.id: #only bounce if trampoline material underneath
        bounce()
