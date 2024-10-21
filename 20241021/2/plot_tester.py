from math import *



def interpreter():
    functions = {}
    processed_lines = 0

    while True:
        line = input().strip()
        processed_lines += 1

        if line == 'quit':
            break

        if not line:  # Проверка на пустую строку
            print("Ошибка: Пустая строка.")
            continue

        if line.startswith(':'):
            # Определение функции
            parts = line[1:].split()
            if len(parts) < 2:  # Проверка на корректный ввод
                print("Ошибка: Неправильное определение функции.")
                continue

            func_name = parts[0]
            params = parts[1:-1]
            expression = parts[-1]
            functions[func_name] = (params, expression)

        else:
            # Вызов функции
            parts = line.split()
            if len(parts) == 0:  # Проверка на пустую строку
                print("Ошибка: Пустая строка.")
                continue

            func_name = parts[0]
            args = parts[1:]

            if func_name in functions:
                param_names, expression = functions[func_name]

                # Обработка аргументов
                if len(param_names) == 1 and len(args) == 1:
                    args = [args[0]]  # Один аргумент может содержать пробелы
                elif len(param_names) > 1:
                    if any(' ' in arg for arg in args):
                        print("Ошибка: Для нескольких параметров аргументы не могут содержать пробелы.")
                        continue

                # Создание локального контекста для вычислений
                local_vars = {param: arg for param, arg in zip(param_names, args)}

                # Вычисление выражения
                try:
                    result = eval(expression, {**math.__dict__, **local_vars})
                    print(result)
                except Exception as e:
                    print(f"Ошибка: {e}")
            else:
                print(f"Функция '{func_name}' не определена.")

    # Вывод результатов завершения
    print(f"{len(functions) + 1}, {processed_lines}")


# Запуск интерпретатора
interpreter()


"""
:sin x sin(x)
sin 1
:decorate s "--<<{}>>--".format(s)
decorate "ЖЖЖ"
sin 2
quit "{}, {}"
"""