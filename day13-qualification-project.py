print("Exam Grade Calculator")
print()
input("Name of exam: ")
Maxscore = int(input("Max. Possible Score: "))
score = float(input("Your score: "))

pretotal = score / Maxscore
total = round((pretotal * 100), 2)

if total >= 90:
    print("You got", total, "% which is a A+")
elif total <= 89 and total >= 80:
    print("You got", total, "% which is a A-")
elif total <= 79 and total >= 70:
    print("You got", total, "% which is a B")
elif total <= 69 and total >= 60:
    print("You got", total, "% which is a C")
elif total <= 59 and total >= 50:
    print("You got", total, "% which is a D")
elif total <= 49:
    print("You got", total, "% which is a U")
else:
    print("Re-enter your score")
