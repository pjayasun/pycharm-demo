from calc import *


def division(a, b):
    return a / b


def smart_division(func):
    def inner(a, b):
        if a < b:
            a, b = b, a
        return func(a, b)
    return inner


division1 = smart_division(division)
print(division1(2, 4))


print(add(65, 65))