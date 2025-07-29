def sum(n, tot):
    if n == 0:
        return tot
    tot += n
    ans = sum(n - 1, tot)
    return ans


print(sum(10, 0))
