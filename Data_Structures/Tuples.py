# Creating a Tuple
tup = (1, 2, 3)
print(type(tup), tup)
mixed = (1, "Siam", 3.14)
print(type(mixed), mixed)

# Single element Tuple
tup = 1
print(type(tup), tup)
tup = (1,)
print(type(tup), tup)

# Accessing Elements
tup = (1, 2, 3, 4, 5)
print(tup[0])
print(tup[-1])

# Slicing Tuples
tup2 = tup[:-2]
print("Tup2: ", type(tup2), tup2)

# Tuple is Immutable
# tup[0] = -1
# print(tup)

# Tuple Unpacking
tup = (1, 2, 3)
a, b, c = tup
print(a, b, c)
