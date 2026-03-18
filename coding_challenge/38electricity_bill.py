units = int(input("Enter units: "))
bill = 0

if units > 200:
    bill += (units - 200) * 4
    units = 200

if units > 100:
    bill += (units - 100) * 2.5
    units = 100

bill += units * 1.5

print("Total bill amount:", bill)