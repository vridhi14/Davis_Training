age = int(input("Enter age: "))
print(["Not Eligible", "Eligible"][min(age//18, 1)])