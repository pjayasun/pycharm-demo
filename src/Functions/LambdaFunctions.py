from functools import reduce

"""
Parameterized function
"""
def square(x):
    return x*x

print(square(5))


"""
Lambda function
"""
square_v2=lambda x: x*x
print(square_v2(10))

f=lambda x, y: x+y
print(f'Sum of 2 numbers: {f(98, 99)}')


"""
Map, Filter, Reduce
"""

nums=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

### Filter: (function, iterable)

even=list(filter(lambda a: a%2==0 , nums))
print(even)

### Map:
doubles=list(map(lambda x: x*2, even))
print(doubles)

### Reduce
sum=reduce(lambda x, y: x+y, doubles)
print(f'Sum: {sum}')

