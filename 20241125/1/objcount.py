def objcount(cls):
    cls.counter = 0
    original_init = getattr(cls, "__init__", None)
    original_del = getattr(cls, "__del__", None)

    def new_init(self, *args, **kwargs):
        cls.counter += 1
        if original_init:
            original_init(self, *args, **kwargs)

    def new_del(self):
        cls.counter -= 1
        if original_del:
            original_del(self)

    cls.__init__ = new_init
    cls.__del__ = new_del

    return cls


import sys
exec(sys.stdin.read())
