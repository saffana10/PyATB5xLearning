my_dict = {
    "name" : "saffana",
    "role"  : "Manual tester",
    "age" : 25,
    "experience" : 2,
}

print(my_dict)
print(my_dict["role"])
del my_dict["age"]

print(my_dict)

my_dict["role"] = "Automation tester"
print(my_dict)

my_dict["test_result"] = 25

print(my_dict)

for key,value in my_dict.items():
    print(key,"->",value)

print("age" in my_dict)
print("role" in my_dict)

my_dict.pop("role")
print(my_dict)