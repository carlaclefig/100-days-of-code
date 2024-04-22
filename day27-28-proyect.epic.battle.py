import random
import os, time


def roll_dice(sides):
    result = random.randint(1, sides)
    return result


def generate_health():
    health = ((roll_dice(6) * roll_dice(12)) / 2) + 10
    return health


def generate_strength():
    strength = ((roll_dice(6) * roll_dice(8)) / 2) + 12
    return strength


def generate_health_and_strength():
    health = generate_health()
    strength = generate_strength()
    return health, strength


def welcome(name, type):
    print("Welcome", name.upper())
    print("You are a", type.upper())
    health, strength = generate_health_and_strength()
    print("Your Health is:", health)
    print("Your Strength is:", strength)
    return health, strength


print("⚔️ CHARACTER BUILDER ⚔️\n")
while True:

    turn = 1
    name_player1 = input("Name your Legend: ")
    type_player1 = input("Character Type (Human, Elf, Wizard, Orc): ")
    print()
    health_player1, strength_player1 = welcome(name_player1, type_player1)
    print("\nWho are they battling?\n")
    name_player2 = input("Name your Legend: ")
    type_player2 = input("Character Type (Human, Elf, Wizard, Orc): ")
    print()
    health_player2, strength_player2 = welcome(name_player2, type_player2)

    while True:
        time.sleep(2)
        os.system("clear")
        print("⚔️ BATTLE TIME ⚔️\n")
        print("The battle begins!\n")

        print("Turn", turn, "\n")
        roll_player1 = roll_dice(6)
        roll_player2 = roll_dice(6)

        damage = abs((strength_player1 - strength_player2) + 1)

        if roll_player1 > roll_player2:
            print(name_player1, "wins the", turn, "blow")

            print(name_player2, "takes a hit, with", damage, "damage\n")

            health_player2 -= damage
            print(name_player1, "the", type_player1, "\n Health:", health_player1)
            print(name_player2, "the", type_player2, "\n Health:", health_player2)

        elif roll_player1 < roll_player2:
            print(name_player2, "wins the", turn, "blow")

            print(name_player1, "takes a hit, with", damage, "damage\n")

            health_player1 -= damage
            print(name_player1, "the", type_player1, "\nHealth:", health_player1)
            print(name_player2, "the", type_player2, "\nHealth:", health_player2)

        else:
            print("Their swords clash and they draw turn", turn)

        if health_player1 <= 0:
            print("\nOh no", name_player1, "has died!")
            print(
                name_player2,
                "the",
                type_player2,
                "destroyed",
                name_player1,
                "the",
                type_player1,
                "in",
                turn,
                "rounds!",
            )
            break
        elif health_player2 <= 0:
            print("\nOh no", name_player2, "has died!")
            print(
                name_player1,
                "the",
                type_player1,
                "destroyed",
                name_player2,
                "the",
                type_player2,
                "in",
                turn,
                "rounds!",
            )
            break
        else:
            print("\nAnd they're both standing for the next turn")
            turn = turn + 1
        time.sleep(2)
        os.system("clear")
    break
