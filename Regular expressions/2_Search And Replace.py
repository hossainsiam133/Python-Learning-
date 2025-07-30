import re

pattern = "colour"
text = "My favourite colour is Red and Hate colour blue"

print(re.sub(pattern, "color", text,count=1))
