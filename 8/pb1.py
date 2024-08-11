a = int(input("Enter a number: "))
b = int(input("Enter another number: "))
c = int(input("Enter a third number: "))

def greatest(a,b,c):
  if a > b and a > c:
    return a
  elif b > a and b > c:
    return b
  else:
    return c
  
print(f"The greatest number is: {greatest(a,b,c)}")