# Write a python program to translate a message into secret code language. Use the rules below to translate normal English into secret code language

# Coding:
# if the word contains atleast 3 characters, remove the first letter and append it at the end
#   now append three random characters at the starting and the end
# else:
#   simply reverse the string

# Decoding:
# if the word contains less than 3 characters, reverse it
# else:
#   remove 3 random characters from start and end. Now remove the last letter and append it to the beginning

# Your program should ask whether you want to code or decode

s = input()
if len(s) <= 2:
    op = int(input("Enter 1 for Code and 2 for Decode: "))
    print(s[::-1])
else:
    op = int(input("Enter 1 for Code and 2 for Decode: "))
    match op:
        case 1:
            print("axz" + s[1:] + s[0] + "yah")
        case 2:
            s = s[3:-3]
            print(s)
            s = s[len(s) - 1] + s[:-1]
            print(s)
            print(s)
