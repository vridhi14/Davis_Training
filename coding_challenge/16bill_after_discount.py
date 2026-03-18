price = float(input("Enter price: "))
discount = float(input("Enter discount percentage: "))

factor = (100 - discount) / 100
final_price = price * factor

print("Final price after discount:", final_price)