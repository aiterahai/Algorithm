from sys import stdin

while True:
    a, b = map(int, stdin.readline().split())
    if not a and not b: break
    print("Yes" if a > b else "No")