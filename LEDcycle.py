import neopixel
import machine
import time

h = 8
np = neopixel.NeoPixel(machine.Pin(4), h) 
m = 0


def cycle(np):
    n = np.n

    # cycle
    for i in range(4 * n):
        for j in range(n):
            np[j] = (0, 0, 0)
        np[i % n] = (255, 255, 255)
        np.write()
        time.sleep_ms(25)

while True:
  m += 1
  cycle(np)
  
