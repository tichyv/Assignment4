import neopixel
import machine
import time

h = 8
np = neopixel.NeoPixel(machine.Pin(4), h) 
m = 0

def fade(np):
    n = np.n
    
    # fade in/out
    for i in range(0, 4 * 256, 8):
        for j in range(n):
            if (i // 256) % 2 == 0:
                val = i & 0xff
            else:
                val = 255 - (i & 0xff)
            np[j] = (val, 0, 0)
        np.write()



while True:
  m += 1
  fade(np)
  
 
