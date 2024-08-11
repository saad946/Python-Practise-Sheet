friends = ['Alice', 'Bob', 'Charlie', 'David', 'Eve'] 
# list are mutable, so we can change the value of a list item directly
print(f'Hello, {friends[0]}!')
friends[0] = 'Grace'

print(f'Hello, {friends[0]}!')
print(friends[1:4])
