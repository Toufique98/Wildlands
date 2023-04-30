import time


def main():
    print("WELCOME TO MY MARVEL QUIZ")
    name = input("What is your name - ")
    print("Hello  ", name, "!")
    ans = input("do you want to continue ?")
    if ans in ["yes" or "yeah" or "y"]:
        start_quiz()
    else:
        print("Okay see you later!")
        quit()


def right():
    print("Correct !")


def wrong():
    print("Wrong one ")


def start_quiz():
    n = 0
    print("Cool starting game!")
    answer = input("What is the spiderman actor name ? ")
    time.sleep(2)
    if answer == "tom holand":
        n = n + 1
        right()
    else:
        wrong()

    answer2 = input("What is Tony's AI called ? ")
    time.sleep(2)
    if answer2 == "jarvis":
        n = n + 1
        right()
    else:
        wrong()

    answer3 = input("What is the nickname of winter soldier ? ")
    time.sleep(2)
    if answer3 == "bucky":
        n = n + 1
        right()
    else:
        wrong()

    answer4 = input("Who wanted to kill half of universe ? ")
    time.sleep(2)
    if answer4 == "thanos":
        n = n + 1
        right()
    else:
        wrong()

    answer5 = input("How many infinity stone were there ? ")
    time.sleep(2)
    if answer5 == "6":
        n = n + 1
        right()
    else:
        wrong()

    time.sleep(2)
    print("you got ", n, " questions correct", end=" ")
    print("and you are ", n / 5 * 100, " % correct")


main()
