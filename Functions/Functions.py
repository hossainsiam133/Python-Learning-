import math


def add(a, b):
    return a + b


def multiplication(a, b):
    return a * b


def substraction(a, b):
    ans = a - b
    pass
    ans += 1
    return ans


def root(a, b, c):
    discriminant = (b * b) - (4 * a * c)
    if discriminant < 0:
        return -1
    discriminant = math.sqrt(discriminant)
    x1 = (-b + discriminant) / (2 * a)
    x2 = (-b - discriminant) / (2 * a)
    return x1, x2


a = 2
b = 5
c = 3
print(f"Summation of {a} + {b} is:", add(a, b))
print(f"Root x1, x2, for {a}, {b}, {c} is:", root(a, b, c))
print(f"Multiplication of {b} and {c} is:", multiplication(b, c))
print(f"Substraction of {b} and {c} is:", substraction(b, c))
