# Taxable   Income	    Rate (in %)
# First     $10,000	    0
# Next      $10,000	    10
# The remaining	        20
case = int(input())
for case in range(case):
    income = int(input())
    print(f"Case-{case+1}_", end="")
    if income <= 10000:
        print(f"Income Tax is for {income}: 0$")
    elif income > 10000 and income <= 20000:
        print(f"Income Tax is for {income}: {income * 10 / 100}$")
    else:
        print(f"Income Tax is for {income}: {income * 20 / 100}$")
