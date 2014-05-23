import time

def fib_tail(n, a = 1, b = 0):
    if n == 0:
        return a 
    else:
      return fib_tail(n-1, a+b, a)

n = input("n = ")
t = time.clock()

print fib_tail(n) 
print time.clock() - t
