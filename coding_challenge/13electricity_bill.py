units = int(input("Enter units: "))

bill = (
    min(units, 100) * 1.5 +
    max(min(units - 100, 100), 0) * 2.5 +
    max(units - 200, 0) * 4
)

print("Total bill amount:", bill)