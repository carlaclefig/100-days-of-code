# ---------------------------------- Example 01 ---------------------------------------
import random


# A subroutine is defined by: def variable():
def rollDice():
    dice = random.randint(1, 6)
    print("You rolled", dice)


for i in range(5):
    # Note that when you call the subroutine, you need to ensure you do NOT indent.
    rollDice()

# ---------------------------------- Example 02 ---------------------------------------


def MyName():
    print("My Name is David")


MyName()

# ---------------------------------- Example 03 ---------------------------------------


def countToFive():
    for i in range(1, 6):
        print(i)


countToFive()

# # ---------------------------------- Exercise 01 ---------------------------------------


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

## ---------------------------------- Exercise 02 ---------------------------------------

# Calculate the double of numbers between 1 and 100


def double(number):
    result = number * 2
    return result


def triple(number):
    result = number * 3
    return result


def print_double(number):
    result = number * 2
    print(result)


for i in range(1, 100):
    tmp_result = double(i)
    print(tmp_result)


level = double(8) + double(3)

print(double(8))
print(print_double(8))

print(triple(double(3)))
