list = [11, 22, 43, 4, 5]

# squaredList =[]

# for item in list:
#     squaredList.append(item**2)


squaredList = [item**2 for item in list]  # List comprehension method

print(squaredList)

