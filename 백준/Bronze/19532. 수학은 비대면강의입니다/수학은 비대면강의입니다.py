from sys import stdin

a, b, c, d, e, f = map(int, stdin.readline().split())
for x in range(-999, 1000, 1):
    for y in range(-999, 1000, 1):
        if a*x + b*y == c and d*x + e*y == f:
            print(x, y)