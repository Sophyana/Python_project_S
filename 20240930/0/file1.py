r = [x for x in range(5, 15 + 1, 1)]
t = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k']
r[4:7] = t[-5:]
print(r)
