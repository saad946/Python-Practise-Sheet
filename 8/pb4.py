'''
sum(1) = 1
sum(2) = 1 + 2 = 3
sum(3) = 1 + 2 + 3 = 6

sum(n) = sum(n-1) + n
'''


def sum1(n):
    if n == 1:
        return 1
    else:
        return sum1(n-1) + n
    
print(sum1(5))  # Output: 15
