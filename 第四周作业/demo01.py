from math import sqrt
for x in range(0, 100001):
    m = sqrt(x + 100)
    n = sqrt(x + 268)
    if m == int(m) and n == int(n):
        print(x)

