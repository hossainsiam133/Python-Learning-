nline = f"\n"
s = "Siam"
for ch in s:
    print(ch)
    if ch == "m":
        print("Hossain" + nline)

## Using Range Function
# One Parameter
for i in range(5):
    print(i)
print(nline)

# Two Parameters
even = 0
odd = 0
for i in range(1, 6):
    print(i)
    if i % 2:
        odd += 1
    else:
        even += 1
print(f"Number of Even: {even} and Odd: {odd}" + nline)

# Three Parameters
for i in range(0, 10, 2):
    print(i)
