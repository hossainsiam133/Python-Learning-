## string
str = """Hello,
Name: Siam Hossain
ID: 23100084
Dept: CSE"""
print(str)

str1 = 'Hey,"Siam"'
str2 = 'Hey, "Siam"'
str3 = "Hey, 'Siam'"

print(str1)
print(str2)
print(str3)

str4 = "Hey, I am No One"
for ch in str4:
    print(ch, end="")
