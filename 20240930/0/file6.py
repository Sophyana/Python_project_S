a = []
while str := input():
    a.append(eval(str))

if any([len(line) != len(a) for line in a]): # allow use all via for
    print("No")
    exit()

m = len(a[0])

for i in range(len(a)):
    for j in range(m // 2): # in range(i + 1, len(a)) # len(a) == len(a[0])
        a[i][j], a[j][i] = a[j][i], a[i][j]

for ln in a:
    print(*ln)




"""
[1, 2, 3, 10]
[4, 5, 6, 12]
[7, 8, 9, 13]

"""