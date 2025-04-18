from gpiozero import OutputDevice, InputDevice
import time


class DHT11():
   BITS_LEN = 40
   #80 us timeout for connection
   connect_timeout = 50
   bit_timeout = 20

   def __init__(self, pin):
      self._pin = pin

   def read_data(self):
      firstbit = 0
      bit_count = 0
      timeout_count = 0
      bits = ""
      # -------------- send start --------------
      gpio = OutputDevice(self._pin)
      gpio.off()
      time.sleep(0.01)
      gpio.close()
      gpio = InputDevice(self._pin, pull_up=False)
      # -------------- wait response --------------
      while gpio.value == 0:
         timeout_count += 1
      if timeout_count > self.connect_timeout:
         raise TimeoutError("No response from sensor")
      timeout_count = 0
      while gpio.value == 1:
         timeout_count += 1
      if timeout_count > self.connect_timeout:
         raise TimeoutError("No response from sensor")
      print('connected')
      # -------------- read data --------------
      while bit_count < self.BITS_LEN:
         timeout_count = 0
         while gpio.value == 0:
            pass
         #start = time.time()
         while gpio.value == 1:
            timeout_count += 1
         if timeout_count > self.bit_timeout:
            bits += "1"
         else:
            bits += "0"
         #end = time.time()
         bit_count += 1
         #print(end-start)
      # -------------- verify --------------
      humidity_integer = int(bits[0:8], 2)
      humidity_decimal = int(bits[8:16], 2)
      temperature_integer = int(bits[16:24], 2)
      temperature_decimal = int(bits[24:32], 2)
      check_sum = int(bits[32:40], 2)

      _sum = humidity_integer + humidity_decimal + temperature_integer + temperature_decimal

      #if check_sum != _sum:
      #      humidity = None
      #      temperature = None
      #else:
      humidity = str(f'{humidity_integer}.{humidity_decimal}')
      temperature = str(f'{temperature_integer}.{temperature_decimal}')

      # -------------- return --------------
      return humidity, temperature, bits


if __name__ == '__main__':
   dht11 = DHT11(17)
   while True:
      humidity, temperature, bits = dht11.read_data()
      print(f"{bits}  temperature:{temperature}°C  humidity: {humidity}%")
      time.sleep(3)
