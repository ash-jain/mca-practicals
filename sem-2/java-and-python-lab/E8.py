"""
* Student Name - Aakash Jain.
* Roll No. - 222010019.
* Subject - Java and Python Lab.
* Lab Experiment 8 - Design the program to demonstrate the use of Lambda expressions, Optional, Streams operations (Map, Reduce, Filter).
"""

from functools import reduce
from random import randrange

functions = {
    'add': lambda x, y: x + y,
    'subtract': lambda x, y: x - y,
    'multiply': lambda x, y: x * y,
    'divide': lambda x, y: x / y,
    'square': lambda x: x ** 2,
    'truncate': lambda x: int(x),
    'is_positive': lambda x: x > 0,
}

a, b = map(int, input('Enter two numbers separated by spaces:\t').split(' '))
print('\nAddition:', functions['add'](a, b))
print('Subtraction:', functions['subtract'](a, b))
print('Multiplication:', functions['multiply'](a, b))
print('Division:', functions['divide'](a, b))
print(f'Squares: {functions["square"](a)}, {functions["square"](b)}')
print()

array = [randrange(-25, 25) for _ in range(25)]
print('Array:', array)
print('Filtering negative numbers with Filter():', list(filter(functions['is_positive'], array)))
print('Squaring every number with Map():', list(map(functions['square'], array)))
print('Sum of the array using Reduce():', reduce(functions['add'], array, 1))
