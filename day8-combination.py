print("Wholesome Positivity Machine")
print()
name = input("Who are you?")
password = input("Password =")
# or to insert answers with upper or lower case that will be accepted
if (
    name == "David"
    and password == "StudentDavid"
    or name == "david"
    and password == "StudentDavid"
):
    print("Hi", name, "welcome!")
    input("How we woke up?")
    print()
    achieve = input("What do you want to achieve?")
    if achieve == "Learn to code" or achieve == "learn to code":
        print()
        print("On a scale of 1 - 10 ready do you feel to", achieve, "? ")
        scale = input("(1: 😥, 10: 🥳):")
        if scale == "1" or scale == "2" or scale == "3" or scale == "4":
            print()
            print(
                "Don't worry, they will teach you step by step so you can learn to code like an expert, let's get to it!😉"
            )
        else:
            print()
            print("You are amazing at coding, keep going!🤓")
    else:
        print("Sorry, try again")
elif name == "Mark" and password == "M4rkPass":
    print("Welcome teacher", name)
    input("How are you?")
    print()
    achieve = input("What do you want to achieve?")
    if achieve == "Teach people to code!" or achieve == "teach people to code!":
        print()
        print("On a scale of 1 - 5, How many topics will you advance today??")
        scale = input("(1:😒, 5:🤩):")
        if scale == "1" or scale == "2":
            print()
            print(
                "Wow, you are taking the time to teach in detail, let's go for more!😉"
            )
        else:
            print()
            print(
                "Incredible, wow, the people learn very quickly, what a good teacher they have, let's keep it up!🫡"
            )
    else:
        print("Sorry teacher, try again")
else:
    print("The user does not exist")
