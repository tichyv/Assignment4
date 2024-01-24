import time

def testFloat():
    testVal = 0.0
    for i in range(1, 1000000):
        testVal += 1.0 / i
    return testVal

start = time.process_time()

val = testFloat()

print(f"The result is: {val}. ")
      
print(time.process_time() - start)