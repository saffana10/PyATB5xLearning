
keys = {"name","age","experience"}
value = {"saffana", 57 }

my_dict = dict(zip(keys,value))
print(my_dict)

# Merge two dictionaries
dict_1 = {"a":1,"b":2}
dict_2 = {"c" : 3,"d":4}
merge_dict = dict_1 | dict_2
print(merge_dict)
print(merge_dict["a"])
print(merge_dict.get("b"))