n = int(input())
i = j = 0
while i < 3:
    while j < 3:
        p = (n + i) * (n + j)
        print((n + i), " * ", (n + j), " = ", end = " ")
        t = p
        s = 0
        while t != 0:
            t = t.__divmod__(10)
            s += t[1]
            t = t[0]

        if s == 6:
            print(":=)", end = "  ")
        else:
            print(p, end = "   ")
        j += 1
    print()
    i += 1
    j = 0





