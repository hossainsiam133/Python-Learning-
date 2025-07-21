file = open(
    "/home/siam-hossain/Documents/Python-Learning-/File Handling/student.txt", "r"
)
# for line in file:
#     print(line)
print(file.readable())

text1 = file.read()
file.seek(0)

text2 = file.readline()
file.seek(0)

text3 = file.readlines()
file.seek(0)

print(f"Whole String:\n" + text1)
print(f"\nFirst Line:\n" + text2)
print(f"Whole string in File as List:")
print(text3)


file.close()

