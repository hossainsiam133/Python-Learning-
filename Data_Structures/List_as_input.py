li = input()
li = li.split()
li = [int(x) for x in li]

sum = 0
for i in range(len(li)):
    sum += li[i]

print(sum)
