from sys import stdin

for _ in range(int(stdin.readline())):
    M, N, x, y = map(int, stdin.readline().split())
    y %= N
    b_break = 1
    while x <= M*N:
        if x % N == y:
            b_break = 0
            print(x)
            break
        x += M
    if b_break: print("-1")