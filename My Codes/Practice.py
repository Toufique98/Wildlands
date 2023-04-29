import time


def delay_trick():
    time.sleep(3)

⁷
name = input("Hii whatts your name? ")
print("Hello ... ", name, "  ", end=" ")
age = int(input("Can you share your age... "))
if age >= 1:
    delay_trick()
if age > 1 and age <= 15:
    print("Youre a kid ")
elif age <= 16 or age <= 25:
    print("Focus now bro")
elif age <= 26 or age <= 40:
    print("you still got time bro")
elif age <= 41 or age <= 50:
    print("live while you can")
else:
    print("youre old, birth year is", 2023 - age)
    vgg