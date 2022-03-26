import mcpi.minecraft as minecraft
import mcpi.block as block
import time
import random

mc = minecraft.Minecraft.create()

### begining of Zombie class definition
class Zombie:

    # the constructor
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        self.colour = 13  # zombie will be green
        mc.setBlock(self.x, self.y, self.z, block.WOOL.id, self.colour)  # build the bottom block of the zombie
        mc.setBlock(self.x, self.y + 1, self.z, block.WOOL.id, self.colour)  # build the upper block of the zombie

    def move(self):
        mc.setBlock(self.x, self.y, self.z, block.AIR.id)                   # remove the original blocks
        mc.setBlock(self.x, self.y+1, self.z, block.AIR.id)
        self.x = self.x + 1                                                 # save the new coordinate
        mc.setBlock(self.x, self.y, self.z, block.WOOL.id, self.colour)     # create the new blocks
        mc.setBlock(self.x, self.y+1, self.z, block.WOOL.id, self.colour)

    def moveRandom(self):
        mc.setBlock(self.x, self.y, self.z, block.AIR.id)
        mc.setBlock(self.x, self.y+1, self.z, block.AIR.id)
        new_x = self.x+random.randint(-1,1)
        if new_x >= X1 and new_x <= X2:                 # check if x within the arena range
            self.x = new_x
        new_z = self.z+random.randint(-1,1)
        if new_z >= Z1 and new_z <= Z2:                 # check if z within the arena range
            self.z = new_z
        mc.setBlock(self.x, self.y, self.z, block.WOOL.id, self.colour)
        mc.setBlock(self.x, self.y+1, self.z, block.WOOL.id, self.colour)

### end of Zombie class definition

X1 = -50  # coordinates of the first corner
Y = 74
Z1 = -390
SIZE = 20
X2 = X1 + SIZE  # coordinates of the opposite corner depends on the SIZE constant
Z2 = Z1 + SIZE

mc.setBlocks(X1, Y, Z1, X2, Y + 3, Z2, block.AIR.id)  # clean up the area
mc.setBlocks(X1, Y - 1, Z1, X2, Y - 1, Z2, block.BEDROCK.id)  # build the ground
mc.player.setTilePos(X1, Y + 10, Z1)  # teleport the player above the zombieland

first = Zombie(random.randint(X1,X2),74,random.randint(Z1,Z2))  # create the first Zombie object
second = Zombie(random.randint(X1,X2),74,random.randint(Z1,Z2))  # create the second Zombie object

while True:
    time.sleep(1)
    first.moveRandom()
    second.moveRandom()

