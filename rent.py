import mcpi.minecraft as minecraft
import mcpi.block as block
import time

mc = minecraft.Minecraft.create()
X1 = 252            # coordinates of the first corner
Z1 = 165
SIZE = 10           # defines the size of the block
X2 = X1 + SIZE
Z2 = Z1 + SIZE
Y = 63
rent = 0

mc.setBlock(X1,Y,Z1,block.SANDSTONE.id) #build the first corner
mc.setBlock(X1,Y,Z2,block.SANDSTONE.id) #2
mc.setBlock(X2,Y,Z1,block.SANDSTONE.id) #3
mc.setBlock(X2,Y,Z2,block.SANDSTONE.id) #4

while True:
    time.sleep(1)                       # wait for 1 second so that user is not spammed with thousands of messages
    pos = mc.player.getTilePos()        # read the current coordinates of the player
    if pos.x  > X1 and pos.x < X2 and pos.z > Z1 and pos.z < Z2:
        rent = rent + 1     # only increase the rent if current coordinates within the boundaries
        mc.postToChat("You owe rent:"+str(rent))
