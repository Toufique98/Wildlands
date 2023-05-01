import time


def delay_show():

    name = input("What is your name? ")
    print("Hello, " + name)
    age = int(input("How old are you? "))
    match age:
        case 10 | 20 | 30 | 40 | 50 | 60:
            print("Nice decade", name)
        case age >= "18":
            print(f"Sorry {name}, you are not old enough.")
        case  age >= 60:
        print(f"Good job {name}, still going strong!")
        case _:
        print("Sorry, not interesting.")


    delay_show():
