# map function to square each element in the list 'l' and store the result in a new list '
from functools import reduce
l =  [1, 2, 3, 4, 5]

square = lambda x: x * x

sqlist = map(square, l)

print(list(sqlist))


# filter example: filter out even numbers from the list 'l'

def even_filter(x):
    if x % 2 == 0:
        return True
    return False

onlyevens = filter(even_filter, l)
print(list(onlyevens))


# reduce function: calculate the sum of all elements in the list 'l'

from functools import reduce

def add_numbers(x, y):
    return x + y

print(reduce(add_numbers, l))