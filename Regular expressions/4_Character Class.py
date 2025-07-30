import re

pattern = r"[aeiou]"

if re.match(pattern, "ant"):  # start any ch (a) from pattern in ant
    print("Matched")
else:
    print("Mismatch")
