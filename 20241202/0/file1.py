with open("text1", "rb") as fl:
    data = fl.read()
    # print(data)

with open("text1_0", "wb") as fl:
    n = len(data) // 2
    fl.write(data[n: ])
    fl.write(data[: n])

# work incorrect
with open("text1_1", "wb") as fl:
    n = len(data) // 3
    for i in range(n, len(data)):
        if data[i] == '\n':
            n = i
            break
    fl.write(data[:n])

