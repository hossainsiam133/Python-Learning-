## Create a python program capable of greeting you with
# Good Morning, Good Afternoon and Good Evening.
# Your program should use time module to get the current hour.

import time

timestamp = time.strftime("%H:%M:%S")
print(timestamp)
hrs = int(time.strftime("%H"))
min = time.strftime("%M")
sec = time.strftime("%S")
# print(hrs)
# print(min)
# print(sec)
if hrs >= 0 and hrs < 12:
    print(f"Good Morning its {12-hrs}:{min}:{sec} AM")
elif hrs == 12:
    print(f"Good Noon its {hrs}:{min}:{sec} PM")
elif hrs > 12 and hrs < 17:
    print(f"Good Noon its {hrs - 12}:{min}:{sec} PM")
else:
    print(f"Good Night its {hrs - 12}:{min}:{sec} PM")
