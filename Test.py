# In the name of ALLAH

import sys
sys.setrecursionlimit(1000000)

# Constants
mx = int(1e5) + 123
h = [0] * mx
dp = [-1] * mx

def solve(i, n):
    if i == n:
        return 0
    if dp[i] != -1:
        return dp[i]

    ret1 = int(2e9)
    ret2 = int(2e9)

    if i + 1 <= n:
        ret1 = abs(h[i] - h[i + 1]) + solve(i + 1, n)
    if i + 2 <= n:
        ret2 = abs(h[i] - h[i + 2]) + solve(i + 2, n)

    dp[i] = min(ret1, ret2)
    return dp[i]

# Input
n = int(input())
heights = list(map(int, input().split()))
for i in range(1, n + 1):
    h[i] = heights[i - 1]

# Output
print(solve(1, n))
