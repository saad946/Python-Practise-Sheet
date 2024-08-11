'''
For n = 3
  *
 ***
*****

'''
n =int(input("Enter a number: "))
for i in range(1, n+1):
    print(" "* (n-i), end="")   # spaces and  end statement to avoid newline character
    print("*"* (2*i-1), end="") # stars and  end statement to avoid newline character
    print("\n")                 # new line character

