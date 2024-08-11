class Employee:
    language = "Python" # Class-specific attribute
    salary = 50000
    def getInfo(self): # Method to print employee information from its own object
        print(f"Language: {self.language}, Salary: {self.salary}")
    @staticmethod   
    def greet(): # Method to greet the employee
        print(f"Hello")

harry = Employee()
harry.language = "Java" #instance attribute has higher precedence over class attribute
harry.name = "Harry" # Object-specific attribute 
print(harry.language, harry.salary, harry.name) # Output: Python 50000 Harry
Employee.getInfo(harry) # Output: Language: Java, Salary: 50
harry.greet() # Output: Hello, my name is Harry.