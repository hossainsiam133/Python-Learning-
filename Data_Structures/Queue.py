from collections import deque

stu = deque(["Munsur", "Sahil", "Soyad"])
stu.popleft()
print(stu)
stu.appendleft("Rehan")
print(stu)