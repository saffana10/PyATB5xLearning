list = [1,2,3,4]
# Indexing
print("element at 0th index-- ",list[0])
print("element at 1th index-- ",list[1])
print("element at 2nd index-- ",list[2])
print("element at 3rd index-- ",list[3])

#append() - append takes multiple arguments
list.append(5)
print(list)

#extend() - can add list
list.extend([6,7,8,10])
print(list)

#insert
list.insert(0,"Saffana")
print(list)
print("-------")
list[1] = True
print(list)

# remove
list.remove("Saffana")
print(list)
print("----------------")

# copy()
my_list = list.copy()
print(my_list)

# sort()
list.sort()

my_list.remove(True)
print(my_list)
print(list)
