# Write a program that classifies a triangle based on its side lengths.
# Given three input values representing the lengths of the sides,
# determine if the triangle is equilateral (all sides are equal),
# isosceles (exactly two sides are equal), or scalene (no sides are equal).
# Use an if-else statement to classify the triangle.

# step1 : Logic building
# i/p -> s1,s2,s3 -> int
# o/p -> string

# step 2 : Rough logic
# if s1=s2 and s1=s3 then print isoceles

# step 3 : Write the logic
s1 = int(input("Enter the length of s1:\n"))
s2 = int(input("Enter the length of s2:\n"))
s3 = int(input("Enter the length of s3:\n"))

if s1==s2 and s1==s3:
    print("Equilateral triangle")
elif s1==s2 or s2==s3 or s1==s3:
    print("isoceles triangle")
else:
    print("Scalene triangle")

