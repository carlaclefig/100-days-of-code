print("Math Game!\n")
number_user = int(input("Name your multiples:\n "))
score = 0
for number in range(1, 11):
    correct = number * number_user
    print(number, "x", number_user, "=")

    correct_answer = int(input("> "))
    if correct_answer == correct:
        print("Great work \n")
        score += 1
    else:
        print("Nope. The answer was", correct, "\n")

if score == 10:
    print("Wow! A perfect score! 🥳", score)
else:
    print("You scored", score, "out of 10")
