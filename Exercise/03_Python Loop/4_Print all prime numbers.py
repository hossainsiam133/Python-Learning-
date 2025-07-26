n = int(input())

for i in range(2, n + 1):
    for j in range(2, i):
        print(i, j) if i == 2 else 0
        if i % j == 0:
            break
    else:
        print(i)
