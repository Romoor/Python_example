num = int(input("Choose number: "))
if num % 4 == 0:
    print("Yo its divis by 4")
elif num % 2 == 0:
    print("Yo its divis by 2...even boi")
elif num % 2 != 0:
    print("Yo its NOT divis by 2...odd boi")

check = int(input("Choose a diff number: "))
if check % num == 0:
    print(str(num) + " is divisible by " + str(check))
else:
    print(str(num) + " is NOT divisible by " + str(check))

flow = float(input("Winder turbine: "))
