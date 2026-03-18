def simple_interest():
    p = float(input("Enter P: "))
    r = float(input("Enter R: "))
    t = float(input("Enter T: "))
    return (p * r * t) / 100

print("Simple Interest:", simple_interest())