from math import *


def show(screen):
    print("\n".join(["".join(s) for s in screen]))


def scale(a, b, A, B, x):
    return (B-A) * (x-a) / (b-a) + A


def graphic(w, h, a, b, func):


    lst = [[" "] * w for j in range(h)]
    s = 0
    val = []
    min, max = inf, -inf
    for i in range(w):
        x = scale(0, w-1, a, b, i)
        y = - eval(func)
        val.append((i, y))
        if y > max:
            max = y
        if y < min:
            min = y

    for eli, ely in val:
        s_pred = s
        s = round(scale(min, max, 0, h-1, ely))
        lst[s][eli] = "*"
        if s_pred > s:
            for k in range(s+1, s_pred):
                lst[k][eli-1] = "*"
        elif s > s_pred and eli != 0:
            for e in range(s_pred+1, s):
                lst[e][eli-1] = "*"
    show(lst)


w, h, a, b, func = input().split(" ")
w, h, a, b = eval(f"{w}, {h}, {a}, {b}")
graphic(w, h, a, b, func)
