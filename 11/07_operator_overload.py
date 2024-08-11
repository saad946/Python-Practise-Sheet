class Number:
    def __init__(self, n):  # Initialization method requiring an argument
        self.n = n

    def __add__(self, other):  # Overloading the + operator and it adds the two instances' values
        return self.n + other.n #it returns the sum of the two instances' values

# Creating instances of the Number class with initial values
f = Number(1)
s = Number(2)


# Modifying the values of the instances directly
f.n = 5
s.n = 10

# Using the + operator, which uses the __add__ method
print(f + s)  # Output will be 15
