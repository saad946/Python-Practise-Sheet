# Initial dictionary
marks = {'John': 85, 'Jane': 92, 'Bob': 7}

# Print all items, keys, and values
print(marks.items())   # dict_items([('John', 85), ('Jane', 92), ('Bob', 7)])
print(marks.keys())    # dict_keys(['John', 'Jane', 'Bob'])
print(marks.values())  # dict_values([85, 92, 7])
print(len(marks))      # 3

# Update the dictionary
marks.update({'Jane': 95, 'Tom': 88})
print(marks)           # {'John': 85, 'Jane': 95, 'Bob': 7, 'Tom': 88}

# Accessing elements
print(marks["Tom"])    # 88
print(marks.get('Tom', 'Not found'))  # 88

# Using pop to remove 'Jane' and return her score
pop = marks.pop('Jans', 8)
print(pop)             # 95
print(marks)           # {'John': 85, 'Bob': 7, 'Tom': 88}

# Using popitem to remove and return the last inserted item
pop_item = marks.popitem()
print(pop_item)        # ('Tom', 88)
print(marks)           # {'John': 85, 'Bob': 7}

# Uncomment the following line to clear all items from the dictionary
# print(marks.clear())  # None
