class programmers:
    company = "Google."
    def __init__(self, name, age, language, experience, salary) -> None:
        self.name = name
        self.age = age
        self.language = language
        self.experience = experience
        self.salary = salary

p = programmers("John Doe", 30, "Python", 5, 5)
print(p.company, p.name,  p.age, p.language, p.experience, p.salary)    

print(f"{p.name} is a {p.experience} years experienced programmer who works at {p.company} and earns ${p.salary} per year.")

