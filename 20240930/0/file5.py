n, m = eval(input())
a = [i for i in range(n, m)]
for x in a:
    if x % 2 and '3' not in str(x):
        print(x, "Good")

