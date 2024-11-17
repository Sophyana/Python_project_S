class Triangle:
    def __init__(self, p1, p2, p3):
        self.points = [tuple(p1), tuple(p2), tuple(p3)]

    def __abs__(self):
        a, b, c = self.points
        return abs((a[0] * (b[1] - c[1]) +
                    b[0] * (c[1] - a[1]) +
                    c[0] * (a[1] - b[1])) / 2)

    def __bool__(self):
        return abs(self) > 0

    def __lt__(self, other):
        return abs(self) < abs(other)

    def contains_point(self, point):
        x, y = point
        a, b, c = self.points

        def sign(p1, p2, p3):
            return (p1[0] - p3[0]) * (p2[1] - p3[1]) - (p2[0] - p3[0]) * (p1[1] - p3[1])

        d1 = sign((x, y), a, b)
        d2 = sign((x, y), b, c)
        d3 = sign((x, y), c, a)

        has_neg = (d1 < 0) or (d2 < 0) or (d3 < 0)
        has_pos = (d1 > 0) or (d2 > 0) or (d3 > 0)

        return not (has_neg and has_pos)

    def __contains__(self, other):
        if not other:
            return True  
        if not self:
            return False  
        return all(self.contains_point(pt) for pt in other.points)

    def __and__(self, other):
        if not self or not other:
            return False  
        return any(self.contains_point(pt) for pt in other.points) or \
               any(other.contains_point(pt) for pt in self.points)

import sys
exec(sys.stdin.read())
