"""import timeit
print( timeit.Timer(input()).autorange())"""

"""import string
import timeit
from string import ascii_lowercase


def func():
    str = "qwertyuiopjffhbjfbvugfkfwgeifdfdbfhvSDifwoarur"
    # glas = ['a', 'e', 'i', 'o', 'u', 'y']
    # sogl = ['b', 'c', 'd', 'f', 'g', 'h',
    #         'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r',
    #         's', 't', 'v', 'w', 'x', 'z']

    glas = set("aeiouy")
    sogl = set(string.ascii_lowercase)
    sogl -= glas
    G = {i.lower() for i in str if i in glas}
    S = {i.lower() for i in str if i in sogl}

    # print(len(G))
    # print(len(S))
    return (len(G), len(S))


print(timeit.Timer(func).autorange())"""

"""st = {"word":0}

while str := input():
    for w in str.split():
        for key, val in st.items():
            if key == w:
                val += 1
        else:
            st |= {key:0}"""

"""
cnt = {}
text = "wert ujhugr dhrh rgetw qeqr wert rge wrgetat wert"

for word in text.split():
    cnt[word] = cnt.get(word, 0) + 1

print(cnt)


from collections import Counter
from timeit import Timer


C = Counter(text.split())
print(C)


def func_cnt():
    cnt = {}
    text = "wert ujhugr dhrh rgetw qeqr wert rge wrgetat wert"

    for word in text.split():
        cnt[word] = cnt.get(word, 0) + 1

    return cnt


def func_Cou():
    C = Counter(text.split())
    return C


print(Timer(func_cnt).autorange())
print(Timer(func_Cou).autorange())
"""
"""
wert ujhugr dhrh rgetw qeqr wert rge wrgetat wert
"""


"""
wert pi rty wert rer wert rge wrgetat wert
"""
"""from collections import Counter
str = "wert pi rty wert rer wert rge wrgetat wert".split()
co = Counter(str)
print(co)
# print(" ".join(Counter(input().split())))
print(" ".join(co))"""

"""
>>> a = 2
>>> eval("x + y * a", None, {"x": 10, "y": 3})
16
>>> eval("x + y * a", {"x": 10, "y": 3, "a": -2})
4
"""


str = input()
a, b = eval(input())
print(eval(str, {"x": a, "y": b}), eval(str, {"x": b, "y": a}))