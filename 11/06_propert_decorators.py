# this is abstraction and encapsulation. 
class Employee:
    a = 1
    
    @classmethod
    def show(cls):
        print(f"The class attribute of a is {cls.a}")

    @property # A property method is used to provide a getter method for a class attribute. it is gatter method which returns the value of the attribute.
    def name(self):
        return f"{self.fname} {self.lname}" #it returns the full name of the employee which is set by setter method 
    
    @name.setter # A setter method is used to provide a setter method for a class attribute
    def name (self,value):
        print("Setting name...")
        self.fname = value.split(" ")[0]
        self.lname = value.split(" ")[1]

e = Employee()
e.a = 45

e.name = "John Khan"
print(e.fname, e.lname)

e.show()