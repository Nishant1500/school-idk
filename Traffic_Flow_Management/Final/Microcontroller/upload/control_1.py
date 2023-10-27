from machine import Pin
from utime import sleep
import tm1637
import usocket as socket

red1 = Pin(0, Pin.OUT)
yellow1 = Pin(2, Pin.OUT)
green1 = Pin(1, Pin.OUT)

step=Pin(28, Pin.IN, Pin.PULL_UP)

Display = tm1637.TM1637(clk=Pin(16), dio=Pin(17))

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

timer=10
z=1
new=True
while timer > 0:
    if(new == True):
        updateZone((z%4), 3)
        updateZone(1 if z==3 else (z+1)%4, 1)
        updateZone(3 if z==1 else (z+3)%4, 1)
        print("Zone" + str(z))
        new = False
    Display.number(timer)
    sleep(1)
    if timer==1:
        Display.number(0)
        sleep(1)
        Display.show("    ")
        sleep(0.5)
        Display.number(0)
        sleep(0.5)
        Display.show("    ")
        sleep(0.5)
        Display.number(0)
        sleep(0.5)
        Display.show("    ")
        sleep(0.5)
        Display.number(0)
        timer=10
        z=1 if z==3 else (z+1)%4
        new = True
    else:
        timer-=1

s = socket.socket()
addr = socket.getaddrinfo('www.micropython.org', 80)[0][-1]
s.connect(addr)