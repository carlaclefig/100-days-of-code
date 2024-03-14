# In a subroutine, the () are for the argument (FYI argument is another word for parameter). These are the pieces of information we pass to the code. These can be variable names that are made up for the first time within the argument ().
def which_cake(ingredient):
    if ingredient == "chocolate":
        print("Mmm, chocolate cake is amazing")
    elif ingredient == "broccoli":
        print("You what mate?!")
    else:
        print("Yeah, that's great I suppose...")


which_cake("chocolate")
