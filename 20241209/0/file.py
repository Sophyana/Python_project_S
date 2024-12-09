"""def init(self, val):
    self.var = val

C = type('C', (), {"var": 100500, "__init__": init})"""

"""C = type('C', (), {"var": 100500, "__init__" : lambda self, var : setattr(self, "var", var)})

print(C.var)
c = C(123)
print(c.var)"""

# упрощаем
"""class final(type):
    def __new__(metacls, name, parents, namespace):
        for cls in parents:
            if isinstance(cls, final):
                raise TypeError(f"{cls.__name__} is final")
        return super().__new__(metacls, name, parents, namespace)
class E(metaclass=final): pass
class C: pass
class A(C, E): pass"""

# example
"""
class Sole(type):
        def __new__(metacls, name, parents, namespace):
            if len(parents) > 1:
                raise TypeError("Cannot have more than one parent")
            return super().__new__(metacls, name, parents, namespace)

class C(metaclass=Sole):
    pass
class D(C): pass
class E(C, int): pass

class E(D, int): pass"""

# doubleton
"""
class Doubleton(type):
    _instance = [None, None]
    ind = 0
    def __call__(cls, *args, **kw):
        cls.ind += 1
        if cls._instance[cls.ind % 2] is None:
            cls._instance[cls.ind % 2] = super().__call__(*args, **kw)
        return cls._instance[cls.ind % 2]


class C(metaclass=Doubleton): pass
print(*(C() for i in range(7)), sep="\n")"""

# matching
"""
res = eval(input())
match res:
    case 1, 2:
        print("Exact 1, 2")
    case a, 3:
        print(a, "with 3") # связанные переменные
    case 2, *tail:
        print("2 with", tail) # распаковка
    case (3 | 4) as a, *tail:
        print(a, "with", *tail)
    case _:
        print("Any", res) # catch all
        """

# тупенький ассемблер
"""
while str := input():
    res = str.split()

    match res:
        case "mov", *tail:
            print("moving <r2> to <r1>")
        case ("push" | "pop") as a, *tail:
            print(f"{a}ing", " ".join(tail))
        case "cmd", *tail:
            print("making cmd with", " ".join(tail))
        case _:
            print("Parse error")"""

# filter for addition
# case ( | ) as a, if len(fgfdh) > jidkfj

# инкапсуляция

"""class CONST:
    A = 12
c = 2
match c:
    case A: print(" = 12")"""


"""
atanol = input().split()
class STRING:
    str_first = atanol[0]
    str_second = atanol[1]
    str_third = atanol[2]

while str := input():
    match str.split():
        case (STRING.str_first, *tail) as qwer if "yes" in qwer:
            print("yes in this")
        case [STRING.str_second]:
            print("all second")
        case STRING.str_third, *tail, STRING.str_second:
            print("begin with third and end with second")
"""

# аннотации бывают у классов и у параметров значений функции

"""
class C:
    a : int = 10
    b: float

    def meth(self, x : int, y : int) -> int:
        return self.a + x + y

# in comand line
import inspect
inspect.get_annotations(C)"""

import inspect

class C:
    a: int
    def __init__(self, val):
        type = inspect.get_annotations(self.__class__)["a"]
        if not isinstance(val, type):
            raise TypeError(f"val must be {type}")
        self.a = val

