#Create a program that determines whether a given year is a leap year.
# A leap year is divisible by 4, but not by 100 unless it is also divisible by 400.
# Use an if-else statement to make this determination.

#step 1: Logic building
#i/p -> int
#o/p -> string
year = int(input("Enter the year:\n"))
# step 2: Rough logic
#if (year % 4 == 0 and year % 100 !=0) or (year % 400 ==0) print(leap year)

#step 3: write the logic
if (year % 4 ==0 and year % 100 !=0) or (year % 400 ==0):
    print("Year is a leap year",year)
else:
    print("Year is not a leap year",year)
