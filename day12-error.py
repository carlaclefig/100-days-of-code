print("100 Days of Code QUIZ")
print()
print ("How many can you answer correctly? ") # first error
ans1 = input("What language are we writing in? ") # second error 
if ans1 == "python":
  print("Correct")
else:
  print("Nope 🙈") # third error 
ans2 = int(input("Which lesson number is this? ")) # 4to error
if ans2 > 12: # 5to error
print("We're not quite that far yet")
else:
  print("We've gone well past that!")
elif ans2 == 12: # 6to error
  print("That's right!")