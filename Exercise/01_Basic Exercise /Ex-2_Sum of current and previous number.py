n = int(input())
pre = 0
for i in range(11):
    print(f"Current Number {i} Previous Number  {pre}  Sum:  {i+pre}")
    pre = i
