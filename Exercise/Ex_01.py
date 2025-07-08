x = int(input("Enter the 1st INT Number: "))
y = int(input("Enter the 2nd INT Number: "))
print(
    """Press: 
      1 for Addition
      2 for Substraction
      3 for Multiplication
      4 for Division
      5 for Mod
      6 for XOR"""
)
op = int(input("Enter the Operation Number: "))
if op == 1:
    print(f"Addition of {x} and {y} is: {x+y}")
elif op == 2:
    print(f"Substraction of {x} and {y} is: {x-y}")
elif op == 3:
    print(f"Multiplication of {x} and {y} is: {x*y}")
elif op == 4:
    print(f"Division of {x} and {y} is: {x/y}")
elif op == 5:
    print(f"Mod of {x} and {y} is: {x%y}")
else:
    print(f"XOR of {x} and {y} is: {x ^ y}")
