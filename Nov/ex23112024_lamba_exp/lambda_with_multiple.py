# write a program to calculate even and odd

# def find_even_odd(num):
#     if num%2 == 0:
#         print("Even")
#     else:
#         print("Odd")
#
# find_even_odd(5)
n = int(input("Enter the number:\n"))
result = lambda num : "Even" if num%2==0 else "odd"
print(result(10))
print(result(n))