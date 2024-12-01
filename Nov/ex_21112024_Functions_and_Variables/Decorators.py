def add_security(func):

    def wrapper():
        print("Begin the function")
        print("Carry gloves,Knee guards,Helmet , Key")
        func()
        print("End of the function")
        print("Stop the bike")
        print("park the bike")

    return wrapper()

@add_security
def drive_ola():
    print("ola-----")



@add_security
def drive_scooty():
    print("On the bike")
    print("Start driving ------")