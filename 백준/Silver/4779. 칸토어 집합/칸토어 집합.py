from sys import stdin

def func(blank, N):
    if N == 1: return "-"
    return func(0, N // 3) + " " * (N // 3) + func(0, N // 3)

while True:
    try:
        N = int(stdin.readline())
        a = func(0, 3 ** N)
        print(a)
    except: break