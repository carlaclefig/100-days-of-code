print("GUESS THE NUMBER")
print("You can choose a number from 1 to 1000, until you guess")
score = 0
while True:
    number = input("What is your guess?: ")
    if number <= 0 and number >= 399:
        print("Too low.")
    elif number <= 401 and number >= 1000:
        print("Too high.")
    elif number == 400:
        print("Correct!")
