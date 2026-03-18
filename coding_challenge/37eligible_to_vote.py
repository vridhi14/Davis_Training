try:
    age = int(input("Enter age: "))
    assert age >= 18
    print("Eligible")
except:
    print("Not Eligible")