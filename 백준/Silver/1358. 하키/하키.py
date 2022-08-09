from sys import stdin

w, h, x, y, p = map(int, stdin.readline().split())
r = h / 2
count = 0
for _ in range(p):
    i, j = map(int, stdin.readline().split())
    d1 = ((i - x) ** 2 + (j - y - r) ** 2) ** 0.5
    d2 = ((i - x - w) ** 2 + (j - y- r) ** 2) ** 0.5
    if d1 <= r or d2 <= r: count += 1
    elif x <= i <= x + w and y <= j <= y + h: count += 1
print(count)