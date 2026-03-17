def check_even_odd(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"


# taking input
num = int(input("Enter a number: "))

# calling function
result = check_even_odd(num)
print(result)
