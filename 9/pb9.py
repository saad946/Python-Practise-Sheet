with open("./log.txt") as f:
    content1 = f.read()

with open("./poem.txt") as f:
    content2 = f.read()

if content1 == content2:
    print("Both files are identical.")
else: 
    print("Files are different.")