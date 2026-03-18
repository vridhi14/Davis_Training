units = int(input("Enter units: "))
bill = 0
i = 1

while i <= units:
    if i <= 100:
        bill += 1.5
    elif i <= 200:
        bill += 2.5
    else:
        bill += 4
    i += 1

print("Total bill amount:", bill)