price = float(input("Enter price: "))
discount = float(input("Enter discount percentage: "))

reduction = discount / 100
price *= (1 - reduction)

print("Final price after discount:", price)