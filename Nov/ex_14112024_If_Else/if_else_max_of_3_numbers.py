#step 1: Logic building
# i/p -> num1 , num2 , num3
#o/p -> Max of three number

#step 2 : Rough logic
# num1 > num2 and num1>num3 print num1
# num2 > num1 and num2>num3 print num2
# Else print num 3

# Step 3 :Write the logic
num1 = int(input("Enter the number 1:\n"))
num2= int(input("Enter the number 2:\n"))
num3 = int(input("Enter the number 3:\n"))

if num1>num2 and num1>num3:
    print("Max no.is",num1)
elif num2>num1 and num2>num3:
    print("Max no.is" ,num2)
else:
    print("Max no.is:",num3)