print("Welcome to the tip calculator.")
total = input("What was the total bill? $")
tip = input("What percentage tip would you like to give? 10, 12, or 15? ")
num_people = input("how many people to split the bill? ")
percent_tip = int(tip) / 100
tip_amount = float(total) * percent_tip
total_with_tip = float(total) + tip_amount
amt_per_person = round(total_with_tip/int(num_people), 2)
print(f"Each person should pay: ${amt_per_person}")