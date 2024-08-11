f = open("./poem.txt")
content = f.read()
if ("twinkle" in content.lower()):
    print("The poem contains the word 'twinkle'.")
else:
    print("The poem does not contain the word 'twinkle'.")

f.close