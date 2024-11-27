# Create a program for sum of three number
# if user does not provide input take default as 100,200,300

#User input 
a = int(input("Enter num 1:\n"))
b = int(input("Enter num2:\n"))
c = int(input("Enter num3:\n"))

def sum_of_three_number(a,b,c):
    return a+b+c

result = sum_of_three_number(a,b,c)
print("Sum of three numbers :" ,result)

#Default value
def sum_of_three_number_with_default(a=100,b=200,c=300):
    return a+b+c
result = sum_of_three_number_with_default()
print(result)