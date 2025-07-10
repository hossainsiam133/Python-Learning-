def nline():
    print(f"\n", end="")


def show(arr):
    for it in arr:
        print(it, end=" ")
    nline()


a = [4, 1, 3, 2]
show(a)

a.append(5)
show(a)

a.insert(2, 6)
a.insert(6, 6)
show(a)

a.remove(6)
show(a)

a.pop()
show(a)

# a.sort() sort all of the elements
a[0:3] = sorted(a[0:3])
show(a)
a[0:3] = sorted(a[0:3], reverse=True)
print(a)

a.reverse()
show(a)

print(len(a))

# List Slicing
# print(a[:4])
# print(a[-4:-1])
# print(a[1:])

# List Comprehension
squares = [x * x for x in range(5)]
print(squares)
