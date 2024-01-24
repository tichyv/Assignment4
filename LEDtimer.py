import neopixel
import machine
import time


h = 8
np = neopixel.NeoPixel(machine.Pin(4), h) 
m = 0
timer = 7.5

def cas(np, timer):
    n = np.n
    
    # timer 
    for i in range(h):
      np[i] = (92, 0, 128)
      time.sleep(timer)
      np.write()
    time.sleep(0.5)



while True:
  m += 1
  colorchase(np, timer)
  
 




