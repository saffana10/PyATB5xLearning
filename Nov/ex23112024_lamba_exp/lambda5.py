import math

def pow(num):
    return math.pow(num,2)

result = pow(5)
print(result)

result = lambda : math.pow(int(input("Enter your number:")),2)
print(result())