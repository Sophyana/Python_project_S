from itertools import islice, count


def slide(seq, n):
    for start in count():
        window = list(islice(seq, start, start + n))
        if not window:
            break
        yield from window


import sys
exec(sys.stdin.read())


# print(*list(slide(range(8), 3)))
