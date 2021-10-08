import PySimpleGUI as sg
import mcpi.minecraft as minecraft
import mcpi.block as block

def buildMaze(filename="", origin_x = 0, origin_y = 0, origin_z = 0):
    z = origin_z
    file = open(filename,"r")
    for line in file.readlines():   #read the content of the file and iterate on lines
        data = line.split(",")      #split the line into individual values
        x = origin_x
        for cell in data:           #iterate on each value in the line
            if cell == "0":
                b = block.AIR.id
            elif cell == "X":
                b = block.DIAMOND_BLOCK.id
            elif cell == "P":
                b = block.AIR.id
            else:
                b = block.GOLD_BLOCK.id
            mc.setBlock(x,origin_y,z,b)
            mc.setBlock(x,origin_y+1,z,b)
            mc.setBlock(x,origin_y-1,z,block.WOOD_PLANKS.id)
            x = x + 1
        z = z + 1

mc = minecraft.Minecraft.create()
layout = [[]]
window = sg.Window('Minecraft Admin Panel', layout, margins=(200, 50))

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break

window.close()
