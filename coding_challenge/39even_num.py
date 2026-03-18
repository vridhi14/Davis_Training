n = int(input("Enter N: "))

evens = {i for i in range(1, n+1) if i % 2 == 0}
print("Even numbers:", sorted(evens))