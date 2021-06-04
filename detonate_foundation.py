import mcpi.minecraft as minecraft
import mcpi.block as block

X =             #coordinates of the trigger
Y = 
Z = 
C_WIDTH = 30        # castle width
C_HEIGHT = 10       # castle height

def buildCastle():
    mc.setBlocks(X-C_WIDTH, Y-1, Z, X+C_WIDTH, Y+3*C_HEIGHT, Z+2*C_WIDTH, block.AIR.id)     # clean up the area
    mc.setBlocks(X-C_WIDTH, Y-1, Z, X+C_WIDTH, Y-1, Z+2*C_WIDTH, block.GRASS.id)            # a lawn
    mc.setBlocks(X-C_WIDTH/2, Y, Z+C_WIDTH/2, X+C_WIDTH/2, Y+C_HEIGHT, Z+3*C_WIDTH/2, block.COBBLESTONE.id) # walls
    mc.setBlocks(X-C_WIDTH/2+2, Y, Z+C_WIDTH/2+2, X+C_WIDTH/2-2, Y+C_HEIGHT, Z+3*C_WIDTH/2-2, block.AIR.id) # carve out inner space
    mc.setBlocks(X-1, Y, Z+C_WIDTH/2, X+2, Y+4, Z+C_WIDTH/2+1, block.WOOD_PLANKS.id)  #gate
        
mc = minecraft.Minecraft.create()
buildCastle()


