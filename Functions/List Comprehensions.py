# list <= [expression for (var in expression) in iterable obj]
num = [1, 2, 3, 4, 5, 6, 7]

sq_num = [x * x for x in num]
print(sq_num)

odd_num = [x for x in num if x % 2 != 0]
print(odd_num)
