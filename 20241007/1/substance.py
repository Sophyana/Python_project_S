def subtract(a, b):

    if type(a) != type(b):
        exit()

    if type(a) in [int, float]:
        return a - b

    if type(a) in [list, tuple, str]:
        b_set = set(b)
        result = [item for item in a if item not in b_set]

        return type(a)(result)


a, b = eval(input())
print(subtract(a, b))
