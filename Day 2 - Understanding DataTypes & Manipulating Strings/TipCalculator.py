print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))

amount = round(( bill + (bill*(tip/100)) ) / people,2)
#instead of explicity converting a data type for printing, we can use fstring
print(f"Each person should pay: ${amount}")

