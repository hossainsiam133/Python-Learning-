# Positional Arguments
def greet(name, age):
    print(f"Hello {name}, you are {age} years old")


greet("Siam", 22)
greet(22, "Siam")
print(f"\n")

# Keyword Arguments
greet(age=22, name="Hossain")
print(f"\n")


# Default Arguments
def welcome(name, age=18):
    print(f"Welcome {name}, you are {age} years old")


welcome("Sufian")  # Uses default age = 18
welcome("Siam", 22)  # Overrides default
print(f"\n")


# Variable-Length Arguments (multiple positional arguments)
def average(*num):
    sum = 0
    for i in num:
        sum += i
    avg = sum / len(num)
    return avg


print(average(1, 2, 3, 4, 5))
print(f"\n")


# Variable-Length Arguments (multiple keyword arguments)
def Name(**name):
    print("Hello!", name["fname"], name["mname"], name["lname"])


Name(fname="MD", mname="Siam", lname="Hossain")
print(f"\n")


def show_info(**info):
    for key, value in info.items():
        print(f"{key}: {value}")


show_info(Name="Siam", Age=22, City="Narayanganj")
