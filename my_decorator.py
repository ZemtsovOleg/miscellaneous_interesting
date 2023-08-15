import functools
from functools import wraps


def decorator(arg):
    def outer(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            return result
        return wrapper
    return outer


@decorator(arg=)
def one(n):
    return n**2

# one = decorator()(one)


print(one(5))
print(one.__name__)


def tax_decorator(tax):
    def outer(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            print('kwargs: ', kwargs)
            print('args: ', args)
            print('__defaults__: ', func.__defaults__)
            for i in kwargs:
                kwargs[i] = kwargs.get(i) * tax
            lst = []
            for i in args:
                lst.append(i * tax)
            result = func(*lst, **kwargs)
            return result
        return wrapper
    return outer


@tax_decorator(1.30)
def salary_calculation(salary, allowance=500, premium=500):
    return salary + allowance + premium


print(salary_calculation(7000, premium=1000))
