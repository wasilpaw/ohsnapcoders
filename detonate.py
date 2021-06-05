import mcpi.minecraft as minecraft
import mcpi.block as block

X = 212             #coordinates of the trigger
Y = 80
Z = -79
C_WIDTH = 30        # castle width
C_HEIGHT = 10       # castle height

def buildCastle():
    mc.setBlocks(X-C_WIDTH, Y-1, Z, X+C_WIDTH, Y+3*C_HEIGHT, Z+2*C_WIDTH, block.AIR.id)     # clean up the area
    mc.setBlocks(X-C_WIDTH, Y-1, Z, X+C_WIDTH, Y-1, Z+2*C_WIDTH, block.GRASS.id)            # a lawn
    mc.setBlocks(X-C_WIDTH/2, Y, Z+C_WIDTH/2, X+C_WIDTH/2, Y+C_HEIGHT, Z+3*C_WIDTH/2, block.COBBLESTONE.id) # walls
    mc.setBlocks(X-C_WIDTH/2+2, Y, Z+C_WIDTH/2+2, X+C_WIDTH/2-2, Y+C_HEIGHT, Z+3*C_WIDTH/2-2, block.AIR.id) # carve out inner space
    mc.setBlocks(X-1, Y, Z+C_WIDTH/2, X+2, Y+4, Z+C_WIDTH/2+1, block.WOOD_PLANKS.id)  #gate
    # use loops to remove every second block from the top layer
    for i in range(int(X-C_WIDTH/2+1),int(X+C_WIDTH/2),2):
        mc.setBlocks(i, Y+C_HEIGHT, Z+C_WIDTH/2, i, Y+C_HEIGHT, Z+3*C_WIDTH/2, block.AIR.id)
    for j in range(int(Z+C_WIDTH/2+1),int(Z+3*C_WIDTH/2),2):
        mc.setBlocks(X-C_WIDTH/2, Y+C_HEIGHT, j, X+C_WIDTH/2, Y+C_HEIGHT, j, block.AIR.id)

def setExplosives():
    mc.setBlock(X,Y +1,Z+C_WIDTH/2-1,block.TNT.id,1)    #explosives
    mc.setBlock(X,Y-1,Z+1,block.WOOL.id,10)             #trigger
    mc.postToChat("Explosives set. Stand on the purple triger to detonate.")

def detectDetonation():
    while True:
        pos = mc.player.getTilePos()
        if X==pos.x and Y==pos.y and Z==pos.z:  #players coordinates to be right above the trigger
            mc.setBlock(X,Y,Z+C_WIDTH/2-1,block.FIRE.id)
            mc.postToChat("Detonation started!")
            break
        
mc = minecraft.Minecraft.create()
buildCastle()
setExplosives()
detectDetonation()
