# A subroutine is defined by: def variable():
def rollDice():
    import random

    dice = random.randint(1, 6)
    print("You rolled", dice)


# Note that when you call the subroutine, you need to ensure you do NOT indent.
rollDice()
