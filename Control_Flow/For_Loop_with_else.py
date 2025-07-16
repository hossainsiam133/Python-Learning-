a = [1, 3, 5, 7]
for it in a:
    if it % 2 == 0:
        print("Even Number Found: ", it)
        break
else:
    print("No Even Number has been Found!!!")


b = {"Asif": 15, "Talha": 16, "Tanmoy": 17, "Siam": 22}

for key, val in b.items():
    if val >= 18:
        print(f"Adult Found! {key} is {val} years old")
        break
else:
    print("No Adults Found!!!")


n = 11
for num in range(2,n):
    if n%num == 0:
        print(f"{n} is not a prime number")
        break
else:
    print(f"{n} is a prime number")