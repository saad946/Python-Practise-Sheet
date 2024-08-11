class Employee:
    comapny_name = "Google"
    
    def show(self):
        print(f"The name is {self.name} and salary is {self.salary}")

class coder:
    language = "Python"
    def print_languages(self):
        print("The programmer's expertise are in:", self.language)

class Programmer(Employee, coder):
    def showlanguages(self):
        # Join the languages into a single string separated by commas
        languages_str = ", ".join(self.languages) # Join the languages into a single string separated by commas
        print("The programmer's favorite languages are:", languages_str)

a = Employee()
b = Programmer()

a.name = "John Doe"
a.salary = 60000
b.languages = ["Python", "Java", "C++"]

print(f"Prohrammer is currently working at {a.comapny_name}")
a.show()
b.showlanguages()
b.print_languages()


