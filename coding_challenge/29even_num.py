n = int(input("Enter N: "))

evens = list(filter(lambda x: x % 2 == 0, range(1, n + 1)))

print("Even numbers:", evens)
