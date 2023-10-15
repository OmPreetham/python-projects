#If the bill was $150.00, split between 5 people, with 12% tip.
print("Welcome to the tip calculator! ")
amount = float(input("What was the total bill? "))
tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))

calculate_tip = amount * (tip / 100)
total = (amount + calculate_tip) / people
print(f"Each person should pay: ${format(total, '.2f')}")