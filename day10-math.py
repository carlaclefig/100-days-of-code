# float, identifies the decimal number that the user enters
myBill = float(input("What was the bill?:"))
# int, Identifies the integer number that the user enters.
numberPeople = int(input("How many people?:"))
answer = myBill / numberPeople
# round, shows the result only with the requested number of decimal places
answer = round(answer, 2)
print("You all owe", answer)
