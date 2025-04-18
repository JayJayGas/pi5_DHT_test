from gpiozero import OutputDevice, InputDevice
from time import sleep

"""Checks if DHT sensor works"""

class DHT22():
    def __init__(self):
        self._pin = 4

    def input(self):
        gpio = OutputDevice(self._pin)
        gpio.off()
        sleep(0.02)
        gpio.close()
        gpio = InputDevice(self._pin)
        
        while gpio.value == 0:
            pass
        while gpio.value == 1:
            pass
        print("I work???")

DHT22 = DHT22() 
DHT22.input()