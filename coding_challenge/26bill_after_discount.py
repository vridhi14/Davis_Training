price = float(input("Enter price: "))
discount = float(input("Enter discount percentage: "))

temp = price * discount
final_price = price - temp / 100

print("Final price after discount:", final_price)