for i in range(10):
    if i == 5:
        break
    print(i)

print(f"\n")
for i in range(10):
    if i%2 == 0:
        continue
    print(i)