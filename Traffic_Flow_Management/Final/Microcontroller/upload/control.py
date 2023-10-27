from machine import Pin
from utime import sleep

red1 = Pin(0, Pin.OUT)
yellow1 = Pin(2, Pin.OUT)
green1 = Pin(1, Pin.OUT)

step=Pin(28, Pin.IN, Pin.PULL_UP)
Pin(27, Pin.OUT).on()

display_list = [27,26,22,21,20,19,18]
dotPin=17

display_obj = []

for seg in display_list:
    display_obj.append(Pin(seg, Pin.OUT))
dot_obj=Pin(dotPin, Pin.OUT)

arrSeg = [[1,1,1,1,1,1,0],
          [0,1,1,0,0,0,0],
          [1,1,0,1,1,0,1],
          [1,1,1,1,0,0,1],
          [0,1,1,0,0,1,1],
          [1,0,1,1,0,1,1],
          [1,0,1,1,1,1,1],
          [1,1,1,0,0,0,0],
          [1,1,1,1,1,1,1],
          [1,1,1,1,0,1,1]]

def SegDisplay(toDisplay):
    numDisplay = int(toDisplay.replace(".", ""))
    for a in range(7):
        display_obj[a].value(arrSeg[numDisplay][a])
    if toDisplay.count(".") == 1:
        dot_obj.value(1)
    else:
        dot_obj.value(0)

led_config = [
    [[0,2,1],[1,0,0],[0,1,0],[0,0,1]],
    [[5,4,3],[1,0,0],[0,1,0],[0,0,1]],
    [[8,7,6],[1,0,0],[0,1,0],[0,0,1]],
]

def updateZone(z, c):
    z-=1
    leds= []

    for pin_no in led_config[z][0]:
        leds.append(Pin(pin_no, Pin.OUT))

    for n in range(3):
        leds[n].value(led_config[z][c][n])

updateZone(1,3)
updateZone(2,1)
updateZone(3,1)
SegDisplay("4")