file = open(
    "/home/siam-hossain/Documents/Python-Learning-/Exercise/Input and Output Exercise/test.txt",
    "r",
)
# for i in range(8):
#     file.write(f"Line {i+1}\n")
s = file.readlines()
i = 0
for line in s:
    i += 1
    print(line) if i != 5 else -1
file.close()
