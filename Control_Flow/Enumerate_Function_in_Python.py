fruits = ["Apple", "Banana", "Mango", "Pine"]

# for ind, ele in enumerate(fruits):
#     print(ind, ele)

for i, x in enumerate(fruits, start=1):
    print(i, x)

print()
for i in range(len(fruits)):
    print(i,fruits[i])
