from fractions import Fraction
from decimal import Decimal
from math import *

# decimal and fraction

"""def multiplier(x, y, type):
     return type(x) * type(y)


print(multiplier("1 / 6", "2 / 3", Fraction))
print(multiplier("1.2", "3.4", float))
print(multiplier("1.2", "3.4", Decimal))"""

"""def fact(n):
    res = 1
    for i in range(1, n + 1):
        res *= i
    return res


def esum(N, one):
    res = one
    #res, fact = one, 1
    for i in range(1, N + 1):
        #fact = i * N
        res += one / fact(i)
    return res


decimal.getcontext().prec = 100
print(esum(10, Decimal(1)) )
print(esum(1000, Decimal(1)))
print(esum(13, Decimal(1)))
print(esum(13, 1))"""


# string

"""surname, name, otchecstvo, year, city = input().split()
print(", ".join((city, name, surname))) """


# graphic

"""a, b = -4, 4
for i in range(20):
    x = a + (b - a) * i / 19
    y = sin(x)
    spc = round((1 + y) * 20)
    print(spc * " ", "*")
"""

"""def scale(a, b, A, B, x):
    return A + (x - a) / (b - a) * (B - A)


A, B = -4, 4
for i in range(20):
    x = scale(0, 19, A, B, i)
    y = sin(x)
    spc = round(scale(-1, 1, 0, 40, y))
    print(spc * " ", "*")"""

"""screen = [ ['.', '.', '.', '.'], ['.', '.', '.', '.'], ['.', '.', '.', '.'] ]
# print("\n".join( ["".join(s) for s in screen ]))

w = 60
h = 20
screen = [['.'] * w for i in range(h)]
# print("\n".join( ["".join(s) for s in screen ]))

for i in range(5):
    screen[i][i + 10] = "@"

print("\n".join( ["".join(s) for s in screen ]))"""

# not lazy graphic

"""def scale(a, b, A, B, x):
    return A + (x - a) / (b - a) * (B - A)


A, B = -4, 4
w = 60
h = 20
screen = [['.'] * w for i in range(h)]
for i in range(w):
    x = scale(0, w - 1, A, B, i)
    y = sin(x)
    spc = round(scale(-1, 1, 0, h - 1, y))
    screen[spc][i] = "@"

print("\n".join(["".join(s) for s in screen]))
"""

# format string

"""a, b = 123, 123.456
print(f"{a + b / 2}")
print(f"{a + b = }")
print(f"{a: b}")
print(f"{a: o}")
print(f"{a:^10}")
print(f"{a:>10}")
print(f"{b:9.9}")
print(f"{b:9.11}")"""

for i in range(12, 23 + 1):
    sx = f"0x{i:x}"
    sb = f"0b{i:b}"
    # print(f"{sb}", f"= {sx}")
    if len(sx) > 3:
        print(f"{sb}"," =",  f" {sx}")
    else:
        print(f"{sb}", " =  ",  f" {sx}")