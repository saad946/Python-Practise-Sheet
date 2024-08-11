list = [11, 22, 43, 4, 5]

# index = 0
# for item in list:
#     print(f"the item at index {item} is {item}")
#     index += 1


# This can be simlified with enumerate function:

for index, item in enumerate(list):
    print(f"the item at index {index} is {item}")
