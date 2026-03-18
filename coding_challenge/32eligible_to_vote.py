age = int(input("Enter age: "))
match age >= 18:
    case True:
        print("Eligible")
    case _:
        print("Not Eligible")