# Function to input numbers
def input_numbers():
    numbers = []
    while True:
        num = input("Enter a number (or type 'done' to finish): ")
        if num.lower() == 'done':
            break
        try:
            numbers.append(int(num))
        except ValueError:
            print("Please enter a valid number.")
    return numbers

# Function to find and print the largest number
def find_largest_number(numbers):
    if not numbers:
        print("No numbers were entered.")
    else:
        largest_number = max(numbers)
        print(f"The largest number is {largest_number}.")

# Main program
numbers = input_numbers()
find_largest_number(numbers)
