import mcpi.minecraft as minecraft
import mcpi.block as block

mc = minecraft.Minecraft.create()

X = 244 # coordinates for the block board corner
Y = 63
Z = 177

board = [[0,0,0],
         [0,0,0],
         [0,0,0],
         ]

def DisplayBoard():
    mc.setBlock(X,Y+2,Z,block.WOOL.id, board[0][0])
    mc.setBlock(X+1,Y+2,Z,block.WOOL.id, board[0][1])
    mc.setBlock(X+2,Y+2,Z,block.WOOL.id, board[0][2])
    mc.setBlock(X,Y+1,Z,block.WOOL.id, board[1][0])
    mc.setBlock(X+1,Y+1,Z,block.WOOL.id, board[1][1])
    mc.setBlock(X+2,Y+1,Z,block.WOOL.id, board[1][2])
    mc.setBlock(X,Y,Z,block.WOOL.id, board[2][0])
    mc.setBlock(X+1,Y,Z,block.WOOL.id, board[2][1])
    mc.setBlock(X+2,Y,Z,block.WOOL.id, board[2][2])

def RandomSleep():
    pass

def IlluminateBlock():
    pass

def DetectPlayersHit():
    pass

def DisplayScore():
    pass

def DisplayFinalScore():
    pass

DisplayBoard()
mc.player.setTilePos(X+2, Y-1, Z-1)

for i in range(0,10):
    RandomSleep()
    IlluminateBlock()
    DetectPlayersHit()
    DisplayScore()
    DisplayBoard()

DisplayFinalScore()


