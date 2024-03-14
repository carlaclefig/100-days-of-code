# A subroutine is defined by: def variable():
def rollDice():
    import random

    dice = random.randint(1, 6)
    print("You rolled", dice)


for i in range(5):
    # Note that when you call the subroutine, you need to ensure you do NOT indent.
    rollDice()


def MyName():
    print("My Name is David")


MyName()


def countToFive():
    for i in range(1, 6):
        print(i)


countToFive()


print("REPLIT LOGIN SYSTEM\n")


def login():
    for i in range(5):
        username = input("What is your username: ")
        password = input("What is you password: ")
        if username == "David" and password == "baldies4life":
            print("Welcome to REPLIT.\n")
            break
        else:
            print("Whops! I don't recognize that username or password, try again.\n")
            continue


login()
