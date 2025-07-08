x = int(input("Enter the Number: "))

match x:
    case 0:
        print("Zero")
    case 1:
        print("One")
    case 2:
        print("Two")
    case _ if x % 2 == 0:
        print("Even numbers > 2")
    case _:
        print("Odd numbers > 2")
