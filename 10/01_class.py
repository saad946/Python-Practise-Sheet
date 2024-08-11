class Employee:
    language = "Python" # Class-specific attribute
    salary = 50000

harry = Employee()
harry.name = "Harry" # Object-specific attribute 
print(harry.language, harry.salary, harry.name) # Output: Python 50000 Harry

saad = Employee()
saad.name = "saad"
print(saad.language, saad.salary, saad.name) 

# Here name is object-specific attribute and language and salary are class-specific attributes.

