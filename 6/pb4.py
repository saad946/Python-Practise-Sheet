password = input("Enter your password: ")

if len(password) < 10:
    print("Password must be at least 10 characters long.")

else:
    print("Password is valid.")