a, b, c = eval((input()))

if a + b > c and a + c > b and c + b > a and min(a, b, c) > 0:
    print("It`s triangle")
else:
    print("It`s not triangle")
