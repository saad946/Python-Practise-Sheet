class calculator:
    def __init__(self, n):
        self.n = n
    def square(self):
        print(f"The square of {self.n} is {self.n*self.n}.")

    def cube(self):
        print(f"The cube of {self.n} is {self.n*self.n*self.n}.")
    def factorial(self):
        fact = 1
        for i in range(1, self.n+1):
            fact *= i # multiplying each number from 1 to n.
        print(f"The factorial of {self.n} is {fact}.")
    def sqrt(self):
        print(f"The square root of {self.n} is {self.n**0.5}.")


a = calculator(5)

print(a.n)  # Output: 5

a.square()  # Output: The square of 5 is 25
a.cube()  # Output: The cube of 5 is 125
a.sqrt()  # Output: The square root of 5 is 2.23606
