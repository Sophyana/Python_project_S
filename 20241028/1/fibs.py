def fib(m, n):
    ls = [1]
    a = 0
    b = 1
    for i in range(1, m + n):
        ls.append(a + b)
        a = b
        b = ls[-1]

    return ls[m: (m + n)]


import sys
exec(sys.stdin.read())

"""m = 4
n = 5
l = fib(m, n)
print(l)
print(l[m: (m + n)])"""

