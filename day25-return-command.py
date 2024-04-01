# ---------------------------------- Example 01 ---------------------------------------
# subroutine has parameter called `number`
# `number` shows how many numbers we want the pin to have
def pin_picker(number):
    import random

    pin = ""  # this is the empty string
    for i in range(number):  # for loop shows defined amount of random numbers
        pin += str(
            random.randint(0, 9)
        )  # we want a string of random numbers between 0-9
    return pin


pin = pin_picker(3)  # 4 means we want 4 random numbers
print(pin, "\n")
# ---------------------------------- Example 02 ---------------------------------------
print("AREA OF TRIANGLE")


def area_of_triangle(base, height):
    area = 0.5 * base * height
    return area


area = area_of_triangle(8, 22)
print(area, "\n")
# ---------------------------------- Exercise 01 - form I ---------------------------------------
import random

print("⚔️ Character Stats Generator ⚔️\n")


def rollDice():
    dice = random.randint(1, 6) * random.randint(1, 8)
    if dice >= 33:
        print("Their health is", "\033['\033[32m", dice, "\033[0m", "hp\n")
    elif dice >= 17 and dice <= 32:
        print("Their health is", "\033['\033[33m", dice, "\033[0m", "hp\n")
    else:
        print("Their health is", "\033['\033[31m", dice, "\033[0m", "hp\n")


while True:
    player = input("Name your warrior: ")

    if player == "exit":
        print("Thanks for playing!")
        break

    for i in range(1):
        rollDice()

# ---------------------------------- Exercise 01 - form II ---------------------------------------
import random


def rollDice(sides):
    result = random.randint(1, sides)
    return result


def roll_6_and_8():
    roll_6_sided_dice = rollDice(6)
    roll_8_sided_dice = rollDice(8)
    health = roll_6_sided_dice * roll_8_sided_dice
    return health


print("⚔️Character stats generator⚔️")


haveACharacter = "yes"

while haveACharacter == "yes":
    character = input("Name your warrior: ")
    health = str(roll_6_and_8())
    print("Their health is ", health, "hp")
    haveACharacter = input("Want to create another character?")
