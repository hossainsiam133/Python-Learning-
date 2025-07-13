Employee = {"Name": "Siam", "ID": 23100084, "Dept": "CSE", "Batch": 26}

keys = Employee.keys()
Employee.update({"Name": "Hossain", "Location": "N.Ganj"})
values = Employee.values()

print(type(keys), keys)
print(type(values), values)

# Nested Dictionaries
students = {
    "1": {"Name": "Siam", "ID": 84, "Dept": "CSE"},
    "2": {"Name": "Talha", "ID": 69, "Dept": "CSE"},
    "3": {"Name": "Asif", "ID": 61, "Dept": "CSE"},
}
print(type(students["1"]), students["1"])
print(type(students["1"]["Name"]), students["1"]["Name"])

for key, value in students.items():
    print(key + ":")
    for i, j in value.items():
        print(i, j)
    print()
