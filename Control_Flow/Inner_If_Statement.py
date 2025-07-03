num1 = int(input("Num1: "))
num2 = int(input("Num2: "))
num3 = int(input("Num3: "))

if num1 > num2:
    if num1 > num3:
        print(num1)
    else:
        print(num3)
elif num1 < num2:
    if num3 < num2:
        print(num2)
    else:
        print(num3)
