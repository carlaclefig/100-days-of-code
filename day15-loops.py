# This variable will be used to keep track of the numbers that are printed in the sequence.
counter = 00
# while: bucle, max number 50
while counter <= 50:
    print(counter)
    # print 5 in 5 from 0 to 50
    counter += 15
print()
print()
exit = ""
# used != with text
while exit != "yes":
    print("🤩")
    exit = input("Exit?: ")
print()
print()
print("Animal Farm")
exit = "no"
while exit == "no":
    animal = input("What animal do you want? ")
    if animal == "Dog" or animal == "dog":
        print("The", animal, "makes the woof sound")
    elif animal == "Cat" or animal == "cat":
        print("The", animal, "makes the meow sound")
    elif animal == "Cow" or animal == "cow":
        print("The", animal, "makes the mooo sound")
    elif animal == "Frog" or animal == "frog":
        print("The", animal, "makes the croac sound")
    else:
        print("Oops, we don't have that animal.")
    exit = input("Do you want to exit? ")
