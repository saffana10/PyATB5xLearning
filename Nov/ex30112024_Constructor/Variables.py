
a = 10  # global variable

class Person:
    b = 20 # instance variable

    def print_info(self):
        c = 30
        print(c)
        print(self.b) #(instance variable will be called by self)
 #       a = "hello"  # local variable will have more preferenve than global variable
        global a
        print(a)

obj_ref = Person()
obj_ref.print_info()