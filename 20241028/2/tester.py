from itertools import *

n = int(input())
print(*sorted(filter(lambda s: s.count("TOR") == 2, map(''.join, product('TOR', repeat=n)))))