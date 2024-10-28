"""from itertools import count


def fun_sum():
    sum = 0
    i = 1
    for i in count(1):
        sum += 1 / i ** 2
        yield sum
        i += 1
"""

# python3 -i file.py
# res = fun_sum()
# next(res)

"""gen = sum(1 / i ** 2 for i in range(1, 10000) )
print(gen)"""

"""
def biased(init):
    bias = yield init
    while bias:
        init += bias
        bias = yield init
"""
# res = g.biased(5)
# res = g.send(123)
# res
# res = g.send(0)

"""
def walk2d():
    x, y = 0, 0
    while True:
        dx, dy = yield (x, y)
        x += dx
        y += dy
        """

"""def gen(string):
    yield from string
    return len(string)


def wrap(string):
    res = yield from gen(string)
    print("Res: ", res)


for s in wrap("QWER"):
    print(s)
"""


"""def travel(n):
    for i in range(n):
        yield "по кочкам"
    return "и в яму"


def travelwrap(n):
    res = yield from travel(n)
    yield res


# for s in travel(10):
for s in travelwrap(10):
    print(s)
"""

"""from itertools import count
from itertools import dropwhile, islice


def fun_sum():
    sum = 0
    i = 1
    for i in count(1):
        sum += 1 / i ** 2
        yield sum
        i += 1


for e in islice(dropwhile(lambda x: x <= 1.6, fun_sum()), 10):
    print(e)"""

"""from itertools import filterfalse


n = eval(input())
print( list(filterfalse( lambda x: x % n, [1, 5, 4, 7, 89, 45, 12, 32, 52, 6, 7, 85, 25, 10, 23, 47, 63])))
print( list(filterfalse( lambda x: x % n, range(50))) )"""

"""from itertools import repeat


def repeater(seq, n):
    for s in seq:
       yield from repeat(s, n)

g = repeater([1, 5, 8, 2], 3)
print( *g)
"""

from itertools import *

# print( list(product("qwe", "ert", [0,1])))
# print( *list(permutations("qwer")), sep ="\n")
# print( *list(combinations("qwert", 2)), sep = "\n")
# print( *list(combinations_with_replacement("qwert", 2)), sep = "\n")


#print( *list(product("abcdefj", range(9))), sep="\n")

ls = [f"{a}{n}" for a, n in product("abcdefj", range(1, 9) )]
print(*ls, sep="\n")

