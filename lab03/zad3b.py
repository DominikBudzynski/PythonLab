import timeit
from functools import lru_cache


def getFibonacci(n):
   if n < 3:
       return 1
   return getFibonacci(n-1) + getFibonacci(n-2)

getFibonacci(10)

@lru_cache(maxsize=128)
def getFibonacci_cached(n):
   if n < 3:
       return 1
   return getFibonacci(n-1) + getFibonacci(n-2)

getFibonacci_cached(10)


t1 = timeit.timeit("getFibonacci(10)",setup="from __main__ import getFibonacci", number=100000)
print(t1)

t2 = timeit.timeit("getFibonacci_cached(10)",setup="from __main__ import getFibonacci_cached", number=100000)
print(t2)

