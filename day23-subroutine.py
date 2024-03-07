# A subroutine is defined by: def variable():
def rollDice():
    import random

    dice = random.randint(1, 6)
    print("You rolled", dice)


for i in range(10):
    # Note that when you call the subroutine, you need to ensure you do NOT indent.
    rollDice()


def MyName():
    print("My Name is David")


MyName()
