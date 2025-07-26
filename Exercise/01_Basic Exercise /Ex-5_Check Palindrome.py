a = input()
n = len(a)
flag = True
for i in range(0, n // 2, 1):
    if a[i] != a[n - 1 - i]:
        flag = False
        break
if flag == True:
    print(f"{a} is a palindrome string")
else:
    print("Not a palindrome")

