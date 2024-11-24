class InvalidInput(Exception): pass


class BadTriangle(Exception): pass


def triangleSquare(input_data):
    try:
        (x1, y1), (x2, y2), (x3, y3) = eval(input_data)
    except Exception:
        raise InvalidInput("Invalid input")

    if not all(isinstance(coord, (int, float)) for coord in [x1, y1, x2, y2, x3, y3]):
        raise InvalidInput("Invalid input")

    area = 0.5 * abs(
        x1 * (y2 - y3) +
        x2 * (y3 - y1) +
        x3 * (y1 - y2)
    )

    if area == 0:
        raise BadTriangle("Not a triangle")

    return round(area, 2)


while True:
    try:
        input_data = input()
        area = triangleSquare(input_data)
    except InvalidInput as e:
        print(e)
    except BadTriangle as e:
        print(e)
    else:
        print(f"{area:.2f}")
        break


"""
asdf
1,2,3,4,5,6
(1,1), (2,2), (11,11)
(1,2), (4,5), (9,8)

Invalid input
Invalid input
Not a triangle
3.00
"""

import sys
exec(sys.stdin.read())