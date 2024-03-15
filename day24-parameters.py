# In a subroutine, the () are for the argument (FYI argument is another word for parameter). These are the pieces of information we pass to the code. These can be variable names that are made up for the first time within the argument ().
print("INGREDIENTS FOR A CAKE")

user_ingredient = input("Name an ingredient: ")
user_base = input("Name a type of base: ")
user_coating = input("Fave cake topping: ")


def which_cake(ingredient, base, coating):
    if ingredient == "chocolate":
        print("Mmm, chocolate cake is amazing")
    elif ingredient == "broccoli":
        print("You what mate?!")
    else:
        print("Yeah, that's great I suppose...")

    print(
        "So you want a",
        ingredient,
        "cake on a",
        base,
        "base with",
        coating,
        "on top?",
    )


which_cake(user_ingredient, user_base, user_coating)
print()

print("BIGGER NUMBER")


def biggerNumber(number1, number2):
    if number1 > number2:
        print(number1, "is bigger")
    else:
        print(number2, "is bigger")


biggerNumber(18, 332)
print()

print("CHOOSE YOUR PIZZA")
topping1 = input("Name a pizza topping: ")
topping2 = input("Name a second pizza topping: ")


def pizza_order(topping1, topping2):
    if topping1 == "pepperoni":
        print(topping1, "is a great choice")
    else:
        print(topping1, "is kinda lame on pizza")

    print(topping2, "sounds delicious, much better than", topping1)


pizza_order(topping1, topping2)
print()

print("INFINITY DICE 🎲")
sides = int(input("How many sides?: "))
import random

number = random.randint(1, sides)
print("You rolled", number, "\n")
while True:
    number = random.randint(1, sides)
    roll = input("Roll again? ")
    if roll == "yes":
        print("You rolled", number, "\n")
    else:
        break

print("INFINITY DICE 🎲 \n")
sides = int(input("How many sides?: "))
import random

played = "yes"


def roll(sides):
    number = random.randint(1, sides)
    print("You rolled", number, "\n")


while played == "yes":
    roll(sides)
    played = input("Roll again? ")
