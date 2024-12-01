pb_global_b = 12

def new_func():
    a = 10 # local variable (within function)
    print(a)
    print(pb_global_b)
#print(a) -> Return error if outside the func
print(pb_global_b)
new_func()