import matplotlib.pyplot as plot
from functools import lru_cache
import time

# fib.py
@lru_cache
def fib(n: int) -> int:
    startTime = time.time()
    if n == 0 or n == 1:
        return n
    print("Finished in ", time.time() - startTime, "s: f(0) -> 0")
    print("Finished in ", time.time() - startTime, "s: f(1) -> 1")
    lastNum = 0
    currNum = 0
    nextNum = 1
    y = [0, 0]
    for i in range(n - 1):
        currNum = nextNum
        nextNum = currNum + lastNum
        lastNum = currNum
        dur = time.time() - startTime
        y.append(dur)
        print(f"Finished in {dur} s: f({i + 2}) -> {nextNum}")
    x = list(range(0, 101))
    plot.plot(x, y)
    plot.show()
    return nextNum

if __name__ == "__main__":
    fib(100)
