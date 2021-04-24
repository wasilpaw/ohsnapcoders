import mcpi.minecraft as minecraft
import mcpi.block as block
import time

DEPTH = 10 # how deep will the metal detactor check
WIDTH = 3 # how far to each of the side to check

mc = minecraft.Minecraft.create()

while True:
    pos = mc.player.getTilePos()
    for y in range(pos.y-DEPTH,pos.y):
        for x in range(pos.x-WIDTH,pos.x+WIDTH):
            b = mc.getBlock(x,y,pos.z)
            if b==block.GOLD_BLOCK.id:
                mc.postToChat("Golden Block detected at x=" + str(x)+" y="+str(y)+" z="+str(pos.z))
            
            
