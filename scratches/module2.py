from gpiozero import OutputDevice, InputDevice
from time import sleep

"""Reads a DHT sensor"""

class DHT():
    def __init__(self):
        self._pin = 4
        self.returnvalue = ""
        self.counter = 0
    def input(self):
        gpio = OutputDevice(self._pin)
        gpio.off()
        sleep(0.02)
        gpio.close()
        gpio = InputDevice(self._pin)
        while gpio.value == 1:
            pass
        while gpio.value == 0:
            pass
        
        while len(self.returnvalue) != 40:
            if gpio.value == 0:
                self.returnvalue += "0"
            if gpio.value == 1:
                self.returnvalue += "1"
            self.counter = self.counter + 1
        print(self.returnvalue)
        test = int(self.returnvalue[0:8], 2)
        test2 = int(self.returnvalue[8:16], 2)
        test = float(f'{test}.{test2}')
        print(test)
DHT = DHT() 
DHT.input()