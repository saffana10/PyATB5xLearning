#Area of circle = pi*r^2
#step 1: Logic building
#Take user input
# input - r -> datatype -> float
#pi = 3.14
#o/p -> float -> area , print area

#step 2 Rough logic
# Area = 3.14 * pow(r,2)
# Area = 3.14 * (r ** 2)

#step 3:


radius = float(input("Enter the radius\n"))
print(radius)
area = 3.140987 * (radius ** 2)
print("Area of circle is :", area)
print(f"Area of circle is ((Area)) : {area:.2f}")

import math
print(math.pi)
area = math.pi * math.pow(radius,2)
print(f"Area of circle is: {area:.3f}" )