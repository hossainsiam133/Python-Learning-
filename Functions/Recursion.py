def factorial(n):
    if n == 0 or n == 1:
        return 1
    n = n * (factorial(n - 1))
    return n


def fibonacci(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    n = fibonacci(n - 1) + fibonacci(n - 2)
    return n


print(factorial(3))
print(fibonacci(6))