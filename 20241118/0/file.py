"""class A:
    v = 1

class B(A):
    v = 2

b = B()
b.v = 3
print(b.v)
del b.v
print(b.v)
del B.v
print(b.v)
del A.v
print(b.v)
"""


"""
class A:
     def __init__(self, val):
        self.val = val

     def __add__(self, other):
        return self.__class__(self.val + other.val)
     def __str__(self):
         return f"<{self.val}>"


class B(A):
    def __str__(self):
        return f"[{self.val}]"


a, b = B(9), B(7)
print(a + b)
print(a, b, a + b)
"""


"""
class C:
    __v = 0
    def inc(self):
        self.__v += 1

    def __str__(self):
        return f"<{self.__v}>"

class D(C):
    def __init__(self):
        self.v = 100500

c = C()
print(c)

c.inc()
print(c)

d = D()
print(d)
c.inc()
print(c)
"""

"""
CC = type("C", (), {"a": 10, "__init__" : lambda self, val: setattr(self, "b", val)} )
print(CC)
print(CC.a)

d = CC(123)
print(d.b)
"""

"""
class C:
    def __init__(self, val):
        self.val = val

class D(C):
    def __init__(self, val):
        super().__init__(val)
        print("Init", val)


d = D(123)
print(d)
print(d.val)
"""

"""
class A:
    def __str__(self):
        return "A"

class B(A):
    def __str__(self):
        return f"{super().__str__()}:B"

class C(B):
    def __str__(self):
        return f"{super().__str__()}:C"


print(A())
print(B())
print(C())
"""

"""
# Exception
b = 0.1

try:
    a = 1 / b
except ZeroDivisionError:
    print("oops")
else:
    print(a)
finally:
    print("END")
    
"""

"""
f = True
while f:
    str = input()
    try:
        num = eval(str)
        if type(num) == int:
            print("Wiiiiiiiin!")
            f = False
        else:
            print("try again")
    except Exception:
        print("try again")

"""

"""
def div_ab(a, b):
    return a / b

def div_exception(a, b):
    try:
        res = div_ab(a, b)
        return res
    except:
        return "errooooorrrrr"


for a, b in ((10, 2), (1, 0), (9, 3), ("#", 3)):
    print( div_exception(a, b))
"""


"""
def div_ab(a, b):
    if abs(b) < 0.001:
        raise ValueError("No operation allowed")
    return a / b


for a, b in ((10, 2), (1, 0.2), (9, 13), (1, 0.0002)):
    print(div_ab(a, b))

"""

class A: pass
class B: pass

class C(A, B): pass
class D(C, B): pass
class E(B, C): pass


