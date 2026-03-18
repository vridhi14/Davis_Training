from functools import reduce

p = float(input("Enter P: "))
r = float(input("Enter R: "))
t = float(input("Enter T: "))

si = reduce(lambda x, y: x*y, [p, r, t]) / 100

print("Simple Interest:", si)