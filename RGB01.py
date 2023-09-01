from machine import Pin
import time

led1 = Pin(20, Pin.OUT)
led2 = Pin(21, Pin.OUT)
led3 = Pin(18, Pin.OUT)
bt = Pin(2, Pin.IN, Pin.PULL_UP)
bt2 = Pin(3, Pin.IN, Pin.PULL_UP)
bt3 = Pin(4, Pin.IN, Pin.PULL_UP)

while True:
    bts = bt.value()
    bts2 = bt2.value()
    bts3 = bt3.value()

    if bts == 0:
        print("R")
        led1.value(1)
        led2.value(0)
        led3.value(0)
    elif bts2 == 0:
        print("G")
        led1.value(0)
        led2.value(1)
        led3.value(0)
    elif bts3 == 0:
        print("B")
        led1.value(0)
        led2.value(0)
        led3.value(1)
    else:
        led1.value(0)
        led2.value(0)
        led3.value(0)

    time.sleep(0.1)  # Add a small delay to avoid rapid button presses