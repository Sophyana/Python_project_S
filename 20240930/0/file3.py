"loop for"
"""a = []
for i in range(8, 20, 1):
    a.append(i)
    if i % 2:
        print("OKS")
        break
else:
    print(a[0])
"""

ls = eval(input())
for i in ls:
    if i % 2:
        print(i)
        break
else:
    print(ls[0])
