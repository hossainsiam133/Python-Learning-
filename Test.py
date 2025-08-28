from math import *

iteration = 0


def func(x0, x1):
    if x0 == x1:
        return x0
    print(x0, x1)
    global iteration
    iteration += 1
    return func(1 / sqrt(x0 + 1), x0)


root = func(0.5, -1)
value = root**3 + root**2 - 1
print(iteration, len(str(root)) - 3)
# print(root, value)
