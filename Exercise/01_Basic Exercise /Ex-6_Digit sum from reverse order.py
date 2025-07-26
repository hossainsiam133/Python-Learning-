num = "7536"
n = len(num)
sum = 0
for i in range(n - 1, -1, -1):
    nums = int(num[i])
    print(nums, end=" ")
    sum += nums

print()
print(sum)
