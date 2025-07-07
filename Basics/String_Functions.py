s1 = "mY name is SIAM"
s2 = "MY name is Hossain"
print(s1.capitalize())
print(s2.capitalize())

s = "Welcome to the CSE Dept. "
print(len(s))
print(s.center(50))
print(len(s.center(50)))

s = "Noting can arise from Noting except GOD"
print(s.count("Noting"))
print(s.count("e"))

s = "Welcome to the console !!!"
print(s.endswith("!!!"))
print(s.endswith("to", 4, 10))
print(s.startswith("Wel"))

s = "He's name is Siam. He is 22 years old"
print(s.find("is"))
print(s.find("ishh"))
print(s.index("is"))
## print(s.index("ishh"))

s = "HeisSiamHeis22yearsold"
print(s.isalnum())
print(s.isalpha())

s = "siam"
print(s.islower())
s = "SIAM"
print(s.isupper())

s = "Allah bless BD\n"
print(s.isprintable())
print(s[:-2].isprintable())

s = " "
print(s.isspace())

s = "World Health Organaization"
print(s.istitle())
s = s.capitalize()
print(s.istitle())

s = "mY name is SIAM"
print(s.swapcase())

s = "MY name is SIAM Hossain"
print(s.title())