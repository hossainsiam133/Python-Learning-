import json

info = '{"Name": "Siam","Age":23,"City":"Narayanganj"}'
x = json.loads(info)
print(type(x), x["Name"])
