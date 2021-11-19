import mcpi.minecraft as minecraft
import mcpi.block as block
import time
import random

X = 165     # starting point coordinates
Y = 66
Z = 302
RANGE = 10  # size of the arena
treasure_x = None   # coordinates of the diamond
treasure_y = None
treasure_z = None

mc = minecraft.Minecraft.create()

while True:
    pos = mc.player.getTilePos()
    b = mc.getBlock(pos.x, pos.y-1, pos.z)
    c = random.randint(0,15)
    if b == block.AIR.id or b == block.WATER_STATIONARY.id or b == block.WATER_FLOWING.id:
        mc.setBlock(pos.x, pos.y-1, pos.z, block.WOOL.id, c)
        coordinate = [pos.x, pos.y-1, pos.z]
        bridge.append(coordinate)
    elif b!= block.WOOL.id and len(bridge) > 0 :
        coordinate = bridge.pop()
        mc.setBlock(coordinate[0], coordinate[1], coordinate[2], block.AIR.id)
        time.sleep(0.25)
