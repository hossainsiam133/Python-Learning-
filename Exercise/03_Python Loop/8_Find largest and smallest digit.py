n = int(input())
mx = -1
mn = 1e3 + 123
while n > 0:
    mod = n % 10
    mx = max(mx, mod)
    mn = min(mn, mod)
    n //= 10
print(f"Max: {mx} and Min: {mn}")
