# match same as switch in java
# applicable for python > 3.10

# write a program to start the automation as per the browser entered by the user

browser = input("Enter your browser\n")
match browser:
    case "firefox":
        print("starting firefox")
    case "safari":
        print("starting safari")
    case "chrome":
        print("starting chrome")
    case _:
        print("Browser not found")