print("100 Days of Code QUIZ")
print()
print input("How many can you answer correctly? ") # first error
ans1 = ("What language are we writing in? ")
if ans1 == "python":
  print("Correct")
else:
  print("Nope 🙈") # second error 
ans2 = input("Which lesson number is this? ")
if ans2>12: # third error
print("We're not quite that far yet")
else:
  print("We've gone well past that!")
elif(ans2==12):
  print("That's right!")