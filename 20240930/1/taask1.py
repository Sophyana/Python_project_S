m, n = eval(input())
print([x for x in range(m, n) if x != 0 and x % 2 and x % 3 and x % 5 and x % 7 or x == 3 or x == 5 or x == 7])

