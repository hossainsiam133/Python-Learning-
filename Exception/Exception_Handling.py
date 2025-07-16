# try:
#     a = int(input())
#     b = int(input())

#     div = a / b
#     print(a / b)
# except Exception as e:
#     print(e)
# else:
#     print("No Error")
# finally:
#     print("Done Checking")

# try:
#     age = 18
#     if age <= 0:
#         raise ValueError("Age cannot be below 0")
#     print(age)
# except Exception as e:
#     print(e)

try:
    b = 1 / 0
    a = int("Siam")

except ZeroDivisionError:
    print("Invalid x/0")
except ValueError:
    print("Invalid Value")
