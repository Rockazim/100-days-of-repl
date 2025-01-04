"""I've given you a CSV file called 'Day54Totals.csv' (look at your file tree) that contains multiple pieces of data in the fields 'cost' and 'quantity' of items sold. How much money did this shop earn in a day?

Your program should:

Read the CSV file in.
Multiply the cost by the quantity.
Add it all together to calculate how much money the shop made in a day."""
import csv
print("🌟Shop $$ Tracker🌟")
with open("Day54Totals.csv") as file:
    reader = csv.DictReader(file)
    total = 0
    for row in reader:
        total += float(row["Cost"]) * float(row["Quantity"])
    
    print(f"Your shop took ${round(total,2)} today")
