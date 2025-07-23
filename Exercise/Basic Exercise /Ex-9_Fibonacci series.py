list = [0, 1]
for i in range(2, 15 + 1, 1):
    list.append(list[i - 1] + list[i - 2])

for i in range(0, 15 + 1):
    print(list[i], end=" ")
