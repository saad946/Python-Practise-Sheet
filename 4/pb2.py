marks = []

# Collecting marks from the user
f1 = int(input("Enter the value of the first mark: "))
marks.append(f1)

f2 = int(input("Enter the value of the second mark: "))
marks.append(f2)

f3 = int(input("Enter the value of the third mark: "))
marks.append(f3)

f4 = int(input("Enter the value of the fourth mark: "))
marks.append(f4)

# Sorting the marks in descending order
marks.sort(reverse=True)

# Displaying the sorted marks
print("The four marks you entered in descending order are:", marks)
