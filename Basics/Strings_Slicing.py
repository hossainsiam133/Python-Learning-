fruit = "Pine_Apple"

print(fruit[0:4])
print(fruit[5 : len(fruit)])

print(fruit[5:])
print(fruit[:4])

print(fruit[0:-5])
print(fruit[-5:-2])
print(fruit[-2:-5])  # Invalid / Range: 8 to 4 (0 based)
print(fruit[:-5])

## fruit[x:y], here x <= y-1 must hold
## print(fruit[-2:-5]) here fruit[len(fruit)-5:-2]
## print(fruit[:-5]) here interpreter put 0 on fruit[0:-5]
