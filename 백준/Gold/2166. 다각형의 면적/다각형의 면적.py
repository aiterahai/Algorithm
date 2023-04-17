from sys import stdin

x, y = [], []
N = int(stdin.readline())
for _ in range(N):
    A, B = map(int, stdin.readline().split())
    x.append(A)
    y.append(B)
x.append(x[0])
y.append(y[0])

A, B = 0, 0
for i in range(N):
    A += x[i] * y[i + 1]
    B += y[i] * x[i + 1]

print(round(abs((A - B) / 2), 2))