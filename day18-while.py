print("GUESS THE NUMBER")
print("You can choose a number from 1 to 1000, until you guess\n")
score = 0
while True:
    number = int(input("What is your guess?: "))
    if number >= 0 and number <= 399:
        print("Too low.\n")
        score += 1
        continue
    elif number >= 401 and number <= 1000:
        print("Too high.\n")
        score += 1
        continue
    if number == 400:
        print("Correct!\n")
        print("It took you", score, "guesses to get correct!")
        exit()
    else:
        print()
        print("Thanks for playing!")
        exit()
