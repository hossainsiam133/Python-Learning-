import re

s = r"fruit"
d = r"Apple is a fruit and it is good source of Vitamin C"
if re.match(s, d):
    print("Matched")
else:
    print("Mismatched")

print(re.findall("it", d))

match = re.search(s, d)
if match:
    print(match.start())
    print(match.end())
    print(match.span())