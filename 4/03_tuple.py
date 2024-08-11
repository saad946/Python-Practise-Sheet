a = (1, 2, 5, 6)
print(type(a)) 
no = a.count(5)
print(f'The number 5 appears {no} times in the tuple.')

i = a.index(5)
print(f'The index of the first occurrence of 5 is {i}.')

b = (1, False, 5, 6, 'hello')
print((b))

tuple_a = (1, 2, 3)
tuple_b = (4, 5, 6)
concatenated_tuple = tuple_a + tuple_b
print(concatenated_tuple)

repeated_tuple = concatenated_tuple * 3
print(repeated_tuple)
print(len(repeated_tuple))

