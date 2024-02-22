print(" M O R E   E P I C 🪨  📄  ✂️  B A T T L E")
print()
print("🪨   Rock: R")
print("📄   Paper: P")
print("✂️   Scissors: S")
score1 = 0
score2 = 0
Round = 0
print("Select your move (R, P or S)")
while True:
    Round = Round + 1
    print("Round", Round)
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
        score1 += 1
    elif (
        player2 == "R"
        and player1 == "S"
        or player2 == "S"
        and player1 == "P"
        or player2 == "P"
        and player1 == "R"
    ):
        print("Player 2's wins with his", player2, "against Player 1 whit his", player1)
        score2 += 1
        print()
    elif (
        player2 == "R"
        and player1 == "R"
        or player2 == "S"
        and player1 == "S"
        or player2 == "P"
        and player1 == "P"
    ):
        print("Oh, there was a tie.\n")
    else:
        ("This play is invalid!")

    if score1 == 3 or score2 == 3:
        print("Player 1 has", score1, "victories")
        print("Player 2 has", score2, "victories")
        print("Thanks for playing!")
        exit()
