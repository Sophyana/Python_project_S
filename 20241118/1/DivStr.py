import collections


class DivStr(collections.UserString):
    def __init__(self, s=""):
        super().__init__(s)

    def __floordiv__(self, n):

        length = len(self.data)
        part_size = length // n
        remainder = length % n

        chunks = []
        start = 0
        for i in range(n):
            end = start + part_size
            chunks.append(self.data[start:end])
            start = end

        return iter(chunks)

    def __mod__(self, n):
        length = len(self.data)
        remainder = length % n
        return DivStr(self.data[-remainder:] if remainder else "")

    def __add__(self, other):
        return DivStr(self.data + str(other))


import sys
exec(sys.stdin.read())