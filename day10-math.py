print("Tip Calculator")
print()
spend = float(input("How much did you spend? $"))
tip = int(input("What percentage do you what to tip? %"))
people = int(input("How many people in your group? "))
# It must be solved step by step according to the requested function.
perctip = tip / 100
totaltip = perctip * spend
totalspend = totaltip + spend
totalpeople = totalspend / people
totalpeople = round(totalpeople, 2)
print("You each owe $", totalpeople)
