#utilzing maths

print("Tip Calculator")

myBill = float(input("What was the bill?: "))
tip = float(input("What percentage do you want to tip?: "))
actual_bill = myBill + (myBill * (tip/100))
numberOfPeople = int(input("How many people?: "))
answer = actual_bill / numberOfPeople
answer = round(answer, 2)
print("You all owe", answer)