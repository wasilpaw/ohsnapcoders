import mcpi.minecraft as minecraft
import mcpi.block as block
import time
import random

X = 131
Y = 80
Z = 172
RANGE = 10
treasure_x = None
treasure_y = None
treasure_z = None
score = 0
TIMEOUT = 10
timer = TIMEOUT
trace = []
def placeTreasure():
    global treasure_x, treasure_y, treasure_z
    treasure_x = random.randint(X,X+RANGE)
    treasure_y = random.randint(Y,Y+RANGE)
    treasure_z = random.randint(Z,Z+RANGE)
    mc.setBlock(treasure_x, treasure_y, treasure_z, block.DIAMOND_BLOCK.id)

def checkHit():
    global treasure_x, score
    events = mc.events.pollBlockHits()
    for e in events:
        pos = e.pos
        if pos.x == treasure_x and pos.y == treasure_y and pos.z == treasure_z:
            mc.postToChat("HIT!")
            score = score + 10
            mc.setBlock(treasure_x, treasure_y, treasure_z, block.AIR.id)
            treasure_x = None

def homeingBeacon():
    global timer
    if treasure_x != None:
        timer = timer - 1
        if timer == 0:
            timer = TIMEOUT
            pos = mc.player.getTilePos()
            diffx = abs(pos.x - treasure_x)
            diffy = abs(pos.y - treasure_y)
            diffz = abs(pos.z - treasure_z)
            mc.postToChat("score:" + str(score) + "x:" + str(diffx) + "y:" + str(diffy) + "z:" + str(diffz))

def goldenTrace ():
    global score
    if treasure_x == None:
        while len(trace) > 0:
            coordinate = trace.pop()
            mc.setBlock(coordinate[0], coordinate[1], coordinate[2], block.AIR.id)
    pos = mc.player.getTilePos()
    b = mc.getBlock(pos.x,pos.y-1,pos.z)
    if b!= block.GOLD_BLOCK.id:
        mc.setBlock(pos.x, pos.y-1,pos.z, block.GOLD_BLOCK.id)
        coordinate = [pos.x, pos.y-1, pos.z]
        trace.append(coordinate)
        score = score - 1
                        
mc = minecraft.Minecraft.create()
mc.setBlocks(X-10, Y, Z-10, X+RANGE+10, Y+RANGE+10, Z+RANGE+10, block.AIR.id)
while True:
    time.sleep(0.1)
    if treasure_x == None:
        placeTreasure()
    checkHit()
    homeingBeacon()
    goldenTrace()

