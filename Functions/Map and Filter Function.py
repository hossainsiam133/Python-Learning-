#  Iterable Obj <= map (function,iterable obj)
def square(x):
    return x * x


a = [1, 3, 5, 7]
sq_a = list(map(square, a))
print(sq_a)

b = [1, 2, 3, 4, 5, 6, 7, 8]
odd_b = list(filter(lambda x: x % 2 != 0, b))
print(odd_b)

