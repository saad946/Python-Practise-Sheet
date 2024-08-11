age = int(input("Enter a number: "))

# if statement1 to check if a number is even
if age%2 == 0:
    print("Number is even.")
else:
    print("Number is odd.")

# if elif else statemnt2 to check eligibility for voting
if age <= 0:
    print("Invalid age.")

elif age >= 18 and age <= 65:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")


