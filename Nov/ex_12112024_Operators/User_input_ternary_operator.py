# program - if age > 18 - allowed to vote
# take user_input

user_age = int(input("Enter your age\n"))

if user_age > 18:
    print("You are allowed to vote")
else:
    print("You are not allowed to vote")

# Ternary operator
print("You are allowed to vote" if user_age>18 else "You are not allowed to vote")


