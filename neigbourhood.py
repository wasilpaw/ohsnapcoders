import mcpi.minecraft as minecraft
import mcpi.block as block

mc = minecraft.Minecraft.create()

SIZE = 20 # size of the house (width, height and depth)
x = -5
y = 64
z = 300
material = block.COBBLESTONE.id

mc.setBlocks(x - 25, y, z - 50, x + 100, y + 50, z + 50, block.AIR.id)

def house():
    midx = x + SIZE/2  # mid point of the front wall horizontally
    midy = y + SIZE/2  # mid point of the front wall vertically

    # Clean up the area
    mc.setBlocks(x, y, z, x + SIZE, y + SIZE, z + SIZE, block.AIR.id)

    # create the main block that later will make the walls
    mc.setBlocks(x,y,z, x + SIZE, y + SIZE, z + SIZE, material)
    # carve out the inner part of the building leaving just the walls and roof
    mc.setBlocks(x +1 ,y, z +1, x + SIZE-1, y + SIZE-1, z + SIZE-1, block.AIR.id)
    # entrance
    mc.setBlocks(midx -1, y, z, midx + 1, y + 3, z, block.AIR.id)
    # left window
    mc.setBlocks(x+3, y + SIZE -3,z, midx - 3, midy + 3, z, block.GLASS.id)
    # right window
    mc.setBlocks(midx+3, y + SIZE -3,z, x + SIZE - 3, midy + 3, z, block.GLASS.id)
    # roof
    mc.setBlocks(x, y + SIZE -1, z, x + SIZE,y + SIZE , z + SIZE, block.WOOD.id)
    # floor
    mc.setBlocks(x+1, y -1, z +1, x + SIZE - 2, y -1, z + SIZE -2, block.WOOL.id,14)

house()
x = x+SIZE+2
SIZE = 22
material = block.BEDROCK.id
house()
x = x+SIZE+2
SIZE = 14
material = block.WOOD.id
house()

# a garage
mc.setBlocks(-15,y,z, -10, y+3, z + 6, block.BRICK_BLOCK.id)
mc.setBlocks(-14,y,z, -11, y+2, z + 5, block.AIR.id)

#lawn
mc.setBlocks(-20, y-1, 270, 70, y-1, 299, block.GRASS.id)

# a road
mc.setBlocks(-20, y-1, 295, 70, y-1, 289, block.SANDSTONE.id)

# road markings
for n in range(-20,70,2):
    mc.setBlock(n, y-1, 292, block.WOOL.id)

# a driveway
mc.setBlocks(-11, y-1, 296, -14, y-1, 299, block.SANDSTONE.id)

#fences
mc.setBlocks(-10, y, 296, 3, y, 296, block.FENCE.id)
mc.setBlocks(3, y, 296, 3, y, 299, block.FENCE.id)
mc.setBlocks(7, y, 296, 7, y, 299, block.FENCE.id)
mc.setBlocks(7, y, 296, 20, y, 296, block.FENCE.id)

# a pond
mc.setBlocks(7, y-1, 284, 13, y-1, 287, block.WATER_STATIONARY.id)

# a tunnel
mc.setBlocks(15,y,z+2, 17, y+3, z + 5, block.BRICK_BLOCK.id)
mc.setBlocks(15,y,z+3, 17, y+2, z + 4, block.AIR.id)

