print("Fill-in the blank Lyrics!")
print("Type in the blank lyrics, see if ")
print()
counter = 1
while True:
    print("Never going to____you up.")
    again = input("What is the missing word?: ")
    if again == "give":
        break
    else:
        print("Nope, try again.")
        counter += 1
        print()
print()
print("Well done.")
print("You got the correct lyrics in", counter, "attempt(s).")
