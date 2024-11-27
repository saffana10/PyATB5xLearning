# # Type 1 : No return type , no argument(no parameter)
# from Nov.ex_16112024_loops.Match_statement import browser
#
#
# def greet():
#     print("Hello")
# greet()
#
# # Type 2 : No return type and with argument / param
# def greet(name):
#     print("Hello,",name)
#
# greet("Saffana")
#
# # Type 3 : No return type with default argument
# def say_hello_default_arg(name ="Saffana"):
#     print("hello," ,name.upper())
# say_hello_default_arg()
# say_hello_default_arg("Siddiqui")
#
# # Type 4 : No return type with multiple arguments
# def mul_arg(name1 ="saff",name2 = "sid"):
#     print("Mul ->", name1,name2)
# mul_arg( ) # default_arg
# mul_arg("A","B")
# mul_arg("A")

# type 5 : Return type with argument
def sum_of_two(a,b):
    return a + b
result = sum_of_two(40,90)
print("Sum of two numbers is :",result)

# Sum of two number with default
def sum_of_two_number_with_default(a=100,b=500):
    return a+b
result = sum_of_two_number_with_default()
print(result)
result = sum_of_two_number_with_default(a=45,b=45)
print(result)
