while True:
    print("This program is running")
    again = input("Go again?: ")
    if again == "no":
        break
print("Aww, i was having a good time 😭")

counter = 0
while True:
    answer = int(input("Enter a number: "))
    print("Adding it up")
    # counter = counter + answer:
    counter += answer
    print("Current total is", counter)
    another = input("Add another? ")
    if another == "no":
        break
print("Bye!")

print("Fill-in the blank Lyrics!")
print("Type in the blank lyrics, see if ")
print()
while True:
    print("Never going to____you up")
    again = input(": ")
    if again == "give":
        break
print("Well done")
