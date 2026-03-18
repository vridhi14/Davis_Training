units = int(input("Enter units: "))
bill = sum(1.5 if i <= 100 else 2.5 if i <= 200 else 4 for i in range(1, units + 1))
print("Total bill amount:", bill)