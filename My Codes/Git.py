def counts(word):
    count = int(input("How many times "))
    if count < 3:
        kick_out()
    else:
        for _ in range(count):
            print(word)


def oath():
    word = input("So you need to say hail hydra 3 times, please type -  ")
    if not word == "hail hydra":
        kick_out()
    else:
        counts(word)


def kick_out():
    print("You are kicked out")


def deny(name):
    print("Well you can't come in ...", name, "Youre evil...")
    good_deeds = int(input(" But wait... how many good deed today ? "))
    if good_deeds >= 3:
        allow(name)
    else:
        kick_out()


def allow(name):
    print("Welcoem youre in ", name)
    oath()


def profile():
    name = input("enter your name: ")
    if (
        name != "red skull"
        and name != "loki"
        and name != "ego"
        and name != "thanos"
        and name != "hella"
        and name != "kang"
        and name != "ultron"
    ):
        allow(name)
    else:
        deny(name)


profile()
