# среднее арифметическое
"""def average(*args):
    print(sum(args) / len(args))


average(*eval(input()))
"""

# сортировка по ключу
"""mas = eval(input())
print(sorted(mas, key = lambda x: x ** 2 % 100))
"""


# все двоичные числа заданной длины
"""def rbin(n, lst, par):
    if n == 1:
        print( *(lst + [par]), sep = "")
        return
    new = lst + [par]
    rbin(n - 1, new, 0)
    rbin(n - 1, new, 1)


rbin(8, [], 1)"""


# функционалы
"""from math import *

def MINF(*args):
    def fun(x):
        return min([f(x) for f in args])
    return fun


f = MINF(cos, sin, tan)
print(f(eval(input())))
print( f.__closure__[0])
print(f.__closure__[0].cell_contents)"""

# замыкание

def Ex(a, b):
    def fun(x):
        return x * a + b
    return fun


d = Ex(10, 5)
print(d.__closure__)
print(d.__closure__[0].cell_contents)
print(d.__closure__[1].cell_contents)