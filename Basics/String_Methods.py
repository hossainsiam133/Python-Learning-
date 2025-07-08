## Updating a String
s1 = "Hello Siam"
print(s1)
s2 = "H" + s1[1:]
print(s2.replace("Siam", "Siam Hossain"))

## Common String Methods
s = "MD. Siam Hossain"
print(len(s))

s = "MD. Siam Hossain"
print(s.upper())
print(s.lower())

s = "      __Siam 	Hossain_		"
print(s.strip())

s = "CSE "
print(s * 5)

Name = "Siam"
Age = 22
s = "My Name is {} and I am {} years old".format(Name, Age)
print(s)

s = "Python"
print("Py" in s)
print("thons" in s)

s = "!!!Siam!!!"
print(s.rstrip("!"))

