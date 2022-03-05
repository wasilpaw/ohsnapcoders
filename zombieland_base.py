import mcpi.minecraft as minecraft
import mcpi.block as block

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

first = Zombie(-47, 74, -388)  # create the first Zombie object
second = Zombie(-43, 74, -386)  # create the second Zombie object
