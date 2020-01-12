from functools import lru_cache
@lru_cache(maxsize=1000)
def fib(num):
    if num == 0:
        return 0
    if num == 1 or num == 2:
        return 1

    return fib(num - 2) + fib(num - 1)
