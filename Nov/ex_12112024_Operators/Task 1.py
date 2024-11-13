# write a program to take user age and let him know if he can go to club
# step 1 : Logic building
# i/p , o/p
# take input from user
# if age > 18 then he can go to the club else "he can't

age = int(input("Enter your age\n"))
#print(age)
if age >= 18:
    print("You are allowed to go to the club")
else:
    print("You are not allowed")