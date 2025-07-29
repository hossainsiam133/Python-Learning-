def print_info(**info):
    for key, val in info.items():
        print(key, val)
    print()


print_info(name="Alice", age=30, city="New York")
print_info(job="Engineer", salary=75000)
print_info(country="USA", state="California", zip_code="90210")
print_info()
