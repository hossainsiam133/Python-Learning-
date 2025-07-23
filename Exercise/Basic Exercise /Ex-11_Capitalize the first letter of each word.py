def Capita(s):
    words = s.split()
    words = [word.capitalize() for word in words]
    return words

s = "I love my country"
print(Capita(s))