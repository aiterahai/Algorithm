from sys import stdin

temp = list(map(int, stdin.read().split()))[::-1]
while temp:
    S, N = temp.pop(), temp.pop()
    print(N // (S + 1))