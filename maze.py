import mcpi.minecraft as minecraft
import mcpi.block as block

file = open("maze1.csv","r")
ORIGIN_X = 246      #coordinates of the first corner of the maze
ORIGIN_Y = 63
ORIGIN_Z = 194
z = ORIGIN_Z
mc = minecraft.Minecraft.create()

for line in file.readlines():   #read the content of the file and iterate on lines
    data = line.split(",")      #split the line into individual values
    x = ORIGIN_X                
    for cell in data:           #iterate on each value in the line
        if cell == "0":
            b = block.AIR.id
        elif cell == "X":
            b = block.DIAMOND_BLOCK.id
        else:
            b = block.GOLD_BLOCK.id
        mc.setBlock(x,ORIGIN_Y,z,b)
        mc.setBlock(x,ORIGIN_Y+1,z,b)
        mc.setBlock(x,ORIGIN_Y-1,z,block.GRASS.id)
        x = x + 1
    z = z + 1
        
