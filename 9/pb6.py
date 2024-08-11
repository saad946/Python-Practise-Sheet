with open("./log.txt", "r") as f:
    content = f.read()
if "python" in content:
    print("Python is present in the log file.")
else:
    print("Python is not present in the log file.")