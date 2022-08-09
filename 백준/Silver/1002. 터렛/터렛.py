from sys import stdin

for _ in range(int(stdin.readline())):
    x, y, r, i, j, k = map(int, stdin.readline().split())
    d = ((x - i) ** 2 + (y - j) ** 2) ** 0.5
    if d == 0: print(-1 if r == k else 0)
    else:
        if r + k == d or abs(r - k) == d: print(1)
        elif abs(r - k) < d < r + k: print(2)
        else: print(0)