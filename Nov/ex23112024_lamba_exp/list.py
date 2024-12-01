# list - collection of items
#Grocery - bread , butter , paneer

list = [1,2,3,4]
print(list)

print(list[0])
print(len(list))
print("----")

list2 = [1,"Saffana",13.42,True]
print(list2)
print("----")

list2[0] = "Python"
list2[1] = "Automation"
print(list2)
print("-----")

for items in list2:
    print(items)

print("---")
for i in range(1,5):
    print(i,end=" ")
#range also returns list