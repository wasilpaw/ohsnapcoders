import mcpi.minecraft as minecraft
import mcpi.block as block
import datetime
import time
from playsound import playsound

X = -130         #coordinates of the clock
Y = 63
Z = 262
AHour = 0       # alarm hour
AMinute = 0     # alarm minute
CHour = 0       # current time - hour
CMinute = 0     # current time - minute
CSecond = 0     # current time - second

def readCurrentTime():
    global CHour, CMinute, CSecond
    date = datetime.datetime.now()      # read the current system date and time
    CHour = date.hour
    CMinute = date.minute
    CSecond = date.second
    print(str(CHour), " ", str(CMinute), " ", str(CSecond))

def displayClock():
    mc.setBlocks(X, Y, Z, X+2, Y+60, Z, block.AIR.id)           # clean the clock area from previous display
    mc.setBlocks(X, Y, Z, X, Y+CHour, Z, block.GOLD_BLOCK.id)   # build the tower representing hours
    mc.setBlocks(X+1, Y, Z, X+1, Y+CMinute, Z, block.GLOWING_OBSIDIAN.id)    # minutes
    mc.setBlocks(X+2, Y, Z, X+2, Y+CSecond, Z, block.SANDSTONE.id)  # seconds

def setAlarm():
    global AHour, AMinute
    AHour = int(input("Please write the alarms' hour and press Enter "))
    AMinute = int(input("Please write the alarm's minute and press Enter "))

def fireAlarm():
    print("Alarm!!")
    playsound('reverse-cymbal-sound.mp3')       # play the sound (must be in the same folder as the .py file

mc = minecraft.Minecraft.create()
setAlarm()
while (True):
    readCurrentTime()
    displayClock()
    if (AHour == CHour) and (AMinute == CMinute): # check if alarm is set for the current time
        fireAlarm()
        break           # exit the loop and the program after alarm fired
    time.sleep(1)


'''
Challenge 1 - add a function that would do something visually striking with the clock once the alarm fires
Challenge 2 - add seconds in the alarm setups
Challenge 3 - validate input
'''
