def nline():
    print(f"\n", end="")


def show(a):
    for i in a:
        print(i)
    nline()


numbers = [1, 2, 3, 4, 5]
fruits = ["Mange", "Apple", "Guava", "Cherry"]
mixed = [1, "Hello", 3.14, True]

print(numbers)
show(fruits)
show(mixed)

print(mixed[0])
print(fruits[-1])
nline()
