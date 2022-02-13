import mcpi.minecraft as minecraft
import mcpi.block as block
import requests

mc = minecraft.Minecraft.create()

SIZE = 20 # size of the house (width, height and depth)
x = 243
y = 63
z = 151
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

X1 = x
Z1 = z
X2 = X1 + SIZE
Z2 = Z1 + SIZE
hasEntered = False
while True:
    pos = mc.player.getTilePos()        # read the current coordinates of the player
    if pos.x > X1 and pos.x < X2 and pos.z > Z1 and pos.z < Z2:
        if hasEntered == False:
            response = requests.get('https://icanhazdadjoke.com/',
                params={'q': 'requests+language:python'},
                headers={'Accept': 'Accept: application/json'},)    # send the GET request
            json_response = response.json()                         # store the response in JSON like format
            mc.postToChat('Welcome home! Let me tell you a joke')
            joke_string = json_response['joke']                     # access the 'joke' element of the response
            joke_encode = joke_string.encode("ascii", "ignore")
            joke_decode = joke_encode.decode()
            mc.postToChat(joke_decode)
            hasEntered = True
    else:
        hasEntered = False

