import re

pattern = r"^col..r$"  # should start with col and end with r and size == 6
pattern2 = r"a+b*"
pattern3 = r"ice(-)?cream"  # 0 or 1 times should present if use ? otherwise must use
pattern4 = r"a{1,3}$"
if re.match(pattern4, "aaa"):
    print("Matched")
else:
    print("Mismatched")
