import mcpi.minecraft as minecraft
import mcpi.block as block
import random
import time

mc = minecraft.Minecraft.create()

X = 244 # coordinates for the block board corner
Y = 63
Z = 177
DISABLED = 0        # id of the wool colour used for standard blocks
ENABLED = 10        # id of the wool colour used for the illuminated block

board_row = 0       # the first coordinate of the illuminated block
board_column = 0    # the second  coordinate of the illuminated block

board = [[DISABLED,DISABLED,DISABLED],
         [DISABLED,DISABLED,DISABLED],
         [DISABLED,DISABLED,DISABLED],
         ]

Score = 0.0

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
    # things to add in this function -
    #       use random.randint() and time.sleep() functions to pause the game for a random time
    pass

def IlluminateBlock():
    # things to add in this function -
    #       randomly choose the row and column of the board and set the new colour, then display the board
    global board_column, board_row
    # add more code here
    return

def DetectPlayersHit():
    # things to add in this function -
    #       detect time taken to click on block using time.time() and printout to the player
    #       update the illuminated block back to the neutral colour and display updated board
    #       return the time taken to click on the block
    while True:
        events = mc.events.pollBlockHits()
        for e in events:
            blockHit = mc.getBlockWithData(e.pos.x, e.pos.y, e.pos.z)
            # if blockHit.data ==
    return # you should return exact time here

def DisplayFinalScore():
    # things to add in this function -
    #       - display the final score
    pass

mc = minecraft.Minecraft.create()
DisplayBoard()
mc.player.setTilePos(X+2, Y-1, Z-2)         #teleport the player in front of the board
for i in range(0,10):
    RandomSleep()
    IlluminateBlock()
    HitTime = DetectPlayersHit()
    Score = Score + HitTime  # increase the score by time taken in the round
DisplayFinalScore()


