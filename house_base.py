import mcpi.minecraft as minecraft
import mcpi.block as block
mc = minecraft.Minecraft.create()

SIZE = 20 # size of the house
x=9
y=76
z=-246

mc.setBlocks(x-2,y,z-2,x+SIZE+50,y+SIZE+50,z+SIZE+50,block.AIR.id) # clean up the area

midx=x+SIZE/2 # mid point of the front wall horizontally
midy=y+SIZE/2 # mid point of the front wall vertically
 
mc.setBlocks(x,y,z,x+SIZE,y+SIZE,z+SIZE ,block.COBBLESTONE.id)          # main block
mc.setBlocks(x+1,y,z+1,x+SIZE-1,y+SIZE-1,z+SIZE-1,block.AIR.id)         # carve out the interior to leave walls
mc.setBlocks(midx-1,y,z, midx+1,y+5,z,block.AIR.id)                     # entrance
mc.setBlocks(x+3,y +SIZE-3,z, midx-3,midy+3,z,block.GLASS.id)           # window 1
mc.setBlocks(midx+3,y +SIZE-3,z, x + SIZE-3,midy+3,z,block.GLASS.id)    # window 2
mc.setBlocks(x,y+SIZE-1,z, x + SIZE,y+SIZE,z + SIZE,block.WOOD.id)      # roof


