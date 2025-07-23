import math

n = int(input())
isprime = (n + 1) * [True]
isprime[0] = False
isprime[1] = False
for i in range(2, int(math.sqrt(n)) + 1):

    if isprime[i]:
        for j in range(i * 2, n + 1, i):
            isprime[j] = False

for i in range(n + 1):
    if isprime[i] == True:
        print(i)
