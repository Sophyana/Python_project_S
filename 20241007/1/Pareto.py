def Pareto(*pairs):
    pareto_front = []
# via reqursia
    for current in pairs:
        dominated = False
        for other in pairs:
            if current != other:
                if (other[0] <= current[0] and other[1] <= current[1] and
                        (other[0] < current[0] or other[1] < current[1])):


                    dominated = True
                    break
        if not dominated:
            pareto_front.append(current)

    return tuple(pareto_front)


# Пример использования
line = eval(input())

"""input_pairs = ((32, 38), (10, 14), (19, 44), (31, 31), (17, 33), 
               (53, 6), (48, 9), (6, 38), (30, 49), (52, 30), 
               (7, 30), (45, 45), (21, 51), (7, 49), (11, 23))"""

result = Pareto(*line)

print(result)
print(Pareto(*result))

"""((53, 6), (30, 49), (52, 30), (45, 45), (21, 51))"""