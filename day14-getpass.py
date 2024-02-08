from getpass import getpass as input

print("E P I C 🪨 📄 ✂️ B A T T L")
print()
print("Select your move (R, P or S)")
print("🪨 Rock: R")
print("📄 Paper: P")
print("✂️ Scissors: S")
print()
player1 = input("Player 1 > ")
player2 = input("Player 2 > ")
if player1 == "R" and player1 == "r":
    if player2 == "R" and player2 == "r":
        print("They both chose Rock, again")
    elif player2 == "P" and player2 == "p":
        print("¡La piedra del jugador 1 supera el papel del jugador 2!")
