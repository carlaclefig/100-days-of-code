print("Exam Grade Calculator")
print()
input("Name of exam: ")
Maxscore = int(input("Max. Possible Score: "))
score = float(input("Your score: "))

pretotal = score / Maxscore
total = round((pretotal * 100), 2)
