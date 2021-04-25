import mcpi.minecraft as minecraft
import mcpi.block as block

DEPTH = 5 # how deep will the metal detactor check
WIDTH = 3 # how far to each of the side to check

metals = {}
metals[block.GOLD_BLOCK.id]="Gold"      # {block.GOLD_BLOCK.id: 'Gold'}    
metals[block.DIAMOND_ORE.id]="Diamond"  # {block.GOLD_BLOCK.id: 'Gold', block.DIAMOND_ORE.id: 'Diamond'}

mc = minecraft.Minecraft.create()

while True:
    pos = mc.player.getTilePos()
    for y in range(pos.y-DEPTH,pos.y):
        for x in range(pos.x-WIDTH,pos.x+WIDTH):
            b = mc.getBlock(x,y,pos.z)
            if b in metals.keys():
                mc.postToChat(metals[b]+" detected at x=" + str(x)+" y="+str(y)+" z="+str(pos.z))
                if x == pos.x:
                    mc.postToChat("!!!")
