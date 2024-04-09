import random
import os, time


def roll_dice(sides):
    result = random.randint(1, sides)
    return result


def roll_6_and_12():
    health = ((roll_dice(6) * roll_dice(12)) / 2) + 10
    return health


def roll_6_and_8():
    strength = ((roll_dice(6) * roll_dice(8)) / 2) + 12
    return strength


while True:
    print("⚔️ CHARACTER BUILDER ⚔️\n")
    name = input("Name your Legend: ")
    character = input("Character Type (Human, Elf, Wizard, Orc): ")
    print()
    print(name.upper())
    print("HEALTH:", roll_6_and_12(), "hp")
    print("STRENGTH:", roll_6_and_8(), "hp\n")
    print("May your name go down in Legend...\n")

    play = input("Again?: ")
    if play == "yes":
        time.sleep(1)
        os.system("clear")
        continue
    else:
        break
