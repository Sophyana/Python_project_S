"""

while s := input():
    x = eval(s)
    if x % 2 == 0:
        print(x)
"""
"""
while s := input():
    x = eval(s)
    if x == 13:
        print("13 is found")
        break
    if x % 2 == 0:
        print(x)
else:
    print("13 is not entered")
"""

while s := input():
    x = eval(s)
    match x:
        case 1:
            print("One")
        case 2:
            print("Two")
        case 3:
            print("Three")
        case val if val % 2 == 0:
            print("Chetnoe")
        case val if val % 2 != 0:
            print(val, "too munch)")