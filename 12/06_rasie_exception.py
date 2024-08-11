a = int(input("Enter a number: "))
b = int(input("Enter another number: "))


if (b == 0):
    raise ZeroDivisionError("Cannot divide by zero")
else:
    print(f"The sum of {a} and {b} is: {a / b}")