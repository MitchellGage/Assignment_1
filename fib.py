from functools import lru_cache

#fib.py
@lru_cache
#@timer
def fib(n: int) -> int:
  if n == 0 or n == 1:
    return n
  lastNum = 0
  currNum = 1
  nextNum = 1
  for i in range(n-1):
    currNum = nextNum
    nextNum = currNum + lastNum
    lastNum = currNum
  print(nextNum)
  return nextNum
  

if __name__ == "__main__":
  fib(100)
