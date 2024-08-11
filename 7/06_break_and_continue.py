for i in range(100):
    if (i== 34):
        break #skip all the iterations where i equals 34.
    print(i)


for i in range(100):
    if (i== 34):
        continue # Skip the current iteration and move to the next one.
    print(i)
else:
    print("All numbers printed with continue statement.")