"""
громкий декоратор
"""

"""def dumper(f):
    def newfun(*args, **kwargs):
        print(">", *args, kwargs)
        res = f(*args, **kwargs)
        print("<", res)
        return res
    return newfun
"""

"""def isint(f):
    def newfun(*args):
        for x in args:
            if type(x) is not int: raise TypeError("Error all are not int")
        return f(*args)
    return newfun
"""
# if not all(isinstance(arg, int) for arg in args: raise TypeError("Not all parameters are int", args)

"""
параметрические декораторы
"""

"""def multicall(times):
    def decorator(fun):
        def newfun(*args):
            return [fun(*args) for i in range(times)]
        return newfun
    return decorator

@multicall(4)
def siplefun(N):
    return N * 2 + 1

print(*siplefun(9) )
"""

"""
def istype(string):
    def decorator(fun):
        def newfun(*args):
            if not all(isinstance(arg, string) for arg in args):
                raise TypeError(f"Not all parameters are {string}", args)
            return fun(*args)
        return newfun
    return decorator


@istype(int)
def fun(a, b, c):
    return a + b + c

print(fun(1, 2, 3))
"""

"""
class Dumper:
    def __init__(self, function):
        self.function = function

    def __call__(self, *args, **kwargs):
        print(args, kwargs, end = " -> ")
        res = self.function(*args, **kwargs)
        print(res)
        return res

@Dumper
def fun(a, b):
    return a + b

print(fun(1, 2))
"""

"""
class istype:
    def __init__(self, string):
        self.string = string

    def __call__(self, fun):
        def newfun(*args):
            if not all(isinstance(arg, string) for arg in args):
                raise TypeError(f"Not all parameters are {string}", args)
            return fun(*args)
        return fun


@istype(int)
def ffun(a, b):
    return a + b

print(ffun(1, 2))"""


"""
class Sender:
    greeted = False

    @classmethod
    def report(cls):
        if cls.greeted:
            print("Get away!")
        else:
            print("Greetings!")
            cls.greeted = True

class  Asker:
    @staticmethod
    def askall(lst):
        for el in lst:
            el.report()


a, b, c = Sender(), Sender(), Sender()
Asker().askall([a, b, c, a, b, c])
"""

# descriptors

"""
class C:
    def __get__(self, obj, cls):
        print("GET", obj)

    def __set__(self, obj, value):
        print("SET", obj, value)
        obj._value = value # abs(value)

    def __delete__(self, obj):
        print("DELET", obj)


class D:
    descr = C()

d = D()
d.descr = 12345
print(d.descr)

del d.descr
print(d.descr)

dd = D()
print(dd.descr)
dd.descr = 42
print(dd.descr)
"""

"""
class Counter:
    def __init__(self):
        self.num = 0

    def __get__(self, obj, cls):
        return self.num

    def __set__(self, obj, value):
        self.num = value 

    def __delete__(self, obj):
        print("DELET", obj)


class C:
    counter = Counter()

    def __init__(self):
        self.counter += 1

    def __del__(self):
        self.counter -= 1

d = C()
print( d.counter)
dd = C()
print(dd.counter)
del d
print(dd.counter)"""

# property skip

# slots as a base

"""
class C:
    __slots__ = "a", "b", "c",
    ro = "Readonly"

    def __init__(self):
        for attr in self.__slots__:
            setattr(self, attr, f"<{attr}>")


c = C()
print(c.a)
print(c.b)
print(c.c)
print(c.ro)

c.b = 123456
print(c.b)
"""

from string import ascii_letters

class Trad:
    def __init__(self):
        for attr in ascii_letters:
            setattr(self, attr, attr)

class Slotter:
    __slots__ = tuple(ascii_letters)

    def __init__(self):
        for attr in ascii_letters:
            setattr(self, attr, attr)