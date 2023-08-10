import datetime


def create_accumulator(count: int = 0) -> 'function':
    def inner(n: int) -> int:
        nonlocal count
        count += n
        return count
    return inner


summator_1 = create_accumulator()
print(summator_1(1))  # печатает 1
print(summator_1(5))  # печатает 6
print(summator_1(2))  # печатает 8

summator_2 = create_accumulator(10)
print(summator_2(3))  # печатает 3
print(summator_2(4))  # печатает 7

print(create_accumulator())
print(type(create_accumulator()))
print(type(summator_2(4)))

# -------------------------------------------


def multiply(a: int) -> 'function':
    def inner(b: int) -> int:
        return a * b
    return inner


f_2 = multiply(2)
print("Умножение 2 на 5 =", f_2(5))  # 10
print("Умножение 2 на 15 =", f_2(15))  # 30
f_3 = multiply(3)
print("Умножение 3 на 5 =", f_3(5))  # 15
print("Умножение 3 на 15 =", f_3(15))  # 45

# ---------------------------------------------


def create_dict() -> 'function':
    count = 0
    res = {}

    def inner(value) -> dict:
        nonlocal count
        nonlocal res
        count += 1
        res.update({count: value})
        return res

    return inner


f_1 = create_dict()
print(f_1('hello'))  # f_1 возвращает {1: 'hello'}
print(f_1(100))  # f_1 возвращает {1: 'hello', 2: 100}
print(f_1([1, 2, 3]))  # f_1 возвращает {1: 'hello', 2: 100, 3: [1, 2, 3]}

f_2 = create_dict()  # создаем новое замыкание в f_2
print(f_2('PoweR'))  # f_2 возвращает {1: 'PoweR'}

# ----------------------------------------------


def decorator_time(func):
    def wrapper(*args, **kwargs):
        start = datetime.datetime.now()
        result = func(*args, **kwargs)
        print(datetime.datetime.now() - start)
        return result
    wrapper.__name__ = func.__name__
    wrapper.__doc__ = func.__doc__
    return wrapper


@decorator_time
def func_one(a: int, b: int) -> int:
    '''функция возводит в степень'''
    return a**b


print(func_one(2, 3))

# help(func_one)
print(func_one.__name__)
# ------------------------------------------


def text_decor(func):
    def wrapper(*args, **kwargs):
        print('Hello')
        result = func(*args, **kwargs)
        print('Goodbye!')
        return result
    return wrapper


@text_decor
def simple_func():
    print('I just simple python func')


simple_func()

# -----------------------------------------------------


def repeater(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        result1 = func(*args, **kwargs)
        return result, result1
    return wrapper


@repeater
def multiply1(num1, num2):
    print(num1 * num2)


multiply1(2, 7)  # после этого распечатается две строки со значением 14
multiply1(5, 3)  # после этого распечатается две строки со значением 15

# ------------------------------------------------


def double_it(func):
    def wrapper(*args, **kwargs):
        temp = func(*args, **kwargs)
        return temp * 2
    return wrapper


@double_it
def multiply2(num1, num2):
    return num1 * num2


# произведение 9*4=36, но декоратор double_it удваивает это значение
res = multiply2(9, 4)
print(res)

# --------------------------------------------------------------


def add_args(func):
    def wrapper(*args, **kwargs):
        args = ('begin', *args, 'end')
        return func(*args, **kwargs)
    wrapper.__name__ = func.__name__
    wrapper.__doc__ = func.__doc__
    return wrapper

# ---------------------------------------------


# Напишите определение декоратора validate_args
def validate_args(func):
    def wrapper(*args, **kwargs):
        if len(args) < 2:
            return 'Not enough arguments'
        if len(args) > 2:
            return 'Too many arguments'
        if not isinstance(args[0], int) or not isinstance(args[-1], int):
            return 'Wrong types'
        return func(*args, **kwargs)
    wrapper.__name__ = func.__name__
    wrapper.__doc__ = func.__doc__
    return wrapper


# Код ниже не удаляйте, он нужен для проверки
@validate_args
def add_numbers(x, y):
    """Return sum of x and y"""
    return x + y


assert add_numbers(4, 5) == 9
assert add_numbers(4) == 'Not enough arguments'
assert add_numbers() == 'Not enough arguments'
assert add_numbers('hello') == 'Not enough arguments'
assert add_numbers(3, 5, 6) == 'Too many arguments'
assert add_numbers('a', 'b', 'c') == 'Too many arguments'
assert add_numbers(4.5, 5.1) == 'Wrong types'
assert add_numbers('hello', 4) == 'Wrong types'
assert add_numbers(9, 'hello') == 'Wrong types'
assert add_numbers([1, 3], {}) == 'Wrong types'
assert add_numbers.__name__ == 'add_numbers'
assert add_numbers.__doc__.strip() == 'Return sum of x and y'
print('Good')
