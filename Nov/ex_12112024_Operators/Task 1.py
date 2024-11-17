# write a program to take user age and let him know if he can go to club
# step 1 : Logic building
#user input  i/p ->datatype-> int
# o/p -> string
# take input from user
#step 2: Rough logic
# if age > 18 then he can go to the club else "he can't
#step 3 : write the logic
age = int(input("Enter your age\n"))
#print(age)
if age >= 18:
    print("You are allowed to go to the club")
else:
    print("You are not allowed")
#step 4: Handle the edge cases
# Age is invalid
# Alphanumeric input
# Negative ages or extremely high ages -> program will break
# step 5 :Optimize the code