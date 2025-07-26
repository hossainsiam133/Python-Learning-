num = int(input())
cnt = 0
while num != 0:
    num //= 10
    # print(num)
    cnt += 1
print(cnt)
