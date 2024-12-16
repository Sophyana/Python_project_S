while s := input():
    res = s.encode('latin1', errors = "replace").decode('cp1251')
    print(res)


import sys
exec(sys.stdin.read())