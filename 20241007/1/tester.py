def pareto(set):
    for para in set:
        for el in set:
            if (para[0] >= el[0] and para[1] >= el[1]) and (para[0] > el[0] or para[1] > el[1]):
                set = [_ for _ in set if el != _]
    return set




line = eval(input())
print(*pareto(line))


# mb1966@yndex.ru






"""s= "(x+100)/y"

print(eval(s,{},{"x":100,"y":20}))"""