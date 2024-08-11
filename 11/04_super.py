class Employee:
    def __init__(self) -> None:
        print("Employee created")
    a = 1

class Programmer(Employee):
    def __init__(self) -> None:
        super().__init__()  # This ensures that Employee.__init__() is called
        print("Programmer created")
    b = 2

class Coder(Programmer, Employee):
    def __init__(self) -> None:
        super().__init__()
        print("Coder created")
    c = 3

# Create instances
d = Employee()      # This will print "Employee created"
e = Programmer()    # This will print "Employee created" followed by "Programmer created"
f = Coder()         # This will print "Employee created", "Programmer created", and "Coder created"

# Access attributes
print(d.a)          # Output: 1
print(e.b)          # Output: 2
print(f.c, d.a, e.b) # Output: 3 1 2

# Modify attribute
d.a = 4
print(d.a)          # Output: 4
