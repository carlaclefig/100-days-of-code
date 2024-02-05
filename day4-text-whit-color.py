print("=== Your Adventure Simulator ===")
print(
    """You'll be asked a bunch of questions
then we'll make you up an amazing
story with YOU as the star! 🤩"""
)
name = input("Your name: ")
enemy = input("Your worst enemy's name: ")
superPower = input("Your super power: ")
print()
print("Our story begins as our hero", name, "approaches a foreboding castle...")
print("Suddenly a bolt of lightning striked the ground at the feet of", name)
print(
    "\033[35m",
    "Our final battle begins! shouts the evil",
    "\033[0m",
    enemy,
    "clearly missing the fact that",
    name,
    "has the power of",
    "\033[34m",
    superPower,
    "\033[0m",
    "which means they'll win quite easily",
)
print("Continue...")
