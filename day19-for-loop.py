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
loan_with_interest = 0
for number in range(10):
    loan_with_interest += number
    print(loan_with_interest)

for days in range(7):
    print("Day", days + 1)


print(
    """
Loa Calculator

$1000 over 10 years at 5% APR
"""
)
loan_with_interest = 1000
interest_rate = 0.05
interest_per_year = 0
for i in range(10):
    interest_of_the_year = loan_with_interest * interest_rate
    loan_with_interest += interest_of_the_year
    interest_per_year += interest_of_the_year
    print("Year", i + 1, "is", round(loan_with_interest, 2))
print("\nYou paid $", round(interest_per_year, 2), "in interest!")
