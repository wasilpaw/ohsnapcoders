import mcpi.minecraft as minecraft
import mcpi.block as block

mc = minecraft.Minecraft.create()

X = 157 # coordinates for the first block in the wall - board[0][0]
Y = 84
Z = 272
NEUTRAL = 8     # the neutral board block colour value - Gray
RED = 14        # player 1's colour
GREEN = 13      # player 2's colour

'''two dimensional list where values represent colour and correspond to a single block on the wall'''
board = [[NEUTRAL,NEUTRAL,NEUTRAL], # the bottom row
         [NEUTRAL,NEUTRAL,NEUTRAL], # the middle
         [NEUTRAL,NEUTRAL,NEUTRAL], # the top row
         ]


'''
This function that reads the colour of the block that is part of the wall
PARAMETERS: x,y,z - coordinates of the brick 
RETURNED VALUES: -1 if not in the range or block not WOOL. Otherwise, the colour code of the WOOL block
'''
def GetBrickColour(x,y,z):
    if z != Z or x<X or x>X+2 or y<Y or y>Y+2:
        print("Block not in range")
        return -1
    bloc = mc.getBlockWithData(x, y, z)
    if bloc.id != block.WOOL.id:
        print("Block is not of WOOL type")
        return -1
    else:
        #print(str(bloc.data))
        return bloc.data

'''
This function updates colour of a particular block on the board. 
PARAMETERS: x,y - coordinates of the brick 
RETURNED VALUES: none
'''
def SetBrickColour(x,y,colour):
    global board
    board[y-Y][x-X]=colour
    return

'''This function rebuilds the wall based on the values in board[][] '''
def DisplayBoard():
    mc.setBlock(X,Y,Z,block.WOOL.id, board[0][0])
    mc.setBlock(X+1,Y,Z,block.WOOL.id, board[0][1])
    mc.setBlock(X+2,Y,Z,block.WOOL.id, board[0][2])
    mc.setBlock(X,Y+1,Z,block.WOOL.id, board[1][0])
    mc.setBlock(X+1,Y+1,Z,block.WOOL.id, board[1][1])
    mc.setBlock(X+2,Y+1,Z,block.WOOL.id, board[1][2])
    mc.setBlock(X,Y+2,Z,block.WOOL.id, board[2][0])
    mc.setBlock(X+1,Y+2,Z,block.WOOL.id, board[2][1])
    mc.setBlock(X+2,Y+2,Z,block.WOOL.id, board[2][2])

def DidPlayerGreenWin():
    return False

def PlayerGreenMove():
    while True:
        events = mc.events.pollBlockHits()
        for e in events:
            #only allow to change the colour to the player's one if not already allocated
            if GetBrickColour(e.pos.x, e.pos.y, e.pos.z) == NEUTRAL:
                SetBrickColour(e.pos.x, e.pos.y,GREEN)
                return


def DidPlayerRedWin():
    return False

def PlayerRedMove():
    pass

mc.player.setTilePos(X+2, Y-1, Z-3)
DisplayBoard()
PlayerGreenMove()   #1
DisplayBoard()
PlayerRedMove()   #2
DisplayBoard()
PlayerGreenMove()   #3
DisplayBoard()
PlayerRedMove()  #4
DisplayBoard()
PlayerGreenMove()   #5
DisplayBoard()
if DidPlayerGreenWin()==True:
    mc.postToChat("Player1 won!")
    exit()
PlayerRedMove()   #6
DisplayBoard()
if DidPlayerRedWin()==True:
     mc.postToChat("Player2 won!")
     exit()
PlayerGreenMove()   #7
DisplayBoard()
if DidPlayerGreenWin()==True:
    mc.postToChat("Player1 won!")
    exit()
PlayerRedMove() #8
DisplayBoard()
if DidPlayerRedWin()==True:
     mc.postToChat("Player2 won!")
     exit()
PlayerGreenMove()   #9
DisplayBoard()
if DidPlayerGreenWin()==True:
    mc.postToChat("Player1 won!")
    exit()
mc.postToChat("It's a draw!")


