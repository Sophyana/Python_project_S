def poli(deg, arr, s):
    ans = 0
    for el in arr:
        ans += el * s ** deg
        deg -= 1
    return ans


line = list(map(eval, input().split(", ")))

s = line[0]
w = line[1]

deg_a = line[2]
deg_b = line[(3 + deg_a)]

degree_A = line[3:(3 + deg_a + 1)]
degree_B = line[(3 + deg_a + 2): ]


fun_a = poli(deg_a, degree_A, s)
fun_b = poli(deg_b, degree_B, s)


if fun_b != 0 and fun_a / fun_b == w:
    print(True)
else:
    print(False)

