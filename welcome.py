import mcpi.minecraft as minecraft
import mcpi.block as block
import time

X = 246                             # coordinates of the mat
Y = 62
Z = 174

mc = minecraft.Minecraft.create()   # connect to Minecraft server
mc.setBlock(X,Y,Z,block.WOOD.id)    # create the welcome mat

while True:
    time.sleep(1)                   # wait for 1 second so that user is not spammed with thousands of messages
    pos = mc.player.getTilePos()    # read the current coordinates of the player
    if pos.x == X and pos.z == Z:   # only display message when players position is exactly same as the mat
        mc.postToChat("Welcome!")
