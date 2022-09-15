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

#login window
login_layout = [ [sg.Text('Password'),sg.InputText(password_char="*")],
            [sg.Button('Login')],
            [sg.Text('',key='Status')],
            ]
login_window = sg.Window('Minecraft Admin Panel login', login_layout)

while True:
    event, values = login_window.read()
    if event == sg.WIN_CLOSED:
        exit(0)
    if event == 'Login':
        if "0hSn@p" == values[0]:
            login_window.close()
            break
        else:
            login_window['Status'].update("Wrong Password")

# the main window
sg.theme('DarkAmber')
layout = [  [sg.Text('Teleport the player to a new location')],   #each line is one line of the window
            [sg.Text('X'), sg.InputText()],     # values[0] would store the text from this input field
            [sg.Text('Y'), sg.InputText()],     #1
            [sg.Text('Z'), sg.InputText()],     #2
            [sg.Button('Teleport'), sg.Cancel()],   # name of the button is the same as event fired when button clicked
            [sg.Text('')],
            [sg.Text('Clear space')],
            [sg.Text('X1'), sg.InputText()],    #3
            [sg.Text('Y1'), sg.InputText()],    #4
            [sg.Text('Z1'), sg.InputText()],    #5
            [sg.Text('X2'), sg.InputText()],    #6
            [sg.Text('Y2'), sg.InputText()],    #7
            [sg.Text('Z2'), sg.InputText()],    #8
            [sg.Button('Clear')],
            [sg.Text('')],
            [sg.Text('Build from csv file')],
            [sg.Input(), sg.FileBrowse()],      #9
            [sg.Text('X'), sg.InputText()],     #10
            [sg.Text('Y'), sg.InputText()],     #11
            [sg.Text('Z'), sg.InputText()],     #12
            [sg.Button('Build')],
            ]


window = sg.Window('Minecraft Admin Panel', layout)
mc = minecraft.Minecraft.create()

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel':
        break
    if event == 'Teleport':
        pass
        #mc.player.setTilePos(int(values[0]),int(values[1]),int(values[2]))
    if event == 'Clear':
        pass
        #mc.setBlocks(int(values[3]),int(values[4]),int(values[5]),int(values[6]),int(values[7]),int(values[8]),block.AIR.id)
    if event == 'Build':
        pass
        #buildMaze(values[9],int(values[10]),int(values[11]),int(values[12]))

window.close()
