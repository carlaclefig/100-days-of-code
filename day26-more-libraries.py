# ---------------------------------- Example 01 ---------------------------------------
import os, time  # import OS and time module

print("Welcome")
print("to")
print("Replit")  # Print the first 3 lines

time.sleep(1)  # generates an erase after "1" second
os.system("clear")  # Instantly calls the operating system's "clear" command,
# which is used to clear the terminal screen
username = input("Username: ")
# Print "Username" after clearing everything in the terminal


# ---------------------------------- Exercise 01 ---------------------------------------
from replit import audio
import os, time

print(" 🎶 MyPOD Music Player 🎶\n")

print("Press 1 to play")
time.sleep(2)
print("Press 2 to exit")
time.sleep(2)
print("Press anything else to see the menu again")
time.sleep(2)
os.system("clear")


def play():
    source = audio.play_file("audio.wav")
    source.paused = False


while True:
    player = input("Select an option > ")
    if player == "1":
        play()
        print("Listen to this")
        time.sleep(10)
    elif player == "2":
        break
    else:
        player = input("Select an option > ")
        continue
