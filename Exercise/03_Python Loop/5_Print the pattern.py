n = 10
for i in range(1, n + 1):
    cnt = i % n
    if i > n // 2:
        cnt = n % i
    for j in range(cnt):
        print("*", end=" ")
    print()
