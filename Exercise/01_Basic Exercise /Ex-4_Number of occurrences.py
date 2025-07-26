from collections import Counter

a = [2, 1, 3, 2, 1, 1, 3, 2, 3]
count = Counter(a)
# print(type(count))
for x in count:
    print(x, count[x])
# print(count[1])

# b = [1, 5, 3, 3, 1, 3, 5]
# cnt = {}
# print(type(cnt))
# for x in b:
#     if x not in cnt:
#         cnt[x] = 1
#     else:
#         cnt[x] += 1

# for a, b in cnt.items():
#     print(a, b)
