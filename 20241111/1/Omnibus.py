class Omnibus:
    attrs_count = {}

    def __init__(self):
        super().__setattr__('local_attrs', set())

    def __setattr__(self, name, value):
        if name.startswith("_"):
            super().__setattr__(name, value)
            return
        if name not in self.__class__.attrs_count:
            self.__class__.attrs_count[name] = 1
        else:
            self.__class__.attrs_count[name] += 1
        self.local_attrs.add(name)

    def __getattr__(self, name):
        if name in self.__class__.attrs_count:
            return self.__class__.attrs_count[name]
        raise AttributeError(f"'{type(self).__name__}' object has no attribute '{name}'")

    def __delattr__(self, *names):
        for name in names:
            if name in self.local_attrs:
                self.local_attrs.remove(name)
                self.__class__.attrs_count[name] -= 1
                if self.__class__.attrs_count[name] == 0:
                    del self.__class__.attrs_count[name]


import sys
exec(sys.stdin.read())
