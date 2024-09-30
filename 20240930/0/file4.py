a = []
while str := input():
    a.append(eval(str))

m = len(a[0])

for i in range(len(a)):
    for j in range(m // 2): # in range(i + 1, len(a)) # len(a) == len(a[0])
        a[i][j], a[j][i] = a[j][i], a[i][j]

for ln in a:
    print(*ln)