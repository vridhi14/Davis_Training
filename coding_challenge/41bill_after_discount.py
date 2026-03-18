price = float(input("Enter price: "))
discount = float(input("Enter discount percentage: "))
final_price = eval(f"{price} - ({price}*{discount}/100)")
print("Final price after discount:", final_price)