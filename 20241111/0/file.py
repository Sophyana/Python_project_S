class Rectangle():
    rectcnt = 0
    def __init__(self, x1, x2, y1, y2):
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2
        self.__class__.rectcnt += 1
        setattr(self, f"rect_{self.__class__.rectcnt}", self.__class__.rectcnt )
        return

    def __str__(self):
        return f"({self.x1}, {self.y1}), ({self.x1}, {self.y2}), " \
               f"({self.x2}, {self.y2}), ({self.x2}, {self.y1}), count = {self.__class__.rectcnt}"

    def __abs__(self):
        return abs((self.x2 - self.x1) * (self.y2 - self.y1))

    def __lt__(self, other):
        return abs(self) < abs(other)

    def __eq__(self, other):
        return abs(self) == abs(other)

    def __mul__(self, other):
        return self.__class__(self.x1 * other, self.y1 * other, self.x2 * other, self.y2 * other)

    __rmul__ = __mul__

    def __getitem__(self, idx):
        return ((self.x1, self.y1), (self.x1, self.y2), (self.x2, self.y2), (self.x2, self.y1))[idx]

    def __bool__(self):
        if abs(self) == 0:
            return False
        else:
            return True
        # return abs(self) != 0

    def __del__(self):
        self.__class__.rectcnt -= 1
        print(self.rectcnt)

    def __iter__(self):
        return iter( ((self.x1, self.y1), (self.x1, self.y2),
                    (self.x2, self.y2), (self.x2, self.y1)) )


r = Rectangle(1, 2, 5, 9)
print(r)
r = Rectangle(7, 8, 5, 2)
print(r)
print(dir(r))
r = Rectangle(27, 38, 54, 22)
print(r)
print(dir(r))

r1 = Rectangle(1, 2, 5, 9)
r2 = Rectangle(41, 2, 5, 9)

print(r2 < r1)

r3 = Rectangle(41, 2, 5, 9)
print(r3 == r2)

print(r1 * 5)
print(5 * r1)

print(r1)
print(r1[2])
print(r1[1])

r4 = Rectangle(5, 5, 5, 5)
if r4:
    print("True")
else:
    print("False")


for x, y in Rectangle(1, 2, 5, 6):
    print(x, y)
