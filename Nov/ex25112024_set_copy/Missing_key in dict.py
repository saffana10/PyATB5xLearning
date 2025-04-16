
dict_1 = {"a" :1 , "b" : 2}
dict_2 = {"a" :1 , "b" : 2 , "c" :3}

missing_keys = set(dict_2.keys()) - set(dict_1.keys())
print(missing_keys)