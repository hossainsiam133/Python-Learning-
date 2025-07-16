## ✅ Basic Syntax
# try:
#     # risky code
# except SomeError:
# handle the error

### Example 1: Division by Zero

try:
    x = 10 / 0
except ZeroDivisionError:
    print("You can't divide by zero!")


## Full Structure
# try:
#     # code that might throw an error
# except ErrorType1:
#     # handle ErrorType1
# except ErrorType2:
#     # handle ErrorType2
# else:
#     # runs if no exception occurs
# finally:
# always runs (even if there is an error)


## Example 2: With `else` and `finally`

try:
    num = int(input("Enter a number: "))
    print("Success!")
except ValueError:
    print("That's not a number!")
else:
    print("You entered:", num)
finally:
    print("Done checking.")

## Common Exception Types

# | Exception           | Raised When...                       |
# | ------------------- | ------------------------------------ |
# | `ZeroDivisionError` | You divide by 0                      |
# | `ValueError`        | Wrong value (e.g., `int("abc")`)     |
# | `TypeError`         | Incompatible types (e.g., `"1" + 2`) |
# | `IndexError`        | Index out of range in a list         |
# | `KeyError`          | Key not found in dictionary          |
# | `FileNotFoundError` | File doesn't exist                   |
# | `NameError`         | Variable not defined                 |


## Example: Catching Multiple Exceptions

try:
    a = int("hello")
    b = 1 / 0
except ValueError:
    print("Invalid value!")
except ZeroDivisionError:
    print("Can't divide by zero!")


## Catching All Exceptions (Not Recommended)
# try:
#     # risky code
# except Exception as e:
#     print("Error:", e)

## Raising Your Own Exceptions


def set_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative!")
    print("Age is", age)


##  Summary

# | Block     | Purpose                        |
# | --------- | ------------------------------ |
# | `try`     | Code that might cause an error |
# | `except`  | Handles the error              |
# | `else`    | Runs if no error occurs        |
# | `finally` | Runs no matter what            |
