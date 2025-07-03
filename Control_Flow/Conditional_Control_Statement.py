mark = int(input("Mark: "))

if mark >= 33 and mark <= 40:
    print("D")
elif mark >= 41 and mark <= 79:
    print("B")
elif mark >= 80 and mark <= 100:
    print("A+")
else:
    print("Failed")
