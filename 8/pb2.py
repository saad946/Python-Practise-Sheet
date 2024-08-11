def fehr_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

f = int(input("Enter a temperature in Fahrenheit: "))
c = fehr_to_celsius(f)
print(f"{round(c,2)} Degrees Celsius")

