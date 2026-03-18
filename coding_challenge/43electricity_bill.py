units = int(input("Enter units: "))
bill = 0

while units > 0:
    if units > 200:
        bill += 4
    elif units > 100:
        bill += 2.5
    else:
        bill += 1.5
    units -= 1

print("Total bill amount:", bill)