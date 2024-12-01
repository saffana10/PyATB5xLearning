def before_after_ui(func):

    def wrapper():
        print("Open the browser")
        print("Start testing the UI")
        func()
        print("Finish the UI testing")
        print("Quit the browser")

    return wrapper()


@before_after_ui
def test_ui():
    print("I will test the UI")