from sys import stdin

while True:
    a, b = map(int, stdin.readline().split())
    if not a and not b: break
    print("factor" if b % a == 0 else ("multiple" if a % b == 0 else "neither"))