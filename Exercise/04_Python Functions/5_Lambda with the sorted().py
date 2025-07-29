def func(a):
    return a[1]


# Approach 1 ->
data = [("apple", 5), ("banana", 2), ("cherry", 8), ("date", 1)]
# data2 = sorted(data, key=lambda x: x[1])
# print(data2)

# Approach 2 ->
data.sort(key=func)
print(data)
