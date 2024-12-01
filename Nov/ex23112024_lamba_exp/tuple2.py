Cities = ["Paris","London","New York","India"]
print("New Delhi" in Cities)
print("Paris" in Cities)

t = (1,2,3,4)
#print(t.append(6))  AttributeError: 'tuple' object has no attribute 'append'

my_list = list(t)
my_list.append(6)
print(my_list)
print("----------------")
t = tuple(my_list)
print(t)