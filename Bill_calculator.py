
Bill = input("Enter the bill amount: ")
numberOfPeople = int(input("No of peoples: "))
tip = float(input("percentage of tip: "))
Btip = 1 + tip/100

billNum = int(Bill)
calculate = (billNum / numberOfPeople) * Btip
TotalBill = round(calculate)

print(f"Each person should pay {TotalBill}")
#used to calculate tips
