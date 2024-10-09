from math import *

def Calc(s, t, u):
    def fun(x):
        y = eval(t)
        x = eval(s)
        return eval(u)
    return fun


import sys
exec(sys.stdin.read())