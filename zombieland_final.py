import mcpi.minecraft as minecraft
import mcpi.block as block
import time
import random
from datetime import datetime

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
        ZOMBIE_SMELL_RANGE = 5      # how many blocks can the zombie sense you
        ZOMBIE_BITE_RANGE = 1       # how many blocks distance for zombie to bite
        pos = mc.player.getTilePos()
        diffx = pos.x - self.x
        diffz = pos.z - self.z
        if abs(diffx) <= ZOMBIE_BITE_RANGE and abs(diffz) <= ZOMBIE_BITE_RANGE:     # bite if close
            self.bite()
        if abs(diffx) < ZOMBIE_SMELL_RANGE and abs(diffz) < ZOMBIE_SMELL_RANGE:     # move towards if zombie in smell distance
            self.chasePlayer()
        else:
            self.moveRandom()

    def moveRandom(self):
        mc.setBlock(self.x, self.y, self.z, block.AIR.id)
        mc.setBlock(self.x, self.y+1, self.z, block.AIR.id)
        new_x = self.x+random.randint(-1,1)
        if new_x >= X1 and new_x <= X2:                 #zsa\    check if x within the arena range
            self.x = new_x
        new_z = self.z+random.randint(-1,1)
        if new_z >= Z1 and new_z <= Z2:                 # check if z within the arena range
            self.z = new_z
        mc.setBlock(self.x, self.y, self.z, block.WOOL.id, self.colour)
        mc.setBlock(self.x, self.y+1, self.z, block.WOOL.id, self.colour)

    # zombie bites the player and decreases the number of lives remaining
    def bite(self):
        global remainingLives
        remainingLives = remainingLives - 1
        mc.postToChat("You've got bitten. Remaining lives:"+str(remainingLives))

    # zombie is moving towards the player
    def chasePlayer(self):
        new_x = self.x
        new_z = self.z
        pos = mc.player.getTilePos()
        diffx = pos.x - self.x
        diffz = pos.z - self.z
        if diffx < 0:      # negative difference for x means zombie should move to a block with lower x to get closer
            new_x = self.x - 1
        elif diffx > 0:
            new_x = self.x + 1
        if diffz < 0:
            new_z = self.z - 1
        elif diffz > 0:
            new_z = self.z + 1
        self.walk(new_x,new_z)

    # relocate zombie to new location (x and z coordianates as arguments). Exceptions checked: 1) is the target location
    # already occupied by another zombie or a diamonds 2) are the new coordinates outside of the arena
    def walk(self,newx, newz):
        cube = mc.getBlockWithData(newx, Y, newz)
        if cube.id == block.WOOL.id or cube.id == block.DIAMOND_BLOCK.id:
            return
        mc.setBlock(self.x, self.y, self.z, block.AIR.id)                   # remove the original blocks
        mc.setBlock(self.x, self.y+1, self.z, block.AIR.id)
        if newx >= X1 and newx <= X2:
            self.x = newx
        if newz >= Z1 and newz <= Z2:
            self.z = newz
        mc.setBlock(self.x, self.y, self.z, block.WOOL.id, self.colour)     # create the new blocks
        mc.setBlock(self.x, self.y+1, self.z, block.WOOL.id, self.colour)

### end of Zombie class definition

def checkPlayerlocation():
    ## prevent the player from flying or digging under
    pos = mc.player.getTilePos()
    if pos.y != Y:
        mc.player.setTilePos(pos.x,Y,pos.z)

def checkDimonds():
    # This function checks if the player collected the diamond. It also checks if the new number of diamonds allows
    # player to get an extra life. Finally the diamond is moved to a new random location.
    global diamondsInBackpack, remainingLives
    events = mc.events.pollBlockHits()
    for e in events:                                                # check all new block hit events since
        blockHit = mc.getBlockWithData(e.pos.x, e.pos.y, e.pos.z)
        if blockHit.id == block.DIAMOND_BLOCK.id:
            diamondsInBackpack = diamondsInBackpack + 1
            if diamondsInBackpack == DIAMONDS_PER_LIFE:
                remainingLives = remainingLives + 1
                diamondsInBackpack = 0
                mc.postToChat("You earned an addition live. Remaining:"+str(remainingLives))
            else:
                mc.postToChat("You have "+str(diamondsInBackpack)+" diamonds")
            mc.setBlock(e.pos.x, e.pos.y, e.pos.z, block.AIR.id)        # remove the collected diamond
            mc.setBlock(random.randint(X1,X2),Y+1,random.randint(Z1,Z2),block.DIAMOND_BLOCK.id) # create a new diamond

DIAMONDS_PER_LIFE = 5
diamondsInBackpack = 0
remainingLives = 3
X1 = -50  # coordinates of the first corner
Y = 74
Z1 = -390
SIZE = 20
X2 = X1 + SIZE  # coordinates of the opposite corner depends on the SIZE constant
Z2 = Z1 + SIZE

mc.setBlocks(X1, Y, Z1, X2, Y + 3, Z2, block.AIR.id)  # clean up the area
mc.setBlocks(X1, Y - 1, Z1, X2, Y - 1, Z2, block.BEDROCK.id)  # build the ground
mc.player.setTilePos(X1, Y, Z1)  # teleport the player to the corner of the arena

zombies = []        # create an empty list that will hold references to Zombie objects
NUMBER_OF_ZOMBIES = 2
NEW_ZOMBIE_FREQUENCY = 5
iteration = 0
startTime = datetime.now()

for e in range(NUMBER_OF_ZOMBIES):
    zombie = Zombie(random.randint(X1,X2),74,random.randint(Z1,Z2))     # create a Zombie in random location
    zombies.append(zombie)                                              # add zombie to the list
mc.setBlock(random.randint(X1,X2),Y+1,random.randint(Z1,Z2),block.DIAMOND_BLOCK.id)     # create the first diamond
while True:
    time.sleep(0.5)
    checkPlayerlocation()
    checkDimonds()
    iteration = iteration + 1
    if iteration % NEW_ZOMBIE_FREQUENCY == 0:    # check remainder of division to span new zombie not in every iteration
        zombie = Zombie(random.randint(X1,X2),74,random.randint(Z1,Z2))     # create a Zombie in random location
        zombies.append(zombie)                                              # add zombie to the list
    for zombie in zombies:
        zombie.move()
    if remainingLives < 1:
        mc.postToChat("You're dead!")
        duration = datetime.now() - startTime
        mc.postToChat("You managed to stay alive for: "+ str(duration.total_seconds())+" seconds")
        exit()

