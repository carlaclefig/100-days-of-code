from getpass import getpass as input

print("E P I C    🪨  📄 ✂️    B A T T L")
print()
print("Select your move (R, P or S)")
print("🪨   Rock: R")
print("📄   Paper: P")
print("✂️   Scissors: S")
print()
player1 = input("Player 1 > ")
player2 = input("Player 2 > ")
if player1 == "R" or player1 == "r":
    if player2 == "R" or player2 == "r":
        print("You both picked Rock, again!")
    elif player2 == "S" or player2 == "s":
        print("Player1 smashed Player2's Scissors into dust with their Rock!")
    elif player2 == "P" or player2 == "p":
        print("Player1's Rock is smothered by Player2's Paper!")
    else:
        print("Invalid Move Player 2!")
elif player1 == "P" or player1 == "p":
    if player2 == "R" or player2 == "r":
        print("Player2's Rock is smothered by Player1's Paper!")
    elif player2 == "S" or player2 == "s":
        print("Player1's Paper is cut into tiny pieces by Player2's Scissors!")
    elif player2 == "P" or player2 == "p":
        print("Two bits of paper flap at each other. Dissapointing, again!")
    else:
        print("Invalid Move Player 2!")
