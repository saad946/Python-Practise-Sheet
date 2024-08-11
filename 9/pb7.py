# Initialize line number
lineno = 1

# Read all lines from the file
with open("./log.txt", "r") as f:
    lines = f.readlines()

# Flag to check if "python" is found
found = False
print(len(lines))
# Iterate through each line
for line in lines:
    if "python" in line:
        print(f"Python is present in the log file at line {lineno}.")
        found = True
        
    lineno += 1

# If "python" is not found in any line
if not found:
    print("Python is not present in the log file.")
