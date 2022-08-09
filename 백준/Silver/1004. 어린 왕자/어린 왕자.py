from sys import stdin

for _ in range(int(stdin.readline())):
    x, y, i, j = map(int, stdin.readline().split())
    count = 0
    for _ in range(int(stdin.readline())):
        k, l, r = map(int, stdin.readline().split())
        start = ((x - k) ** 2 + (y - l) ** 2) ** 0.5
        end = ((i - k) ** 2 + (j - l) ** 2) ** 0.5
        if start < r and end < r: continue
        count += 1 if start < r else (1 if end < r else 0)
    print(count)