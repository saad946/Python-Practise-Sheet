class Demo:
    a = 4

s = Demo()
print(s.a) #Prints the class variable a value. 4 beacomes 5 after modifying the instance variable a.
s.a = 5 # Modifying the instance variable a.
print(s.a)

 
f =Demo()
print(f.a) #still prints the class variable a value. 4 remains unchanged.

