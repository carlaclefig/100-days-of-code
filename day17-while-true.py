while True:
    print("You are in a corridor, do you go left or right?")
    direction = input("> ")
    if direction == "left":
        print("You have fallen to your death.")
        break
    elif direction == "right":
        continue
    else:
        print("Ahh! You're a genius, you've won")
        exit()
print("The game is over, you've failed!")


print(" M O R E   E P I C 🪨  📄  ✂️  B A T T L E")
print()
print("🪨   Rock: R")
print("📄   Paper: P")
print("✂️   Scissors: S")
counter = 1
while True:
    print("Round", counter)
    print("Select your move (R, P or S)")
    player1 = input("Player 1 > ")
    player2 = input("Player 2 > ")
    if (
        player1 == "R"
        and player2 == "S"
        or player1 == "S"
        and player2 == "P"
        or player1 == "P"
        and player2 == "R"
    ):
        print("Player 1's wins with his", player1, "against Player 2 whit his", player2)
    elif (
        player2 == "R"
        and player1 == "S"
        or player2 == "S"
        and player1 == "P"
        or player2 == "P"
        and player1 == "R"
    ):
        print("Player 2's wins with his", player2, "against Player 1 whit his", player1)
        continue
    else:
        print("oh, there was a tie.")
        counter += 1
        exit()
    print("Player1 wins with", counter, "victories")
