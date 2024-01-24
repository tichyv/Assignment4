import time
fib_val = 0

def fibonacci(n):       ##definition of Fibonacci sequency using recursive method
    if n == 0:
        return 0
    elif n ==1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
    
start = time.process_time()

fib_val = fibonacci(20)

print(f"The result is: {fib_val}. ")

print(time.process_time() - start)
