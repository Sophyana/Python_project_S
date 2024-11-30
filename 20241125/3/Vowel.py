class Vowel:
    __slots__ = ('a', 'e', 'i', 'o', 'u', 'y', '_answer')

    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            if k in self.__slots__[:-1]:
                setattr(self, k, v)

        self._answer = 42

    def __str__(self):
        return ', '.join(f"{k}: {getattr(self, k)}" for k in sorted(self.__slots__[:-1]) if hasattr(self, k))

    @property
    def answer(self):
        return self._answer

    @property
    def full(self):
        return all(hasattr(self, k) for k in self.__slots__[:-1])

    def __setattr__(self, key, value):
        if key == 'full':
            return
        if key == 'answer':
            raise AttributeError("Cannot modify 'answer'")
        super().__setattr__(key, value)


import sys
exec(sys.stdin.read())



"""
a: 12, i: 3, y: 22 False
a: 12, e: 100500, i: 3, o: 100500, u: 100500, y: 22 True
"""