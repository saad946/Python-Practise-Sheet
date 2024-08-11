f = open("./file.txt", "r")

# lines = f.readlines()

# print("Total lines in the file:", len(lines))

# print(lines)

# line1 = f.readline()
# print("First line:", line1)

# line2 = f.readline()
# print("Second line:", line2)

# line3 = f.readline()
# print("Third line:", line3)

# line4 = f.readline()
# print(line4=="")



line = f.readline()
while(line!=""):
    print("Line:", line.strip()) # remove newline character using strip() method
    line = f.readline() 


f.close()