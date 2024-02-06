print("MY LOGIN SYSTEM")
print("+++++++++++++++")
username = input("Username >")
password = input("Password >")
print()
if username == "David" and password == "totallyNotBald":
    print(
        "Why hello there David, what a lovely accent you have, you could have charmed your way in here even without a password."
    )
    print("Have a great day.")
    print("Don't forget to wear a hat in the sun!")
# elif: If the variable responds to 'Marck' along with its password, then it prints the following:
elif username == "Marck" and password == "M4rckPass":
    print("Hi Marck, you will do an excellent job today.")
    print("Have a productive day.")
    print("Don't forget to use sunscreen when you're in the sun!")
elif username == "Pamela" and password == "PamPassWk":
    print("Welcome Pamela, it's good to see you here again.")
    print("Have an excellent day.")
    print("Don't forget to bring an umbrella in case it rains!")
else:
    print("What's up, get out of here!")
