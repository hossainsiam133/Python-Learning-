# Concatenation
a = (1, 2)
b = (2, 3)
c = a + b
print(type(c), c)
# Repetition
r = (1, 2)
print(r * 3)

# Membership Test
m = (2, 3, 5)
print(2 in m)
print(7 not in m)

# Iteration
tup = (1, 2, 3, 4, 5)
for it in tup:
    print(it, end=" ")
print()

# Useful Built-in Functions
tup = (1, 2, 1, 3, 2)
print(tup)
print("Length:", len(tup))
print("Max:", max(tup))
print("Min:", min(tup))
print("Count 1:", tup.count(1))
print("Index of 2 is:", tup.index(2, 0, -2))
print("Index of 2 is:", tup.index(2, 2))  # index from 2 to rest of the tupple

# Manipulate Tuple
Names = ("Siam", "Talha", "Asif", "Mehedi")
print(Names)
temp = list(Names)
temp.append("Imran")
print(temp)
temp.pop(2)
print(temp)
temp[-1] = "Alif"
print(temp)
Names = tuple(temp)
print(type(Names), Names)
