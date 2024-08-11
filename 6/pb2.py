maths = int(input("Enter the marks obtained in Mathematics: "))
physics = int(input("Enter the marks obtained in Physics: "))
computer = int(input("Enter the marks obtained in Computer Science: "))

Percentage= ((maths+physics+computer)/300)*100

if maths >= 40 and physics >= 40 and computer >= 40 and Percentage > 33:
    print("You are eligible for admission.", Percentage)

else:
    print("You are failed.", Percentage)