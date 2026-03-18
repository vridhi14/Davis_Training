n = int(input("Enter N: "))

for i in range(n + 1):
    if i % 2 != 1:
        if i != 0:
            print(i, end=" ")