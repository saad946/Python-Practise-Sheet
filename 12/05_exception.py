try:
    a = int(input("Enter a number: "))
    print(f"You entered: {a}")
except ValueError as e:
    print(e)
    print("Invalid input. Please enter a valid integer.")
    
except Exception as e:
    print("An unexpected error occurred:", e)
    print("Please try again later.")

print("Thanks for using our service!")