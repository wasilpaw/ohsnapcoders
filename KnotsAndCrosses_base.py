import mcpi.minecraft as minecraft
import mcpi.block as block

mc = minecraft.Minecraft.create()

X = -157 # coordinates for the block board corner
Y = 64
Z = 272

board = [[0,1,2],
         [3,4,5],
         [6,7,8],
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

def DidPlayer1Win():
    return False

def Player1Move():
    pass

def DidPlayer2Win():
    return False

def Player2Move():
    pass

mc.player.setTilePos(X+2, Y-1, Z-1)
DisplayBoard()
for i in range(9):  # there's only 9 moves in the game
    Player1Move()
    DisplayBoard()
    if DidPlayer1Win()==True:
        mc.postToChat("Player1 won!")
        exit()
    Player2Move()
    DisplayBoard()
    if DidPlayer2Win()==True:
        mc.postToChat("Player2 won!")
        exit()
mc.postToChat("It's a draw!")


