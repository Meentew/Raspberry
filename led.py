from machine import Pin,Timer
from time import sleep
led = Pin(25,Pin.OUT)
ledG= Pin(16,Pin.OUT)
ledY= Pin(17,Pin.OUT)
ledR= Pin(18,Pin.OUT)
timer=Timer()
def blink(timer):
    led.toggle()
    ledR.toggle()
    ledY.toggle()
    ledG.toggle()
def ledRun():
    a=[Pin(17,Pin.OUT),Pin(16,Pin.OUT),Pin(18,Pin.OUT)]
    
    while True:
        for i in a:
            i.value(1)
            sleep(0.5)
            i.value(0)
            sleep(0.5)
            
ledRun()
#timer.init(freq=5,mode=Timer.PERIODIC,callback=blink)
#timer.init(freq=1,mode=Timer.PERIODIC,callback=ledRun)

