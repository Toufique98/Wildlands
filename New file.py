def delay():
    import time

    time.sleep(2)


def main():
    print("Welcome ...")
    name = input("What's the name? ")
    if (
        name == "red skull"
        or name == "loki"
        or name == "ego"
        or name == "thanos"
        or name == "hella"
        or name == "kang"
        or name == "ultron"
    ):
        print("Well you can't come in ...", name, end=" ")
    else:
        print("Welcome", name)

        good_deeds = int(input("wait... how many good deed today ? "))
        if good_deeds >= 3:
            print("Okay you can come in... ")
        else:
            print("Get out  " + name)

        word = input("So you need to say hail avengers 3 or more times, please type ")
    if word != "hail avengers":
        print("Get out !!")
    else:
        count = int(input(" How many times ? "))
    if word == "hail avengers" and count >= 3:
        for i in range(count):
            print(word)
    else:
        print("Get out !! told you 3 times ")


main()
