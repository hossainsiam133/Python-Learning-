student = {"Name": "Asif", "Age": 21, "Dept": "CSE", "Name": "Siam"}


def show():
    for key, value in student.items():
        print(key, value)
    print()


print(student["Name"])
print(student.get("Dept"))
print(student.get("ID", "N/A"))

student["Age"] = 22
student["City"] = "Narayanganj"

show()
student.pop("Name", "")
student.popitem()
show()

del student["Dept"]
show()
student.clear()
print(type(student), student)
