print("Welcome to the Tip Calculator!")
bill = int(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))
tip_as_percent = tip / 100
total_tip_amount = bill * tip_as_percent
total_amount = bill + total_tip_amount
print(f"Each person should pay: ${total_amount / people:.2f}")
