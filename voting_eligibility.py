age = int(input("Enter your age: "))
if age >= 18:
    print("You are eligible to vote.")
else:
    print("Not eligible. Come back in", 18 - age, "year(s).")