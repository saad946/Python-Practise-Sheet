class Employee:
    language = "Python" # Class-specific attribute
    salary = 50000

harry = Employee()
harry.language = "Java" #instance attribute has higher precedence over class attribute
harry.name = "Harry" # Object-specific attribute 
print(harry.language, harry.salary, harry.name) # Output: Python 50000 Harry