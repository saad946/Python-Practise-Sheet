age = int(input("Enter your age: "))

# if elif else ladder to check eligibility for voting
if age <= 0:
    print("Invalid age.")

elif age >= 18 and age <= 65:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")


