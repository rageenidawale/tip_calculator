print("Welcome to the tip calculator!")

total_bill = input("What was the total bill? $")
bill_as_float = float(total_bill)

tip_percentage = input("What percentage tip would you like to give? 10, 12 or 15? ")
tip_as_int = int(tip_percentage)

add_tip_percentage = (bill_as_float * (tip_as_int / 100))

final_bill = bill_as_float + add_tip_percentage

no_of_people = input("How many people to split the bill? ")
people_as_int = int(no_of_people)

contri = (round(final_bill / people_as_int, 2))

print(f"Each person should pay: ${contri}")
