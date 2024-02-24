counter = 0
while counter < 8:
    print(counter)
    counter += 1

# for new variable in range (number of values):
# new variable: crea una nueva variable
# number of values: crea una lista de números
for i in range(5):
    print(i)

# The total variable starts at 0.
# For the new variable number in the range of 100.
# The total will be added from 0 to 99
total = 0
for number in range(10):
    total += number
    print(total)

for days in range(7):
    print("Day", days + 1)


print("Loan Calculator\n")
print("$1000 over 10 years at 5% APR\n")
total = 1000
apr = 0.05
int_pain = 0
for i in range(10):
    int = total * apr
    total += int
    int_pain += int
    print("Year", i + 1, "is", round(total, 2))
print()
print("You paid $", round(int_pain, 2), "in interest!")
