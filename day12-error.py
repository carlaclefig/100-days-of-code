print("100 Days of Code QUIZ")
print()
print ("How many can you answer correctly? ") # first error
ans1 = input("What language are we writing in? ") # second error 
if ans1 == "python":
  print("Correct")
else:
  print("Nope 🙈") # third error 
ans2 = input("Which lesson number is this? ")
if ans2 > 12: 
print("We're not quite that far yet")
else:
  print("We've gone well past that!")
elif(ans2==12):
  print("That's right!")