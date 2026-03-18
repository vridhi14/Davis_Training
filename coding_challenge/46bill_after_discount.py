from functools import reduce

price = float(input("Enter price: "))
discount = float(input("Enter discount percentage: "))

final_price = reduce(lambda x, y: x*y, [price, (1 - discount/100)])

print("Final price after discount:", final_price)