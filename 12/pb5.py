n = int(input("Enter a number: "))

table = [n*i for i in range(1, 11)]
print(table)


with open ('numbers.txt', 'a') as f:
    f.write(str(table) + '\n')
