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
    pass

def displayClock():
    pass

def setAlarm():
    pass

def fireAlarm():
    pass

mc = minecraft.Minecraft.create()
setAlarm()
while (True):
    readCurrentTime()
    displayClock()
    if (AHour == CHour) and (AMinute == CMinute): # check if alarm is set for the current time
        fireAlarm()
        break           # exit the loop and the program after alarm fired
    time.sleep(1)
