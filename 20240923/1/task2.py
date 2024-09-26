sum = 0
while (x := int(input())) > 0:
    sum += x
    if sum > 21:
        print(sum)
        break
else:
    print(x)

