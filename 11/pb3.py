# class Employee:
#     salary = 250000
#     def raise_salary(self, percentage):
#         self.salary += self.salary * (percentage / 100)


# e = Employee()
# e.raise_salary(10) # Raises the salary by 10%

# print(e.salary) # Output: 268.5

class Employee:
    salary = 250000
    increment = 10

    @property
    def raise_salary(self):
        return int((self.salary * (self.increment / 100)) + self.salary)

    @raise_salary.setter
    def raise_salary(self, new_salary):
        self.increment = ((new_salary / self.salary) - 1) * 100

e = Employee()
e.raise_salary = 300000  # Raises the salary to 300000

print(f"Your base salary is Rs.{e.salary}")  # This will still output 250000, which is correct
print(f"Your salary has been increased to Rs.{e.raise_salary}")  # This will output the new salary, which is 275000
print(f"Congratulations!! The raise you received is {e.increment:.2f}%")





