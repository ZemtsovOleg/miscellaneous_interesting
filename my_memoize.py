from functools import wraps


def memoize(func):
    cache = {}

    @wraps(func)
    def wrapper(a):
        return cache.get(a) or cache.setdefault(a, func(a))
    return wrapper

# # ----------------------------------------------


# def memoize(func):
#     cache = {}

#     def wrapper(a):
#         if a not in cache:
#             cache[a] = func(a)
#         return cache[a]
#     wrapper.__name__ = func.__name__
#     wrapper.__doc__ = func.__doc__
#     return wrapper

# # ----------------------------------------------


# cache = {0: 0, 1: 1}
# def fibonacci_cache(n):
#     if n in cache:
#         return cache[n]
#     cache[n] = fibonacci_of(n - 1) + fibonacci_of(n - 2)
#     return cache[n]

# print(fibonacci_cache(20))


@memoize
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

# fibonacci = memoize(fibonacci)

print(fibonacci(10))
assert fibonacci(50) == 12586269025
# assert fibonacci(60) == 1548008755920
# assert fibonacci(70) == 190392490709135
# assert fibonacci(80) == 23416728348467685
# assert fibonacci(90) == 2880067194370816120
# assert fibonacci(100) == 354224848179261915075
assert fibonacci.__name__ == 'fibonacci'
