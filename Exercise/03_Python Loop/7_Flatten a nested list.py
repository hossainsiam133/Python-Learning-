def flatten_list(array):
    lst = []
    for it in array:
        if isinstance(it, list):
            for x in it:
                lst.append(x)
        else:
            lst.append(it)
    return lst


array = [4, 2, [3, 1], 9, 6, [8, 7], 5]

# print(type(array[1]), array[2])
flatten = flatten_list(array)
print(flatten)
