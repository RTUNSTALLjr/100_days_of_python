print("Welcome to the tip calculator.")
bill = float(input("What was the total bill ? "))
tip_percent = int(input("What percentage tip would you like to give ? "))
people = int(input("How many people to split the bill ? "))

tip = tip_percent / 100 * bill
total = bill + tip
per_person = total / people


print(f"Each person should pay: ${round(per_person,2)} ")