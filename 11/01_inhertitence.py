class Employee:
    comapny_name = "Google"
    
    def show(self):
        print(f"The name is {self.name} and salary is {self.salary}")

class Programmer(Employee):
    def showlanguages(self):
        # Join the languages into a single string separated by commas
        languages_str = ", ".join(self.languages) # Join the languages into a single string separated by commas
        print("The programmer's favorite languages are:", languages_str)

a = Employee()
b = Programmer()

a.name = "John Doe"
a.salary = 60000
b.languages = ["Python", "Java", "C++"]

a.show()
b.showlanguages()

print(a.comapny_name, b.comapny_name)
