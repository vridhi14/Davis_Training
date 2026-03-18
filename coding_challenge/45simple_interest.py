data = {
    "p": float(input("Enter P: ")),
    "r": float(input("Enter R: ")),
    "t": float(input("Enter T: "))
}

print("Simple Interest:", (data["p"] * data["r"] * data["t"]) / 100)