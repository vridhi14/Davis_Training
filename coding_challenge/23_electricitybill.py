def calculate_discount(price, discount):
    return price - (price * discount / 100)

price = float(input("Enter price: "))
discount = float(input("Enter discount percentage: "))

print("Final price after discount:", calculate_discount(price, discount))