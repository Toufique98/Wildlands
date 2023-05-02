import time


def main():
    print("WELCOME TO MY MARVEL QUIZ")
    name = input("What is your name - ")
    print("Hello  ", name, "!")
    ans = input("do you want to continue ?")
    if ans.lower() in ["yes", "yeah", "y"]:
        start_quiz(name)
    else:
        print("Okay see you later!")
        quit()


def right():
    print("Correct !")


def wrong():
    print("Wrong one ")


def start_quiz(name):
    n = 0
    print("Cool starting game!")
    time.sleep(1)
    answer = input("What is the spiderman actor name ? ")
    time.sleep(2)
    if answer.lower() == "tom holland" or "tom holland":
        n = n + 1
        right()
    else:
        wrong()

    time.sleep(1)
    answer2 = input("What is Tony's AI called ? ")
    time.sleep(2)
    if answer2.lower() == "jarvis":
        n = n + 1
        right()
    else:
        wrong()

    time.sleep(1)
    answer3 = input("What is the nickname of winter soldier ? ")
    time.sleep(2)
    if answer3.lower()== "bucky":
        n = n + 1
        right()
    else:
        wrong()

    time.sleep(1)
    answer4 = input("Who wanted to kill half of universe ? ")
    time.sleep(2)
    if answer4.lower() == "thanos":
        n = n + 1
        right()
    else:
        wrong()

    time.sleep(1)
    answer5 = input("How many infinity stone were there ? ")
    time.sleep(2)
    if answer5.lower() == "6":
        n = n + 1
        right()
    else:
        wrong()

    time.sleep(2)
    print("you got ", n, " questions correct", end=" ")
    print("and", name, "you are", n / 5 * 100, " % correct")


main()
