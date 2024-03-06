import random

print("GUESS THE NUMBER")
print("You can choose a number from 1 to 100, until you guess\n")

number = random.randint(1, 100)
score = 0
print(number)
while True:
    number_user = int(input("What is your guess?: "))
    score += 1
    if number_user < 0:
        print(
            "You have entered a negative number , which is the secret way to exit the game."
        )
        exit()

    if number_user > number:
        print("Too high.\n")
    elif number_user < number:
        print("Too low.\n")
    elif number_user == number:
        print("Correct!\n")
        print("It took you", score, "guesses to get correct!")
        exit()
