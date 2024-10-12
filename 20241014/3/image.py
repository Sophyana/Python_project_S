image = []
count_grid = 0
count_point = 0
count_tilda = 0

frac = []
while str := input():
    for c in str:
        if c == '#': count_grid += 1
        if c == '.': count_point += 1
        if c == '~': count_tilda += 1
    image.append(count_grid)
    count_grid = 0
frac.append(count_point)
frac.append(count_tilda)
top = image[0]
wall = len(image)


top, wall = wall, top
str = ""
for i in range(top): str += "#"
print(str)
for i in range(wall - 2):
    str = "#"
    if count_point > 0:
        for j in range(top - 2):
            str += "."
            count_point -= 1
    else:
        for j in range(top - 2):
            str += "~"
            count_tilda -= 1
    str += "#"
    print(str)
str = ""
for i in range(top): str += "#"
print(str)

for i in range(frac[0]):
    print(".", end="")
print(frac[0], "/", (frac[0] + frac[1]))
for j in range(frac[1]):
    print("~", end="")
print(frac[1], "/", (frac[0] + frac[1]))



"""
########
#......#
#~~~~~~#
#~~~~~~#
########
"""