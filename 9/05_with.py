f = open("./file.txt")

print(f.read())

f.close()

# same can be done with with statement to automatically close the file

with open("./file.txt") as f:
    print(f.read())

f = open("./file.txt")

# you don't need to close the file manually, it gets closed automatically when the with block ends