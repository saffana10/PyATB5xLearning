def decorator1(func):
    def wrapper():
        print("Start the browser")
        func()
    return wrapper

def decorator2(func):
    def wrapper():
        print("Quit the browser")
        func()
    return wrapper


@decorator1
@decorator2
def say_hello():
    print("Hi")

say_hello()