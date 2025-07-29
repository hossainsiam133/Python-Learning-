# list.sort(reverse=True|False, key=myFunc)
# reverse	Optional. reverse=True will sort the list descending. Default is reverse=False
# key	Optional. A function to specify the sorting criteria(s)


# A function that returns the length of the value:
def myFunc(e):
    return len(e)


cars = ["Ford", "Mitsubishi", "BMW", "VW"]
cars2 = sorted(cars,key=lambda x:len(x))
print(cars2)

# cars.sort(reverse=True, key=myFunc)
# print(cars)