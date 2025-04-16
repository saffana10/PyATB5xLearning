# function that returns a max value from a dictionary

dict ={"a" : 10 , "b" : 30 , "c" : 20}

def max_dict_value(dict):
    #return max(dict.values())
    return min(dict.values())

print(max_dict_value(dict))