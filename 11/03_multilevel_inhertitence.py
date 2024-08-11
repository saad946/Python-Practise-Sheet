class Employee:
    a = 1
class Programmer(Employee):
    b= 2

class Coder(Programmer):
    c = 3

d = Employee()
e = Programmer()
f = Coder()

print(d.a)
print(e.b)
print(f.c,d.a,e.b)

d.a = 4
print(d.a)


