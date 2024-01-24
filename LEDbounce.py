import neopixel
import machine
import time

h = 8
np = neopixel.NeoPixel(machine.Pin(4), h) 
m = 0

def bounce(np):
    n = np.n
    
    # bounce
    for i in range(4 * n):
        for j in range(n):
            np[j] = (0, 0, 128)
        if (i // n) % 2 == 0:
            np[i % n] = (0, 0, 0)
        else:
            np[n - 1 - (i % n)] = (0, 0, 0)
        np.write()
        time.sleep_ms(60)


while True:
  m += 1
  bounce(np)
  
 

