class Undead(Exception): pass
class Skeleton(Undead): pass
class Zombie(Undead): pass
class Ghoul(Undead): pass


def necro(a):
    remainder = a % 3
    if remainder == 0:
        raise Skeleton("Skeleton")
    elif remainder == 1:
        raise Zombie("Zombie")
    elif remainder == 2:
        raise Ghoul("Ghoul")


x, y = map(int, input().split(","))
for i in range(x, y):
    try:
        necro(i)
    except Skeleton:
        print("Skeleton")
    except Zombie:
        print("Zombie")
    except Undead:
        print("Generic Undead")


"""
11, 17
Generic Undead
Skeleton
Zombie
Generic Undead
Skeleton
Zombie
"""