try:
    a = int(input("Enter a number: "))
    print(f"You entered: {a}")
    
except Exception as e:
    print("An unexpected error occurred:", e)
    print("Please try again later.")
else: # Code in this block will be executed if no exceptions are raised from the try block.
    print("No exceptions occurred.")

print("Thanks for using our service!")