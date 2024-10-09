def pareto(set):
    for para in set:
        for el in set:
            if (para[0] >= el[0] and para[1] >= el[1]) and (para[0] > el[0] or para[1] > el[1]):
                set = [_ for _ in set if el != _]
    return set


import sys
exec(sys.stdin.read())