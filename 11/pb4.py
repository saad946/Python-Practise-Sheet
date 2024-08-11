class complex_calculator:
    def __init__(self, r, i):
        self.r = r
        self.i = i
    
    def __add__(self, c2):
        return complex_calculator(self.r + c2.r, self.i + c2.i)
    
    def __str__(self) -> str:
        return f"{self.r}i+{self.i}j" # Returning a string representation of the complex number after adding the two complex numbers.
    

c1 = complex_calculator(3, 4)
c2 = complex_calculator(1, 2)

print(c1 + c2)  # Output: 4+6j
