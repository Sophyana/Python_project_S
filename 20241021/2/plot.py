from math import *

functions = {}
func_count = 1
line_count = 0


def process_definition(line):
    global func_count
    parts = line[1:].split()
    func_name = parts[0]
    params = parts[1:-1]
    expr = parts[-1]

    functions[func_name] = lambda *args, expr=expr, params=params: eval(expr, None, dict(zip(params, args)))
    func_count += 1


def process_call(line):
    parts = line.split()
    func_name = parts[0]
    args = parts[1:]

    if func_name in functions:
        if len(args) == 1:
            args = [eval(args[0])]
        else:
            args = [eval(arg) for arg in args]

        result = functions[func_name](*args)
        print(result)

while True:
    line = input().strip()
    line_count += 1

    if line.startswith(':'):
        process_definition(line)
    elif line.startswith('quit'):
        _, format_str = line.split(maxsplit=1)
        print(format_str.format(func_count, line_count))
        break
    else:
        process_call(line)
