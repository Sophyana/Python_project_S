def igor(a):
    for k in range(len(a)):
        for i in range(len(a) - 1):
            if a[i][1] >= a[i + 1][1]:
                a[i], a[i + 1] = a[i + 1], a[i]
    return a


a = [x for x in eval(input())]
c = []
for i in range(len(a)):
    c.append([a[i], a[i] ** 2 % 100])


c = igor(c)
"""print(c)"""


i = 0
while i < len(c):
    for j in range(len(a)):
        if c[i][0] == a[j]:
            print(a[j], end = " ")
            i += 1
            if i == len(c): break

