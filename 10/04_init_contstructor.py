class Employee:
    language = "Python" # Class-specific attribute
    salary = 50000

    def __init__(self, name, salary, language) -> None: #dunder method for object initialization automatically when an object is created
        self.name = name # Object-specific attribute which can be changed by the object itself
        self.salary = salary
        self.language = language

    def getInfo(self): # Method to print employee information from its own object
        print(f"Language: {self.language}, Salary: {self.salary}")

    @staticmethod   
    def greet(): # Method to greet the employee
        print(f"Hello")

harry = Employee("Harry", 50000, "Java") # Object-specific attribute can be
print(harry.language, harry.salary, harry.name) # Output: Python 50000 Harry
Employee.getInfo(harry) # Output: Language: Java, Salary: 50) # Output: Language: Java, Salary: 50
Employee.greet() # Output: Hello, my name is Harry.
