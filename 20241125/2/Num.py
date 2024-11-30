class Num:
    def __init__(self, default = 0):
        self.values = {}
        self.default = default

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return self.values.get(instance, self.default)

    def __set__(self, instance, value):
        if hasattr(value, 'real'):
            self.values[instance] = value.real
        elif hasattr(value, '__len__'):
            self.values[instance] = len(value)
        else:
            raise TypeError("Unsupported value type")

import sys
exec(sys.stdin.read())