class Employee:
    name = "John Doe"
    
    @classmethod # Class method can access and modify class attributes
    def show(cls):
        print(f"The class attribute of a is {cls.name}")

e = Employee()
# Employee.name = "Govinda"  # Modifying the class attribute directly.
e.name = "Saad Doe" #cant modify instance attribute so will print the default value of name attribute from class attribute

e.show()