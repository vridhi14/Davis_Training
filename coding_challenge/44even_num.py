n = int(input("Enter N: "))
for i in range(1, n+1):
    if not (i & 1):
        print(i, end=" ")